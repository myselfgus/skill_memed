https://doc.memed.com.br/docs/frontend/comandos-mdhub/find/

# Opções de Receituario (Find)

Com o comando `find` é possível ativar um dos quatro temas configurados nas opções de receituário.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.sdk";
nome_do_comando = "find";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.sdk", "find", {
  propriedade: "valor",
});
```

#### Propriedades do comando find

| Propriedade | Valor padrão | Obrigatório/Opcional | Descrição |
| --- | --- | --- | --- |
| resource | `opcoes-receituario/ativar/2` | obrigatório | Endpoint que ativa o receituário |
| cache | false | obrigatório | Flag que força a limpeza do cache de opções de receituário |

### Exemplo

```js
await MdHub.command.send("plataforma.sdk", "find", {
  resource: "opcoes-receituario/ativar/2",
  cache: false,
});
```
