---
name: memed-prescricao
description: Integração com a prescrição digital Memed (receita digital) em sistemas de saúde — backend (API REST, cadastro/token do prescritor, prescrições, protocolos, opções de receituário) e frontend (script sinapse-prescricao, MdSinapsePrescricao, MdHub, comandos como setPaciente/setWorkplace/setFeatureToggle/addItem, eventos como prescricaoImpressa/prescricaoExcluida), homologação, credenciais de produção, assinatura digital e solução de erros. Use esta skill sempre que o usuário mencionar Memed, receita digital/prescrição eletrônica em prontuário, MdHub, MdSinapsePrescricao, integrations.api.memed.com.br, "data-token", ou pedir para integrar, depurar, revisar ou homologar uma integração de prescrição digital — mesmo que não diga "Memed" explicitamente mas esteja num código que a usa.
---

# Integração com a prescrição digital Memed

A Memed é uma plataforma de prescrição digital que o seu software embute via script JavaScript. A integração tem duas metades que **precisam** ficar separadas:

- **Backend** (seu servidor): guarda `API_KEY`/`SECRET_KEY`, cadastra/consulta o prescritor na API REST da Memed e obtém o **token do prescritor**.
- **Frontend** (navegador): carrega o script Memed com `data-token=<token>`, envia comandos (`MdHub.command.send`) e escuta eventos (`MdHub.event.add`).

A Memed usa o termo **prescritor** para qualquer profissional habilitado (médico, dentista, enfermeiro, veterinário etc.).

Este arquivo cobre o fluxo essencial e as regras que reprovam homologação. Para detalhes de payloads, campos e exemplos completos, leia o arquivo de `references/` indicado na tabela no fim.

## Ambientes e credenciais

| | Homologação (testes) | Produção |
|---|---|---|
| `MEMED_API_URL` | `https://integrations.api.memed.com.br/v1` | `https://api.memed.com.br/v1` |
| `MEMED_SCRIPT_URL` | `https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js` | `https://partners.memed.com.br/integration.js` |
| Chaves | fixas e públicas (abaixo) | liberadas só após o formulário de credenciais de produção |

Chaves de homologação (são públicas na documentação oficial, servem só para testes):

```
API_KEY=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm
SECRET_KEY=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
```

- Homologação fica **indisponível de 0h às 6h (seg–sex) e no fim de semana inteiro** — se algo falha nesses horários, não é necessariamente bug.
- Coloque `API_KEY`, `SECRET_KEY`, `MEMED_API_URL` e `MEMED_SCRIPT_URL` em variáveis de ambiente para trocar de ambiente sem mudar código.
- As chaves **nunca** podem chegar ao frontend nem a repositórios. Credenciais expostas no front são motivo explícito de revogação das chaves de produção.

## Fluxo essencial

### 1. Backend: obter o token do prescritor

Todas as chamadas à API partem do backend. A API usa JSON:API (`Accept: application/vnd.api+json`, `Content-Type: application/json`) e autentica por query string.

**Consultar** (se já existe):
```
GET {MEMED_API_URL}/sinapse-prescricao/usuarios/{ID}?api-key={API_KEY}&secret-key={SECRET_KEY}
```
`{ID}` pode ser CPF (11 dígitos), o `external_id` do seu sistema, ou registro+UF (ex.: `12345SP`).

**Cadastrar** (se não existe):
```
POST {MEMED_API_URL}/sinapse-prescricao/usuarios?api-key={API_KEY}&secret-key={SECRET_KEY}
```
```json
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "external_id": "id-unico-no-seu-sistema",
      "nome": "Ana",
      "sobrenome": "Costa",
      "cpf": "52998224725",
      "data_nascimento": "15/03/1985",
      "board": { "board_code": "CRM", "board_number": "00000", "board_state": "SP" },
      "email": "ana@exemplo.com",
      "telefone": "11999999999",
      "sexo": "F"
    },
    "relationships": {
      "cidade":        { "data": { "type": "cidades", "id": 1 } },
      "especialidade": { "data": { "type": "especialidades", "id": 1 } }
    }
  }
}
```
Obrigatórios: `external_id`, `nome`, `sobrenome`, `cpf`, `data_nascimento`, `board.*`. Desde **13/02/2026 (RDC 1000/25)** CPF (ou passaporte) e data de nascimento são exigidos na emissão. `relationships` é opcional, mas se presente exige `type` e `id`; IDs vêm de `GET {MEMED_API_URL}/cidades` e `/especialidades` (vale cachear). Envie o cadastro o mais completo possível: o que faltar o prescritor terá de preencher dentro da Memed, e a homologação verifica que nenhum dado do prescritor é pedido durante a prescrição.

