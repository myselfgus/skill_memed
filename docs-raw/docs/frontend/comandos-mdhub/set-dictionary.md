https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-dictionary/

# Definir o nome do modulo (setDictionary)

Com o comando `setDictionary` você tem a possibilidade de customizar alguns textos da prescrição digital.
O botão que chamamos de "Protocolos" pode ser personalizado com o nome que o parceiro desejar. Ex: Modelos de Receita.
Para alterar o nome de onde tiver escrito "Protocolo", basta usar o comando abaixo:

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setDictionary";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "setDictionary", {
  propriedade: "valor",
});
```

### Propriedades de dicionário que você pode modificar

| Propriedade | Tipo | Obrigatório/Opcional | Valor Padrão |
| --- | --- | --- | --- |
| protocolPlural | string(255) | opcional | 'Protocolos' |
| protocolSingular | string(255) | opcional | 'Protocolo' |
| protocolSaved | string(255) | opcional | 'Protocolo salvo com sucesso!' |

## Exemplos

Veja abaixo um exemplo de implementação do comando `setDictionary`

```js
await MdSinapsePrescricao.command.send("hub", "core:setDictionary", {
  protocolPlural: "Padrões de receitas",
  protocolSingular: "Padrão de receita",
  protocolSaved: "Modelo de Receita salvo!",
});
```
