https://doc.memed.com.br/docs/frontend/autenticacao/

# Autenticação no frontend

A autenticação, no frontend da prescrição digital Memed, é feita através do
**token de acesso** do usuário prescritor.

Essa autenticação acontece no momento em que você faz o carregamento do script digital Memed para dentro da sua aplicação.

Como mostra o exemplo abaixo:

```html
<script
  src="{MEMED_SCRIPT_URL}"
  token="{TOKEN_DE_ACESSO_DO_USUARIO_PRESCRITOR}"
></script>
```

Nota

Saiba mais detalhes sobre como configurar e onde obter [**MEMED\_SCRIPT\_URL**](/docs/frontend/configuracoes#urls)
e o [**TOKEN\_DE\_ACESSO\_DO\_USUARIO\_PRESCRITOR**](/docs/backend/usuario-prescritor#obtendo-o-token-do-usu%C3%A1rio-prescritor).
