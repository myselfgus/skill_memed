https://doc.memed.com.br/docs/frontend/mdsinapseprescricao-mdhub/

# MdSinapsePrescricao & MdHub

Ao fazer o [carregamento correto](/docs/modos-de-carregamento) do script de prescição digital Memed, você
terá disponível a propriedade **MdSinapsePrescricao** que serve como ponte de acesso entre o seu front-end e a biblioteca **MdHub**.

É importante entender que todo o front-end da prescrição digital Memed é composta por módulos
e submódulos. Esses módulos são orquestrados pela biblioteca
interna chamada **MdHub**, e para ter acesso as funcionalidades do MdHub você
precisa acessar a biblioteca **MdSinapsePrescricao**.

Funcionalidades como: **adicionar paciente**, **manipular a interface da prescrição**,
**ligar e desligar funcionalidades** além de controlar também quando a prescrição digital Memed
deve ou não ser exibida dentro do seu sistema, estão disponíveis na biblioteca **MdHub**.

## MdSinapsePrescricao

Na biblioteca **MdSinapsePrescricao** existem dois eventos que você deve utilizar para
saber se os módulos do **MdHub** estão disponíveis ou foram encerrados.

Os eventos do `MdSinapsePrescricao` aceitam dois parâmetros: o primeiro é o nome do evento e
o segundo é uma função de callback que traz como parametro o módulo que foi iniciado ou encerrado.

Veja abaixo um exemplo de implementação destes eventos.

### Quando o módulo é iniciado.

```js
MdSinapsePrescricao.event.add("core:moduleInit", function (module) {});
```

Verificando se o módulo `plataforma-prescricao` foi **iniciado**

```js
MdSinapsePrescricao.event.add("core:moduleInit", (module) => {
  if (module.name === "plataforma.prescricao") {
    // significa que módulo de plataforma-prescrição foi iniciado
  }
});
```

### Quando o módulo é encerrado

```js
MdSinapsePrescricao.event.add("core:moduleHide", function (module) {});
```

Verificando se o módulo `plataforma-prescricao` foi **fechado**

```js
MdSinapsePrescricao.event.add("core:moduleHide", (module) => {
  if (module.moduleName === "plataforma.prescricao") {
    // significa que módulo plataforma-prescrição foi encerrado.
  }
});
```

Atenção

Note que na verificação do nome do módulo dentro do evento `core:moduleHide` não é igual a verificação
do módulo anterior. Isso acontece porque a propriedade retornanda no callback desse evento é `module.moduleName`, e não simplesmente
`module.name`.

## MdHub

Através da biblioteca **MdHub** você pode escutar eventos e enviar comandos no front-end da prescrição digital Memed.

### Comandos do MdHub

Através dos comandos do MdHub você pode incluir dados do paciente, adicionar configurações de impressão da prescrição e etc.

Comandos

Veja no detalhe [todos os comandos do Mdhub](/docs/frontend/comandos-mdhub)

A sintaxe do comando MdHub é:

```js
MdHub.command.send("nome_do_modulo", "nome_do_comando", {});
```

### Eventos do MdHub

Através dos eventos do MdHub você é avisado sobre eventos como: quando uma [prescrição foi concluída](/docs/frontend/eventos-mdhub/prescricao-impressa),
quando um [medicamento foi adicionando](/docs/frontend/eventos-mdhub/medicamento-adicionado)
ou quando um [medicamento foi removido](/docs/frontend/eventos-mdhub/medicamento-removido) da prescrição e etc.

Eventos

Veja no detalhe [todos os eventos do Mdhub](/docs/frontend/eventos-mdhub)

A sintaxe dos eventos do Mdhub é:

```js
MdHub.event.add("nome_do_evento", function (parametro_de_resposta) {});
```
