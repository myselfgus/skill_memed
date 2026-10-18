https://doc.memed.com.br/docs/frontend/estilizar-front/

# Estilização da prescrição

É possível estilizar a cor primária da prescrição digital Memed para se adequar a cor primária do seu sistema.

Para mudar a cor padrão da prescrição você precisa enviar um atributo adicional ao
[carregamento do script](/docs/modos-de-carregamento) e informar uma cor
em **hexadecimal** para o atributo `data-color`.

Nota

O valor padrão para esse atributo é a cor primária da Memed. `#6161ff`

```html
<script data-color="{COR_EM_HEXADECIMAL}"></script>
```

Imagine que a cor do seu sistema seja vermelho(`#FF0000`) por exemplo.
O [carregamento do seu script](/docs/modos-de-carregamento) ficaria semelhante ao exemplo abaixo.

```html
<script
  src="{MEMED_SCRIPT_URL}"
  data-token="{TOKEN_ACESSO_USUARIO_PRESCRITOR}"
  data-color="#FF0000"
></script>
```

A mesma cenário vale para o [carregamento dinâmico do script](/docs/modos-de-carregamento#carregamento-din%C3%A2mico). Basta adicionar um atributo
chamado `data.color` ao carregamento do script e enviar o valor da cor em hexadecimal.

```js
script.data.color = "{COR_EM_HEXADECIMAL}";
```

Imagine que a cor do seu sistema seja vermelho (`#FF0000`) por exemplo.
O [carregamento dinâmico do seu script](/docs/modos-de-carregamento#carregamento-din%C3%A2mico) ficaria semelhante ao exemplo abaixo.

```js
var script = document.createElement("script");
script.src = "MEMED_SCRIPT_URL";
script.dataset.token = "TOKEN_ACESSO_USUARIO_PRESCRITOR";

//Adiciona o atributo data-color ao script que será carregado dinamicamente.
script.dataset.color = "#FF0000";

document.body.appendChild(script);
```