O token está em `data.attributes.token`. **Ele não é estático**: busque o token atual antes de cada atendimento em vez de guardá-lo para sempre. Prescritor com `status` "Inativo" não consegue prescrever (gera erro de autenticação); "Ativo" e "Em análise" podem.

Outras rotas de usuário: `PATCH .../usuarios/{EXTERNAL_ID}` (atualizar), `DELETE .../usuarios/{ID}`, `POST .../usuarios/validate-board` (validar registro no conselho). Rotas que agem em nome do prescritor (prescrições, protocolos, opções de receituário) usam `?token=<token do prescritor>` — veja `references/backend.md`.

### 2. Frontend: carregar o script uma única vez

```js
const PRESCRIPTION_MODULE = 'plataforma.prescricao';
const MEMED_SCRIPT_ID = 'memed-prescricao-script';

function carregarScriptMemed(token) {
  if (document.getElementById(MEMED_SCRIPT_ID)) return; // já carregado
  const script = document.createElement('script');
  script.id = MEMED_SCRIPT_ID;
  script.src = MEMED_SCRIPT_URL;          // vindo da config do ambiente
  script.setAttribute('data-token', token); // token obtido pelo backend
  script.addEventListener('error', () => setBotaoPrescricaoDisabled(true));
  document.head.appendChild(script);
}
```

O `id` fixo + guarda `getElementById` é critério de homologação: a segunda prescrição da mesma sessão deve abrir **sem reinjetar** o script. Não detecte duplicidade pela URL (ela muda entre ambientes). Carregue cedo, no início do atendimento, não no clique.

Também é possível usar `<script src=... data-token=...>` estático. Para exibir embutido num `div` em vez de tela inteira (padrão recomendado), adicione `data-container="<id-do-div>"` (no carregamento dinâmico, `script.dataset.container = '<id-do-div>'`); o elemento precisa de no mínimo 820×700px.

### 3. Esperar o módulo, registrar eventos, abrir no clique

```js
let listenersRegistrados = false;

function iniciarAtendimento(token) {
  setBotaoPrescricaoDisabled(true);
  carregarScriptMemed(token);

  MdSinapsePrescricao.event.add('core:moduleInit', async (module) => {
    if (module.name !== PRESCRIPTION_MODULE) return;

    if (!listenersRegistrados) {
      listenersRegistrados = true;
      MdHub.event.add('prescricaoImpressa', async (prescricao) => {
        await salvarPrescricaoNoBackend(prescricao);   // persistir no servidor
      });
      MdHub.event.add('prescricaoExcluida', async (payload) => {
        // a doc diverge: o evento entrega o id direto (número); Boas Práticas usa payload.id
        const id = typeof payload === 'object' && payload !== null ? payload.id : payload;
        await excluirPrescricaoNoBackend(id);          // sincronizar exclusão
      });
    }

    await MdHub.command.send(PRESCRIPTION_MODULE, 'setWorkplace', {
      local_name: 'Clínica Exemplo', // obrigatório em novos onboardings
      cnes: '1234567',               // obrigatório em novos onboardings
      address: 'Rua das Flores, 100',
      city: 'São Paulo',
      state: 'SP',
      phone: '1133334444',           // use string (necessário para números 0800)
    });
    setBotaoPrescricaoDisabled(false);
  });

  MdSinapsePrescricao.event.add('core:moduleHide', (module) => {
    // atenção: aqui a propriedade é moduleName, não name
    if (module.moduleName === PRESCRIPTION_MODULE) setBotaoPrescricaoDisabled(false);
  });
}

btnPrescricao.addEventListener('click', async () => {
  setBotaoPrescricaoDisabled(true);
  try {
    await MdHub.command.send(PRESCRIPTION_MODULE, 'setPaciente', {
      idExterno: 'parceiro-pac-a1b2c3d4', // obrigatório, único e estável
      nome: 'Maria Souza',                // obrigatório
      sexo: 'Feminino',                   // "Masculino"/"Feminino"/"M"/"F"
      cpf: '39053344705',                 // só dígitos (ou passaporte)
      data_nascimento: '15/05/1985',      // dd/mm/aaaa
      telefone: '11987654321',
      email: 'paciente@exemplo.com',
    });
    await MdHub.module.show(PRESCRIPTION_MODULE);
  } catch (err) {
    setBotaoPrescricaoDisabled(false);
  }
});
```

