https://doc.memed.com.br/docs/como-fazer/validar-dados-prescritor-cfm/

# Validação de Dados de Prescritores no CFM

Esta documentação orienta o processo de adequação dos dados obrigatórios do prescritor, tendo
em vista a nova regulamentação da ANVISA sobre prescrição digital de medicamentos de controle
especial. Ao longo dela você encontra: como testar a validação sem alterar nada (dry-run), como
atualizar o cadastro em produção quando os dados precisarem de correção, quais campos são
cobertos nesta v1, o que a validação não garante e as perguntas mais frequentes sobre o
processo.

ATENÇÃO: VIGÊNCIA EM 30/09/2026

A partir de 30/09/2026, conforme a regulamentação da ANVISA sobre prescrição digital de
medicamentos de controle especial, entra em vigência a disponibilização de receituários de
controle especial digital. Prescritores com dados cadastrais divergentes dos registrados em
seu respectivo conselho profissional não emitem receituário de controle especial nem acessam
a Memed a partir dessa data. Valide e corrija sua base com antecedência.

VALIDAÇÃO AUTOMATIZADA DISPONÍVEL APENAS PARA O CFM

A Memed disponibiliza atualmente rota de validação automatizada apenas para registros no CFM.
A conferência de registros de outros conselhos profissionais (CFO e demais) deve ser tratada
diretamente com o time Memed: entre em contato com o time de Customer Success (CX) da Memed
para alinhar o processo de sanitização da sua base.

DADOS DE EXEMPLO

Os exemplos utilizam dados fictícios. Em produção, trate dados pessoais de prescritor conforme
a LGPD.

## Quando usar esta validação​

Valide, sem persistir nada, se nome, data de nascimento, CRM, UF e CPF de um prescritor
conferem com o registro no CFM, usando a rota de validação
`POST /v1/sinapse-prescricao/usuarios/validate-board`. CRM e UF são campos separados no
payload: não envie o número do CRM concatenado com a sigla do estado (envie
`board_number: "123456"` e `board_state: "SP"`, e não `board_number: "123456-SP"`). Use essa
rota para sanear sua base antes de emitir prescrições e, se necessário, atualize o cadastro em
produção. Ela é útil especialmente para:

* Parceiros com prescritores cujos dados cadastrais estejam incompletos ou inconsistentes em
  relação ao CFM, estejam eles ativos ou já inativados.
* Saneamento em lote da base de prescritores antes de 30/09/2026.
* Testar uma correção de cadastro antes de aplicá-la de fato via `PATCH`.

## Visão geral do fluxo​

## Rota de validação (dry-run)​

```text
POST: MEMED_API_URL/sinapse-prescricao/usuarios/validate-board?api-key=API_KEY&secret-key=SECRET_KEY
```

Autenticação desta rota

Esta rota segue o mesmo padrão de autenticação das demais rotas de usuários: `api-key` e
`secret-key` como parâmetros de URL (veja [Usuário Prescritor](/docs/backend/usuario-prescritor)).

A validação não persiste dados, i.e., nenhum cadastro é criado, alterado ou reativado nesta
chamada.

### Campos validados​

| Propriedade | Tipo | Obrigatório | Observações |
| --- | --- | --- | --- |
| `nome` | string(255) | ✅ | Nome civil, exatamente como registrado no CFM |
| `sobrenome` | string(255) | ✅ | Sobrenome do prescritor, exatamente como registrado no CFM |
| `cpf` | string(11) | ✅ | Apenas dígitos |
| `data_nascimento` | date(10) | ✅ | dd/mm/YYYY |
| `board.board_code` | string(5) | ✅ | Esta documentação cobre o fluxo com `CRM` |
| `board.board_number` | string(255) | ✅ | Apenas dígitos |
| `board.board_state` | string(2) | ✅ | Sigla do estado (UF) |
| `external_id` | int/string(255) | ✅ | Identificador do prescritor no seu sistema |

Sobre o campo `nome`: nome civil x nome social

