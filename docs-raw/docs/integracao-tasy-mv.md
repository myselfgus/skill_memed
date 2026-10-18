https://doc.memed.com.br/docs/integracao-tasy-mv/

# Integrando com Phillips Tasy e MV Soul

A Memed é uma plataforma 100% online, e por conta disso, é possível renderizar a Memed através das opções de abertura de páginas WEB disponíveis nos sistemas Tasy e Soul. Através dessas opções é possível disponibilizar a Memed das seguintes maneiras:

* Disponibilizar uma integração através de um barramento de dados + micro-aplicação
* Nativamente através do barramento TIE (Somente Phillips Tasy)

## Integrando com Phillips Tasy via micro-aplicacão

A Memed é uma plataforma 100% web, e por isso, para esse modelo de integração é preciso construir uma micro-aplicação web que será responsável por intermediar a comunicação entre a Memed e o serviço do MV/Tasy. Essa aplicação intermediária tem como principal objetivo ser a principal ponte de dados entre o sistema e a Memed, atuando como um gateway de comunicação na integração.

**Obs:**

* A plataforma da Memed somente suporta navegadores modernos (Google Chrome, Mozilla Firefox, IE 11+).
* Recomendamos que o desenvolvedor responsável pela integração tenha noção básica de Javascript e alguns conceitos como [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html).
* Será preciso subir uma aplicação web no servidor do parceiro.
* Se for usar o navegador Internet Explorer, algumas funcionalidades podem apresentar incompatibilidade. Caso isso ocorra, entre em contato com o time técnico da Memed.

**Webservice / API**

Será necessário um WebService/API do parceiro que abstraia os seguintes pontos:

* Capturar as informações do atendimento, com as informações do prescritor e do paciente dos sistemas MV/Tasy;
* Salvar a prescrição gerada na Memed (JSON, PDF, etc.) no lado do parceiro;
* Excluir a prescrição no lado do parceiro caso o prescritor exclua na Memed;
* Excluir a prescrição na Memed caso o prescritor exclua no MV/Tasy.

Alguns detalhes que o desenvolvedor do parceiro deve levar em consideração:

* A aplicação intermediária deve buscar os dados do prescritor e seu atendimento através do Webservice/API descrito anteriormente;
* O código deve conseguir ser executado através de informações que o MV/Tasy é capaz de informar no uso do prescritor. Ex.: Número de atendimento e número do prontuário;
* Código deve ser hospedado em um servidor do parceiro. Exemplo de URL para acesso: `https://home.suainstituicao.com.br?num_atendimento=<NUM_ATENDIMENTO>&num_prontuario=<NUM_PRONTUARIO>&usuario=<NUM_REGISTRO_PROFISSIONAL>`

**Desenho da arquitetura e detalhamento (1, 2 e 3)**

![desenho-arquitetura](https://cdn.memed.com.br/doc/desenho-arquitetura.png)

**1 - Aplicação Web Intermediária:** 
A URL com os parâmetros para pegar as informações da base de dados do MV/Tasy precisará apontar para essa aplicação. Nela estará toda a lógica de como cadastrar um prescritor, recuperar o token de um prescritor já cadastrado, etc.
Ela também será responsável por incluir os scripts da Memed, definir o paciente, entre outras ações que venham a ser necessárias.

**2 - Link para chamar a aplicação intermediária:** 
Aqui deve conter a URL da aplicação web intermediária, que será aberta no webview.

**3 - Módulo de prescrição da Memed:** 
Aqui é onde o prescritor terá toda a inteligência da plataforma da Memed como:

* Busca de medicamentos com uma base atualizada diariamente;
* Alertas de interações medicamentosas e alergias;
* Separação de vias inteligentes, levando em consideração a tarja do receituário;
* Entre outras features.

**Exemplo de como o usuário irá visualizar a Memed:**

![visualizacao-memed](https://cdn.memed.com.br/doc/visualizacao-memed.png)  

**A estrutura de integração neste esquema deverá ficar conforme fluxo de dados abaixo**

![tasy-mv-integrations-scheme](https://cdn.memed.com.br/doc/tasy-mv-integrations-scheme.jpg)

## Integrando Phillips Tasy via Integração Nativa

## MV/Tasy

Nesta parte de integração com o MV, o processo é semelhante ao aplicado com a integração Tasy via micro-aplicação.

Atenção!

Antes de prosseguir com a integração, garanta que o sistema cumpra os requisitos descritos em
[**Pré-requisitos**](/docs/intro#pr%C3%A9-requisitos).

### Gateway de comunicação

Será um serviço de Webservice / API. Esse serviço deverá contemplar os seguintes requisitos:

* Capturar as informações do atendimento, com as informações do prescritor e paciente dos sistemas MV/Tasy;
* Salvar a prescrição gerada na Memed (JSON, PDF, etc.) no sistema MV/Tasy;
* Excluir a prescrição no lado do parceiro caso o prescritor exclua na Memed;
* Excluir a prescrição na Memed caso o prescritor exclua no MV/Tasy.

### Memed Front-end

Aqui será a etapa onde as informações do sistema serão carregadas na Memed.

* Você pode criar um serviço utilizando os passos disponíveis na nossa documentação em [**primeiros passos**](/docs/primeiros-passos).

## Parceiros de software

Como uma solução de barramento de dados para integrações com Tasy/MV. Temos como parceiro de software a [CM Tecnologia](https://cmtecnologia.com.br/) que fornece soluções de barramento que podem ser usadas para integrar com a Memed.
