# Como fazer (tutoriais)

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- 📄️ Reordenação das abas da busca — `https://doc.memed.com.br/docs/como-fazer`
- Cadastrando o prescritor — `https://doc.memed.com.br/docs/como-fazer/cadastrar-prescritor`
- Como capturar evento de prescrição excluída — `https://doc.memed.com.br/docs/como-fazer/capturar-prescricao-excluida`
- Como capturar evento de prescrição impressa — `https://doc.memed.com.br/docs/como-fazer/capturar-prescricao-impressa`
- Configurar cabeçalho e rodapé — `https://doc.memed.com.br/docs/como-fazer/configurar-cabecalho-rodape`
- Configurar dados do prescritor — `https://doc.memed.com.br/docs/como-fazer/configurar-dados-prescritor`
- Documentos estruturados — `https://doc.memed.com.br/docs/como-fazer/documentos-estruturados`
- Como fechar o módulo da plataforma prescrição — `https://doc.memed.com.br/docs/como-fazer/fechar-modulo-plataforma`
- Gestão do prescritor — `https://doc.memed.com.br/docs/como-fazer/gestao-do-prescritor`
- Gestão do paciente — `https://doc.memed.com.br/docs/como-fazer/gestao-paciente`
- Configurar impressão do prescritor — `https://doc.memed.com.br/docs/como-fazer/impressao-medico`
- Manter a responsividade da aplicação embedded — `https://doc.memed.com.br/docs/como-fazer/manter-responsividade-prescricao`
- Abrir modulo da Memed em modo de edição — `https://doc.memed.com.br/docs/como-fazer/memed-modo-edicao`
- Mudar a fonte do PDF da receita — `https://doc.memed.com.br/docs/como-fazer/mudar-fonte-pdf`
- Obter dados do Usuário (prescritor) — `https://doc.memed.com.br/docs/como-fazer/obter-dados-usuario`
- Remover cabeçalho e rodapé — `https://doc.memed.com.br/docs/como-fazer/removendo-cabecalho-rodape`
- Reordenação das abas da busca — `https://doc.memed.com.br/docs/como-fazer/reordenacao-busca`
- Validação de Dados de Prescritores no CFM — `https://doc.memed.com.br/docs/como-fazer/validar-dados-prescritor-cfm`

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer -->
### 📄️ Reordenação das abas da busca

A busca é dividida em abas e cada uma delas tem seu nome de identificação de acordo com os tipos de resultados retornados.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/cadastrar-prescritor -->
## Cadastrando o prescritor

Para cadastrar um novo usuário prescritor, realize uma requisição **POST** na rota de usuários da API Memed, enviando os dados do profissional no corpo da requisição.

**Estrutura da Requisição**

**Formato obrigatório:** Os dados devem ser enviados no **corpo (body)** da requisição seguindo rigorosamente a estrutura de payload especificada pela API. A formatação correta garante o sucesso da operação e evita erros de validação.

**Relacionamentos opcionais:** Ao incluir as propriedades `cidade` e/ou `especialidade` no objeto `relationships`, os campos `type` e `id` dentro delas tornam-se **obrigatórios**.

**APIs de Consulta:**

- **Cidades:** Obtenha o ID da cidade em:  
  `https://integrations.api.memed.com.br/v1/cidades`

- **Especialidades:** Obtenha o ID da especialidade em:  
  `https://integrations.api.memed.com.br/v1/especialidades`

**💡 Dica:** Consulte essas APIs previamente e armazene os IDs mais utilizados em cache no seu sistema para otimizar o desempenho do processo de cadastro.

#### Rota de cadastro do usuário

```
POST: MEMED_API_URL/sinapse-prescricao/usuarios?api-key={API_KEY}&secret-key={SECRET_KEY}
```

#### Estrutura do payload de cadastro

**Estrutura Obrigatória**

A requisição deve seguir **exatamente** a estrutura de payload (contrato) especificada abaixo. Qualquer desvio desta estrutura resultará em erro de validação:

```
{
  // obrigatório
  "data": {
    "type": "usuarios",
    "attributes": {
      "external_id": "0753879b-362d-4126-9146-a16cf6eb14bd", // Obrigatório
      "nome": "Gustavo", // Obrigatório
      "sobrenome": "Ribeiro Sousa", // Obrigatório
      "cpf": "53076220403", // Obrigatório
      "board": {
            "board_code": "CRM", // Obrigatório
            "board_number": "315435435", // Obrigatório
            "board_state": "SP"}, // Obrigatório
      "email": "gustavo.ribeiro@meuhospital.com", // Opcional
      "telefone": "19938742708", // Opcional
      "sexo": "M", // Opcional
      "data_nascimento": "05/09/1972" // Obrigatório
    },

    // opcional
    "relationships": {
      "cidade": {
        "data": {
          "type": "cidades", // Obrigatório
          "id": 1 // Obrigatório
        }
      },
      "especialidade": {
        "data": {
          "type": "especialidades", // Obrigatório
          "id": 1 // Obrigatório
        }
      }
    }
  }
}
```

#### Dados do prescritor

| Propriedade | Tipo | Obrigatório | Observações |
|---|---|---|---|
| external_id | int/string(255) | ✅ | Recomendável ser do tipo UUID, pois é um campo único |
| nome | string(255) | ✅ |  |
| sobrenome | string(255) | ✅ |  |
| cpf | string(11) | ✅ | Apenas dígitos |
| board_code | string(5) | ✅ | CRM / CRO / COREN / CRMV / CRF / CRN / CREFITO / CRP / CRFa / CREF |
| board_number | string(255) | ✅ | Apenas dígitos |
| board_state | string(2) | ✅ | Siglas dos estados brasileiros |
| email | string(255) |  |  |
| telefone | string(16) |  | Apenas dígitos ou formatado (DDD) XXXXX-XXXX |
| sexo | string(1) |  | M / F |
| data_de_nascimento | date(10) | ✅ | dd/mm/YYYY |
| cidade | int(10) |  | O id da API https://integrations.api.memed.com.br/v1/cidades |
| especialidade | int(10) |  | O id da API https://integrations.api.memed.com.br/v1/especialidades |

**Melhores Práticas para Experiência do Usuário**

Embora diversos campos sejam marcados como opcionais na estrutura de cadastro, é importante compreender que **quanto mais completo for o cadastro inicial, melhor será a experiência** do prescritor na plataforma.

Dados não preenchidos durante a integração precisarão ser completados posteriormente pelo próprio usuário dentro da plataforma de prescrição da Memed, o que pode gerar interrupções no fluxo de trabalho e frustração.

**Recomendação:** Envie o máximo de informações disponíveis durante o processo de cadastro (CPF, e-mail, telefone, sexo, data de nascimento, cidade e especialidade). Esta prática resulta em:

