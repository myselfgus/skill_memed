# Visão geral, primeiros passos, carregamento, exibição e credenciais

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- Integrando com Phillips Tasy e MV Soul — `https://doc.memed.com.br/docs/integracao-tasy-mv`
- Prescrição Digital Memed — `https://doc.memed.com.br/docs/intro`
- Modos de carregamento do script da prescrição digital — `https://doc.memed.com.br/docs/modos-de-carregamento`
- Modos de exibição da prescrição — `https://doc.memed.com.br/docs/modos-de-exibicao`
- Autorização para Credenciais de Produção — `https://doc.memed.com.br/docs/obter-credenciais`
- Primeiros passos — `https://doc.memed.com.br/docs/primeiros-passos`

---

<!-- fonte: https://doc.memed.com.br/docs/integracao-tasy-mv -->
## Integrando com Phillips Tasy e MV Soul

A Memed é uma plataforma 100% online, e por conta disso, é possível renderizar a Memed através das opções de abertura de páginas WEB disponíveis nos sistemas Tasy e Soul. Através dessas opções é possível disponibilizar a Memed das seguintes maneiras:

- Disponibilizar uma integração através de um barramento de dados + micro-aplicação
- Nativamente através do barramento TIE (Somente Phillips Tasy)

### Integrando com Phillips Tasy via micro-aplicacão

A Memed é uma plataforma 100% web, e por isso, para esse modelo de integração é preciso construir uma micro-aplicação web que será responsável por intermediar a comunicação entre a Memed e o serviço do MV/Tasy. Essa aplicação intermediária tem como principal objetivo ser a principal ponte de dados entre o sistema e a Memed, atuando como um gateway de comunicação na integração.

**Obs:**

- A plataforma da Memed somente suporta navegadores modernos (Google Chrome, Mozilla Firefox, IE 11+).
- Recomendamos que o desenvolvedor responsável pela integração tenha noção básica de Javascript e alguns conceitos como [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html).
- Será preciso subir uma aplicação web no servidor do parceiro.
- Se for usar o navegador Internet Explorer, algumas funcionalidades podem apresentar incompatibilidade. Caso isso ocorra, entre em contato com o time técnico da Memed.

**Webservice / API**

Será necessário um WebService/API do parceiro que abstraia os seguintes pontos:

- Capturar as informações do atendimento, com as informações do prescritor e do paciente dos sistemas MV/Tasy;
- Salvar a prescrição gerada na Memed (JSON, PDF, etc.) no lado do parceiro;
- Excluir a prescrição no lado do parceiro caso o prescritor exclua na Memed;
- Excluir a prescrição na Memed caso o prescritor exclua no MV/Tasy.

Alguns detalhes que o desenvolvedor do parceiro deve levar em consideração:

- A aplicação intermediária deve buscar os dados do prescritor e seu atendimento através do Webservice/API descrito anteriormente;
- O código deve conseguir ser executado através de informações que o MV/Tasy é capaz de informar no uso do prescritor. Ex.: Número de atendimento e número do prontuário;
- Código deve ser hospedado em um servidor do parceiro. Exemplo de URL para acesso: `https://home.suainstituicao.com.br?num_atendimento=<NUM_ATENDIMENTO>&num_prontuario=<NUM_PRONTUARIO>&usuario=<NUM_REGISTRO_PROFISSIONAL>`

**Desenho da arquitetura e detalhamento (1, 2 e 3)**

