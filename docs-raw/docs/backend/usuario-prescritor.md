https://doc.memed.com.br/docs/backend/usuario-prescritor/

# Usuário Prescritor

Atenção: Obrigatoriedade de Dados (RDC n° 1000/25)

A partir de **13/02/2026**, conforme exigência da **RDC n° 1000/25**, passará a ser **obrigatório** informar o CPF (ou passaporte, no caso de estrangeiros) e a Data de Nascimento nas emissões de prescrições.

Além disso, a data da prescrição considerada será sempre a **data da assinatura digital**. Certifique-se de que sua integração já esteja enviando esses parâmetros corretamente para evitar erros de validação na emissão.

## Tipos de usuário prescritor

A plataforma Memed permite a emissão de prescrições por diversos tipos de profissionais de saúde devidamente habilitados pelos seus respectivos conselhos profissionais:

* **Médicos** (CRM)
* **Dentistas** (CRO)
* **Enfermeiros** (COREN)
* **Médicos Veterinários** (CRMV)
* **Farmacêuticos** (CRF)
* **Nutricionistas** (CRN)
* **Fisioterapeutas** (CREFITO)
* **Psicólogos** (CRP)
* **Fonoaudiólogos** (CRFa)
* **Profissionais de Educação Física** (CREF)

A identificação do tipo de prescritor é realizada automaticamente durante o cadastro, com base no registro profissional informado (CRM, CRO, COREN, etc.).

Base de Medicamentos Unificada

A base de medicamentos da Memed é **única e compartilhada** entre todas as categorias profissionais. Cabe ao sistema integrado implementar o controle e validação dos medicamentos que podem ser prescritos por cada categoria profissional, respeitando suas respectivas competências e legislações vigentes.

### Status do usuário prescritor

Cada prescritor cadastrado na Memed possui um **status** que determina se ele está autorizado a emitir prescrições. Este status indica o estado atual da validação do cadastro.

Importante

Prescritores com status "Inativo" **não podem** emitir prescrições e receberão um [erro de autenticação](/docs/erros-comuns/ocorreu-erro-autenticacao) ao tentarem acessar a plataforma.

**Status possíveis:**

| Status | Descrição | Pode prescrever? |
| --- | --- | --- |
| Ativo | Cadastro validado e aprovado | ✅ |
| Em análise | Cadastro em processo de validação interna | ✅ |
| Inativo | Cadastro bloqueado ou desativado | ❌ |

## Obtendo o token do usuário (prescritor)

