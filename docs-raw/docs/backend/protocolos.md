https://doc.memed.com.br/docs/backend/protocolos/

# Protocolos

## Medicamentos, exames e documentos

Para cadastrar um modelo de prescrição padrão, seja a nível de profissional prescritor ou instituição de saúde, deve se considerar, principalmente o uso do array de medicamento nas requisições de cadastro (POST). Ele é importante para definir comportamentos no pós prescrição, como uso do marketplace e dispensação correta de medicamentos. Abaixo temos exemplos de como o array `medicamentos` se comporta em cada caso:

Obs: o ID do medicamento/exame deve possuir correspondência correta com a Memed, caso contrario ocorrera a seguinte mensagem:

```text
Apresentação especificada no medicamento não encontrada
```

Fica a dica!

Para facilitar o uso e criação, um protocolo pode ser cadastrado via frontEnd e recuperado com as rotas abaixo para replicar para outros profissionais.

### Medicamentos

Para o cadastro correto de medicamentos, é necessário informar todas as medidas necessárias referente ao medicamento, abaixo temos um exemplo dos preenchimentos:

```json
"medicamentos": [
{
  "id": "a1046503030027106379",
  "posologia": "Tomar de 6 em 6h",
  "nome": "Dipirona"
},
```

### Exames

Para exames, é necessário informar somente os campos de ID e nome do exame, conforme catalogo da Memed.

```json
"medicamentos": [
{
  "id": "e10",
  "posologia": "Jejum de 8 a 10 horas",
  "nome": "Hemograma"
},
```

### Documentos

Para utilização de documentos, os campos de id são removidos do array, logo, toda inserção dentro do array de medicamentos sem um campo de ID será considerada texto livre.

```json
"medicamentos": [
{
  "nome": "Atestado",
  "posologia": "<p>ATESTADO<br> Atesto que o(a) Sr.(a) ___________________________________________________________________<br> encontra-se sob meus cuidados profissionais ...."
}
```

Sobre os ID's

A Memed não possui uma rota direta para captura dos ID's de medicamento/exames, por favor, contate a Memed sobre como adquirir esses ID's

## Cadastrar protocolos para o usuário prescritor

É possível cadastrar protocolos de tratamento para o usuário através da API, informando o token do usuário
prescritor e, dentro do array de medicamentos informando, os dados do medicamento.

Veja um exemplo de requisição em cURL abaixo:

```shell
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": "string",
      "medicamentos": [
        {
          "nome": "string",
          "posologia": "string",
          "quantidade": 0,
          "composicao": "string",
          "fabricante": "string",
          "titularidade": "string",
          "preco": 0
        }
      ]
    }
  }
}'
```

info

* O campo `data.attributes.nome` possui um limite de 500 caracteres;
* Caso não tenha o ID, o item/medicamento será adicionado como texto livre na prescrição.

Após inserido, o usuário visualizará o protocolo no menu Protocolos, conforme print a seguir

