https://doc.memed.com.br/docs/intro/

# Prescrição Digital Memed

Esta página é uma visão geral da documentação da integração com a prescrição digital Memed

Atenção

Como a Memed é uma plataforma para profissionais de saúde, usamos a referência **prescritor** ao invés de títulos específicos como **médico**, **dentista**, **enfermeiro** ou outros profissionais habilitados nos textos da documentação.

### Conheça a prescrição digital Memed

**Aproximamos e conectamos o ecossistema de saúde:** Tornamos o prescritor muito mais próximo do paciente por meio da receita digital, promovendo uma prática médica que valoriza e encanta os pacientes.

**Prescrição com apenas 3 cliques:** Mais produtividade e segurança no suporte a decisão clínica com a nossa central de alertas de interação medicamentosas

**Gestão baseada em informações em tempo real:** Informações estruturadas sobre a prescrição, compra de medicamento e agendamento de exames.

### Por que o seu software deveria se integrar com a prescrição digital Memed

Existem uma variedade de prescrições digitais no mercado, porém acreditamos que a Memed é a melhor escolha por entregar segurança, confiabilidade, flexibilidade e produtividade para o prescritor. Além de fornecer as melhores ferramentas para a adesão do paciente ao tratamento.

* Temos a maior e mais atualizada base de medicamentos, exames e periféricos, com mais de 60.000 itens
* Alerta de interações medicamentosas e alergias com monografia em português
* Acesso rápido ao histórico de prescrições para envio e reenvio por SMS, e-mail ou WhatsApp
* Base de medicamentos e exames atualizada diariamente
* Sempre disponível para prescritores e pacientes
* Aceita em mais de 30 mil farmácias
* O paciente tem possibilidade de compra de medicamentos da prescrição digital com desconto e comodidade
* Integração com assinadores digitais pronta para uso
* Possibilidades de personalizações do sistema e do PDF da prescrição digital

### Como funciona a nossa integração?

A imagem abaixo ilustra de forma simplificada o fluxo de integração entre o seu software e a prescrição digital Memed.
![fluxo](https://cdn.memed.com.br/doc/simplified-integration-flux.png)

### Pré-requisitos

Para se integrar com a prescrição digital Memed, você precisa garantir alguns pré-requisitos:

Guia rápido

Consulte [Boas Práticas de Integração](/docs/boas-praticas-integracao) para a implementação de referência completa — fluxo frontend, conformidade LGPD e critérios de homologação.

#### Configurações

* **Par de chaves:** Obter um par de chaves(`api-key` + `secret-key`)
  para ter acesso aos ambientes de **HOMOLOGAÇÃO** e **PRODUÇÃO** da Memed.

#### Backend

* **Conexão segura entre servidores:** O seu software precisa ser capaz de enviar e receber requisições seguras utilizando o protocolo **HTTPS** em ambiente de homologação e produção.
* **Requisições entre APIs:** Seu software precisa ser capaz de enviar requisições via **backend** para a **API** da Memed.

#### Frontend

* **Script Memed:**  Seu software precisa ser capaz de baixar o **script Memed** no seu **frontend**.

#### Compatibilidade de navegadores

Recomendamos sempre o uso de navegadores modernos e atualizados para um bom aproveitamento da nossa prescrição digital. Navegadores desatualizados como IE (Internet Explore) podem apresentar incompatibilidades com nosso software. Portanto, não damos suporte a esse tipo de navegador.

| Nome | Fornecedor | Versão |
| --- | --- | --- |
| Firefox | Mozilla Foundation | 112 |
| Chrome | Google | 112.0 |
| Opera | Opera Software | 97 |
| Safari | Apple | 15.6 |
| Internet Explorer | Microsoft | 15.0 |
| Edge | Microsoft | 111 |

### Comece agora!

Agora que você já entende o nosso fluxo de integração
e conhece os pré-requisitos necessários, você já pode começar o passo a passo da integração.

* Inicie a sua integração através dos [primeiros passos](/docs/primeiros-passos)
* Tenha a mão tutoriais na parte de [Como fazer](/docs/como-fazer)
* Entenda funções exclusivas do [Backend da API Memed](/docs/backend-api)
* Customize o módulo de prescrição através das funcionalidades do [Frontend](/docs/frontend)
* Consulte os [erros comuns](/docs/erros-comuns)
* Tire suas duvidas nos tópicos de [duvidas frequentes](/docs/duvidas-frequentes)
* Faça uso dos [certificados digitais](/docs/assinaturas-digitais) na plataforma
* Conclua sua integração obtendo a [Autorização para Credenciais de Produção](/docs/obter-credenciais)