![desenho-arquitetura](https://cdn.memed.com.br/doc/desenho-arquitetura.png)

**1 - Aplicação Web Intermediária:** A URL com os parâmetros para pegar as informações da base de dados do MV/Tasy precisará apontar para essa aplicação. Nela estará toda a lógica de como cadastrar um prescritor, recuperar o token de um prescritor já cadastrado, etc. Ela também será responsável por incluir os scripts da Memed, definir o paciente, entre outras ações que venham a ser necessárias.

**2 - Link para chamar a aplicação intermediária:** Aqui deve conter a URL da aplicação web intermediária, que será aberta no webview.

**3 - Módulo de prescrição da Memed:** Aqui é onde o prescritor terá toda a inteligência da plataforma da Memed como:

- Busca de medicamentos com uma base atualizada diariamente;
- Alertas de interações medicamentosas e alergias;
- Separação de vias inteligentes, levando em consideração a tarja do receituário;
- Entre outras features.

**Exemplo de como o usuário irá visualizar a Memed:**

![visualizacao-memed](https://cdn.memed.com.br/doc/visualizacao-memed.png)  

**A estrutura de integração neste esquema deverá ficar conforme fluxo de dados abaixo**

![tasy-mv-integrations-scheme](https://cdn.memed.com.br/doc/tasy-mv-integrations-scheme.jpg)

### Integrando Phillips Tasy via Integração Nativa

### MV/Tasy

Nesta parte de integração com o MV, o processo é semelhante ao aplicado com a integração Tasy via micro-aplicação.

**Atenção!**

Antes de prosseguir com a integração, garanta que o sistema cumpra os requisitos descritos em [**Pré-requisitos**](https://doc.memed.com.br/docs/intro#pr%C3%A9-requisitos).

#### Gateway de comunicação

Será um serviço de Webservice / API. Esse serviço deverá contemplar os seguintes requisitos:

- Capturar as informações do atendimento, com as informações do prescritor e paciente dos sistemas MV/Tasy;
- Salvar a prescrição gerada na Memed (JSON, PDF, etc.) no sistema MV/Tasy;
- Excluir a prescrição no lado do parceiro caso o prescritor exclua na Memed;
- Excluir a prescrição na Memed caso o prescritor exclua no MV/Tasy.

#### Memed Front-end

Aqui será a etapa onde as informações do sistema serão carregadas na Memed.

- Você pode criar um serviço utilizando os passos disponíveis na nossa documentação em [**primeiros passos**](https://doc.memed.com.br/docs/primeiros-passos).

### Parceiros de software

Como uma solução de barramento de dados para integrações com Tasy/MV. Temos como parceiro de software a [CM Tecnologia](https://cmtecnologia.com.br/) que fornece soluções de barramento que podem ser usadas para integrar com a Memed.

---

<!-- fonte: https://doc.memed.com.br/docs/intro -->
## Prescrição Digital Memed

Esta página é uma visão geral da documentação da integração com a prescrição digital Memed

**Atenção**

Como a Memed é uma plataforma para profissionais de saúde, usamos a referência **prescritor** ao invés de títulos específicos como **médico**, **dentista**, **enfermeiro** ou outros profissionais habilitados nos textos da documentação.

#### Conheça a prescrição digital Memed

**Aproximamos e conectamos o ecossistema de saúde:** Tornamos o prescritor muito mais próximo do paciente por meio da receita digital, promovendo uma prática médica que valoriza e encanta os pacientes.

**Prescrição com apenas 3 cliques:** Mais produtividade e segurança no suporte a decisão clínica com a nossa central de alertas de interação medicamentosas

**Gestão baseada em informações em tempo real:** Informações estruturadas sobre a prescrição, compra de medicamento e agendamento de exames.

#### Por que o seu software deveria se integrar com a prescrição digital Memed

Existem uma variedade de prescrições digitais no mercado, porém acreditamos que a Memed é a melhor escolha por entregar segurança, confiabilidade, flexibilidade e produtividade para o prescritor. Além de fornecer as melhores ferramentas para a adesão do paciente ao tratamento.

- Temos a maior e mais atualizada base de medicamentos, exames e periféricos, com mais de 60.000 itens
- Alerta de interações medicamentosas e alergias com monografia em português
- Acesso rápido ao histórico de prescrições para envio e reenvio por SMS, e-mail ou WhatsApp
- Base de medicamentos e exames atualizada diariamente
- Sempre disponível para prescritores e pacientes
- Aceita em mais de 30 mil farmácias
- O paciente tem possibilidade de compra de medicamentos da prescrição digital com desconto e comodidade
- Integração com assinadores digitais pronta para uso
- Possibilidades de personalizações do sistema e do PDF da prescrição digital

#### Como funciona a nossa integração?

A imagem abaixo ilustra de forma simplificada o fluxo de integração entre o seu software e a prescrição digital Memed. ![fluxo](https://cdn.memed.com.br/doc/simplified-integration-flux.png)

#### Pré-requisitos

Para se integrar com a prescrição digital Memed, você precisa garantir alguns pré-requisitos:

**Guia rápido**

Consulte [Boas Práticas de Integração](https://doc.memed.com.br/docs/boas-praticas-integracao) para a implementação de referência completa — fluxo frontend, conformidade LGPD e critérios de homologação.

##### Configurações

- **Par de chaves:** Obter um par de chaves(`api-key` + `secret-key`) para ter acesso aos ambientes de **HOMOLOGAÇÃO** e **PRODUÇÃO** da Memed.

##### Backend

- **Conexão segura entre servidores:** O seu software precisa ser capaz de enviar e receber requisições seguras utilizando o protocolo **HTTPS** em ambiente de homologação e produção.

- **Requisições entre APIs:** Seu software precisa ser capaz de enviar requisições via **backend** para a **API** da Memed.

##### Frontend

- **Script Memed:** Seu software precisa ser capaz de baixar o **script Memed** no seu **frontend**.

##### Compatibilidade de navegadores

Recomendamos sempre o uso de navegadores modernos e atualizados para um bom aproveitamento da nossa prescrição digital. Navegadores desatualizados como IE (Internet Explore) podem apresentar incompatibilidades com nosso software. Portanto, não damos suporte a esse tipo de navegador.

| Nome | Fornecedor | Versão |
|---|---|---|
| Firefox | Mozilla Foundation | 112 |
| Chrome | Google | 112.0 |
| Opera | Opera Software | 97 |
| Safari | Apple | 15.6 |
| Internet Explorer | Microsoft | 15.0 |
| Edge | Microsoft | 111 |

#### Comece agora!

Agora que você já entende o nosso fluxo de integração e conhece os pré-requisitos necessários, você já pode começar o passo a passo da integração.

- Inicie a sua integração através dos [primeiros passos](https://doc.memed.com.br/docs/primeiros-passos)
- Tenha a mão tutoriais na parte de [Como fazer](https://doc.memed.com.br/docs/como-fazer)
- Entenda funções exclusivas do [Backend da API Memed](https://doc.memed.com.br/docs/backend-api)
- Customize o módulo de prescrição através das funcionalidades do [Frontend](https://doc.memed.com.br/docs/frontend)
- Consulte os [erros comuns](https://doc.memed.com.br/docs/erros-comuns)
- Tire suas duvidas nos tópicos de [duvidas frequentes](https://doc.memed.com.br/docs/duvidas-frequentes)
- Faça uso dos [certificados digitais](https://doc.memed.com.br/docs/assinaturas-digitais) na plataforma
- Conclua sua integração obtendo a [Autorização para Credenciais de Produção](https://doc.memed.com.br/docs/obter-credenciais)

---

<!-- fonte: https://doc.memed.com.br/docs/modos-de-carregamento -->
## Modos de carregamento do script da prescrição digital

Existem duas formas de carregar o script da prescrição digital em sua aplicação.

- [**Estático**](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-est%C3%A1tico): carrega o script Memed diretamente pela tag `<script>` em seu html
- [**Dinâmico**](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-din%C3%A2mico): carrega o script Memed dinamicamente a partir de outro script.

#### Carregamento Estático

Para carregar o script da prescrição digital de forma direta dentro do seu html, basta criar uma tag `<script>` passando os dois principais atributos, o **src** com a url [MEMED_SCRIPT_URL](https://doc.memed.com.br/docs/frontend/configuracoes#urls), e o **data-token** com o [token do usuário prescritor](https://doc.memed.com.br/docs/backend/usuario-prescritor#obtendo-o-token-do-usu%C3%A1rio-prescritor)

Veja o exemplo abaixo:

```
<script
  src="{MEMED_SCRIPT_URL}"
  data-token="{TOKEN_ACESSO_USUARIO_PRESCRITOR}"
></script>
```

#### Carregamento Dinâmico

Você também pode carregar o script Memed de forma dinâmica. Para isso basta criar um elemento de script e injetar dinamicamente na sua página HTML passando exatamente os mesmos atributos que você passaria carregando o script de forma estática.

Veja o exemplo abaixo:

```
// Cria um elemento de script
var script = document.createElement("script");

// Adiciona o atributo src com a url do script Memed
script.src = "MEMED_SCRIPT_URL";

// Adiciona o atributo token com o token de acesso do usuário prescritor
script.dataset.token = "TOKEN_ACESSO_USUARIO_PRESCRITOR";

//Injeta no html o elemento que foi criado dinamicamente
document.body.appendChild(script);
```

Para não haver problemas com o carregamendo dinâmico do script, recomendamos que você só performe alguma lógica relacionada a prescrição Memed após ter a garantia que o script foi completamente carregado. Você pode fazer isso através do evento `load` atrelado ao elemento que você acabou de criar. Assim o seu html irá dizer quando esse elemento foi completamente carregado.

Veja abaixo um exemplo de como implementar:

```
var script = document.createElement("script");
script.src = "MEMED_SCRIPT_URL";
script.dataset.token = "TOKEN_ACESSO_USUARIO_PRESCRITOR";

// Quando o script terminar de carregar retorna uma função de callback
script.addEventListener("load", function () {
  // Aqui você pode performar qualquer lógica relacionado a prescrição Memed.
});

document.body.appendChild(script);
```

Uma boa prática do carregamento dinâmico é colocar tudo isso dentro de uma (ou mais) funções para organizar melhor o seu código.

Segue abaixo um exemplo completo de como fazer isso.

---

<!-- fonte: https://doc.memed.com.br/docs/modos-de-exibicao -->
## Modos de exibição da prescrição

Existem dois modos de exibir a prescrição Memed dentro da sua aplicação.

- [**Tela inteira**](https://doc.memed.com.br/docs/modos-de-exibicao#tela-inteira): a tela da Memed sobrepõe a sua aplicação
- [**Incorporado**](https://doc.memed.com.br/docs/modos-de-exibicao#incorporado): a tela da Memed pode ser incluída em um espaço definido dentro da sua aplicação

#### Tela inteira

**Este é o modo de exibição que recomendamos**

A exibição de tela inteira, como o próprio nome já diz, apresentará a prescrição ocupando toda a tela do seu sistema. O modo de exibição de **tela inteira** já é o padrão Memed. Portanto não precisa fazer nada adicional além dos passos de [carregamento do script da prescrição memed](https://doc.memed.com.br/docs/modos-de-carregamento).

#### Incorporado

O modo incorporado carregará a tela da Memed em um elemento específico dentro de sua aplicação. Assim você pode adequar a prescrição digital Memed a um layout já implementado dentro de seu software.

**Atenção**

É importante se atentar aos tamanhos **mínimos** que o **elemento(div)** em que a prescrição incorporada terá.

```
/* mínimo de largura */
min-width: 820px;
/* mínimo de altura */
min-height: 700px;
```

Não respeitar essas dimensões pode ocasionar em erro na hora de exibir sua prescrição digital.

Para utilizar o modo incorporado no [carregamento estatico do script](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-est%C3%A1tico) você precisa enviar no um atributo adicional chamado `data-container`. Nesse atributo você deve indicar o identificador do elemento em que a prescrição será incorporada.

```
<script data-container="{ID_ELEMENTO_HTML}"></script>
```

Junto com os outros atributos ficaria algo como:

```
<script
  src="{MEMED_SCRIPT_URL}"
  data-token="{TOKEN_ACESSO_USUARIO_PRESCRITOR}"
  data-container="{ID_ELEMENTO_HTML}"
></script>
```

Um exemplo com a junção do carregamento do script mais a estrutura HTML da sua página seria algo semelhante ao exemplo mostrado abaixo.

```
<!DOCTYPE html>
<html>
  <head>
    <title>Titulo do seu Software</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <!-- Elemento com identificador "prescricao-memed" -->
    <div id="prescricao-memed"></div>

    <!--Carrega o script Memed-->
    <script
      src="{MEMED_SCRIPT_URL}"
      data-token="{TOKEN_ACESSO_USUARIO_PRESCRITOR}"
      data-container="prescricao-memed"
    ></script>
  </body>
</html>
```

**Nota**

O identificador **"prescricao-memed"** é apenas exemplo, você pode usar o nome que quiser para o identificador da sua DIV. Apenas fique atento para que o nome do identificador seja o mesmo nome que estará no atributo `data-container` do carregamento do script da prescrição.

Segue um exemplo completo do modo incorporado no carregamento estático do script:

Agora para utilizar o modo incorporado, no caso de [carregamento dinâmico do script](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-din%C3%A2mico) de prescrição Memed, você deve também enviar o atributo adicional na criação do elemento

```
// doc oficial: script.data.container (não existe no DOM); correto:
script.dataset.container = "{ID_ELEMENTO_HTML}";
```

Veja um exemplo abaixo de como ficaria código javascript do modo carregamento estático com a tela incorporada:

```
var script = document.createElement("script");
script.src = "{MEMED_SCRIPT_URL}";
script.dataset.token = "{TOKEN_ACESSO_USUARIO_PRESCRITOR}";

//Adiciona o atributo data-container ao script que será carregado dinamicamente.
// doc oficial: script.data.container (não existe no DOM); correto:
script.dataset.container = "{ID_ELEMENTO_HTML}";

document.body.appendChild(script);
```

---

<!-- fonte: https://doc.memed.com.br/docs/obter-credenciais -->
## Autorização para Credenciais de Produção

**Último passo antes de colocar a integração em produção**

Neste [formulário](https://forms.gle/Z3M6TGhf2GMVmzH56), procederemos ao registro das informações necessárias para que sua empresa se torne nossa parceira, assegurando o cumprimento das boas práticas descritas em nossa documentação e o seguimento dos passos essenciais para uma integração bem-sucedida.

## Requisitos Obrigatórios

**IMPORTANTE:** Antes de realizar o preenchimento do formulário, certifique-se que os seguintes passos foram implementados:

## 1) Cadastro do Usuario Prescritor

Verifique se o cadastro do prescritor foi realizado contendo todas as informações listadas abaixo:

- Nome e Sobrenome
- Registro Profissional + UF (O Registro pode ser o número de registro CRM, CRO, COREN, CRMV, CRF, CRN, CREFITO, CRP, CRFa ou CREF)
- E-mail
- Especialidade
- Data de Nascimento
- CPF

## 2) Configurando o Paciente

O comando é `setPaciente` utilizado para enviar os dados do paciente para a prescrição da Memed. Verifique se o comando `setPaciente` foi implementado contendo todas as informações listadas abaixo:

- Nome e Sobrenome
- E-mail
- Telefone celular (Exemplo: 11999999999)
- Data de Nascimento
- CPF

Confira [Comandos Mdhub](https://doc.memed.com.br/docs/frontend/comandos-mdhub)

## 3) Eventos

Caso esteja salvando a receita gerada no prontuário do paciente, implementar os eventos:

- [`prescricaoImpressa`](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa) (para capturar o momento em que a prescrição foi emitida e recuperar os dados para o prontuário)

- [`prescricaoExcluida`](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-excluida) (para evitar que prescritor tente acessar um documento que foi excluído).

- Obs: a receita pode ser excluída pelo prescritor no histórico ou ao editá-la, e se ele tentar abrir uma receita salva no prontuário que foi excluída, vai dar erro.

  Confira [Eventos Mdhub](https://doc.memed.com.br/docs/frontend/eventos-mdhub)

## 4) Termo de Responsabilidade

A Memed se resguarda o direito de avaliar a sua Integração em até 180 dias após a liberação das Chaves de Produção serem enviadas e de, eventualmente, revogar as mesmas em caso de não-cumprimento das Boas Práticas apontadas na documentação e validadas neste [formulário](https://forms.gle/mjPRJpaJ1EsKZp18A).

## 5) A permissão será revogada caso:

- O cadastro do prescritor não esteja completo.
- Sejam identificadas falhas de segurança no front-end do parceiro, como deixar as credenciais **API-KEY** e **SECRET-KEY** visíveis.
- Features desativadas com o comando [setFeatureToggle](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle) estejam em funcionamento inadequadamente.
- Revisaremos o fluxo de [capturar uma prescrição](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa).

---

<!-- fonte: https://doc.memed.com.br/docs/primeiros-passos -->
## Primeiros passos

Integrar com a prescrição digital Memed é simples e rápido. Siga o passo a passo e ao final desse módulo de primeiros passos, você já será capaz de utilizar vários recursos da nossa prescrição digital.

**Atenção**

Lembre-se que todo o passo a passo dessa documentação estará apontando para o **ambiente de homologação (testes)** da Memed. No momento em que você obtiver as **chaves de produção (api-key e secret-key)**, você precisará reconfigurar os endpoints de [BACKEND](https://doc.memed.com.br/docs/backend/configuracoes#urls-de-produ%C3%A7%C3%A3o) e [FRONTEND](https://doc.memed.com.br/docs/frontend/configuracoes#urls-de-produ%C3%A7%C3%A3o) da sua aplicação para apontar para o **ambiente de produção** da Memed.

### Fluxo de integração

Segue abaixo um desenho do fluxo simplifiacado da integração com a prescrição digital memed. ![fluxo](https://cdn.memed.com.br/doc/simplified-integration-flux.png)

### Configurações básica

**Atenção**

O nosso ambiente de **homologação** estará **indisponível** das 0h às 6h, de segunda a sexta-feira, e ao longo de **todo o fim de semana**.

#### Obtendo o par de chaves (homologação)

O par de chaves utilizados no ambiente de **homologação** é fixo.

**API_KEY**

```
iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm
```

**SECRET_KEY**

```
Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
```

**Atenção**

**Nunca** deixe o seu par de chaves **visíveis** no **front-end**.

#### URLs Memed (homologação)

**API URL**

Essa url abaixo é utilizada para fazer as requisições do tipo `HTTP Rest` para o back-end da api da Memed.

**MEMED_API_URL**

```
https://integrations.api.memed.com.br/v1
```

**Script URL**

Essa url abaixo é utilizada para baixar os scripts da Memed.

**MEMED_SCRIPT_URL**

```
https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js
```

**Recomendamos**

Recomendamos que você veja no detalhe as nossas recomendações de como configurar o seu [**backend**](https://doc.memed.com.br/docs/backend/configuracoes) e o seu [**frontend**](https://doc.memed.com.br/docs/frontend/configuracoes) para uma integração mais completa com a prescrição digital memed.

### Backend

A integração com a prescrição digital Memed é baseada na perspectiva do usuário prescritor (profissional de saúde). Por isso, para renderizar a prescrição digital Memed dentro do seu software, você precisa efetuar o cadastro do prescritor e obter o token de acesso dele.

#### Cadastrando o prescritor via API

Para obter o Token do usuário prescritor (`data-token`), temos as seguintes opções:

- [Cadastrar um usuário prescritor novo](https://doc.memed.com.br/docs/como-fazer/cadastrar-prescritor)
- [Obter dados do usuário prescritor](https://doc.memed.com.br/docs/como-fazer/obter-dados-usuario)

**Veja mais detalhes**

Para o nosso exemplo de integração não vamos utilizar todas as **funcionalidades** disponíveis na **api da Memed**. Para mais detalhes de todas as **ações disponíveis entre o seu backend e a API Memed** [clique aqui](https://doc.memed.com.br/docs/backend-api)

### Frontend

Agora que você já tem o token do usuário (`data-token`), podemos seguir com a implementação no frontend.

#### Configurando o Frontend

A primeira etapa que você precisa fazer é carregar o script de prescrição digital informando a ***MEMED_SCRIPT_URL*** junto com o ***TOKEN*** de acesso do usuário prescritor. Estes dois você já obteve via backend na requisição de [obter](https://doc.memed.com.br/docs/como-fazer/obter-dados-usuario) ou [cadastrar](https://doc.memed.com.br/docs/como-fazer/cadastrar-prescritor) o prescritor.

**Atenção**

*MEMED_SCRIPT_URL* que vamos utilizar neste exemplo é a **URL** de **homologação** da Memed.

Agora um exemplo de uma pagina em HTML + javascript no seu frontend passando os seguintes atributos:

```
src="MEMED_SCRIPT_URL"
data-token="TOKEN_DO_USUARIO_OBTIDO_NO_CADASTRO_VIA_API"
```

##### Exemplo da página completa com o script da **MEMED_SCRIPT_URL** junto com o **TOKEN**:

```
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Meu sistema de Saúde</title>
  </head>
  <body>
    <script
      type="text/javascript"
      src="https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js"
      data-token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I"
    ></script>
    <!-- Proximo passo é acionar os comandos do modulo da prescrição -->
  </body>
</html>
```

Resultado: ![Integração rodando, pagina em branco](https://cdn.memed.com.br/doc/integracao_exemplo_page_0.png)

Como resultado temos a tela em branco que já está disponivel para executar comandos para acionar os comandos do modulo da prescrição.  
Outro ponto é que o console avisa em qual ambiente a integração da Memed está rodando:

```
ENVIRONMENT integrations
we are all set!!!
```

**Veja mais detalhes**

Você também pode carregar o script dinâmicamente. Para mais detalhes de todas as formas de carregar o script da Memed [clique aqui](https://doc.memed.com.br/docs/modos-de-carregamento#carregamento-din%C3%A2mico).

#### Exibindo a prescrição digital

Agora que já adicionou o script de prescrição digital Memed no seu frontend, já podemos começar a acionar os comandos, ouvir eventos e habilitar ou desabilitar os módulos para a renderização da prescrição.

Para mostrar a prescrição digital na tela do usuário, você precisará utilizar o método `show` do módulo `plataforma.prescricao`. Porém, se você tentar acessar alguma propriedade do módulo antes que o mesmo esteja completamente disponível, isso acarretará em vários erros.

**Erros comuns**

Caso esteja enfrentando algum problema favor verificar nossa seção de [erros comuns](https://doc.memed.com.br/docs/erros-comuns)

Então, antes de utilizar qualquer comando do módulo de prescrição, você precisa garantir que o módulo esteja devidamente carregado (e disponível). Para isso, vamos utilizar o evento `core:moduleInit` que retornar em seu segundo parâmetro uma função de callback contendo algumas informações sobre o módulo.

```
MdSinapsePrescricao.event.add("core:moduleInit", callbackFunction);
```

**Veja mais detalhes**

Existem vários eventos que você pode escutar durante a interação com a prescrição da Memed. Para mais detalhes sobre os eventos da prescrição digital da Memed [clique aqui](https://doc.memed.com.br/docs/frontend/eventos-mdhub).

Veja um exemplo de como ficaria essa estrutura com o evento mais a verificação se o módulo de prescrição está devidamente carregado.

```
// Evento que fica escutando o carregamento do core:moduleInit
// que contém o dentre outros o módulo de prescrição
MdSinapsePrescricao.event.add("core:moduleInit", function (module) {
  // aqui você verifica se o módulo que retornou nesse callback é o 'plataforma.prescricao'
  if (module.name === "plataforma.prescricao") {
    // aqui você aciona os comandos
    // ativa e desativa funcionalidades
    // renderiza a prescrição na tela do usuário
  }
});
```

Agora que você já entende o funcionamento básico dos módulos da prescrição digital, vamos ver um exemplo mais completo que adiciona os dados do paciente e mostra na tela do usuário a prescrição digital da Memed.

**Fique atento!**

Dados de paciente enviados via MdHub não podem ser alterados na prescrição manualmente! Veja a seção [dados do paciente](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient) para mais detalhes.

**Fluxo completo de integração**

Este snippet cobre apenas o comando `setPaciente`. Para a implementação de referência completa — carregamento do script, eventos LGPD e abertura do módulo — consulte [Boas Práticas de Integração](https://doc.memed.com.br/docs/boas-praticas-integracao).

```
// Enviar dados do paciente (await obrigatório — comando assíncrono)
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  // Campos obrigatórios
  idExterno: "parceiro-demo-pac-a1b2c3d4",
  nome: "Maria Souza",
  sexo: "Feminino",

  // Campos opcionais (obrigatórios para LME)
  cpf: "39053344705",
  data_nascimento: "15/05/1985",
  telefone: "11987654321",
  email: "paciente.exemplo@email.com",
  raca: "branca",
  peso: 75,
  altura: 1.75,
  endereco: "Rua das Flores, 100",
  cidade: "São Paulo",
  nome_mae: "Nome da mãe",
  dificuldade_locomocao: false,
});
```

Após `setPaciente`, abra o módulo com `await MdHub.module.show("plataforma.prescricao")` — preferencialmente no clique do botão, e não dentro de `core:moduleInit`.

**Implementação de referência**

O exemplo acima cobre apenas o comando `setPaciente`. Para o fluxo completo de integração — carregamento do script, eventos LGPD, `setWorkplace` e abertura do módulo — consulte [Boas Práticas de Integração](https://doc.memed.com.br/docs/boas-praticas-integracao).

**Veja mais detalhes**

No exemplo acima, estamos utilizando apenas o **comando** de `setPaciente` para setar os dados do paciente na prescrição e a função `show` do módulo de prescrição para mostrar a tela de prescrição. Existem vários comandos e funções relacionados aos módulos. Para mais detalhes sobre os comandos e módulos da prescrição Memed [clique aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient).

#### Veja como ficaria o seu frontend após implementar a prescrição Memed

**Veja mais detalhes**

Para o nosso exemplo simplificado acima, não utilizamos todas as funcionalidades disponíveis no frontend da Memed. Para mais detalhes de todas as funcionalidades, voce pode consultar nosso guia de [clique aqui](https://doc.memed.com.br/docs/frontend).

### Garantindo uma integração robusta

A Memed disponibiliza uma documentação completa sobre nossas APIs e scripts. Temos também alguns tutoriais e exemplos de implementação em algumas linguagens.

Para garantir que todas as funcionalidades estejam implementadas, você pode conferir através da tabela abaixo as principais funcionalidades e caminhos para a implantação:

- Ao cadastrar o prescritor, estou definindo os principais dados
  - ID Externo do prescritor
  - Nome
  - Sobrenome
  - CPF
  - Registro profissional + UF
  - Especialidade
  - Cidade
- Ao informar o paciente, estou definindo os principais dados
  - Nome completo
  - ID Externo do paciente
  - CPF
  - Telefone
  - Data de nascimento
- Recupero o retorno de informações da prescrição gerada
- Setar alergias do paciente
- Setar alertas de condições
- Definir configurações de impressão
- Definir cores conforme meu sistema
- Salvo uma cópia do PDF gerado na prescrição
- Salvo o link da receita digital
- Definir locais de atendimento do profissional
- Setar Feature Toggles no atendimento
- Cadastro os meus protocolos
- Campos adicionais no documento de impressão

### O que fazer a seguir?

Com a experiencia completa, você pode ainda explorar nossas documentações para mais informações adicionais!

- Se aprofunde nas [funcionalidades da API Memed](https://doc.memed.com.br/docs/backend-api)
- Entenda as diferentes formas de [renderizar a prescrição Memed](https://doc.memed.com.br/docs/modos-de-carregamento)
- Saiba como funciona para [habilitar e desabilitar funcionalidades da prescrição](https://doc.memed.com.br/docs/frontend/comandos-mdhub)
- Garanta agilidade ao prescritor e segurança de prescrição com [alertas de alergias](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-allergy) e [condições](https://doc.memed.com.br/docs/frontend/comandos-mdhub/categories-condition)
