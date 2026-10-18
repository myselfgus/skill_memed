https://doc.memed.com.br/docs/frontend/comandos-mdhub/new-prescription/

# Nova Prescrição (newPrescription)

Com o comando `newPrescription` é possível ter a mesma ação do botão "Nova Prescrição" da plataforma da Memed.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "newPrescription";
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "newPrescription");
```

### Exemplo

```js
await MdHub.command.send("plataforma.prescricao", "newPrescription");
```