Por que cada detalhe importa:
- **Nada antes de `core:moduleInit`** — acessar o módulo antes de carregar gera erros.
- **Todos os comandos MdHub são assíncronos** — use `await` (ou `.then`); `setPaciente` precisa terminar antes do `show`.
- **Listeners uma vez só** — registrar em cada clique duplica gravações.
- **`idExterno` do paciente** — sem ele a Memed cria um paciente novo a cada atendimento e o histórico se perde. Em homologação use prefixo do parceiro (`parceiro-demo-123`), nunca `"123"`, para não colidir com outros parceiros.
- **Dados enviados por `setPaciente` não podem ser editados pelo prescritor** dentro da Memed — mande dados corretos.
- **`setWorkplace`** — define o local que sai no receituário. `cnes` + `local_name` são obrigatórios para parceiros novos (nomes de campo: ver "Inconsistências" abaixo).
- **Trocar de paciente** = só chamar `setPaciente` de novo; não recarregue o script.
- **SPA (React/Vue/Angular)**: centralize o carregamento num singleton; em React, `useEffect(() => { if (token) iniciarAtendimento(token); }, [token])` — nunca `useEffect` sem array de dependências.
- **Máquina compartilhada entre prescritores**: ao sair, chame `await MdHub.command.send('plataforma.sdk', 'logout')` para limpar o localStorage (obrigatório pela doc, evita vazamento entre cadastros).

### 4. Persistir a prescrição

`prescricaoImpressa` entrega o objeto completo (paciente, prescritor, `medicamentos[]` com `nome`, `posologia`, `quantidade`, `tipo`, `receituario`…). Envie ao **seu backend** e guarde lá (id da prescrição, PDF, link da receita digital). Com o id, o backend pode usar `GET {MEMED_API_URL}/prescricoes/{id}/url-document/full?token=...` (PDF) e `.../get-digital-prescription-link?token=...` (link). Para reabrir/reimprimir uma prescrição existente no front use o comando `viewPrescription`. O prescritor pode excluir prescrições na Memed; por isso `prescricaoExcluida` deve marcar como excluída no seu sistema, senão o prontuário aponta para um documento que dá erro.

## Checklist de homologação

Ausência de qualquer item obrigatório reprova a homologação ou leva à revogação das chaves de produção (a Memed reavalia até 180 dias após liberar).

Obrigatórios:
1. `API_KEY`/`SECRET_KEY` só no backend.
2. Homologação apontando para `integrations.memed.com.br` (script) e `integrations.api.memed.com.br` (API).
3. Cadastro do prescritor completo: nome, sobrenome, registro+UF, e-mail, especialidade, data de nascimento, CPF — nada pedido durante a prescrição.
4. `setPaciente` com `idExterno` único + nome, e-mail, celular, data de nascimento, CPF.
5. Script com `id="memed-prescricao-script"`, injetado uma vez; segunda emissão abre sem reinjetar.
6. `prescricaoImpressa` implementado e persistido no backend.
7. `prescricaoExcluida` implementado e sincronizado no backend.
8. `setWorkplace` configurado.
9. Fluxo completo de emissão testado, incluindo um medicamento controlado (ex.: Amoxil).
10. Features desligadas com `setFeatureToggle` funcionando corretamente.

Recomendado: script carregado no início do atendimento e botão habilitado só após `core:moduleInit`.

Quando tudo estiver pronto, o parceiro preenche o formulário de Autorização para Credenciais de Produção (link em `references/visao-geral.md`) e troca URLs + chaves para produção.

### Validar no navegador

No DevTools, selecione o contexto do iframe da Memed (normalmente `sinapse-prescricao`) e rode:

| Verificação | Comando |
|---|---|
| Dados do prescritor | `locator.get('usuarioRepository').getUser()` |
| Dados do paciente | `locator.get('usuarioRepository').getPaciente()` |
| Prescrição atual | `locator.get('prescricao')` |
| Script duplicado | `document.querySelectorAll('#memed-prescricao-script').length` (deve ser `1`) |

O console também mostra o ambiente: `ENVIRONMENT integrations` = homologação.

## Diagnóstico rápido

| Sintoma | Causa provável |
|---|---|
| Vários 401 no console / erro de autenticação | token desatualizado (muda quando os dados do prescritor mudam — busque de novo); prescritor "Inativo" (atualize via `PATCH` com dados válidos); usuário apagado na limpeza periódica do banco de homologação (cadastre de novo); chaves e URLs de ambientes diferentes |
| Módulo carrega várias vezes / eventos duplicados | script reinjetado a cada clique, listeners registrados fora de `core:moduleInit` ou sem guarda |
| `net::ERR_INVALID_URL` | HTML aberto via `file://`; sirva por um servidor web |
| Só aviso de `autofocusing`, nada aparece | módulo carregou mas `MdHub.module.show(...)` não foi chamado |
| `Failed to read the 'localStorage' property` | cookies/armazenamento bloqueados para o domínio da Memed no navegador |
| `Blocked a frame with origin` | `Referrer-Policy: same-origin` na sua página; use `strict-origin-when-cross-origin` |
| Erro 400 ao cadastrar | leia `errors[].detail`: CPF/data inválidos, registro não encontrado no conselho, `external_id` já usado, campo obrigatório faltando |
| `core:moduleHide` nunca casa | usar `module.moduleName` (não `module.name`) |

## Inconsistências da documentação oficial

A doc da Memed se contradiz em alguns pontos. Ao escrever código, siga a coluna "use" e, quando o comportamento importar, peça ao usuário para confirmar em homologação (logar o valor recebido).

| Ponto | O que a doc diz | Use |
|---|---|---|
| Argumento de `prescricaoExcluida` | página do evento: o id (número); Boas Práticas: objeto com `.id` | aceitar os dois (código acima) |
| Campos de `setWorkplace` | página do comando: `local_name`, `cnes`, `address`, `city`, `state`, `phone`; Boas Práticas: `nome`, `endereco`, `uf`… | os da página do comando |
| Modo incorporado dinâmico | `script.data.container = ...` | `script.dataset.container = ...` (`script.data` não existe) |
| Autenticação no front | uma página usa o atributo `token=` | `data-token=` |
| Rota `check-key` | `MEMED_API_URL/v1/sinapse-prescricao/check-key` | `MEMED_API_URL/sinapse-prescricao/check-key` (a base já termina em `/v1`) |
| Resposta das rotas de PDF e link da receita | formato do JSON não documentado | guardar a resposta inteira e ler os campos depois de inspecionar em homologação |

As referências já trazem essas correções anotadas como "doc oficial: …".

## Onde está cada detalhe

Os arquivos de `references/` são a documentação oficial convertida, agrupada por tema; cada página traz um comentário `<!-- fonte: URL -->`. Leia só o que a tarefa pede — use `grep` para achar o trecho (ex.: `grep -n "setFeatureToggle" references/comandos-mdhub.md`).

| Arquivo | Conteúdo |
|---|---|
| `references/boas-praticas.md` | implementação de referência completa, critérios de homologação, problemas frequentes |
| `references/visao-geral.md` | intro, primeiros passos, modos de carregamento (estático/dinâmico) e exibição (tela inteira/incorporado), credenciais de produção, integração Tasy/MV |
| `references/backend.md` | API REST: configurações, usuário prescritor (GET/POST/PATCH/DELETE, validate-board, status), prescrições (listar, filtrar por data, PDF, link, excluir), protocolos (do prescritor e do parceiro, com CIDs), impressão/opções de receituário (temas, cabeçalho/rodapé, upload de template), check-key |
| `references/backend-tabelas.md` | listas de cidades e especialidades com IDs (arquivo grande — use grep) |
| `references/frontend.md` | autenticação no front, configuração de URLs, MdSinapsePrescricao & MdHub, estilização (cores) |
| `references/comandos-mdhub.md` | todos os comandos: setPaciente (todos os campos, LME, história clínica), setAllergy, categoriesConditions (gestante, lactante, atleta, aeronauta), setFeatureToggle (lista de features), setAdditionalData, setWorkplace, setDictionary, addItem, find (temas), logout, viewPrescription, newPrescription, hide |
| `references/eventos-mdhub.md` | prescricaoImpressa (estrutura completa do payload), prescricaoExcluida, medicamentoAdicionado, medicamentoRemovido, core:moduleHide, core:moduleInit |
| `references/como-fazer.md` | tutoriais: cadastrar/obter/gerir prescritor, validar no CFM, gestão de paciente, cabeçalho/rodapé, fonte do PDF, impressão, modo edição, responsividade, reordenar busca, documentos estruturados |
| `references/erros-comuns.md` | cada erro comum com causa e solução |
| `references/duvidas-frequentes.md` | FAQ de backend/frontend, base de medicamentos, navegadores, sincronizar usuários, prescrição por API, profissionais e especialidades |
| `references/assinaturas-digitais.md` | provedores de certificado em nuvem: BirdID, Lacuna, RemoteID, SafeID, Vidaas, e o fluxo de avaliação |

Se a documentação oficial parecer ter mudado (comportamento diferente do descrito, campo novo), regenere as referências com `python3 scripts/atualizar_docs.py` (requer `beautifulsoup4` e `pandoc`) e, se possível, confira a página original em `https://doc.memed.com.br/docs/`.

## Ao escrever código para o usuário

- Mantenha a separação backend/frontend: o endpoint do seu backend devolve só o token ao navegador.
- Use a linguagem/framework do projeto do usuário para o backend (a API é REST simples); o frontend é sempre JS no navegador.
- Use dados fictícios em exemplos e trate dados de paciente/prescritor conforme a LGPD.
- Quando o usuário pedir uma revisão de integração existente, percorra o checklist de homologação acima item a item e aponte o que falta, com o trecho de código correspondente.
