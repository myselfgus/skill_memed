# Dúvidas frequentes

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- Base de medicamentos e exames de homologação e de produção — `https://doc.memed.com.br/docs/duvidas-frequentes/base-medicamentos`
- Copiar e colar textos de outras fontes — `https://doc.memed.com.br/docs/duvidas-frequentes/copiar-colar-textos`
- Dúvidas Frequentes Integração back-end — `https://doc.memed.com.br/docs/duvidas-frequentes/duvidas-back-end`
- Integração - Front-End — `https://doc.memed.com.br/docs/duvidas-frequentes/duvidas-front-end`
- Quais navegadores de internet são suportados pela Memed? — `https://doc.memed.com.br/docs/duvidas-frequentes/navegadores-suportados`
- Como obtenho as chaves (API-KEY e SECRET-KEY) de produção? — `https://doc.memed.com.br/docs/duvidas-frequentes/obter-chaves-api-secret`
- Outras Dúvidas — `https://doc.memed.com.br/docs/duvidas-frequentes/outras-duvidas`
- A Memed possibilita realizar prescrição por API ? — `https://doc.memed.com.br/docs/duvidas-frequentes/prescricao-por-api`
- Profissional pode ter mais de uma especialidade na plataforma da Memed ? — `https://doc.memed.com.br/docs/duvidas-frequentes/profissionais-especialidades`
- Quais são os provedores de assinatura integrados com a Memed? — `https://doc.memed.com.br/docs/duvidas-frequentes/provedores-assinaturas`
- Retirar o horário da data — `https://doc.memed.com.br/docs/duvidas-frequentes/retirar-hora-data`
- Sincronizar usuários — `https://doc.memed.com.br/docs/duvidas-frequentes/sincronizar-usuarios`

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/base-medicamentos -->
## Base de medicamentos e exames de homologação e de produção

A Memed possue milhares de medicamentos e exames cadastrados em sua base de dados no ambiente de produção `https://partners.memed.com.br/integration.js`

Porém, no ambiente de homologação `https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js` , a nossa base de medicamentos e exames não está completa, disponibilizamos apenas uma pequena amostra.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/copiar-colar-textos -->
## Copiar e colar textos de outras fontes

A Memed não recomenda o usuário prescritor copiar textos de outros documento e colar dentro da plataforma de prescrição.

Se no documento que usuário prescritor está copiando conter uma fonte não utilizada pelo sistema Memed, irá acontecer alguns problemas, conforme exemplo abaixo:

