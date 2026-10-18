https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-abre/

# Módulo da Memed não abre

### Token do prescritor inválido

Outra questão que pode afetar o acesso à Memed é o token do prescritor.
Caso o parceiro esteja armazenando o token no banco de dados e utilizando-o para iniciar a integração com a plataforma, é possível que ocorra um erro.
Isso acontece porque o token não é fixo e pode mudar, por exemplo, caso os dados do prescritor sejam alterados.
Por isso, é importante que o parceiro [recupere o token](/docs/backend/usuario-prescritor#obtendo-o-token-do-usu%C3%A1rio-prescritor) sempre que for iniciar a integração com a Memed.

### Cookies bloqueados

Além disso, a Memed pode estar bloqueada nos cookies do navegador, o que impede o seu funcionamento.
É necessário verificar as configurações do navegador e permitir o acesso à plataforma para solucionar o problema.
Mais detalhes são dados na página [Memed não carrega](/docs/erros-comuns/modulo-memed-nao-carrega#uso-de-cookies-negado).

### Carregamento do script

Outras possíveis causas para a não abertura da Memed incluem problemas no carregamento do script da plataforma ou falhas na execução do comando de abertura do modal.
A resolução para esses problemas podem ser encontradas com mais detalhes [aqui](/docs/erros-comuns/modulo-memed-nao-carrega).