O CFM registra o prescritor pelo nome civil. Se o seu cadastro guarda o nome social, a
divergência com o CFM é esperada; envie o nome civil neste campo. Outras causas comuns de
divergência: acentuação diferente, abreviações, sobrenome desatualizado após ele ou ela ter
casado ou se separado, e sobrenomes compostos grafados de forma diferente da registrada no CFM.

Nesta v1, apenas estes 4 campos (nome, data de nascimento, CRM, UF e CPF) são validados contra
o CFM. RQE, especialidade e número de cadastro ANVISA ficam para fases posteriores.

### Exemplo de requisição​

* cURL
* Sucesso
* Erro

```bash
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/validate-board?api-key=SUA_API_KEY&secret-key=SUA_SECRET_KEY' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/vnd.api+json' \
  --data '{
    "data": {
      "type": "usuarios",
      "attributes": {
        "external_id": "PARCEIRO-12345",
        "nome": "Gustavo",
        "sobrenome": "Ribeiro Sousa",
        "cpf": "53076220403",
        "data_nascimento": "05/09/1972",
        "board": {
          "board_code": "CRM",
          "board_number": "315435435",
          "board_state": "SP"
        }
      }
    }
  }'
```

```json
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "outcome": "approved",
      "validated": true,
      "reason_code": null
    }
  }
}
```

```json
{
  "errors": [
    {
      "status": "400",
      "code": "invalid_practitioner_data",
      "title": "Dados reprovados na validação",
      "detail": "O CFM não conseguiu confirmar os dados informados para este prescritor."
    }
  ]
}
```

### Códigos de resposta​

| HTTP | Situação | Quando acontece |
| --- | --- | --- |
| `200` | Aprovado | Os 4 campos passaram na validação local e no CFM |
| `400` | Reprovado | Input inválido, duplicidade local (mesmo CRM ou `external_id` já cadastrado) ou dados reprovados pelo CFM |
| `401` | Não autorizado | `api-key` / `secret-key` ausentes ou inválidas |
| `429` | Limite excedido | Rate limit da rota foi ultrapassado |
| `503` | Indisponível | Serviço de validação do CFM indisponível ou desabilitado no ambiente |

## Rota de atualização de cadastro​

Depois de validar, use esta rota para corrigir os dados no cadastro real do prescritor. Ela
valida novamente no CFM durante o próprio update e, se os dados forem aceitos, **reativa** o
prescritor automaticamente.

CAMPOS OBRIGATÓRIOS PARA REATIVAÇÃO AUTOMÁTICA

Para que o prescritor seja reativado automaticamente, envie todos os campos obrigatórios
(nome, sobrenome, data de nascimento, CRM, UF e CPF) no `PATCH`, não apenas o campo que você
está corrigindo. Se enviar, por exemplo, somente o CPF ou apenas a data de nascimento, o CFM
não valida os demais campos e o prescritor não é reativado, mesmo que a resposta seja `200`.

```text
PATCH: MEMED_API_URL/sinapse-prescricao/usuarios/{EXTERNAL_ID}?api-key=API_KEY&secret-key=SECRET_KEY
```

* cURL
* Sucesso
* Erro

```bash
curl --request PATCH \
  --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/PARCEIRO-12345?api-key=SUA_API_KEY&secret-key=SUA_SECRET_KEY' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/vnd.api+json' \
  --data '{
    "data": {
      "type": "usuarios",
      "attributes": {
        "nome": "Gustavo",
        "sobrenome": "Ribeiro Sousa",
        "cpf": "53076220403",
        "data_nascimento": "05/09/1972",
        "board": {
          "board_code": "CRM",
          "board_number": "315435435",
          "board_state": "SP"
        }
      }
    }
  }'
```

```json
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "outcome": "approved",
      "validated": true,
      "status": "ativo"
    }
  }
}
```

```json
{
  "errors": [
    {
      "status": "400",
      "code": "invalid_practitioner_data",
      "title": "Dados reprovados na validação",
      "detail": "O CFM não conseguiu confirmar os dados informados para este prescritor."
    }
  ]
}
```

