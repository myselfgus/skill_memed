https://doc.memed.com.br/docs/backend/prescricao/

# Prescrição

## Capturar histórico de prescrições

É possível recuperar o histórico de prescrições do usuário prescritor.
A seguinte requisição retorna as 10 últimas prescrições do usuário prescritor.

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

Nota

* É possível recuperar o histórico que abrangem mais do que as últimas 10 prescrições. Com o exemplo abaixo, você pode consultar qualquer período desejado e aplicar paginação caso o limite de 100 registros seja atingido.
* Exemplo de uso da paginação:

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/?page%5Blimit%5D=100&page%5Boffset%5D=0&token=<TOKEN-DO-MEDICO>&initialDate=2024-09-23&finalDate=2024-09-23' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

> **Importante:** Para recuperar prescrição com a estruturação de documentos (documentos estruturados) de uma prescrição via API, é necessário passar o parâmetro `structuredDocuments=true` na requisição. Isso garante que a resposta traga os dados estruturados dos documentos associados à prescrição.

**Exemplo de requisição com `structuredDocuments=true`:**

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/<id_prescription>?structuredDocuments=true' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <seu_token_aqui>'
```

## Remover uma prescrição

É possível remover via api uma prescrição informando o id da prescrição e o token do usuário prescritor.
Veja um exemplo de requisição em cURL abaixo:

```js
curl --request DELETE \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/{id_prescription}?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

## Consultar princípios ativos

É possível buscar/listar os princípios ativos dos medicamentos informando a api-key e secret-key como
parametro da url (Query Parameters).

### Veja um exemplo de requisição em cURL abaixo:

* cURL
* Resposta

**Requisição GET**

```shell
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/drugs/ingredients?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
  &terms=dipirona&limit=10&order[field]=name&order[sort]=ASC' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

**Resposta: Http status 200 - OK**

```json
{
    "data": [
        {
            "type": "ingredient",
            "attributes": {
                "unii": "n.d.",
                "slug": "dipirona",
                "base": 1,
                "radical": null,
                "related": "Dipirona magnésica, Dipirona sódica, Dipirona mono-hidratada",
                "name": "Dipirona",
                "name_en": "Dipyrone"
            },
            "links": {
                "self": "https:\/\/integrations.api.memed.com.br\/v1\/ingredient\/622"
            },
            "id": 622
        }
    ],
    "links": {
        "self": "https:\/\/integrations.api.memed.com.br\/ingredient"
    },
    "meta": {
        "total": 1
    }
}
```

## Recuperar o link da Receita Digital

Para recuperar o link da receita digital enviado ao paciente, informe o id da prescrição e o token do usuário.
Veja um exemplo de requisição em cURL abaixo:

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/{id_prescription}/get-digital-prescription-link?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

Nota

* O link da receita e o código de desbloqueio são fixos. Esses dados podem ser armazenados em banco de dados;
* Ao implementar essa opção, SEMPRE informe o código de desbloqueio para o paciente no local
  em que for exibir o link.

## Salvar o PDF da prescrição

Caso necessite salvar o PDF da prescrição em seu sistema, informe o id da prescrição e o token do usuário.
Veja um exemplo de requisição em cURL abaixo:

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/{id_prescription}/url-document/full?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```
