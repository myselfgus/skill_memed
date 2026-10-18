https://doc.memed.com.br/docs/erros-comuns/modulo-memed-carrega-varias-vezes/

# Modulo da Memed é carregado várias vezes

Há casos em que o usuário prescritor clica em um botão para abrir a prescrição da Memed, com isso, o script
é carregado a cada vez que o usuário clica nesse botão. Este fato pode gerar um problema na
comunicação da integração, pois haverá duplicação dos iframes.

**Recomendação de ajuste:** Quando o usuário prescritor clicar no botão para abrir a prescrição da Memed,
deixar este botão bloqueado até a
[identificação do carregamento completo do script](/docs/frontend/eventos-mdhub/modulo-terminou-carregar).

Após o módulo ter sido completamente carregado, habilitar o botão novamente.
Caso o usuário clique no botão de abrir o módulo da
prescriçao da Memed novamente, executar apenas o comando de abertura do módulo
`MdHub.module.show('plataforma.prescricao');`.

Isso fará com que não tenha um delay na abertura da Memed
e também removerá a possibilidade de erro de comunicação entre os iframes.
