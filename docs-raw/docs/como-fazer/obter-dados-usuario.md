https://doc.memed.com.br/docs/como-fazer/obter-dados-usuario/

# Obter dados do Usuário (prescritor)

O token de acesso do usuário prescritor é retornado junto com todos os outros dados do usuário.
[Veja abaixo](#obtendo-os-dados-do-usu%C3%A1rio-prescritor) como recuperar os dados do usuário e o token de acesso.

Atenção

O **token** não é estático, portanto sempre que for fazer uma requisição na **API Memed**,
você precisa recuperar o último token válido do usuário.

### Obtendo os dados do usuário prescritor

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
