https://doc.memed.com.br/docs/backend/chaves/

# Par de Chaves

## Sobre pares de chaves

Os pares de chave são o principal atributo para realizar a integração Memed, sem ele, não é possível cadastrar um prescritor e inciar as integrações com a plataforma de fato. A seguir, você pode usar o nosso endpoint de validação para entender se a chave de produção recebida é valida para realizar uma integração.

### Consultar se o par de chaves está ativo e funcional:

```text
PATCH: MEMED_API_URL/v1/sinapse-prescricao/check-key
```

* cURL
* Sucesso
* Erro

**Requisição GET**  
Query Parameters:

* api-key
* secret-key

Abaixo segue um **exemplo** da requisição na api apontando para o ambiente de **integrations** (QA/Testes).  
Nessa rota é possivel consultar se a chave está funcional.

Atenção

Para ambientes de **produção** a url deve ser:
<https://api.memed.com.br/>

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/check-key?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

**Retorno: Http status 200**

```json
{
    "success": [
        {
            "code": "chave-valida",
            "title": "Sucesso",
            "detail": "Código de acesso valido"
        }
    ]
}
```

**Retorno: Http status 401 - UNAUTHORIZED**

```json
{
    "errors": [
        {
            "code": "token-invalido",
            "title": "Erro",
            "detail": "Token vazio"
        }
    ]
}
```
