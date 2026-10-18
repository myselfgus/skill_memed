https://doc.memed.com.br/docs/como-fazer/manter-responsividade-prescricao/

# Manter a responsividade da aplicação embedded

Como os monitores de vídeos possuem diversos tamanhos e, também, o
parceiro pode colocar a plataforma prescrição no modo embedded, a Memed pode se adaptar aos diversos
tamanhos. Ou seja, a plataforma de prescrição da Memed é responsiva.

## Como fazer a plataforma de prescrição ficar responsiva?

A plataforma precisa ser carregada de forma [incorporada](/docs/modos-de-exibicao#incorporado)

Nesta forma de incorporada, precisa-se definir o nome da propriedade do `data-container`, e dentro do código HMTL,
o nome do elemento identificador da `div` que conterá o conteúdo da plataforma prescrição conforme exemplo abaixo:

```js
<script
  src="https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js"
  data-token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I"
  data-container="minha-prescricao"
></script>

<div id="minha-prescricao"></div>
```

Após definir as configurações acima, precisa-se definir as estilizações `CSS` do elemento `minha-prescricao`.
Exemplo:

```css
#minha-prescricao {
    position: relative;
    width: 100%;
    height: 100%;
    min-width: 820px;
    min-height: 700px;
}
```

Com isso, a plataforma de prescrição ocupará 100% da largura e altura do tamanho que a `div` tiver, porém terá o
tamanho mínimo de 820px largura e 700px de altura.

**Obs:**  A plataforma de prescrição precisa de um container (div) com a largura e altura mínima de, respectivamente,
820px e 700px. Caso esses valores forem menores, a visualização ficará prejudicada.

Veja um exemplo completo abaixo:
