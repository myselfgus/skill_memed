https://doc.memed.com.br/docs/duvidas-frequentes/duvidas-back-end/

# Dúvidas Frequentes Integração back-end

## Existe alguma forma de realizar uma integração puramente com o backend da Memed sem a utilização dos módulos de FrontEnd?

Não! Para realizar a integração com a Memed, é necessário que se utilizem métodos de API via back-end e os módulos de prescrição via front-end. A Memed não possui API's de base de medicamentos no momento.

## Qual é a forma de autenticação da API da Memed?

Para utilizar os recursos da Memed via API, é necessário possuir um usuário com token válido.
Utilizamos o padrão [JWT (JSON Web Tokens)](https://jwt.io/) para os nossos tokens de usuários.

## Como saber se já efetuei o cadastro de um prescritor?

É possível ver todas as informações de um usuário (incluindo o token), através de nossa API Rest para
[consulta do prescritor](/docs/backend/usuario-prescritor#recuperar-dados-do-usu%C3%A1rio)

## Estou fazendo uma requisição e está sendo retornado um bloco de comentário, o que pode ser?

Confira na requisição enviada se está indo os cabeçalhos necessários:

`Accept: application/vnd.api+json;`

`Content-type: application/json`

## Quais são as credenciais da Memed?

Para  **parceiros**  (via software/API/Web Service), a autenticação é através das credenciais [API-KEY e SECRET-KEY](/docs/backend/configuracoes).

Para  **usuários/prescritores de parceiros**  , a autenticação é realizada através do  **TOKEN**  .

## Posso fazer REQUEST's que utilizem API-KEY e SECRET-KEY pelo front-end?

Todos os REQUEST's que necessitam de  **API-KEY e SECRET-KEY**  devem ser realizados pelo back-end.

Como temos um vínculo de compromisso com o parceiro, disponibilizamos as credenciais para ter acesso ilimitado à nossa API. Deixar as chaves visíveis no front-end é uma falha de segurança grave.

## É possível colocar imagem no cabeçalho e rodapé?

Pelas opções de receituário da Memed não é possível, mas temos um comando que permite importar o cabeçalho
e o rodapé com base em um template PDF enviado para a Memed, que pode ter imagens.

Clique [aqui](/docs/backend/impressao#importar-cabe%C3%A7alhorodap%C3%A9-de-um-pdf) para saber como fazer isso.

## É possível consultar os princípios ativos para cadastrar as alergias do paciente?

Sim, disponibilizamos um endpoint para consultar nossa base de princípios ativos.
Clique [aqui](/docs/backend/prescricao#consultar-princ%C3%ADpios-ativos) para saber como fazer isso.

## O TOKEN do usuário tem validade?

O token de usuário prescritor precisa ser consultado a cada vez que o usuário prescritor irá utilizar o módulo, para que não ocorram erros de autenticação, o token deve ser conferido antes da abertura da Memed seguindo o fluxo de implantação.

O token não é estático, portanto sempre que for fazer uma requisição na API Memed, você precisa recuperar o último token válido do usuário.

info

As bases de dados de integração e de produção são diferentes.
