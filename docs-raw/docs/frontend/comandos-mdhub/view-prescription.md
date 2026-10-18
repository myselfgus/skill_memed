https://doc.memed.com.br/docs/frontend/comandos-mdhub/view-prescription/

# Reimpressão e edição de uma prescrição (viewPrescription)

Com o comando `viewPrescription` é possível implementar a reimpressão e edição de uma prescrição já gerada.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "viewPrescription";
parametro = "string";
```

### Sintaxe do comando

```js
await MdHub.command.send(
  "plataforma.prescricao",
  "viewPrescription",
  "ID_DA_PRESCRICAO"
);
```

### Exemplo

```js
await MdHub.command.send("plataforma.prescricao", "viewPrescription", "1234");
```
