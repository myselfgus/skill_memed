https://doc.memed.com.br/docs/frontend/comandos-mdhub/logout/

# Sair do sistema (Logout)

A limpeza do local storage do navegador é necessária quando prescritores compartilham a mesma máquina (notebook/pc). Ela deve ser implementada OBRIGATORIAMENTE para evitar conflitos de informações entre os cadastros e consequentemente falhas de segurança.
Com o comando `logout` é possível executar essa limpeza.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.sdk";
nome_do_comando = "logout";
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.sdk", "logout");
```

### Exemplo

```js
await MdHub.command.send("plataforma.sdk", "logout");
```
