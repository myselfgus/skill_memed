https://doc.memed.com.br/docs/como-fazer/configurar-cabecalho-rodape/

# Configurar cabeçalho e rodapé

# setAdditionalData

Com esse comando é possível adicionar informações extras no cabeçalho e rodapé da receita digital,
como dados do paciente, do prescritor, e local do atendimento.

Aqui está um exemplo de como ficaria os dados no cabecalho e rodapé no PDF da receita.

![exemplo-dados-header-footer](https://cdn.memed.com.br/doc/exemplo-dados-header-footer.png)

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/frontend/comandos-mdhub/set-additional-data).

## Configurar o cabeçalho e rodapé via api

O parceiro pode configurar através do cURL para fazer uma requisição para a api.
Para saber como utilizá-lo, leia esse [artigo](/docs/backend/impressao#configurar-impress%C3%A3o)

Os atributos do `cURL` do artigo acima como `margem_esquerda`, `margem_direita`, `margem_superior`, `margem_inferior`,
`tamanho_cabecalho`, `tamanho_rodape`, `mostrar_cabecalho_rodape_simples`, `mostrar_cabecalho_rodape_especial`
`header_image` e `footer_image` são utilizados para realizar essa configuração.

## Importar cabeçalho/rodapé de um PDF

É possível importar um cabeçalho e rodapé personalizados através de um arquivo em PDF pela api da Memed.
Para saber mais, leia esse [artigo](/docs/backend/impressao#importar-cabe%C3%A7alhorodap%C3%A9-de-um-pdf)