O token de acesso do usuário prescritor é retornado junto com todos os outros dados do usuário.
[Veja abaixo](#obtendo-os-dados-do-usu%C3%A1rio-prescritor) como recuperar os dados do usuário e o token de acesso.

Atenção

O **token** não é estático, portanto sempre que for fazer uma requisição na **API Memed**,
você precisa recuperar o último token válido do usuário.

## Obtendo os dados do usuário prescritor

Para consultar os dados completos de um prescritor, incluindo seu **token de acesso**, realize uma requisição **GET** na API da Memed utilizando a rota de usuários.

**Parâmetros necessários:**

* **Identificador do usuário** (veja opções abaixo)
* **Par de chaves** (API Key + Secret Key)

Token de Acesso

O **token de acesso** do usuário prescritor é retornado automaticamente junto com todos os demais dados do usuário na resposta da requisição.

Identificadores Válidos

O **identificador do usuário** pode ser informado de três formas diferentes:

* **CPF:** Apenas números (11 dígitos)
* **External ID:** Identificador único definido pelo seu sistema
* **Registro + UF:** Número do registro profissional seguido da sigla do estado (Ex: `12345SP`, `01234MG`)

> **Tipos de registro aceitos:** CRM, CRO, COREN, CRMV, CRF, CRN, CREFITO, CRP, CRFa, CREF

### Rota para obter os dados do usuário

```text
GET: MEMED_API_URL/sinapse-prescricao/usuarios/{ID_USUARIO}?api-key=API_KEY&secret-key=SECRET_KEY
```

### Exemplo de requisição

Abaixo está um exemplo completo de requisição para obter os dados e o **token de acesso** do usuário.

* cURL
* Sucesso
* Erro

#### Requisição GET

```shell
curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/1234?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL'\
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

#### ✅ Retorno de Sucesso - HTTP 200 OK

```json
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

#### ❌ Retorno de Erro - HTTP 404 NOT FOUND

```json
{
  "errors": [
    {
      "title": "Erro",
      "detail": "Nenhum usuário encontrado com este este CRM, CPF ou Id: 1234"
    }
  ]
}
```

## Cadastrando o prescritor

Para cadastrar um novo usuário prescritor, realize uma requisição **POST** na rota de usuários da API Memed, enviando os dados do profissional no corpo da requisição.

Estrutura da Requisição

**Formato obrigatório:** Os dados devem ser enviados no **corpo (body)** da requisição seguindo rigorosamente a estrutura de payload especificada pela API. A formatação correta garante o sucesso da operação e evita erros de validação.

**Relacionamentos opcionais:** Ao incluir as propriedades `cidade` e/ou `especialidade` no objeto `relationships`, os campos `type` e `id` dentro delas tornam-se **obrigatórios**.

**APIs de Consulta:**

* **Cidades:** Obtenha o ID da cidade em:  
  `https://integrations.api.memed.com.br/v1/cidades`
* **Especialidades:** Obtenha o ID da especialidade em:  
  `https://integrations.api.memed.com.br/v1/especialidades`

**💡 Dica:** Consulte essas APIs previamente e armazene os IDs mais utilizados em cache no seu sistema para otimizar o desempenho do processo de cadastro.

### Rota de cadastro do usuário

```text
POST: MEMED_API_URL/sinapse-prescricao/usuarios?api-key={API_KEY}&secret-key={SECRET_KEY}
```

### Estrutura do payload de cadastro

Estrutura Obrigatória

A requisição deve seguir **exatamente** a estrutura de payload (contrato) especificada abaixo. Qualquer desvio desta estrutura resultará em erro de validação:

```json
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

### Dados do prescritor

| Propriedade | Tipo | Obrigatório | Observações |
| --- | --- | --- | --- |
| external\_id | int/string(255) | ✅ | Recomendável ser do tipo UUID, pois é um campo único |
| nome | string(255) | ✅ |  |
| sobrenome | string(255) | ✅ |  |
| cpf | string(11) | ✅ | Apenas dígitos |
| board\_code | string(5) | ✅ | CRM / CRO / COREN / CRMV / CRF / CRN / CREFITO / CRP / CRFa / CREF |
| board\_number | string(255) | ✅ | Apenas dígitos |
| board\_state | string(2) | ✅ | Siglas dos estados brasileiros |
| email | string(255) |  |  |
| telefone | string(16) |  | Apenas dígitos ou formatado (DDD) XXXXX-XXXX |
| sexo | string(1) |  | M / F |
| data\_de\_nascimento | date(10) | ✅ | dd/mm/YYYY |
| cidade | int(10) |  | O id da API   `https://integrations.api.memed.com.br/v1/cidades` |
| especialidade | int(10) |  | O id da API   `https://integrations.api.memed.com.br/v1/especialidades` |

Melhores Práticas para Experiência do Usuário

Embora diversos campos sejam marcados como opcionais na estrutura de cadastro, é importante compreender que **quanto mais completo for o cadastro inicial, melhor será a experiência** do prescritor na plataforma.

Dados não preenchidos durante a integração precisarão ser completados posteriormente pelo próprio usuário dentro da plataforma de prescrição da Memed, o que pode gerar interrupções no fluxo de trabalho e frustração.

**Recomendação:** Envie o máximo de informações disponíveis durante o processo de cadastro (CPF, e-mail, telefone, sexo, data de nascimento, cidade e especialidade). Esta prática resulta em:

* **Acesso imediato e completo** às funcionalidades da plataforma
* **Redução de etapas** para o prescritor após o primeiro login
* **Onboarding mais ágil** e sem interrupções
* **Dados mais completos** para análises e relatórios

### Exemplo de requisição de cadastro

Abaixo está um exemplo completo de requisição para cadastrar um novo prescritor. O **token** do usuário será retornado na resposta de sucesso:

* cURL
* Sucesso
* Erro

**Requisição POST**

```shell
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

#### ✅ Retorno de Sucesso - HTTP 200 OK

```json
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

#### ❌ Retorno de Erro - HTTP 400 BAD REQUEST

```json
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

Tratamento de Erros

As mensagens de erro são específicas para cada situação. Analise cuidadosamente o campo `detail` do erro retornado para identificar e corrigir o problema antes de reenviar a requisição.

**Principais causas de erro:**

* Dados em formato inválido (ex: CPF com letras, data mal formatada)
* Registro profissional não encontrado nos conselhos oficiais
* CPF inválido ou não cadastrado
* E-mail em formato inválido
* Campos obrigatórios ausentes ou vazios
* `external_id` já cadastrado para outro usuário

## Atualizando os dados do usuário prescritor

Para atualizar os dados de um prescritor existente, realize uma requisição **PATCH** na rota de usuários, informando:

* **Identificador do usuário** (CPF, External ID ou Registro+UF)
* **Par de chaves** (API Key + Secret Key)
* **Dados a atualizar** no corpo da requisição

Atenção ao `external_id`

**Importante:** Só inclua o campo `external_id` no payload se você realmente deseja **alterar** seu valor.

Se você enviar o `external_id` com o **mesmo valor atual**, a API retornará o erro:  
`"Prescritor já cadastrado para o parceiro com esse id externo"`

**Recomendação:** Para atualizações comuns (nome, e-mail, telefone, etc.), **não inclua** o campo `external_id` no payload.

### Rota para atualizar os dados do usuário prescritor

```text
PATCH: MEMED_API_URL/sinapse-prescricao/usuarios/{EXTERNAL_ID}?api-key=API_KEY&secret-key=SECRET_KEY
```

### Exemplo de requisição de atualização

Exemplo de requisição para atualizar o CPF de um prescritor existente:

* cURL
* Sucesso
* Erro

**Requisição PATCH**

```shell
curl --request PATCH \
  --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/EXTERNAL_ID?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
        "type": "usuarios",
        "attributes": {
            "cpf": "84587617008"
        }
    }
}'
```

**Retorno: Http status 200 - OK**

```json
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
      "crm": "016964",
      "email": "novoemail@test.com"
    }
  }
}
```

**Retorno: Http status 400 - BAD REQUEST**

```json
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

