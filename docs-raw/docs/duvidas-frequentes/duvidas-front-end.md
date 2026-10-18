https://doc.memed.com.br/docs/duvidas-frequentes/duvidas-front-end/

# Integração - Front-End

## Como obtenho os dados da receita gerada?

Emitimos eventos em determinadas ações da nossa plataforma, e o software do parceiro pode
ficar escutando quando for emitido.

Quando uma prescrição é gerada, emitimos o evento `prescricaoImpressa`.
Esse evento retorna o ID da prescrição gerada.
Clique [aqui](/docs/frontend/eventos-mdhub/prescricao-impressa) e veja um exemplo de implementação para escutar o evento.

## Como eu sei que o módulo da prescrição está pronto?

Você pode assinar eventos que são disparados pelos módulos e implementá-los conforme necessidade em sua plataforma.

Os módulos da Memed emitem eventos quando inicializados e podem ser capturados.
Clique [aqui](/docs/frontend/eventos-mdhub/modulo-terminou-carregar) para ver como fazer isso.

## Quais opções da Memed consigo desabilitar?

É possível customizar algumas funcionalidades e características da receita médica.

Para isso, você pode usar o comando setFeatureToggle após inicializar o Sinapse Prescrição.
Clique [aqui](/docs/frontend/comandos-mdhub/set-feature-toggle) e saiba todas as
opções disponíveis.

## Como posso iniciar uma nova prescrição mantendo o mesmo paciente?

Para manter os dados do paciente após clicar no botão "Nova Prescrição", precisa utilizar o comando
`setFeatureToggle`, passando a opção `removePatient` como `false`.

Clique [aqui](/docs/frontend/comandos-mdhub/set-feature-toggle#removepatient) e veja como fazer isso.
