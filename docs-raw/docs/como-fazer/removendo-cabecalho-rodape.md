https://doc.memed.com.br/docs/como-fazer/removendo-cabecalho-rodape/

# Remover cabeçalho e rodapé

Para entender como funciona a remoção de cabeçalho e rodapé, é preciso primeiro entender o que são esses elementos.

O cabeçalho e o rodapé são informações adicionais que aparecem na prescrição, além das informações principais sobre os medicamentos prescritos.
O cabeçalho geralmente contém informações sobre o prescritor que fez a prescrição, como nome, registro profissional e especialidade.
O rodapé, por sua vez, pode conter informações como o endereço e telefone do consultório ou clínica, o número da receita entre outras informações.

## Como fazer a remoção do cabeçalho e rodapé

### Removendo através dos atributos header e footer

A remoção do cabeçalho e rodapé pode ser feita através dos parametros `header_image` e `footer_image`, esses atributos são do tipo string e ao passar uma string vazia o cabeçalho/rodapé atual é removido.
A alteração é feita no indice que deve ser passado junto na requisição nas opções de receituário.
A remoção é feita através do endpoint `/opcoes-receituario`. Confira como deve ser feita a requisição abaixo:

* cURL
* Sucesso
* Erro

**Requisição POST**

```js
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

```json
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

```json
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

### Controlando a exibição do cabeçalho e rodapé

A exibição de cabeçalho e rodapé em uma prescrição médica pode ser personalizada de duas maneiras diferentes na API: usando os atributos `mostrar_cabecalho_rodape_simples` e `mostrar_cabecalho_rodape_especial`.

O atributo `mostrar_cabecalho_rodape_simples` é utilizado para exibir um cabeçalho e rodapé simples na prescrição médica.
Esse cabeçalho e rodapé incluirá informações básicas, como o nome e registro profissional do prescritor, a data da prescrição, o nome do paciente e a data de nascimento.
Para utilizar esse atributo, basta defini-lo como `1` para exibir ou `0` para não exibir passando no corpo da solicitação da API.

O atributo `mostrar_cabecalho_rodape_especial`, por sua vez, permite que o prescritor personalize o cabeçalho e rodapé da prescrição médica de acordo com suas necessidades.
Com esse atributo, o prescritor pode incluir informações adicionais, como o logotipo da clínica, informações de contato e instruções especiais para o paciente.
Para utilizar esse atributo, basta defini-lo como `1` para exibir ou `0` para não exibir passando no corpo da solicitação da API.

Abaixo como a requisição deve ser feita.

* cURL
* Sucesso
* Erro

**Requisição POST**

```js
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

```json
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

```json
{
    "errors": [
        {
            "title": "Erro",
            "detail": "Ocorreu um erro inesperado, por favor contate o nosso suporte."
        }
    ]
}
```
