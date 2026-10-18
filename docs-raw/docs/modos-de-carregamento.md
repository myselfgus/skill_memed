https://doc.memed.com.br/docs/modos-de-carregamento/

# Modos de carregamento do script da prescrição digital

Existem duas formas de carregar o script da prescrição digital em sua aplicação.

* [**Estático**](/docs/modos-de-carregamento#carregamento-est%C3%A1tico): carrega o script Memed diretamente pela tag `<script>` em seu html
* [**Dinâmico**](/docs/modos-de-carregamento#carregamento-din%C3%A2mico): carrega o script Memed dinamicamente a partir de outro script.

### Carregamento Estático

Para carregar o script da prescrição digital de forma direta dentro do seu html, basta
criar uma tag `<script>` passando os dois principais atributos, o **src** com a url
[MEMED\_SCRIPT\_URL](/docs/frontend/configuracoes#urls),
e o **data-token** com o [token do usuário prescritor](/docs/backend/usuario-prescritor#obtendo-o-token-do-usu%C3%A1rio-prescritor)

Veja o exemplo abaixo:

```html
<script
  src="{MEMED_SCRIPT_URL}"
  data-token="{TOKEN_ACESSO_USUARIO_PRESCRITOR}"
></script>
```

### Carregamento Dinâmico

Você também pode carregar o script Memed de forma dinâmica. Para isso basta criar um elemento
de script e injetar dinamicamente na sua página HTML passando exatamente os mesmos atributos
que você passaria carregando o script de forma estática.

Veja o exemplo abaixo:

```js
// Cria um elemento de script
var script = document.createElement("script");

// Adiciona o atributo src com a url do script Memed
script.src = "MEMED_SCRIPT_URL";

// Adiciona o atributo token com o token de acesso do usuário prescritor
script.dataset.token = "TOKEN_ACESSO_USUARIO_PRESCRITOR";

//Injeta no html o elemento que foi criado dinamicamente
document.body.appendChild(script);
```

Para não haver problemas com o carregamendo dinâmico do script, recomendamos
que você só performe alguma lógica relacionada a prescrição Memed após ter a garantia
que o script foi completamente carregado. Você pode fazer isso através do evento `load`
atrelado ao elemento que você acabou de criar. Assim o seu html irá dizer quando esse
elemento foi completamente carregado.

Veja abaixo um exemplo de como implementar:

```js
var script = document.createElement("script");
script.src = "MEMED_SCRIPT_URL";
script.dataset.token = "TOKEN_ACESSO_USUARIO_PRESCRITOR";

// Quando o script terminar de carregar retorna uma função de callback
script.addEventListener("load", function () {
  // Aqui você pode performar qualquer lógica relacionado a prescrição Memed.
});

document.body.appendChild(script);
```

Uma boa prática do carregamento dinâmico é colocar tudo isso dentro de uma (ou mais) funções
para organizar melhor o seu código.

Segue abaixo um exemplo completo de como fazer isso.