- **Acesso imediato e completo** às funcionalidades da plataforma
- **Redução de etapas** para o prescritor após o primeiro login
- **Onboarding mais ágil** e sem interrupções
- **Dados mais completos** para análises e relatórios

#### Exemplo de requisição de cadastro

Abaixo está um exemplo completo de requisição para cadastrar um novo prescritor. O **token** do usuário será retornado na resposta de sucesso:

- cURL
- Sucesso
- Erro

**Requisição POST**

```
curl --location 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL' \
--header 'Accept: application/vnd.api+json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "type": "usuarios",
    "attributes": {
      "external_id": "0753879b-362d-4126-9146-a16cf6eb14bd",
      "nome": "Gustavo",
      "sobrenome": "Ribeiro Sousa",
      "cpf": "53076220403",
      "board": {
            "board_code": "CRM",
            "board_number": "315435435",
            "board_state": "SP"},
      "email": "gustavo.ribeiro@meuhospital.com",
      "telefone": "19938742708",
      "sexo": "M",
      "data_nascimento": "05/09/1972"
    },
    "relationships": {
      "cidade": {
        "data": {
          "type": "cidades",
          "id": 1
        }
      },
      "especialidade": {
        "data": {
          "type": "especialidades",
          "id": 1
        }
      }
    }
  }
}'
```

##### ✅ Retorno de Sucesso - HTTP 200 OK

```
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "nome": "Jhon",
      "sobrenome": "Doe",
      "cpf": "84168858006",
      "email": "jhon@doe.com",
      "telefone": "(00) 00000-0000",
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I",
      "uf": "MG",
      "crm": "016964"
    }
  }
}
```

##### ❌ Retorno de Erro - HTTP 400 BAD REQUEST

```
{
  "errors": [
    {
      "code": "codigo_do_erro",
      "title": "titulo do erro",
      "detail": "detalhes sobre o erro"
    }
  ]
}
```

**Tratamento de Erros**

As mensagens de erro são específicas para cada situação. Analise cuidadosamente o campo `detail` do erro retornado para identificar e corrigir o problema antes de reenviar a requisição.

**Principais causas de erro:**

- Dados em formato inválido (ex: CPF com letras, data mal formatada)
- Registro profissional não encontrado nos conselhos oficiais
- CPF inválido ou não cadastrado
- E-mail em formato inválido
- Campos obrigatórios ausentes ou vazios
- `external_id` já cadastrado para outro usuário

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/capturar-prescricao-excluida -->
## Como capturar evento de prescrição excluída

O parceiro pode implementar o evento de MdHub que captura os dados de cada prescrição excluída pelo usuário prescritor. Com isso, o parceiro pode ter um controle maior sobre seus dados excluído através da plataforma da Memed.

Para saber como implementar esse evento, leia este [artigo](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-excluida)

A Memed recomenda implementar o evento de [prescrição impressa](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa) em conjunto com esse comando, pois esses são complementares.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/capturar-prescricao-impressa -->
## Como capturar evento de prescrição impressa

O parceiro pode implementar o evento de MdHub que captura os dados de cada prescrição criada pelo usuário prescritor. Com isso, o parceiro pode ter um controle maior sobre seus dados gerados através da plataforma da Memed.

Para saber como implementar esse evento, leia este [artigo](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa)

A Memed recomenda implementar o evento de [prescrição excluída](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-excluida) em conjunto com esse comando, pois esses são complementares.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/configurar-cabecalho-rodape -->
## Configurar cabeçalho e rodapé

## setAdditionalData

Com esse comando é possível adicionar informações extras no cabeçalho e rodapé da receita digital, como dados do paciente, do prescritor, e local do atendimento.

Aqui está um exemplo de como ficaria os dados no cabecalho e rodapé no PDF da receita.

![exemplo-dados-header-footer](https://cdn.memed.com.br/doc/exemplo-dados-header-footer.png)

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-additional-data).

### Configurar o cabeçalho e rodapé via api