![copia-cola-fonte](https://cdn.memed.com.br/doc/copia-cola-fonte.png)

Caso o usuário queria utilizar algum texto de outro documento dentro da plataforma, aconselhamos o usuário copiar os textos do documento, colar os textos em um editor de textos do tipo "bloco de notas", depois copiar esse texto do bloco notas e realizar o procedimento de colar o dentro da plataforma.

Assim o texto estará sem nenhuma formatação e não ocorrerá nenhum problema.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/duvidas-back-end -->
## Dúvidas Frequentes Integração back-end

### Existe alguma forma de realizar uma integração puramente com o backend da Memed sem a utilização dos módulos de FrontEnd?

Não! Para realizar a integração com a Memed, é necessário que se utilizem métodos de API via back-end e os módulos de prescrição via front-end. A Memed não possui API's de base de medicamentos no momento.

### Qual é a forma de autenticação da API da Memed?

Para utilizar os recursos da Memed via API, é necessário possuir um usuário com token válido. Utilizamos o padrão [JWT (JSON Web Tokens)](https://jwt.io/) para os nossos tokens de usuários.

### Como saber se já efetuei o cadastro de um prescritor?

É possível ver todas as informações de um usuário (incluindo o token), através de nossa API Rest para [consulta do prescritor](https://doc.memed.com.br/docs/backend/usuario-prescritor#recuperar-dados-do-usu%C3%A1rio)

### Estou fazendo uma requisição e está sendo retornado um bloco de comentário, o que pode ser?

Confira na requisição enviada se está indo os cabeçalhos necessários:

`Accept: application/vnd.api+json;`

`Content-type: application/json`

### Quais são as credenciais da Memed?

Para **parceiros** (via software/API/Web Service), a autenticação é através das credenciais [API-KEY e SECRET-KEY](https://doc.memed.com.br/docs/backend/configuracoes).

Para **usuários/prescritores de parceiros** , a autenticação é realizada através do **TOKEN** .

### Posso fazer REQUEST's que utilizem API-KEY e SECRET-KEY pelo front-end?

Todos os REQUEST's que necessitam de **API-KEY e SECRET-KEY** devem ser realizados pelo back-end.

Como temos um vínculo de compromisso com o parceiro, disponibilizamos as credenciais para ter acesso ilimitado à nossa API. Deixar as chaves visíveis no front-end é uma falha de segurança grave.

### É possível colocar imagem no cabeçalho e rodapé?

Pelas opções de receituário da Memed não é possível, mas temos um comando que permite importar o cabeçalho e o rodapé com base em um template PDF enviado para a Memed, que pode ter imagens.

Clique [aqui](https://doc.memed.com.br/docs/backend/impressao#importar-cabe%C3%A7alhorodap%C3%A9-de-um-pdf) para saber como fazer isso.

### É possível consultar os princípios ativos para cadastrar as alergias do paciente?

Sim, disponibilizamos um endpoint para consultar nossa base de princípios ativos. Clique [aqui](https://doc.memed.com.br/docs/backend/prescricao#consultar-princ%C3%ADpios-ativos) para saber como fazer isso.

### O TOKEN do usuário tem validade?

O token de usuário prescritor precisa ser consultado a cada vez que o usuário prescritor irá utilizar o módulo, para que não ocorram erros de autenticação, o token deve ser conferido antes da abertura da Memed seguindo o fluxo de implantação.

O token não é estático, portanto sempre que for fazer uma requisição na API Memed, você precisa recuperar o último token válido do usuário.

**info**

As bases de dados de integração e de produção são diferentes.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/duvidas-front-end -->
## Integração - Front-End

### Como obtenho os dados da receita gerada?

Emitimos eventos em determinadas ações da nossa plataforma, e o software do parceiro pode ficar escutando quando for emitido.

Quando uma prescrição é gerada, emitimos o evento `prescricaoImpressa`. Esse evento retorna o ID da prescrição gerada. Clique [aqui](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa) e veja um exemplo de implementação para escutar o evento.

### Como eu sei que o módulo da prescrição está pronto?

Você pode assinar eventos que são disparados pelos módulos e implementá-los conforme necessidade em sua plataforma.

Os módulos da Memed emitem eventos quando inicializados e podem ser capturados. Clique [aqui](https://doc.memed.com.br/docs/frontend/eventos-mdhub/modulo-terminou-carregar) para ver como fazer isso.

### Quais opções da Memed consigo desabilitar?

É possível customizar algumas funcionalidades e características da receita médica.

Para isso, você pode usar o comando setFeatureToggle após inicializar o Sinapse Prescrição. Clique [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle) e saiba todas as opções disponíveis.

### Como posso iniciar uma nova prescrição mantendo o mesmo paciente?

Para manter os dados do paciente após clicar no botão "Nova Prescrição", precisa utilizar o comando `setFeatureToggle`, passando a opção `removePatient` como `false`.

Clique [aqui](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle#removepatient) e veja como fazer isso.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/navegadores-suportados -->
## Quais navegadores de internet são suportados pela Memed?

Nossa plataforma possui diversas funcionalidades construídas com tecnologia moderna, visando uma melhor experiência do usuário.

Recomendamos sempre o uso de navegadores modernos e atualizados para um bom aproveitamento da nossa prescrição digital. Navegadores desatualizados como IE (Internet Explorer) podem apresentar incompatibilidades com nosso software. Portanto, não damos suporte a esse tipo de navegador.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/obter-chaves-api-secret -->
## Como obtenho as chaves (API-KEY e SECRET-KEY) de produção?

Neste [formulário](https://forms.gle/Z3M6TGhf2GMVmzH56), procederemos ao registro das informações necessárias para que sua empresa se torne nossa parceira, assegurando o cumprimento das boas práticas descritas em nossa documentação e o seguimento dos passos essenciais para uma integração bem-sucedida.

Uma vez concluída a Validação Técnica, o responsável pela integração enviará via e-mail as credenciais **API-KEY e SECRET-KEY** .

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/outras-duvidas -->
## Outras Dúvidas

#### Quero automatizar as configurações de cabeçalho e rodapé com o logo do plano de saúde do paciente para cada atendimento. Como faço?

Basta consultar a seção [**Impressão**](https://doc.memed.com.br/docs/backend/impressao). Através dessas opções de impressão é possível definir uma rotina de atualização para o prescritor.

#### Já atualizei os dados de cadastro do prescritor, mas o endereço ou telefone continua saindo errado no receituário especial.

Os dados no receituário especial são definidos através do [**setWorkplace**](https://doc.memed.com.br/docs/como-fazer/gestao-do-prescritor#setworkplace).

#### Quais são as estilizações disponíveis na Memed?

As personalizações disponíveis podem ser consultadas na seção [Estilização da prescrição](https://doc.memed.com.br/docs/frontend/estilizar-front).

#### O status do prescritor está em análise e não consigo deixar como ativo. Como faço?

O status retornado nas consultas e cadastro de prescritores são apenas utilizados em outros sistemas da Memed. O status "Em análise" não impede o prescritor de utilizar a Memed.

#### Como faço para desabilitar o nome do laboratório nas prescrições do prescritor?

O parametro responsável pelo nome do laboratório é o `mostrar_nome_fabricante` nas opções de [**receituário**](https://doc.memed.com.br/docs/backend/impressao), ele deve ser setado como `false`.

#### Não vejo necessidade de manter o mini histórico da Memed, pois já tenho uma cópia no meu prontuário. Qual o impacto de desabilitar?

Não haverá impacto algum. O mini histórico da Memed é util para uma reemissão na abertura do módulo, porém, caso deseje desabilita-lo, é possível realizar através das opções de Ativar ou desativar [**funcionalidades**](https://doc.memed.com.br/docs/frontend/comandos-mdhub).

#### Quero mandar a especialidade médica estruturada, mas não encontrei as mesmas especialidades que tenho na minha base (subespecialidades). O que posso fazer?

Sabemos que os profissionais da saúde podem ser de diferentes especialidades.

Contudo, no momento, é possível cadastrar apenas uma especialidade por prescritor e parceiro na Memed. A lista de especialidades é curada por um time de inteligencias clinicas e atualizada regularmente, caso a sua especialidade principal não esteja listada, você pode entrar em contato com o nosso suporte para solicitação, e iremos avaliar a inclusão da especialidade conforme os conselhos de prescritores.

#### Como consigo subir modelos favoritos de receita para os prescritores de maneira massiva com texto livre?

Para protocolos de prescritores, consulte a seção [**Protocolos**](https://doc.memed.com.br/docs/backend/protocolos).

#### Seria possível criar um login teste no Memed Standalone para que eu (parceiro) possa fazer demonstrações comerciais com meus clientes? Se não, como posso permitir que colaboradores consigam acessar a Memed?

Não, para uso de demonstrações para clientes, sugerimos que utilizem o ambiente de homologação. Para isso, é necessário uma minima integração com o ambiente.

#### O que devo fazer quando a API retorna que há um cadastro duplicado?

As chaves de API de homologação são de uso compartilhado, portanto, um dado utilizado no cadastro pode ter sido utilizado antes e acusar duplicidade. Nesse caso, sugerimos que utilize outros dados para seu teste.

Caso a duplicidade aconteça em ambiente de produção, sugerimos que recupera o cadastro duplicado e utilize o mesmo afim de evitar novas tentativas de cadastro duplicado.

#### Como saber se a receita foi assinada ou não?

Para usuários prescritores, essa informação ficará disponível na receita emitida, no seu rodapé, indicando que a receita possui assinatura e informações para validação da mesma.

Para pacientes, a prescrição digital também recebe essa informação.

Para fins de desenvolvimento, no evento da prescrição [**prescricaoImpressa**](https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa) será devolvido o objeto `signed` com valor `true` ou `false` indicando o status da assinatura no documento.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/prescricao-por-api -->
## A Memed possibilita realizar prescrição por API ?

Não há possibilidade de realizar/criar prescrições via api. Somente via plataforma de prescrição. Pode-se, no entanto, [consultar](https://doc.memed.com.br/docs/backend/prescricao#recuperar-o-link-da-receita-digital) ou [deletar](https://doc.memed.com.br/docs/backend/prescricao#remover-uma-prescri%C3%A7%C3%A3o) prescrição via api.

A Memed disponibiliza comandos via MdHub para [preencher os medicamentos](https://doc.memed.com.br/docs/frontend/comandos-mdhub/add-item) que irão compor a receita digital, e para preencher os [dados do paciente](https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient) na receita digital. Com isso o processo de elaboração da receita digital é agilizado.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/profissionais-especialidades -->
## Profissional pode ter mais de uma especialidade na plataforma da Memed ?

Sabemos que os profissionais da saúde podem ser de diferentes especialidades.

Contudo, no momento, é possível cadastrar apenas uma especialidade por prescritor de um parceiro específico na Memed. A especialidade é usada para refinar os resultados das buscas dentro da plataforma Memed. Caso o parceiro não tenha essa informação, recomendamos que deixem como Generalista para que o prescritor possa atualizar o seu cadastro posteriormente dentro da plataforma Memed.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/provedores-assinaturas -->
## Quais são os provedores de assinatura integrados com a Memed?

Atualmente a Memed possui integração com 6 provedores de assinatura. São eles: **Lacuna** (WebPKI), **Soluti** (BirdID), **E-val** , **RemoteId** , **Dinamo** , **VIDaaS** e **SafeID** .

**Lacuna** (WebPKI), **Soluti** (BirdID), **VIDaaS** e **SafeID** aparecem automaticamente para que o prescritor consiga autenticar sua assinatura.

![provedores](https://cdn.memed.com.br/doc/provedores.png)

Além disso, caso você possua os serviços da **E-val** , **Dinamo** ou **RemoteId** , é possível configurar para que a Memed também exiba essas opções de autenticação. Para isso, é preciso apenas informar pelo nosso chat da Memed qual o endereço do host do servidor interno (nos casos da **E-val** e **Dinamo** ), para que habilitemos esses provedores.

Após essa configuração, a opção irá aparecer para os seus prescritores (conforme imagem abaixo).

![todos-provedores](https://cdn.memed.com.br/doc/todos-provedores.png)

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/retirar-hora-data -->
## Retirar o horário da data

Em uma prescrição comum, a data e o horário da elaboracão da receita digital é impressa no PDF da receita.

Em alguns casos, o usuário prescritor pode não desejar que o horário da data apareça no PDF da receita.

Se a data da receita for a mesma do dia corrente, não é possível retirar a hora da data.

Porém se a data da receita for maior que a do dia corrente, o horário na data não irá aparecer.

Em outro caso, o usuário prescritor pode desabilitar a impressão da data e da hora no PDF da receita.

---

<!-- fonte: https://doc.memed.com.br/docs/duvidas-frequentes/sincronizar-usuarios -->
## Sincronizar usuários

Saiba o momento em que o prescritor pode sincronizar os perfis, com o usuário gerado pelo site ou app da Memed.

Assim que a plataforma da Memed for aberta no software do parceiro, será mostrada uma opção no cabeçalho para **entrar** (fazer login com um usuário existente na Memed) ou **criar uma nova conta** .

![sinc-usuarios](https://cdn.memed.com.br/doc/sinc-usuarios.png)

A partir desse momento, os perfis serão sincronizados, tendo acesso a conteúdos como os protocolos salvos e posologias memorizadas.
