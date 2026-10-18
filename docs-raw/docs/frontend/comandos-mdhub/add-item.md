https://doc.memed.com.br/docs/frontend/comandos-mdhub/add-item/

# Adicionar item a Prescrição (addItem)

Com o comando `addItem` é possível manipular os itens da prescrição digital.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "addItem";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "addItem", {
  propriedade: "valor",
});
```

#### Propriedades do comando Add Item

| Propriedade | Valor padrão | Obrigatório/Opcional | Descrição |
| --- | --- | --- | --- |
| id | null | opcional | ID do medicamento na Memed (quando não informado, se transforma em texto livre) |
| nome | null | opcional | Nome do medicamento (utilizado em caso de texto livre). |
| posologia | null | opcional | Posologia descrição do uso. |
| quantidade | null | opcional | Quantidade do medicamento que será adicionado à prescrição (opcional, valor padrão é 1) informe quantidade 0 para uso contínuo |
| unit | null | opcional | Os valores válidos para o campo unit são: **"|embalagem|embalagens|form\_units.singular|form\_units.plural"**. |
| fabricante | null | opcional | Forma física relacionada à quantidade (opcional, valor padrão é 'embalagem'). Os valores válidos para o campo unit são: **"|embalagem|embalagens|form\_units.singular|form\_units.plural"**. |
| titularidade | null | opcional | Titularidade do medicamento |
| preco | null | opcional | Preço do medicamento |
| descricao | null | opcional | Descrição do medicamento |

### Medicamento com ID

Para adicionar um medicamento você precisa passar o ID desse medicamento da base de dados da Memed.

```js
await MdHub.command.send("plataforma.prescricao", "addItem", {
  id: "a123123123",
  posologia: "<p>HTML da posologia</p>",
  quantidade: 2,
  unit: "embalagens",
});
```

### Fórmulas com ID

```js
await MdHub.command.send("plataforma.prescricao", "addItem", {
  id: "f123123123",
  posologia: "<p>HTML da posologia</p>",
  quantidade: 2,
  unit: "embalagens",
});
```

### Exame com ID

```js
await MdHub.command.send("plataforma.prescricao", "addItem", {
  id: "e123123123",
  indicacoes: "<p>HTML da indicação</p>",
});
```

### Texto Livre

```js
await MdHub.command.send("plataforma.prescricao", "addItem", {
  nome: "Vitamina C, comprimido (100un)",
  posologia: "<p>HTML da posologia</p>",
  quantidade: 1,
  fabricante: "Nome do fabricante",
  titularidade: "Similar",
  preco: 1.99,
  descricao: "Ácido Ascórbico",
});
```
