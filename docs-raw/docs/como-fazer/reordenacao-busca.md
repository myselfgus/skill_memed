https://doc.memed.com.br/docs/como-fazer/reordenacao-busca/

# Reordenação das abas da busca

A busca é dividida em abas e cada uma delas tem seu nome de identificação de acordo com os tipos de resultados retornados.
Os nomes são:

```text
["industrializados", "composicoes", "manipulados", "perifericos", "exames"]
```

Essa é a ordem padrão dos resultados. Para fazer a reordenação das abas, basta alterar a ordem dos nomes citados acima, e
fazer uma requisição para o endpoint de configurações do prescritor passando a nova ordem das abas da busca.

Para fazer a requisição você precisará passar o token do prescritor via query params.
O token é recuperado através da nova API, veja como recuperar
[aqui](/docs/backend/usuario-prescritor#obtendo-os-dados-do-usu%C3%A1rio-prescritor).

Abaixo um exemplo da requisição para alterar a ordenação.

* cURL
* Sucesso
* Erro

**Requisição POST**

```js
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

```json
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

```json
{
  "errors": [
    {
            "title": "Erro",
            "detail": "A configuração solicitada não existe."
        }
  ]
}
```

O atributo `chave` passa o valor `tab_orders`. Este comunica para nossa aplicação qual configuração você quer alterar.
A nova ordem das abas deve ser passada dentro de `data.attributes.valor` e os nomes devem ser passados
dentro de um array, contendo apenas os nomes conhecidos por nossa aplicação, sem acentuação.
