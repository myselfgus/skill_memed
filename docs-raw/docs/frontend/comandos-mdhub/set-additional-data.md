https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-additional-data/

# Adicionar dados (setAdditionalData)

Com o comando `setAdditionalData` é possível adicionar informações extras no cabeçalho e rodapé.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setAdditionalData";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "setAdditionalData", {
  propriedade: "valor",
});
```

#### Propriedades do comando setAdditionalData

| Propriedade | Tipo | Obrigatório/Opcional | Descrição |
| --- | --- | --- | --- |
| header | Array[Object] | opcional | O Atributo `header` é um array de objetos que você pode passar informações para o cabeçalho da prescrição |
| footer | string | opcional | O footer é do tipo string e você pode passar informações adicionais para o rodapé da prescrição |

### Exemplo

Cada item do array do atributo `header` se transforma em 1 linha
no cabeçalho da prescrição.

Você pode usar `\n` para quebrar linha na string do atributo `footer` no rodapé

```js
await MdHub.command.send("plataforma.prescricao", "setAdditionalData", {
  header: [
    {
      Registro: "2911116",
    },
    {
      Sexo: "Masculino",
      "Estado Civil": "Solteiro",
      "Data de Nasc": "17/09/1991",
    },
    {
      Endereço: "Rua  Arthur prado, 513",
    },
    {
      Profissional: "Dra. Emilia Reis(CRM: 123456SP)",
    },
  ],
  footer:
    "Informações adicionais na primeira linhad do rodapé \n Segunda linha do rodapé",
});
```