ATUALIZANDO O external\_id

Só inclua o campo `external_id` no payload se você realmente deseja alterar seu valor. Para
atualizações comuns (nome, data de nascimento, CRM, UF, CPF), não inclua esse campo.

## O que esta validação não garante​

No retorno `200` (aprovado), confirma-se apenas que nome, data de nascimento, CRM, UF e CPF
foram aceitos. Isso não atesta:

* Aptidão para emissão de Notificação de Receita (RQE, especialidade) ou outras categorias de
  receituário controlado que dependam de campos além destes 4.
* Validade do número de cadastro ANVISA.
* Que o prescritor está apto em todas as categorias de receituário: apenas nas que dependem
  exclusivamente destes 4 campos.

Status do médico no conselho

O status do prescritor no conselho (ativo, inativo ou suspenso) não é retornado como campo
explícito da resposta nesta v1. A validação usa esse status internamente (um CRM inativo ou
suspenso reprova a validação), mas o parceiro recebe apenas o resultado agregado de
aprovação/reprovação.

## Limitações conhecidas​

* **Indisponibilidade do CFM:** o CFM pode ficar temporariamente indisponível. Nesse cenário a
  resposta é `503`; tente novamente mais tarde, pois não é um erro definitivo do cadastro.
* **O CFM valida os 4 campos em conjunto:** nome, data de nascimento, CRM, UF e CPF. Uma
  divergência em qualquer um deles pode levar à reprovação da validação.
* **Retorno genérico em caso de reprovação:** o CFM informa apenas que os dados não conferem,
  sem detalhar qual campo específico está incorreto. Ao receber `400`, revise os 4 campos em
  conjunto.
* **Rate limit:** por padrão, até 120 requisições por hora por parceiro. Ao exceder, a resposta
  é `429`.
* **Duplicidade de `external_id`:** cenários de duplicidade não são tratados nesta versão. Se o
  `external_id` enviado já existir para outro cadastro, trate isso na sua integração antes de
  chamar o endpoint.

## Perguntas frequentes​

**Recebi `400` mesmo achando que os dados estão corretos. O que faço?**
Confira primeiro se o CRM e a UF correspondem ao registro ativo do prescritor no CFM. Revise
também se nome, data de nascimento e CPF foram digitados exatamente como no seu cadastro de
origem. Atenção especial ao formato da data de nascimento: ela deve ser enviada como
`DD/MM/AAAA`. Datas em formato diferente do indicado (por exemplo, `AAAA-MM-DD`) ou com
alguma parte ausente (ano, mês ou dia) são consideradas inválidas e retornam `400`, mesmo que
o restante do cadastro esteja correto. Teste novamente pela validação (dry-run) antes de
atualizar o cadastro real.

**Recebi `503`. Preciso abrir chamado?**
Não. Esse retorno indica indisponibilidade temporária do CFM. Aguarde alguns minutos e tente
novamente.

**O prescritor usa nome social. A validação vai reprovar?**
Possivelmente sim, se o nome social divergir do nome civil registrado no CFM. Envie o nome
civil completo no campo `nome`.

**A resposta traz o status do médico no conselho (ativo/inativo/suspenso)?**
Não nesta v1. A validação considera esse status internamente, mas o campo explícito não é
retornado ao parceiro.

**Quando devo acionar o time de CX da Memed?**
Apenas em casos de exceção ou insucesso persistente: quando a mesma tentativa continuar sendo
reprovada após múltiplas tentativas em dias diferentes, ou quando você suspeitar de um problema
no lado da Memed.

## Próximos passos​

| Tópico | Documentação |
| --- | --- |
| Cadastro completo do prescritor | [Usuário Prescritor](/docs/backend/usuario-prescritor) |
| Boas práticas de integração | [Boas Práticas de Integração](/docs/boas-praticas-integracao) |
| Solução de problemas | [Erros comuns](/docs/erros-comuns) |
| Dúvidas gerais | [Dúvidas Frequentes](/docs/duvidas-frequentes) |
