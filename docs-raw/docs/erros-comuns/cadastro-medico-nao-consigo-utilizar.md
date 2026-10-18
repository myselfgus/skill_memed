https://doc.memed.com.br/docs/erros-comuns/cadastro-medico-nao-consigo-utilizar/

# Fiz um cadastro de um prescritor para testar integração e não consigo mais utilizá-lo

É comum que parceiros da Memed relatem dificuldades no acesso à plataforma devido a erros nas requisições.
Uma situação recorrente é a apresentação de erro 401 nas requisições após criação de um cadastro de prescritor em Integrations
e a utilização do mesmo para testes de integração.

A fim de solucionar essa questão, é necessário verificar alguns pontos importantes:

1. O token de autenticação do prescritor pode ser modificado caso os dados do usuário sejam alterados via API ou através
   do uso da plataforma Memed pelo próprio usuário. Sendo assim, é recomendado que o parceiro sempre [recupere o token](/docs/backend/usuario-prescritor#obtendo-os-dados-do-usu%C3%A1rio-prescritor)
   do prescritor antes de iniciar a integração com a Memed;
2. Caso o usuário esteja inativo, basta [atualizar as informações do prescritor via API](/docs/backend/usuario-prescritor#atualizando-os-dados-do-usu%C3%A1rio-prescritor) com dados válidos para que o usuário se
   torne ativo novamente.
3. Todos os parceiros utilizam o mesmo ambiente para testar suas integrações e alguns podem utilizar dados reais.
   Por questões de segurança e para manter uma boa performance do ambiente, nós limpamos o banco de Integrations periodicamente.
   Sendo assim, é possível que o usuário criado anteriormente não exista mais em nosso banco de dados e seja preciso realizar um [novo cadastro](/docs/backend/usuario-prescritor#cadastrando-o-prescritor).

Segue imagem ilustrativa da mensagem de erro 401:

![Mensagem de erro 401](https://cdn.memed.com.br/doc/nao-consegue-utilizar-mais-o-medico.png)