![protocols-list.png](https://cdn.memed.com.br/doc/protocols-list.png)

## Recuperar protocolos de um prescritor

Para recuperar o protocolo do usuário prescritor, utilize o cURL abaixo, enviando o token do usuário prescritor na
url como parametro (Query Parameters).

```shell
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/protocolos?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNTc5LCIwOTZiZDY5MDBhYjYxMTMyZTkzNzUzYjU2NDA5NWM0MSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjI1LjI2OTgxIl0.3i20Y7OZ3RSuyajuBlxGLxsjsMKqMB3egbNmjeKz5Y8' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

## Excluir protocolo de um prescritor

Para excluir o protocolo do usuário prescritor, utilize o cURL abaixo, enviando o token do usuário prescritor na
url como parametro (Query Parameters).

```shell
curl --request DELETE \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/1367?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNTc5LCIwOTZiZDY5MDBhYjYxMTMyZTkzNzUzYjU2NDA5NWM0MSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjI1LjI2OTgxIl0.3i20Y7OZ3RSuyajuBlxGLxsjsMKqMB3egbNmjeKz5Y8' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

## Criar protocolo para todos os prescritores

Dentro de uma instituição/hospital é comum a padronização de protocolos para certo tipo de tratamento/doença.
Pensando nisso, a Memed disponibiliza aos parceiros integrados a possibilidade de criar e gerenciar
os protocolos que aparecerão a todos os seus prescritores.

Para criar um protocolo é preciso informar os seguintes dados:

* Nome do protocolo;
* Lista de item do protocolo, o item pode ser uma das opções abaixo:
  + Medicamento
  + Exame
  + Texto Livre

No exemplo abaixo, vamos adicionando um protocolo cujo o nome vai ser `NomeQueVaiAparecerParaTodosMedicos` e nesse protocolo vai possuir um medicamento dipirona e exame hemograma sendo exibido automaticamente para todos os prescritores do seu hospital.

info

Os protocolos cadastrados a nível de instituição são exibidos para todos os profissionais prescritores do par de chaves utilizado.

```shell
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": string,
      "medicamentos": [
        {
          "id": string,
          "posologia": string,
          "nome": string
        },
        {
          "id": string,
          "nome": string
        }
      ]
    }
  }
}'
```

Obs: o id do medicamento deve ser utilizado do ambiente correspondente (integrations ou produção), caso contrario ocorrera a seguinte mensagem de erro:

```text
Apresentação especificada no medicamento não encontrada
```

### Associar diagnósticos (CID) ao protocolo

Além dos dados acima, este mesmo endpoint (`POST /v1/protocolos/parceiros`) aceita o array `cids`, para associar um ou mais diagnósticos ao protocolo do parceiro. Cada código deve seguir o padrão CID-10 (ex.: `A10`, `J54`, `Z50`) e não pode se repetir dentro da mesma lista. Essa associação é o que permite que o modelo seja posteriormente encontrado por CID na busca de modelos (ver [Documentos estruturados](/docs/como-fazer/documentos-estruturados#busca-e-favoritos-de-modelos-por-cid)).

```shell
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": "NomeQueVaiAparecerParaTodosMedicos",
      "cids": ["A10", "B29", "J54"],
      "medicamentos": [
        {
          "id": string,
          "posologia": string,
          "nome": string
        },
        {
          "id": string,
          "nome": string
        }
      ]
    }
  }
}'
```

O comportamento é o mesmo do cadastro sem `cids`: os diagnósticos informados ficam disponíveis para todos os prescritores vinculados ao par de chaves utilizado, e são retornados em `data.attributes.cids` na resposta (`201 Created`).

Erros de validação de CID

Se algum código não seguir o padrão CID-10 ou vier duplicado na lista, a API retorna `400` antes de criar o protocolo:

```json
{
  "status": 400,
  "errors": [
    { "title": "invalid-cid", "detail": "Códigos CID incorretos: AA10, J9911" }
  ]
}
```

```json
{
  "status": 400,
  "errors": [
    { "title": "invalid-cid", "detail": "Códigos CID duplicados: A10" }
  ]
}
```

## Consultar todos os protocolos

É possível consultar todos os protocolos de um determinado parceiro. Para isto, utilize a cURL abaixo enviando
as chaves api-key e secret-key na url como parâmetro (Query Parameters).

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

Essa requisição retorna todos os protocolos que foram criados e estão sendo exibidos aos prescritores do parceiro.

## Consultar/Excluir protocolo por ID

Para a exclusão e consulta de um protocolo específico, o parceiro precisa informar o ID deste protocolo nas requisições.
Esse ID pode ser recuperado de duas formas:

* Após a criação de um protocolo, o sistema retorna todos os dados do mesmo de forma estruturada, inclusive o ID;
* Consultando todos os protocolos do parceiro

# Consultar:

```js
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros/{protocolo_id}?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

# Excluir:

```js
curl --request DELETE \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros/{protocolo_id}?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

## Cadastrar múltiplos protocolos para o usuário

É possível cadastrar vários protocolos de tratamento para o usuário apenas com um REQUEST para a nossa API.

Veja um exemplo de requisição em cURL abaixo:

```js
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/multiplos?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNTc5LCIwOTZiZDY5MDBhYjYxMTMyZTkzNzUzYjU2NDA5NWM0MSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjI1LjI2OTgxIl0.3i20Y7OZ3RSuyajuBlxGLxsjsMKqMB3egbNmjeKz5Y8' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": "string",
      "medicamentos": [
        {
          "nome": "string",
          "posologia": "string",
          "quantidade": 0,
          "composicao": "string",
          "fabricante": "string",
          "titularidade": "string",
          "preco": 0
        }
      ]
    }
  }
}'
```

info

* O campo `data[].attributes.nome` possui um limite de 250 caracteres;
