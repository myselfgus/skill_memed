# Frontend: script, autenticação, MdSinapsePrescricao/MdHub, estilo

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- [](https://doc.memed.com.br/docs/frontend/comandos-mdhub) — `https://doc.memed.com.br/docs/frontend`
- Autenticação no frontend — `https://doc.memed.com.br/docs/frontend/autenticacao`
- Configurações — `https://doc.memed.com.br/docs/frontend/configuracoes`
- Estilização da prescrição — `https://doc.memed.com.br/docs/frontend/estilizar-front`
- MdSinapsePrescricao & MdHub — `https://doc.memed.com.br/docs/frontend/mdsinapseprescricao-mdhub`

---

<!-- fonte: https://doc.memed.com.br/docs/frontend -->
[](https://doc.memed.com.br/docs/frontend/comandos-mdhub)

### 🗃️ Comandos Mdhub

13 items

[](https://doc.memed.com.br/docs/frontend/eventos-mdhub)

### 🗃️ Eventos Mdhub

6 items

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/autenticacao -->
## Autenticação no frontend

A autenticação, no frontend da prescrição digital Memed, é feita através do **token de acesso** do usuário prescritor.

Essa autenticação acontece no momento em que você faz o carregamento do script digital Memed para dentro da sua aplicação.

Como mostra o exemplo abaixo:

```
<script
  src="{MEMED_SCRIPT_URL}"
  data-token="{TOKEN_DE_ACESSO_DO_USUARIO_PRESCRITOR}"  <!-- doc oficial: token=; o atributo correto é data-token -->
></script>
```

**Nota**

Saiba mais detalhes sobre como configurar e onde obter [**MEMED_SCRIPT_URL**](https://doc.memed.com.br/docs/frontend/configuracoes#urls) e o [**TOKEN_DE_ACESSO_DO_USUARIO_PRESCRITOR**](https://doc.memed.com.br/docs/backend/usuario-prescritor#obtendo-o-token-do-usu%C3%A1rio-prescritor).

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/configuracoes -->
## Configurações

As configurações propostas logo abaixo são apenas sugestões para facilitar a sua integração com a prescrição digital Memed.

**Dica**

Aproveite para ver detalhes das configurações do [**backend**](https://doc.memed.com.br/docs/backend/configuracoes).

### Variáveis de ambiente

Sugerimos a criação de algumas **variáveis de ambiente** para facilitar a alteração dos valores das chaves e das urls entre os ambientes de **homologação** e **produção**

```
#envs
MEMED_SCRIPT_URL=
```

### URLs

#### URLs de homologação

**MEMED_SCRIPT_URL**

```
https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js
```

#### URLs de produção

**MEMED_SCRIPT_URL**

```
https://partners.memed.com.br/integration.js
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/estilizar-front -->
## Estilização da prescrição

É possível estilizar a cor primária da prescrição digital Memed para se adequar a cor primária do seu sistema.

Para mudar a cor padrão da prescrição você precisa enviar um atributo adicional ao [carregamento do script](https://doc.memed.com.br/docs/modos-de-carregamento) e informar uma cor em **hexadecimal** para o atributo `data-color`.

**Nota**

O valor padrão para esse atributo é a cor primária da Memed. `#6161ff`

```
<script data-color="{COR_EM_HEXADECIMAL}"></script>
```

Imagine que a cor do seu sistema seja vermelho(`#FF0000`) por exemplo. O [carregamento do seu script](https://doc.memed.com.br/docs/modos-de-carregamento) ficaria semelhante ao exemplo abaixo.

```
<script
  src="{MEMED_SCRIPT_URL}"
  data-token="{TOKEN_ACESSO_USUARIO_PRESCRITOR}"
  data-color="#FF0000"
></script>
```

A mesma cenário vale para o [carregamento dinâmico do script](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-din%C3%A2mico). Basta adicionar um atributo chamado `data.color` ao carregamento do script e enviar o valor da cor em hexadecimal.

```
script.data.color = "{COR_EM_HEXADECIMAL}";
```

Imagine que a cor do seu sistema seja vermelho (`#FF0000`) por exemplo. O [carregamento dinâmico do seu script](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-din%C3%A2mico) ficaria semelhante ao exemplo abaixo.

```
var script = document.createElement("script");
script.src = "MEMED_SCRIPT_URL";
script.dataset.token = "TOKEN_ACESSO_USUARIO_PRESCRITOR";

//Adiciona o atributo data-color ao script que será carregado dinamicamente.
script.dataset.color = "#FF0000";

document.body.appendChild(script);
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/mdsinapseprescricao-mdhub -->
## MdSinapsePrescricao & MdHub

Ao fazer o [carregamento correto](https://doc.memed.com.br/docs/modos-de-carregamento) do script de prescição digital Memed, você terá disponível a propriedade **MdSinapsePrescricao** que serve como ponte de acesso entre o seu front-end e a biblioteca **MdHub**.

É importante entender que todo o front-end da prescrição digital Memed é composta por módulos e submódulos. Esses módulos são orquestrados pela biblioteca interna chamada **MdHub**, e para ter acesso as funcionalidades do MdHub você precisa acessar a biblioteca **MdSinapsePrescricao**.

Funcionalidades como: **adicionar paciente**, **manipular a interface da prescrição**, **ligar e desligar funcionalidades** além de controlar também quando a prescrição digital Memed deve ou não ser exibida dentro do seu sistema, estão disponíveis na biblioteca **MdHub**.

### MdSinapsePrescricao

Na biblioteca **MdSinapsePrescricao** existem dois eventos que você deve utilizar para saber se os módulos do **MdHub** estão disponíveis ou foram encerrados.

Os eventos do `MdSinapsePrescricao` aceitam dois parâmetros: o primeiro é o nome do evento e o segundo é uma função de callback que traz como parametro o módulo que foi iniciado ou encerrado.

Veja abaixo um exemplo de implementação destes eventos.

#### Quando o módulo é iniciado.

```
MdSinapsePrescricao.event.add("core:moduleInit", function (module) {});
```

Verificando se o módulo `plataforma-prescricao` foi **iniciado**

```
MdSinapsePrescricao.event.add("core:moduleInit", (module) => {
  if (module.name === "plataforma.prescricao") {
    // significa que módulo de plataforma-prescrição foi iniciado
  }
});
```

#### Quando o módulo é encerrado

```
MdSinapsePrescricao.event.add("core:moduleHide", function (module) {});
```

Verificando se o módulo `plataforma-prescricao` foi **fechado**

```
MdSinapsePrescricao.event.add("core:moduleHide", (module) => {
  if (module.moduleName === "plataforma.prescricao") {
    // significa que módulo plataforma-prescrição foi encerrado.
  }
});
```

**Atenção**

Note que na verificação do nome do módulo dentro do evento `core:moduleHide` não é igual a verificação do módulo anterior. Isso acontece porque a propriedade retornanda no callback desse evento é `module.moduleName`, e não simplesmente `module.name`.

### MdHub

Através da biblioteca **MdHub** você pode escutar eventos e enviar comandos no front-end da prescrição digital Memed.

#### Comandos do MdHub

Através dos comandos do MdHub você pode incluir dados do paciente, adicionar configurações de impressão da prescrição e etc.

**Comandos**

Veja no detalhe [todos os comandos do Mdhub](https://doc.memed.com.br/docs/frontend/comandos-mdhub)

A sintaxe do comando MdHub é:

```
MdHub.command.send("nome_do_modulo", "nome_do_comando", {});
```

#### Eventos do MdHub

Através dos eventos do MdHub você é avisado sobre eventos como: quando uma [prescrição foi concluída](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa), quando um [medicamento foi adicionando](https://doc.memed.com.br/docs/frontend/eventos-mdhub/medicamento-adicionado) ou quando um [medicamento foi removido](https://doc.memed.com.br/docs/frontend/eventos-mdhub/medicamento-removido) da prescrição e etc.

**Eventos**

Veja no detalhe [todos os eventos do Mdhub](https://doc.memed.com.br/docs/frontend/eventos-mdhub)

A sintaxe dos eventos do Mdhub é:

```
MdHub.event.add("nome_do_evento", function (parametro_de_resposta) {});
```