## Excluindo usuário prescritor

Para excluir permanentemente um prescritor, realize uma requisição **DELETE** na rota de usuários, informando o **identificador do usuário** e o **par de chaves**.

Ação Irreversível

Ao excluir um prescritor, você estará:

* Removendo **permanentemente** todo o histórico de atividades
* Excluindo **todas as prescrições** associadas
* Apagando **todos os dados e configurações** do usuário

Mesmo recriando o cadastro com os mesmos dados, **não será possível** recuperar o histórico, prescrições ou configurações anteriores.

### Rota para excluir o usuário prescritor

```text
DELETE: MEMED_API_URL/sinapse-prescricao/usuarios/{ID_USUARIO}?api-key=API_KEY&secret-key=SECRET_KEY
```

### Exemplo de requisição de exclusão

Exemplo de requisição para excluir permanentemente um prescritor:

* cURL
* Sucesso
* Erro

**Requisição DELETE**

```shell
    curl --request DELETE \
        --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/1234?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL'\
        --header 'Accept: application/vnd.api+json' \
        --header 'Cache-Control: no-cache' \
        --header 'Content-Type: application/json'
```

**Retorno: Http status 200 - OK**

```json
no content
```

**Retorno: Http status 404 - NOT FOUND**

```json
{
  "errors": [
    {
      "title": "titulo do erro",
      "detail": "detalhes do erro"
    }
  ]
}
```
