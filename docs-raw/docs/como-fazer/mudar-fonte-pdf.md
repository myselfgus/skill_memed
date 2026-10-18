https://doc.memed.com.br/docs/como-fazer/mudar-fonte-pdf/

# Mudar a fonte do PDF da receita

A Memed possibilita alterar o tamanho da fonte, e o tipo de fonte no PDF da receita.

**Obs:** Recomendamos utilizar tamanhos de fontes menores que 18, pois acima deste valor e
dependendo da quantidades de dados no PDF da receita, poderá haver sobreposição de textos.

## Mudar fonte do PDF da receita via API

Dentro desse [artigo](/docs/backend/impressao) existe uma explicação de como utilizar um cURL para
alterar as configurações de impressão.

Mas para alterar somente o tamanho e o tipo da fonte da prescrição, prescisa-se utilizar as propriedades
`titulo_tamanho_fonte`, `titulo_fonte`, `rodape_fonte`, `rodape_tamanho_fonte`,
`subtitulo_fonte` e `subtitulo_tamanho_fonte`.

Os atributos `titulo_tamanho_fonte` e `titulo_fonte` se referem aos textos do cabeçalho.
Os atributos `rodape_fonte` e `rodape_tamanho_fonte` se referem aos textos do rodapé.
Os atributos `subtitulo_fonte` e `subtitulo_tamanho_fonte` se referem aos textos do corpo da prescrição.

Pode-se também alterar as cores da fonte editando as propriedades `titulo_cor`, `rodape_cor` e `subtitulo_cor`.
Os valores podem ser em hexadecimal.

Segue um exemplo de cURL abaixo de como ficaria essas configurações:

```js
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
        "type": "configuracoes-prescricao",
        "attributes": {
                "indice": 1,
                "titulo_fonte": "Droid Serif Italic",
                "titulo_tamanho_fonte": 22,
                "titulo": "Dr. Teste da Silva Teste",
                "titulo_cor": "#20afd6",
                "subtitulo_fonte": "Proxima Nova",
                "subtitulo_tamanho_fonte": 6,
                "subtitulo": "",
                "subtitulo_cor": "#8c8c8c",
                "tamanho_cabecalho": 1,
                "rodape_fonte": "Proxima Nova",
                "rodape_tamanho_fonte": 14,
                "rodape": "",
                "rodape_cor": "#8c8c8c",
                "tamanho_rodape": 8,
                "modelo_cabecalho_rodape": 0,
                "ativo": true,
                "imprimir_controle_especial": false,
                "imprimir_controle_especial_antibioticos": true,
                "imprimir_controle_especial_c4": false,
                "imprimir_lme": false,
                "zoom_logo": 65,
                "header_image": "parceiros\/templates\/parceiro-template-552-39456-header.jpeg",
                "footer_image": "parceiros\/templates\/parceiro-template-552-39456-footer.jpeg",
                "number_of_lme_copies": 1
            }
     }
}'
```

O atributo `indice` com valor 1 se refere ao modelo 1 do PDF da receita.
Lembrando que a Memed disponibiliza 4 tipos de modelos para cada usuário prescritor. Se preferir
editar o modelo 2 do PDF da receita, coloque o valor 2 no atributo `indice`.
