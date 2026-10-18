https://doc.memed.com.br/docs/boas-praticas-integracao/

# Boas Práticas de Integração

Guia rápido para integrar, homologar e publicar a prescrição digital Memed — fluxo backend/frontend, implementação de referência e critérios de validação.

Dados de exemplo

Os exemplos utilizam **dados fictícios**. Em produção, trate dados pessoais de **prescritor** e **paciente** nos payloads enviados à API e no comando `setPaciente`, conforme a LGPD.

## Início rápido

Antes de solicitar homologação, confirme:

1. **Backend** obtém o token do prescritor e nunca expõe `API_KEY` / `SECRET_KEY` no frontend.
2. **Script** carregado uma única vez por sessão, com `id` fixo e guard `getElementById` antes de injetar.
3. **Listeners de eventos** (`prescricaoImpressa`, `prescricaoExcluida`) registrados uma vez, dentro de `core:moduleInit`.
4. **`idExterno`** do paciente enviado e único (com prefixo do parceiro em homologação).
5. **Abertura do módulo** via `await setPaciente` + `await module.show()` no clique — sem reinjetar script.
6. **Ambiente** — URLs de API e script conforme [Configuração do ambiente](#configura%C3%A7%C3%A3o-do-ambiente) (homologação ou produção).

## Configuração do ambiente

Credenciais de servidor

A `API_KEY` e a `SECRET_KEY` são segredos de backend. **Nunca** as exponha no frontend ou em repositórios públicos.

* Homologação
* Produção

**Par de chaves**

**API\_KEY**

```dotenv
iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm
```

**SECRET\_KEY**

```dotenv
Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
```

**URL da API**

**MEMED\_API\_URL**

```dotenv
https://integrations.api.memed.com.br/v1
```

**URL do script**

**MEMED\_SCRIPT\_URL**

```dotenv
https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js
```

Credenciais de produção

O par de chaves de produção só é liberado após a [Autorização para Credenciais de Produção](/docs/obter-credenciais). Configure `API_KEY` e `SECRET_KEY` como variáveis de ambiente no backend.

**URL da API**

```dotenv
https://api.memed.com.br/v1
```

**URL do script**

```dotenv
https://partners.memed.com.br/integration.js
```

Detalhes em [Configurações do backend](/docs/backend/configuracoes#urls-de-produ%C3%A7%C3%A3o) e [Configurações do frontend](/docs/frontend/configuracoes#urls-de-produ%C3%A7%C3%A3o).

## Visão geral do fluxo

## Autenticação do prescritor

Todas as requisições à API Memed devem ser originadas pelo **backend**. O valor de `data.attributes.token` na resposta da API é utilizado no atributo `data-token` do script de prescrição.

RDC n° 1000/25

A partir de **13/02/2026**, CPF (ou passaporte) e data de nascimento passam a ser obrigatórios na emissão. Garanta que o cadastro do prescritor envie esses campos. Consulte [Usuário Prescritor](/docs/backend/usuario-prescritor).

* Consultar prescritor
* Cadastrar prescritor
* Resposta da API

```shell
GET https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/{ID_USUARIO}?api-key=SUA_API_KEY&secret-key=SUA_SECRET_KEY
```

`{ID_USUARIO}` aceita **CPF** (11 dígitos), **external\_id** do seu sistema ou **registro+UF** (ex.: `00000SP`).

```shell
POST https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios?api-key=SUA_API_KEY&secret-key=SUA_SECRET_KEY
```

Consulte o payload em [Cadastrar prescritor](/docs/como-fazer/cadastrar-prescritor) e [Obter dados do usuário](/docs/como-fazer/obter-dados-usuario).

```json
{
  "data": {
    "id": 100001,
    "type": "usuarios",
    "attributes": {
      "nome": "Ana",
      "sobrenome": "Costa",
      "cpf": "52998224725",
      "email": "prescritor.exemplo@email.com",
      "data_nascimento": "15/03/1985",
      "sexo": "F",
      "status": "Ativo",
      "external_id": "parceiro-demo-CRM00000SP",
      "token": "SEU_TOKEN_JWT",
      "crm": "00000",
      "uf": "SP",
      "telefone": "(11) 4000-0000",
      "especialidade": "Clínico Geral",
      "board": {
        "board_code": "CRM",
        "board_number": "00000",
        "board_state": "SP"
      }
    },
    "relationships": {
      "cidade": {
        "data": { "id": 1001, "type": "cidades" }
      },
      "especialidade": {
        "data": { "id": 1, "type": "especialidades" }
      }
    },
    "links": {
      "self": "https://integrations.api.memed.com.br/v1/usuarios/100001"
    }
  }
}
```

Utilize `data.attributes.token` no atributo `data-token` do script de prescrição.

Validade do token

O token **não é estático**. Recupere o token válido mais recente do prescritor antes de cada atendimento.

## Implementação de referência

* **`MdSinapsePrescricao`**: eventos de ciclo de vida (`core:moduleInit`, `core:moduleHide`). Registre os listeners de eventos **uma única vez**.
* **`MdHub`**: comandos (`command.send`) e eventos de negócio (`prescricaoImpressa`, `prescricaoExcluida`). Todos retornam **promises** — use `async`/`await`.

Documentação completa em [MdSinapsePrescricao & MdHub](/docs/frontend/mdsinapseprescricao-mdhub).

* Integração completa
* Eventos

```javascript
const PRESCRIPTION_MODULE = 'plataforma.prescricao';
const MEMED_SCRIPT_ID = 'memed-prescricao-script';
// Homologação — em produção: https://partners.memed.com.br/integration.js
const MEMED_SCRIPT_URL =
  'https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js';

let listenersRegistrados = false;

const paciente = {
  idExterno: 'parceiro-demo-pac-a1b2c3d4',
  nome: 'Maria Souza',
  sexo: 'Feminino',
  cpf: '39053344705',
  data_nascimento: '15/05/1985',
  telefone: '11987654321',
  email: 'paciente.exemplo@email.com',
};

const workplace = {
  id: 'parceiro-demo-clinica-001',
  nome: 'Clínica Exemplo',
  endereco: 'Rua das Flores, 100 — São Paulo — SP',
  telefone: '(11) 3333-4444',
  cidade: 'São Paulo',
  uf: 'SP',
};

function setBotaoPrescricaoDisabled(disabled) {
  btnPrescricao.disabled = disabled;
}

function carregarScriptMemed(token) {
  if (document.getElementById(MEMED_SCRIPT_ID)) {
    console.warn('[Memed] Script já carregado.');
    return;
  }

  const script = document.createElement('script');
  script.id = MEMED_SCRIPT_ID;
  script.type = 'text/javascript';
  script.src = MEMED_SCRIPT_URL;
  script.setAttribute('data-token', token);
  script.addEventListener('error', () => {
    console.error('[Memed] Falha ao carregar o script.');
    setBotaoPrescricaoDisabled(true);
  });
  document.head.appendChild(script);
}

function registrarListenersLGPD() {
  if (listenersRegistrados) return;
  listenersRegistrados = true;

  MdHub.event.add('prescricaoImpressa', async (prescricao) => {
    await salvarPrescricaoNoBackend(prescricao);
  });

  MdHub.event.add('prescricaoExcluida', async (data) => {
    await excluirPrescricaoNoBackend(data.id);
  });
}

function iniciarAtendimento(tokenMemed) {
  setBotaoPrescricaoDisabled(true);
  carregarScriptMemed(tokenMemed);

  MdSinapsePrescricao.event.add('core:moduleInit', async (module) => {
    if (module.name !== PRESCRIPTION_MODULE) return;

    registrarListenersLGPD();
    await MdHub.command.send(PRESCRIPTION_MODULE, 'setWorkplace', workplace);
    setBotaoPrescricaoDisabled(false);
  });

  MdSinapsePrescricao.event.add('core:moduleHide', (module) => {
    if (module.moduleName !== PRESCRIPTION_MODULE) return;
    setBotaoPrescricaoDisabled(false);
  });
}

btnPrescricao.addEventListener('click', async () => {
  setBotaoPrescricaoDisabled(true);

  try {
    await MdHub.command.send(PRESCRIPTION_MODULE, 'setPaciente', paciente);
    await MdHub.module.show(PRESCRIPTION_MODULE);
  } catch (err) {
    console.error('[Memed] Erro ao abrir prescrição', err);
    setBotaoPrescricaoDisabled(false);
  }
});

async function trocarPaciente(novoPaciente) {
  await MdHub.command.send(PRESCRIPTION_MODULE, 'setPaciente', novoPaciente);
}
```

```javascript
// Registrar uma única vez, dentro de core:moduleInit
MdHub.event.add('prescricaoImpressa', async (prescricao) => {
  await fetch('/api/prescricoes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(prescricao),
  });
});

MdHub.event.add('prescricaoExcluida', async (data) => {
  await fetch(`/api/prescricoes/${data.id}`, {
    method: 'DELETE',
  });
});
```

Substitua `/api/prescricoes` pelo endpoint do seu backend. A persistência deve ocorrer **sempre no servidor** — nunca exponha credenciais da API Memed no frontend.

### Comportamento por etapa

| Etapa | Ação esperada |
| --- | --- |
| Início do atendimento | Injetar o script **uma vez** com `data-token`, `id="memed-prescricao-script"` e guard `getElementById` |
| `core:moduleInit` | Registrar listeners de eventos; executar `await setWorkplace` (recomendado); habilitar o botão |
| Abertura do módulo | `await setPaciente` → `await module.show()` — **sem** reinjetar o script |
| Troca de paciente | Executar apenas `await setPaciente` |

Campo idExterno

Sem `idExterno`, a Memed cria um novo registro a cada atendimento e o histórico do paciente é perdido. Em homologação, utilize prefixo do parceiro (ex.: `parceiro-demo-123`). Referência de campos em [setPaciente](/docs/frontend/comandos-mdhub/set-patient).

## Eventos

Critério de homologação

A implementação de `prescricaoImpressa` (persistência no backend) e `prescricaoExcluida` (sincronização de exclusão) é **obrigatória**. A ausência resulta em reprovação na homologação.

* **`prescricaoImpressa`** — disparado ao concluir a emissão. Persista o payload no backend via `POST`. Detalhes: [Prescrição impressa](/docs/frontend/eventos-mdhub/prescricao-impressa).
* **`prescricaoExcluida`** — disparado quando o prescritor exclui a prescrição. Sincronize com `DELETE` ou soft-delete. Detalhes: [Prescrição excluída](/docs/frontend/eventos-mdhub/prescricao-excluida).

Registre cada handler **uma única vez**, dentro de `core:moduleInit`.

## Critérios de homologação

* Obrigatórios
* Recomendados

**Segurança das chaves** — API\_KEY e SECRET\_KEY restritas ao backend.

**Ambiente de integração** — endpoints em `integrations.memed.com.br` e `integrations.api.memed.com.br`.

**Emissão de prescrição** — fluxo completo validado; incluir medicamento controlado (ex.: Amoxil).

**Dados do prescritor** — nenhum campo solicitado durante a prescrição (validar com `getUser()` no iframe).

**Identificação do paciente** — `idExterno` presente e único no `setPaciente`.

**Script único** — atribua `id="memed-prescricao-script"` ao script; aborte a injeção se `document.getElementById('memed-prescricao-script')` já existir; a segunda emissão na mesma sessão deve abrir sem reinjetar.

**Persistência de prescrições** — evento `prescricaoImpressa` implementado e dados salvos no backend.

**Local de trabalho** — `setWorkplace` configurado ([setWorkplace](/docs/frontend/comandos-mdhub/set-workplace)).

**Sincronização de exclusão** — evento `prescricaoExcluida` implementado no backend.

**Inicialização antecipada** — script no início do atendimento; botão habilitado após `core:moduleInit`.

## Problemas frequentes

**Ambiente sandbox incorreto** — use `integrations.memed.com.br` (script) e `integrations.api.memed.com.br` (API).

**Script recarregado a cada clique** — carregue o script uma vez por sessão; no clique, use apenas `await MdHub.module.show()`.

**Campo `idExterno` ausente** — envie `idExterno` único e estável no `setPaciente`.

**Colisão de `idExterno` em homologação** — use prefixo do parceiro (ex.: `parceiro-demo-123`), não valores genéricos como `"123"`.

**Evento `prescricaoImpressa` não implementado** — registre o handler em `core:moduleInit` e persista no backend.

**Evento `prescricaoExcluida` não implementado** — sincronize a exclusão no backend.

**Handlers duplicados** — registre cada evento uma única vez, dentro de `core:moduleInit`.

**Verificação de script duplicado incorreta** — use `getElementById` com `id` fixo no script; não dependa da URL (`sinapse-prescricao` vs `integration.js`).

Consulte também [Erros comuns](/docs/erros-comuns).

## Aplicações de página única

Centralize o carregamento do script em um **singleton**. A troca de paciente **não** requer recarregamento do script.

```jsx
useEffect(() => {
  if (token) iniciarAtendimento(token);
}, [token]);
```

Evite `useEffect` sem array de dependências. Consulte [Modos de carregamento](/docs/modos-de-carregamento).

## Validação e diagnóstico

No DevTools, selecione o iframe da prescrição Memed (geralmente `sinapse-prescricao`) no seletor de contexto e execute:

| Verificação | Comando |
| --- | --- |
| Dados do prescritor | `locator.get('usuarioRepository').getUser()` |
| Dados do paciente | `locator.get('usuarioRepository').getPaciente()` |
| Dados da prescrição | `locator.get('prescricao')` |
| Script carregado | `document.getElementById('memed-prescricao-script')` |
| Script duplicado | `document.querySelectorAll('#memed-prescricao-script').length` |

O script deve usar `id="memed-prescricao-script"`. Após o carregamento, `getElementById` retorna o elemento; `querySelectorAll` deve retornar `1`. Valores acima de `1` indicam injeção duplicada.

## Próximos passos

| Tópico | Documentação |
| --- | --- |
| Primeiros passos | [Primeiros passos](/docs/primeiros-passos) |
| Comando setPaciente | [Configurar paciente](/docs/frontend/comandos-mdhub/set-patient) |
| Eventos MdHub | [Prescrição impressa](/docs/frontend/eventos-mdhub/prescricao-impressa) |
| API do prescritor | [Usuário Prescritor](/docs/backend/usuario-prescritor) |
| Solução de problemas | [Erros comuns](/docs/erros-comuns) |