O parceiro pode configurar através do cURL para fazer uma requisição para a api. Para saber como utilizá-lo, leia esse [artigo](https://doc.memed.com.br/docs/backend/impressao#configurar-impress%C3%A3o)

Os atributos do `cURL` do artigo acima como `margem_esquerda`, `margem_direita`, `margem_superior`, `margem_inferior`, `tamanho_cabecalho`, `tamanho_rodape`, `mostrar_cabecalho_rodape_simples`, `mostrar_cabecalho_rodape_especial` `header_image` e `footer_image` são utilizados para realizar essa configuração.

### Importar cabeçalho/rodapé de um PDF

É possível importar um cabeçalho e rodapé personalizados através de um arquivo em PDF pela api da Memed. Para saber mais, leia esse [artigo](https://doc.memed.com.br/docs/backend/impressao#importar-cabe%C3%A7alhorodap%C3%A9-de-um-pdf)

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/configurar-dados-prescritor -->
## Configurar dados do prescritor

Para configurar os dados do prescritor, temos esse [artigo](https://doc.memed.com.br/docs/backend/usuario-prescritor#cadastrando-o-prescritor) onde mostra como cadastrar os dados básicos do usuário prescritor. Aqui os cadastros são feitos via api.

Além dos dados básicos, temos um comando MdHub para cadastrar os endereços do prescritor que sairá no receituário, além de cadastrar o local e cidade de atendimento do usuário prescritor.

Para saber mais leia esse [artigo](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-workplace)

Com esses comandos, o usuário prescritor não precisa preencher os seus dados e ajuda na experiência do usuário na geração de prescrições com medicamentos especiais (Ex.: Amoxil). Alguns receituários necessitam de informações adicionais para serem gerados e, caso o parceiro não envie, o usuário terá de preencher.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/documentos-estruturados -->
## Documentos estruturados

### Visão geral

Esta página explica como *estruturar* documentos de texto livre dentro da prescrição, com possibilidade de classificação e associação a diagnósticos **CID-10**. Essa estruturação melhora relatórios clínicos, integrações e rastreabilidade.

**Nova funcionalidade disponível!**

A nova versão do módulo de prescrição médica traz uma funcionalidade essencial: **categorização de documentos de texto livre** e **inclusão de CIDs (Classificação Internacional de Doenças)**.

Essa funcionalidade moderniza o fluxo de prescrição, organizando melhor documentos como:

- **Atestado**
- **Encaminhamento**
- **Laudo**
- **Relatório**
- **Outro documento**

Essas categorias são selecionadas diretamente no item de texto livre da prescrição.

**Vantagens desta melhoria**

Esta nova melhoria visa facilitar a estruturação de documentos médicos, oferecendo:

- Interface mais intuitiva e robusta
- Inclusão formal de diagnósticos com CID
- Melhor organização clínica e rastreabilidade de informações

------------------------------------------------------------------------

### Como utilizar

#### Na interface (Canvas de Prescrição)

1.  No campo de busca da prescrição, digite o nome ou trecho do documento desejado (ex.: "atesta").
2.  Clique na aba **Documentos** para visualizar os modelos disponíveis, já organizados por categoria (*Atestado*, *Encaminhamento*, *Laudo*, *Relatório* ou *Outro documento*).
3.  Selecione o modelo desejado na lista (ex.: "Atestado de afastamento de atividades laborais") para inseri-lo na prescrição já com o tipo de documento associado.
4.  (Opcional) Abra a guia **CID**, pesquise pelo código ou descrição e selecione um ou mais diagnósticos.
5.  (Opcional) Utilize **Salvar como protocolo** para reutilizar este documento em futuras prescrições.
6.  Finalize ou imprima a prescrição normalmente.

**Atenção**

A aba de busca **CID** só será habilitada para inclusão se constar um documento ou medicamento no documento.

**Dica**

O tipo de documento será exibido na impressão e pode ser usado para classificar melhor os documentos clínicos.

------------------------------------------------------------------------

### Inclusão de CID

Após escolher o tipo de documento, a busca por CID será liberada na guia específica:

![Busca por CID](/assets/images/inclusao-cid-ad8d4ee5ec2da1080c58abdab70493cc.png)

Digite parte do nome ou código CID (ex: B16, C34, etc) e selecione a entrada desejada.

**Atenção**

A aba CID só aparecerá quando houver **conteúdo textual preenchido** no item.

### CIDs selecionados

Os CIDs adicionados aparecerão abaixo do documento:

> O paciente pode optar por **compartilhar ou ocultar** o CID no documento impresso.

------------------------------------------------------------------------

### Resumo do fluxo

1.  Insira um item em texto livre.
2.  Escolha o tipo de documento (Atestado, Laudo, etc).
3.  Digite o nome ou código do CID.
4.  Clique na aba "CID" e selecione o diagnóstico.
5.  Verifique se os CIDs foram listados abaixo corretamente.

**Benefícios**

Essa funcionalidade permite padronizar documentos clínicos e associá-los com diagnósticos (CID), oferecendo mais clareza e rastreabilidade para instituições de saúde.

------------------------------------------------------------------------

### Exemplo de estrutura de dados

Abaixo, um exemplo de como as informações de CID e categoria do documento podem ser estruturadas em um objeto de integração:

```
{
  "cids": [
    {
      "id": "c171555",
      "code": "B16",
      "name": "CID",
      "description": "B16 - Hepatite aguda B",
      "category": "cid_atestado",
      "observation": "Paciente solicitou compartilhamento do CID no documento",
      "is_cid": true
    }
  ],
  "medicamentos": [
    {
      // ... outros campos do medicamento ...
      "custom_categoria": "atestado"
    }
  ]
}
```

> **Nota:**  
> O campo `custom_categoria` indica a categoria selecionada para o documento (ex: "atestado").  
> O array `cids` traz os diagnósticos associados, incluindo observações relevantes.

------------------------------------------------------------------------

### Busca e favoritos de modelos por CID

**Nova funcionalidade disponível!**

Os modelos de prescrição (protocolos) agora também podem ser encontrados por CID e marcados como favoritos direto no painel de Modelos da prescrição, facilitando a reutilização dos modelos mais relevantes para cada diagnóstico.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/fechar-modulo-plataforma -->
## Como fechar o módulo da plataforma prescrição

Se o módulo de prescrição da Memed estiver no modo [tela inteira](https://doc.memed.com.br/docs/modos-de-exibicao#tela-inteira), a Memed disponibiliza o comando `hide` para fechar o módulo. Para saber mais leia esse [artigo](https://doc.memed.com.br/docs/frontend/comandos-mdhub/hide).

Caso o módulo de prescrição da Memed estiver no modo [incoporado](https://doc.memed.com.br/docs/modos-de-exibicao#incorporado), ou seja, dentro de um container HTML `<div>`, o parceiro pode fechar o módulo no próprio contexto da aplicação escondendo o módulo que está dentro da `<div>` via javascript.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/gestao-do-prescritor -->
## Gestão do prescritor

Para executar os comandos do paciente é necessário que o módulo da Memed seja [completamente carregado](https://doc.memed.com.br/docs/primeiros-passos#renderizando-a-prescri%C3%A7%C3%A3o-digital), após isso temos acesso ao MdHub para a execução de nosso comandos.

## Set Workplace

É possível resgatar o endereço do prescritor de seu sistema para preenchê-lo no receituário Memed. Dessa forma, o prescritor não precisa escrever manualmente seu endereço nas opções de receituário. É comum que o prescritor atenda em diferentes lugares durante sua jornada de trabalho. Pensando nessa situação, criamos o comando Javascript setWorkplace.

Através desse comando é possível adicionar dados do prescritor como:

- Cidade do local de trabalho;
- UF do local de trabalho
- Cadastro Nacional de Estabelecimentos de Saúde
- Nome do local de trabalho
- Endereço completo com número
- Telefone do prescritor

Com isso, o prescritor não precisará preencher os seus dados quando for prescrever um medicamento controlado, pois eles já foram preenchidos com esse comando.

Abaixo há um exemplo de como ficaria o PDF da receita com os dados do prescritor preenchidos:

![pdf-impresso](https://cdn.memed.com.br/doc/pdf-impresso.webp)

Veja um exemplo de código utilizando o comando `setWorkPlace` abaixo:

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-workplace)

## setAdditionalData

Com esse comando é possível adicionar informações extras no cabeçalho e rodapé da receita digital, como dados do paciente, do prescritor, e local do atendimento.

Aqui está um exemplo de como ficaria os dados no cabecalho e rodapé no PDF da receita.

![exemplo-dados-header-footer](https://cdn.memed.com.br/doc/exemplo-dados-header-footer.png)

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-additional-data).

## Formulário de Alto Custo

CNES do estabelecimento (pode ser alterado de acordo com o local de atendimento do prescritor)

![formulario-alto-custo](https://cdn.memed.com.br/doc/formulario-alto-custo.webp)

## Trocar usuário (SPA)

Caso sua aplicação seja do tipo SPA (Single Page Application) e não faça refresh após a ação de login/logout, você pode redefinir o token do usuário logado utilizando o código abaixo

```
MdSinapsePrescricao.setToken('TOKEN_DO_NOVO_USUARIO');
```

## Ativar tema nas opções de receituário

Agora que você já [sabe cadastrar um tema](https://doc.memed.com.br/docs/backend/impressao#configurar-impress%C3%A3o), podemos chavear qual é o tema ativo ao iniciar a prescrição.

```
MdHub.command.send('plataforma.sdk', 'find', {
    resource: 'opcoes-receituario/ativar/2',
    cache: false,
});
```

Com esse comando, será enviada uma requisição para nosso backend, ativando o tema 2 cadastrado nas opções de receituário.

**info**

É importante que valor de cache sempre seja `false` para esse comando

**Limpar o local storage do navegador web** A limpeza do local storage do navegador é necessária quando prescritores compartilham a mesma máquina (notebook/pc). Ela deve ser implementada OBRIGATORIAMENTE para evitar conflitos de informações entre os cadastros e consequentemente falhas de segurança. Através do objeto `MdHub`, pode-se chamar o método abaixo para realizar a limpeza do local storage:

```
MdHub.command.send('plataforma.sdk', 'logout');
```

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/gestao-paciente -->
## Gestão do paciente

A Memed disponibiliza os seguintes comandos para realizar a gestão do paciente:

- [setPacient](https://doc.memed.com.br/docs/como-fazer/gestao-paciente#setpacient)
- [setAllergy](https://doc.memed.com.br/docs/como-fazer/gestao-paciente#setallergy)
- [categoryConditions](https://doc.memed.com.br/docs/como-fazer/gestao-paciente#categoryconditions)
- [addItem](https://doc.memed.com.br/docs/como-fazer/gestao-paciente#additem)
- [setFeatureToggle](https://doc.memed.com.br/docs/como-fazer/gestao-paciente#setfeaturetoggle)

#### Definir Pacientes (setPacient)

Este comando possibilita ao parceiro configurar o envio previamente dos dados do paciente para a plataforma de prescrição da Memed. Ou seja, assim que a plataforma de prescrição for carregada, os dados do paciente estarão previamente preenchidos, e o usuário prescritor não precisará preenchê-los.

Para saber como implementar esse comando leia este artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient)

#### setAllergy

Este comando possibilita ao parceiro configurar o envio previamente das alergias do seu paciente à Memed para que o usuário prescritor. Assim este não precisa cadastrar as alergias do paciente dentro da plataforma, e proporciona maior segurança ao paciente no momento de prescrever. Ou seja, assim que a plataforma de prescrição for carregada, essas alergias já estarão cadastradas no paciente.

Para saber como implementar esse comando leia este artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-allergy)

#### categoryConditions

Este comando possibilita ao usuário prescritor receber alertas após inserir um determinado medicamento na plataforma, e caso este medicamento oferecer algum risco ao paciente com condições específicas, como exemplo aeronautas e pacientes com risco de dopagem, um alerta irá aparecer na plataforma.

Para saber como implementar esse comando leia este artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient#category-condition)

#### addItem

Este comando possibilita ao parceiro configurar o envio previamente dos medicamentos ou exames que serão receitados para o paciente na plataforma de prescrição da Memed. Ou seja, assim que a plataforma de prescrição for carregada, esses medicamentos já estarão no receituario do paciente.

Para saber como implementar esse comando leia este artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/add-item)

#### setFeatureToggle

Este comando possibilita ao parceiro realizar configurações que habilite ou não algumas ações do usuário prescritor sobre os dados do paciente. Por exemplo:

- `deletePatient` Permite que o prescritor exclua o paciente da base de dados.
- `removePatient` Permite que o prescritor remova o paciente da prescrição.
- `editPatient` Permite que o prescritor edite os dados do paciente na base de dados.
- `setPatientAllergy` Permite que o prescritor registre alergias conhecidas do paciente.
- `conclusionModalEdit` Permite que o prescritor visualize o botão de protocolos.
- `editIdentification` Controla se é permitido editar ou não os dados já preenchidos nos campos da tela de identificação de prescritor e paciente no fluxo de prescrição
- `addPrescriptionDrug` Permite que o prescritor utilize o botão de adicionar medicamentos
- `removePrescriptionDrug` Permite que o prescritor utilize o botão de excluir medicamentos
- `editPrescriptionDrugTitle` Permite ao prescritor a edição do nome do medicamento quando este for texto livre

Para saber como implementar esse comando leia este artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle)

#### Veja como ficaria um exemplo após implementar esses 5 comandos ao mesmo tempo:

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/impressao-medico -->
## Configurar impressão do prescritor

A Memed disponibiliza comandos via MdHub e API para configurar os dados que serão impressos no PDF da receita.

### Os seguintes comandos utilizam o MdHub:

## Set Workplace

É possível resgatar o endereço do prescritor de seu sistema para preenchê-lo no receituário Memed. Dessa forma, o prescritor não precisa escrever manualmente seu endereço nas opções de receituário. É comum que o prescritor atenda em diferentes lugares durante sua jornada de trabalho. Pensando nessa situação, criamos o comando Javascript setWorkplace.

Através desse comando é possível adicionar dados do prescritor como:

- Cidade do local de trabalho;
- UF do local de trabalho
- Cadastro Nacional de Estabelecimentos de Saúde
- Nome do local de trabalho
- Endereço completo com número
- Telefone do prescritor

Com isso, o prescritor não precisará preencher os seus dados quando for prescrever um medicamento controlado, pois eles já foram preenchidos com esse comando.

Abaixo há um exemplo de como ficaria o PDF da receita com os dados do prescritor preenchidos:

![pdf-impresso](https://cdn.memed.com.br/doc/pdf-impresso.webp)

Veja um exemplo de código utilizando o comando `setWorkPlace` abaixo:

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-workplace)

## setAdditionalData

Com esse comando é possível adicionar informações extras no cabeçalho e rodapé da receita digital, como dados do paciente, do prescritor, e local do atendimento.

Aqui está um exemplo de como ficaria os dados no cabecalho e rodapé no PDF da receita.

![exemplo-dados-header-footer](https://cdn.memed.com.br/doc/exemplo-dados-header-footer.png)

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-additional-data).

#### Find

Com esse comando é possível alterar o tema da prescrição do prescritor. Cada prescritor possui até 4 temas, e cada tema tem personalizações diferentes. Os temas podem ser trocados pelo prescritor dentro da plataforma de prescrição ou via comando MdHub.

Para saber mais sobre esse comando, leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/find)

#### Estilizar a prescrição

É possível estilizar a cor primária da prescrição digital Memed para se adequar a cor primária do seu sistema.

Segue um exemplo de como mudar a cor da prescrição digital no modo de carregamento estático:

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/frontend/estilizar-front)

### Os seguintes comandos utilizam api da Memed:

## Configurar Impressão

Esse comando permite personalizar algumas configurações relacionadas à impressão do PDF da receita, como margens, cabeçalho, rodapé, fonte, entre outros do PDF da receita.

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/backend/impressao#configurar-impress%C3%A3o)

## Importar um cabeçalho e/ou rodapé do PDF da receita

A Memed disponibiliza uma forma de importar um cabeçalho e/ou rodapé com base em um template (PDF). Este é enviado para a Memed através da api, e assim será usado como imagem de fundo na prescrição.

Para mais informações sobre esse comando leia esse artigo [aqui](https://doc.memed.com.br/docs/backend/impressao#importar-cabe%C3%A7alhorodap%C3%A9-de-um-pdf)

## Remover o cabeçalho e/ou rodapé do PDF da receita

É possível remover cabeçalho e/ou rodapé através da api da Memed. Para saber como, leia esse artigo [aqui](https://doc.memed.com.br/docs/como-fazer/removendo-cabecalho-rodape)

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/manter-responsividade-prescricao -->
## Manter a responsividade da aplicação embedded

Como os monitores de vídeos possuem diversos tamanhos e, também, o parceiro pode colocar a plataforma prescrição no modo embedded, a Memed pode se adaptar aos diversos tamanhos. Ou seja, a plataforma de prescrição da Memed é responsiva.

### Como fazer a plataforma de prescrição ficar responsiva?

A plataforma precisa ser carregada de forma [incorporada](https://doc.memed.com.br/docs/modos-de-exibicao#incorporado)

Nesta forma de incorporada, precisa-se definir o nome da propriedade do `data-container`, e dentro do código HMTL, o nome do elemento identificador da `div` que conterá o conteúdo da plataforma prescrição conforme exemplo abaixo:

```
<script
  src="https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js"
  data-token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I"
  data-container="minha-prescricao"
></script>

<div id="minha-prescricao"></div>
```

Após definir as configurações acima, precisa-se definir as estilizações `CSS` do elemento `minha-prescricao`. Exemplo:

```
#minha-prescricao {
    position: relative;
    width: 100%;
    height: 100%;
    min-width: 820px;
    min-height: 700px;
}
```

Com isso, a plataforma de prescrição ocupará 100% da largura e altura do tamanho que a `div` tiver, porém terá o tamanho mínimo de 820px largura e 700px de altura.

**Obs:** A plataforma de prescrição precisa de um container (div) com a largura e altura mínima de, respectivamente, 820px e 700px. Caso esses valores forem menores, a visualização ficará prejudicada.

Veja um exemplo completo abaixo:

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/memed-modo-edicao -->
## Abrir modulo da Memed em modo de edição

Abrir o modo de edição de prescrição é muito simples, você precisará chamar o comando responsável por exibir o preview através do `MdHub` e passar as seguintes informações:

- Nome do modulo `plataforma.prescricao`
- Nome do comando `viewPrescription`
- Id da prescrição

Quando o comando `viewPrescription` é executado, uma prévia da prescrição selecionada é exibida, conforme exemplo abaixo, e as ações que podem ser executadas são a reemissão ou criação de uma cópia da prescrição.

![tela-impressao.png](https://cdn.memed.com.br/doc/tela-impressao.png)

### Como executar o comando

Abaixo temos um exemplo de como pode ser feita a chamada do comando `viewPrescription`. Recuperando o botão com o id `btnViewPrescription`, escutamos o evento de `click` e passamos a chamada para o modulo de prescrição enviando o comando de visualização da prescrição através do `MdHub`.

A resposta desse comando é assincrona e retorna `true` quando o preview é aberto. Caso seja passado um `id` inexistente na nossa base, o preview ainda irá abrir, mas exibirá a mensagem de id não encontrado.

Segue o exemplo da execução do comando.

```
document
  .getElementById("btnViewPrescription")
  .addEventListener("click", function() {
    MdHub.command.send(
      'plataforma.prescricao',
      'viewPrescription',
      ID_DA_PRESCRICAO
    );
});
```

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/mudar-fonte-pdf -->
## Mudar a fonte do PDF da receita

A Memed possibilita alterar o tamanho da fonte, e o tipo de fonte no PDF da receita.

**Obs:** Recomendamos utilizar tamanhos de fontes menores que 18, pois acima deste valor e dependendo da quantidades de dados no PDF da receita, poderá haver sobreposição de textos.

### Mudar fonte do PDF da receita via API

Dentro desse [artigo](https://doc.memed.com.br/docs/backend/impressao) existe uma explicação de como utilizar um cURL para alterar as configurações de impressão.

Mas para alterar somente o tamanho e o tipo da fonte da prescrição, prescisa-se utilizar as propriedades `titulo_tamanho_fonte`, `titulo_fonte`, `rodape_fonte`, `rodape_tamanho_fonte`, `subtitulo_fonte` e `subtitulo_tamanho_fonte`.

Os atributos `titulo_tamanho_fonte` e `titulo_fonte` se referem aos textos do cabeçalho. Os atributos `rodape_fonte` e `rodape_tamanho_fonte` se referem aos textos do rodapé. Os atributos `subtitulo_fonte` e `subtitulo_tamanho_fonte` se referem aos textos do corpo da prescrição.

Pode-se também alterar as cores da fonte editando as propriedades `titulo_cor`, `rodape_cor` e `subtitulo_cor`. Os valores podem ser em hexadecimal.

Segue um exemplo de cURL abaixo de como ficaria essas configurações:

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
        "type": "configuracoes-prescricao",
        "attributes": {
                "indice": 1,
                "titulo_fonte": "Droid Serif Italic",
                "titulo_tamanho_fonte": 22,
                "titulo": "Dr. Teste da Silva Teste",
                "titulo_cor": "#20afd6",
                "subtitulo_fonte": "Proxima Nova",
                "subtitulo_tamanho_fonte": 6,
                "subtitulo": "",
                "subtitulo_cor": "#8c8c8c",
                "tamanho_cabecalho": 1,
                "rodape_fonte": "Proxima Nova",
                "rodape_tamanho_fonte": 14,
                "rodape": "",
                "rodape_cor": "#8c8c8c",
                "tamanho_rodape": 8,
                "modelo_cabecalho_rodape": 0,
                "ativo": true,
                "imprimir_controle_especial": false,
                "imprimir_controle_especial_antibioticos": true,
                "imprimir_controle_especial_c4": false,
                "imprimir_lme": false,
                "zoom_logo": 65,
                "header_image": "parceiros\/templates\/parceiro-template-552-39456-header.jpeg",
                "footer_image": "parceiros\/templates\/parceiro-template-552-39456-footer.jpeg",
                "number_of_lme_copies": 1
            }
     }
}'
```

O atributo `indice` com valor 1 se refere ao modelo 1 do PDF da receita. Lembrando que a Memed disponibiliza 4 tipos de modelos para cada usuário prescritor. Se preferir editar o modelo 2 do PDF da receita, coloque o valor 2 no atributo `indice`.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/obter-dados-usuario -->
## Obter dados do Usuário (prescritor)

O token de acesso do usuário prescritor é retornado junto com todos os outros dados do usuário. [Veja abaixo](#obtendo-os-dados-do-usu%C3%A1rio-prescritor) como recuperar os dados do usuário e o token de acesso.

**Atenção**

O **token** não é estático, portanto sempre que for fazer uma requisição na **API Memed**, você precisa recuperar o último token válido do usuário.

#### Obtendo os dados do usuário prescritor

Para consultar os dados completos de um prescritor, incluindo seu **token de acesso**, realize uma requisição **GET** na API da Memed utilizando a rota de usuários.

**Parâmetros necessários:**

- **Identificador do usuário** (veja opções abaixo)
- **Par de chaves** (API Key + Secret Key)

**Token de Acesso**

O **token de acesso** do usuário prescritor é retornado automaticamente junto com todos os demais dados do usuário na resposta da requisição.

**Identificadores Válidos**

O **identificador do usuário** pode ser informado de três formas diferentes:

- **CPF:** Apenas números (11 dígitos)
- **External ID:** Identificador único definido pelo seu sistema
- **Registro + UF:** Número do registro profissional seguido da sigla do estado (Ex: `12345SP`, `01234MG`)

> **Tipos de registro aceitos:** CRM, CRO, COREN, CRMV, CRF, CRN, CREFITO, CRP, CRFa, CREF

#### Rota para obter os dados do usuário

```
GET: MEMED_API_URL/sinapse-prescricao/usuarios/{ID_USUARIO}?api-key=API_KEY&secret-key=SECRET_KEY
```

#### Exemplo de requisição

Abaixo está um exemplo completo de requisição para obter os dados e o **token de acesso** do usuário.

- cURL
- Sucesso
- Erro

##### Requisição GET

```
curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/1234?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL'\
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

##### ✅ Retorno de Sucesso - HTTP 200 OK

```
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "nome": "Jhon",
      "sobrenome": "Doe",
      "cpf": "84168858006",
      "email": "jhon@doe.com",
      "telefone": "(00) 00000-0000",
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I",
      "uf": "SP",
      "crm": "016964"
    }
  }
}
```

##### ❌ Retorno de Erro - HTTP 404 NOT FOUND

```
{
  "errors": [
    {
      "title": "Erro",
      "detail": "Nenhum usuário encontrado com este este CRM, CPF ou Id: 1234"
    }
  ]
}
```

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/removendo-cabecalho-rodape -->
## Remover cabeçalho e rodapé

Para entender como funciona a remoção de cabeçalho e rodapé, é preciso primeiro entender o que são esses elementos.

O cabeçalho e o rodapé são informações adicionais que aparecem na prescrição, além das informações principais sobre os medicamentos prescritos. O cabeçalho geralmente contém informações sobre o prescritor que fez a prescrição, como nome, registro profissional e especialidade. O rodapé, por sua vez, pode conter informações como o endereço e telefone do consultório ou clínica, o número da receita entre outras informações.

### Como fazer a remoção do cabeçalho e rodapé

#### Removendo através dos atributos header e footer

A remoção do cabeçalho e rodapé pode ser feita através dos parametros `header_image` e `footer_image`, esses atributos são do tipo string e ao passar uma string vazia o cabeçalho/rodapé atual é removido. A alteração é feita no indice que deve ser passado junto na requisição nas opções de receituário. A remoção é feita através do endpoint `/opcoes-receituario`. Confira como deve ser feita a requisição abaixo:

- cURL
- Sucesso
- Erro

**Requisição POST**

```
    curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNjk0LCJjZDFlNDU5NjYwYjQ2MDYwMzdhNmFiZDI0YTliOTJiOSIsIjIwMjEtMDUtMjciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMjcwOTYiXQ._dCco9H_BkJccPOPn82CbtFxDfVdvA1vzpSIu3OG8xA' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
    "type": "configuracoes-prescricao",
        "attributes": {
            ... // todos parametros retornados no opções de receituário
            indice: 2,
            "header_image": "",
            "footer_image": "",
        }
    }
}'
```

**Retorno: Http status 201 - Created**

```
{
    "data": {
        "type": "configuracoes-prescricao",
        "attributes": {
            ... // todos parametros retornados no opções de receituário
            indice: 2,
            "header_image": "",
            "footer_image": "",
        },
        "links": {
            "self": "https:\/\/integrations.api.memed.com.br\/v1\/configuracoes-prescricao\/3422"
        },
        "id": 3422
    },
    "links": {
        "self": "https:\/\/integrations.api.memed.com.br\/opcoes-receituario\/3422"
    }
}
```

**Retorno: Http status 403 - Forbidden**

```
{
    "errors": [
        {
            "title": "Erro",
            "detail": "Ocorreu um erro inesperado, por favor contate o nosso suporte."
        }
    ]
}
```

Antes da remoção:

![receita com cabeçalho](https://cdn.memed.com.br/doc/receita-com-cabecalho.png)

Depois da remoção:

![receita sem cabeçalho](https://cdn.memed.com.br/doc/receita-sem-cabecalho.png)

#### Controlando a exibição do cabeçalho e rodapé

A exibição de cabeçalho e rodapé em uma prescrição médica pode ser personalizada de duas maneiras diferentes na API: usando os atributos `mostrar_cabecalho_rodape_simples` e `mostrar_cabecalho_rodape_especial`.

O atributo `mostrar_cabecalho_rodape_simples` é utilizado para exibir um cabeçalho e rodapé simples na prescrição médica. Esse cabeçalho e rodapé incluirá informações básicas, como o nome e registro profissional do prescritor, a data da prescrição, o nome do paciente e a data de nascimento. Para utilizar esse atributo, basta defini-lo como `1` para exibir ou `0` para não exibir passando no corpo da solicitação da API.

O atributo `mostrar_cabecalho_rodape_especial`, por sua vez, permite que o prescritor personalize o cabeçalho e rodapé da prescrição médica de acordo com suas necessidades. Com esse atributo, o prescritor pode incluir informações adicionais, como o logotipo da clínica, informações de contato e instruções especiais para o paciente. Para utilizar esse atributo, basta defini-lo como `1` para exibir ou `0` para não exibir passando no corpo da solicitação da API.

Abaixo como a requisição deve ser feita.

- cURL
- Sucesso
- Erro

**Requisição POST**

```
    curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNjk0LCJjZDFlNDU5NjYwYjQ2MDYwMzdhNmFiZDI0YTliOTJiOSIsIjIwMjEtMDUtMjciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMjcwOTYiXQ._dCco9H_BkJccPOPn82CbtFxDfVdvA1vzpSIu3OG8xA' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
    "type": "configuracoes-prescricao",
        "attributes": {
            ... // todos parametros retornados no opções de receituário
            indice: 1,
            "mostrar_cabecalho_rodape_simples": 1,
            "mostrar_cabecalho_rodape_especial": 0,
        }
    }
}'
```

**Retorno: Http status 201 - Created**

```
{
    "data": {
        "type": "configuracoes-prescricao",
        "attributes": {
            ... // todos parametros retornados no opções de receituário
            indice: 1,
            "mostrar_cabecalho_rodape_simples": 1,
            "mostrar_cabecalho_rodape_especial": 0,
        },
        "links": {
            "self": "https:\/\/integrations.api.memed.com.br\/v1\/configuracoes-prescricao\/3422"
        },
        "id": 3422
    },
    "links": {
        "self": "https:\/\/integrations.api.memed.com.br\/opcoes-receituario\/3422"
    }
}
```

**Retorno: Http status 403 - Forbidden**

```
{
    "errors": [
        {
            "title": "Erro",
            "detail": "Ocorreu um erro inesperado, por favor contate o nosso suporte."
        }
    ]
}
```

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/reordenacao-busca -->
## Reordenação das abas da busca

A busca é dividida em abas e cada uma delas tem seu nome de identificação de acordo com os tipos de resultados retornados. Os nomes são:

```
["industrializados", "composicoes", "manipulados", "perifericos", "exames"]
```

Essa é a ordem padrão dos resultados. Para fazer a reordenação das abas, basta alterar a ordem dos nomes citados acima, e fazer uma requisição para o endpoint de configurações do prescritor passando a nova ordem das abas da busca.

Para fazer a requisição você precisará passar o token do prescritor via query params. O token é recuperado através da nova API, veja como recuperar [aqui](https://doc.memed.com.br/docs/backend/usuario-prescritor#obtendo-os-dados-do-usu%C3%A1rio-prescritor).

Abaixo um exemplo da requisição para alterar a ordenação.

- cURL
- Sucesso
- Erro

**Requisição POST**

```
    curl --request POST \
    --url 'https://integrations.api.memed.com.br/v1/medicos-configuracoes?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNjk0LCJjZDFlNDU5NjYwYjQ2MDYwMzdhNmFiZDI0YTliOTJiOSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMjcwOTYiXQ.j9KDNyz1jZR08DF2D-_uNpMH6peXRTDanYWWGGHlsoQ' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json' \
    --data '{
      "data": {
        "type": "medicos-configuracoes",
        "attributes": {
          "chave": "tab_orders",
          "valor": [
            "exames",
            "composicoes",
            "industrializados",
            "perifericos",
            "manipulados"
          ]
        }
      }
    }'
```

**Retorno: Http status 200 - OK**

```
{
    "data": {
        "type": "medicos-configuracoes",
        "attributes": {
            "chave": "tab_orders",
            "valor": [
                "exames",
                "composicoes",
                "industrializados",
                "perifericos",
                "manipulados"
            ],
            "metadata": null
        },
    },
}
```

**Retorno: Http status 403 - Forbidden**

```
{
  "errors": [
    {
            "title": "Erro",
            "detail": "A configuração solicitada não existe."
        }
  ]
}
```

O atributo `chave` passa o valor `tab_orders`. Este comunica para nossa aplicação qual configuração você quer alterar. A nova ordem das abas deve ser passada dentro de `data.attributes.valor` e os nomes devem ser passados dentro de um array, contendo apenas os nomes conhecidos por nossa aplicação, sem acentuação.

---

<!-- fonte: https://doc.memed.com.br/docs/como-fazer/validar-dados-prescritor-cfm -->
## Validação de Dados de Prescritores no CFM

Esta documentação orienta o processo de adequação dos dados obrigatórios do prescritor, tendo em vista a nova regulamentação da ANVISA sobre prescrição digital de medicamentos de controle especial. Ao longo dela você encontra: como testar a validação sem alterar nada (dry-run), como atualizar o cadastro em produção quando os dados precisarem de correção, quais campos são cobertos nesta v1, o que a validação não garante e as perguntas mais frequentes sobre o processo.

**ATENÇÃO: VIGÊNCIA EM 30/09/2026**

A partir de 30/09/2026, conforme a regulamentação da ANVISA sobre prescrição digital de medicamentos de controle especial, entra em vigência a disponibilização de receituários de controle especial digital. Prescritores com dados cadastrais divergentes dos registrados em seu respectivo conselho profissional não emitem receituário de controle especial nem acessam a Memed a partir dessa data. Valide e corrija sua base com antecedência.

**VALIDAÇÃO AUTOMATIZADA DISPONÍVEL APENAS PARA O CFM**

A Memed disponibiliza atualmente rota de validação automatizada apenas para registros no CFM. A conferência de registros de outros conselhos profissionais (CFO e demais) deve ser tratada diretamente com o time Memed: entre em contato com o time de Customer Success (CX) da Memed para alinhar o processo de sanitização da sua base.

**DADOS DE EXEMPLO**

Os exemplos utilizam dados fictícios. Em produção, trate dados pessoais de prescritor conforme a LGPD.

### Quando usar esta validação​

Valide, sem persistir nada, se nome, data de nascimento, CRM, UF e CPF de um prescritor conferem com o registro no CFM, usando a rota de validação `POST /v1/sinapse-prescricao/usuarios/validate-board`. CRM e UF são campos separados no payload: não envie o número do CRM concatenado com a sigla do estado (envie `board_number: "123456"` e `board_state: "SP"`, e não `board_number: "123456-SP"`). Use essa rota para sanear sua base antes de emitir prescrições e, se necessário, atualize o cadastro em produção. Ela é útil especialmente para:

- Parceiros com prescritores cujos dados cadastrais estejam incompletos ou inconsistentes em relação ao CFM, estejam eles ativos ou já inativados.
- Saneamento em lote da base de prescritores antes de 30/09/2026.
- Testar uma correção de cadastro antes de aplicá-la de fato via `PATCH`.

### Visão geral do fluxo​

### Rota de validação (dry-run)​

```
POST: MEMED_API_URL/sinapse-prescricao/usuarios/validate-board?api-key=API_KEY&secret-key=SECRET_KEY
```

**Autenticação desta rota**

Esta rota segue o mesmo padrão de autenticação das demais rotas de usuários: `api-key` e `secret-key` como parâmetros de URL (veja [Usuário Prescritor](https://doc.memed.com.br/docs/backend/usuario-prescritor)).

A validação não persiste dados, i.e., nenhum cadastro é criado, alterado ou reativado nesta chamada.

#### Campos validados​

| Propriedade | Tipo | Obrigatório | Observações |
|---|---|---|---|
| nome | string(255) | ✅ | Nome civil, exatamente como registrado no CFM |
| sobrenome | string(255) | ✅ | Sobrenome do prescritor, exatamente como registrado no CFM |
| cpf | string(11) | ✅ | Apenas dígitos |
| data_nascimento | date(10) | ✅ | dd/mm/YYYY |
| board.board_code | string(5) | ✅ | Esta documentação cobre o fluxo com CRM |
| board.board_number | string(255) | ✅ | Apenas dígitos |
| board.board_state | string(2) | ✅ | Sigla do estado (UF) |
| external_id | int/string(255) | ✅ | Identificador do prescritor no seu sistema |

**Sobre o campo nome : nome civil x nome social**

O CFM registra o prescritor pelo nome civil. Se o seu cadastro guarda o nome social, a divergência com o CFM é esperada; envie o nome civil neste campo. Outras causas comuns de divergência: acentuação diferente, abreviações, sobrenome desatualizado após ele ou ela ter casado ou se separado, e sobrenomes compostos grafados de forma diferente da registrada no CFM.

Nesta v1, apenas estes 4 campos (nome, data de nascimento, CRM, UF e CPF) são validados contra o CFM. RQE, especialidade e número de cadastro ANVISA ficam para fases posteriores.

#### Exemplo de requisição​

- cURL
- Sucesso
- Erro

```
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

```
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

```
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

#### Códigos de resposta​

| HTTP | Situação | Quando acontece |
|---|---|---|
| 200 | Aprovado | Os 4 campos passaram na validação local e no CFM |
| 400 | Reprovado | Input inválido, duplicidade local (mesmo CRM ou external_id já cadastrado) ou dados reprovados pelo CFM |
| 401 | Não autorizado | api-key / secret-key ausentes ou inválidas |
| 429 | Limite excedido | Rate limit da rota foi ultrapassado |
| 503 | Indisponível | Serviço de validação do CFM indisponível ou desabilitado no ambiente |

### Rota de atualização de cadastro​

Depois de validar, use esta rota para corrigir os dados no cadastro real do prescritor. Ela valida novamente no CFM durante o próprio update e, se os dados forem aceitos, **reativa** o prescritor automaticamente.

**CAMPOS OBRIGATÓRIOS PARA REATIVAÇÃO AUTOMÁTICA**

Para que o prescritor seja reativado automaticamente, envie todos os campos obrigatórios (nome, sobrenome, data de nascimento, CRM, UF e CPF) no `PATCH`, não apenas o campo que você está corrigindo. Se enviar, por exemplo, somente o CPF ou apenas a data de nascimento, o CFM não valida os demais campos e o prescritor não é reativado, mesmo que a resposta seja `200`.

```
PATCH: MEMED_API_URL/sinapse-prescricao/usuarios/{EXTERNAL_ID}?api-key=API_KEY&secret-key=SECRET_KEY
```

- cURL
- Sucesso
- Erro

```
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

```
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

```
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

**ATUALIZANDO O external_id**

Só inclua o campo `external_id` no payload se você realmente deseja alterar seu valor. Para atualizações comuns (nome, data de nascimento, CRM, UF, CPF), não inclua esse campo.

### O que esta validação não garante​

No retorno `200` (aprovado), confirma-se apenas que nome, data de nascimento, CRM, UF e CPF foram aceitos. Isso não atesta:

- Aptidão para emissão de Notificação de Receita (RQE, especialidade) ou outras categorias de receituário controlado que dependam de campos além destes 4.
- Validade do número de cadastro ANVISA.
- Que o prescritor está apto em todas as categorias de receituário: apenas nas que dependem exclusivamente destes 4 campos.

**Status do médico no conselho**

O status do prescritor no conselho (ativo, inativo ou suspenso) não é retornado como campo explícito da resposta nesta v1. A validação usa esse status internamente (um CRM inativo ou suspenso reprova a validação), mas o parceiro recebe apenas o resultado agregado de aprovação/reprovação.

### Limitações conhecidas​

- **Indisponibilidade do CFM:** o CFM pode ficar temporariamente indisponível. Nesse cenário a resposta é `503`; tente novamente mais tarde, pois não é um erro definitivo do cadastro.
- **O CFM valida os 4 campos em conjunto:** nome, data de nascimento, CRM, UF e CPF. Uma divergência em qualquer um deles pode levar à reprovação da validação.
- **Retorno genérico em caso de reprovação:** o CFM informa apenas que os dados não conferem, sem detalhar qual campo específico está incorreto. Ao receber `400`, revise os 4 campos em conjunto.
- **Rate limit:** por padrão, até 120 requisições por hora por parceiro. Ao exceder, a resposta é `429`.
- **Duplicidade de `external_id`:** cenários de duplicidade não são tratados nesta versão. Se o `external_id` enviado já existir para outro cadastro, trate isso na sua integração antes de chamar o endpoint.

### Perguntas frequentes​

**Recebi `400` mesmo achando que os dados estão corretos. O que faço?** Confira primeiro se o CRM e a UF correspondem ao registro ativo do prescritor no CFM. Revise também se nome, data de nascimento e CPF foram digitados exatamente como no seu cadastro de origem. Atenção especial ao formato da data de nascimento: ela deve ser enviada como `DD/MM/AAAA`. Datas em formato diferente do indicado (por exemplo, `AAAA-MM-DD`) ou com alguma parte ausente (ano, mês ou dia) são consideradas inválidas e retornam `400`, mesmo que o restante do cadastro esteja correto. Teste novamente pela validação (dry-run) antes de atualizar o cadastro real.

**Recebi `503`. Preciso abrir chamado?** Não. Esse retorno indica indisponibilidade temporária do CFM. Aguarde alguns minutos e tente novamente.

**O prescritor usa nome social. A validação vai reprovar?** Possivelmente sim, se o nome social divergir do nome civil registrado no CFM. Envie o nome civil completo no campo `nome`.

**A resposta traz o status do médico no conselho (ativo/inativo/suspenso)?** Não nesta v1. A validação considera esse status internamente, mas o campo explícito não é retornado ao parceiro.

**Quando devo acionar o time de CX da Memed?** Apenas em casos de exceção ou insucesso persistente: quando a mesma tentativa continuar sendo reprovada após múltiplas tentativas em dias diferentes, ou quando você suspeitar de um problema no lado da Memed.

### Próximos passos​

| Tópico | Documentação |
|---|---|
| Cadastro completo do prescritor | Usuário Prescritor |
| Boas práticas de integração | Boas Práticas de Integração |
| Solução de problemas | Erros comuns |
| Dúvidas gerais | Dúvidas Frequentes |
