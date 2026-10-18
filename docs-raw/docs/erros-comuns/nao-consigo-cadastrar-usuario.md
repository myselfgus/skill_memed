https://doc.memed.com.br/docs/erros-comuns/nao-consigo-cadastrar-usuario/

# Não consigo cadastrar o usuário

As solicitações da Memed retornam uma mensagem de erro que explica qual foi o problema encontrado. Para identificar o erro, o primeiro passo é recuperar a mensagem de erro.

## Situação 1:

```js
{
  "errors": [
    {
      "title": "Erro",
      "detail": "O objeto enviado não contém a propriedade \"data\"."
    }
  ]
}
```

Se o código acima for retornado, significa que a aplicação da Memed não conseguiu receber uma estrutura JSON no corpo da solicitação.
Isso pode ter duas possíveis causas:

* O cabeçalho Content-Type: application/json não foi adicionado à solicitação;
* Há um erro de sintaxe no JSON do corpo;
  + Uma vírgula está faltando;
  + Há comentários dentro do JSON;

## Situação 2:

A Memed valida alguns campos enviados na criação de usuários.
Portanto, é possível que alguns dados enviados não sejam válidos, o que resulta em uma solicitação mal-sucedida.

```js
{
  "errors": [
    {
      "code": "CPF",
      "title": "Erro de validação",
      "detail": "CPF precisa ser um CPF válido"
    }
  ]
}
```
