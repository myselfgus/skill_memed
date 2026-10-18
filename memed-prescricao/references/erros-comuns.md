# Erros comuns e soluções

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- Blocked a frame with origin — `https://doc.memed.com.br/docs/erros-comuns/blocked-frame-with-origin`
- Fiz um cadastro de um prescritor para testar integração e não consigo mais utilizá-lo — `https://doc.memed.com.br/docs/erros-comuns/cadastro-medico-nao-consigo-utilizar`
- Fonte muito grande na receita digital — `https://doc.memed.com.br/docs/erros-comuns/fonte-muito-grande`
- Modulo da Memed é carregado várias vezes — `https://doc.memed.com.br/docs/erros-comuns/modulo-memed-carrega-varias-vezes`
- Módulo da Memed não abre — `https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-abre`
- O módulo da Memed não carrega — `https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-carrega`
- Não consigo cadastrar o usuário — `https://doc.memed.com.br/docs/erros-comuns/nao-consigo-cadastrar-usuario`
- Ocorreu um erro na autenticação — `https://doc.memed.com.br/docs/erros-comuns/ocorreu-erro-autenticacao`

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/blocked-frame-with-origin -->
## Blocked a frame with origin

Se você está recebendo o erro `Uncaught DOMException: Blocked a frame with origin` ao carregar a sua página, pode ser necessário ajustar o cabeçalho `Referrer-Policy` da página que está carregando o módulo da Memed para o valor `strict-origin-when-cross-origin`.

Veja abaixo uma imagem desse erro:

![blocked-frame-with-origin.png](https://cdn.memed.com.br/doc/blocked-frame-with-origin.png)

#### Como esse erro ocorre

Esse erro ocorre quando há uma tentativa de carregar recursos de uma página web com uma origem diferente da página principal que está sendo carregada. Esse tipo de comportamento é conhecido como `cross-origin framing` e é uma medida de segurança implementada pelos navegadores para prevenir que sites maliciosos carreguem conteúdo de outras páginas da web sem o consentimento do usuário.

Se o cabeçalho `Referrer-Policy` da sua aplicação estiver configurado como `same-origin`, o carregamento da Memed pode ser bloqueado. Isso ocorre porque a Memed realiza uma verificação de domínio internamente através de um dos módulos que é carregado via iframe, e a presença do cabeçalho `same-origin` pode impedir que essa verificação seja realizada corretamente.

Para obter mais informações sobre o cabeçalho Referrer-Policy, consulte a documentação disponível em [Referrer-Policy](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Referrer-Policy).

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/cadastro-medico-nao-consigo-utilizar -->
## Fiz um cadastro de um prescritor para testar integração e não consigo mais utilizá-lo

É comum que parceiros da Memed relatem dificuldades no acesso à plataforma devido a erros nas requisições. Uma situação recorrente é a apresentação de erro 401 nas requisições após criação de um cadastro de prescritor em Integrations e a utilização do mesmo para testes de integração.

A fim de solucionar essa questão, é necessário verificar alguns pontos importantes:

1.  O token de autenticação do prescritor pode ser modificado caso os dados do usuário sejam alterados via API ou através do uso da plataforma Memed pelo próprio usuário. Sendo assim, é recomendado que o parceiro sempre [recupere o token](https://doc.memed.com.br/docs/backend/usuario-prescritor#obtendo-os-dados-do-usu%C3%A1rio-prescritor) do prescritor antes de iniciar a integração com a Memed;

2.  Caso o usuário esteja inativo, basta [atualizar as informações do prescritor via API](https://doc.memed.com.br/docs/backend/usuario-prescritor#atualizando-os-dados-do-usu%C3%A1rio-prescritor) com dados válidos para que o usuário se torne ativo novamente.

3.  Todos os parceiros utilizam o mesmo ambiente para testar suas integrações e alguns podem utilizar dados reais. Por questões de segurança e para manter uma boa performance do ambiente, nós limpamos o banco de Integrations periodicamente. Sendo assim, é possível que o usuário criado anteriormente não exista mais em nosso banco de dados e seja preciso realizar um [novo cadastro](https://doc.memed.com.br/docs/backend/usuario-prescritor#cadastrando-o-prescritor).

Segue imagem ilustrativa da mensagem de erro 401:

![Mensagem de erro 401](https://cdn.memed.com.br/doc/nao-consegue-utilizar-mais-o-medico.png)

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/fonte-muito-grande -->
## Fonte muito grande na receita digital

Se a fonte utilizada na receita digital estiver muito grande, é possível que a data e hora presentes no documento se sobrepõem aos demais dados da receita. Para solucionar esse problema, há três possibilidades:

1.  Reduzir o tamanho da fonte utilizada.
2.  Remover a data e hora da receita.
3.  Emitir uma nova prescrição com data futura, de forma que a hora não seja exibida na receita.

Para ilustrar esse erro, segue um exemplo na imagem abaixo:

![fonte-grande](https://cdn.memed.com.br/doc/fonte-grande.png)

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/modulo-memed-carrega-varias-vezes -->
## Modulo da Memed é carregado várias vezes

Há casos em que o usuário prescritor clica em um botão para abrir a prescrição da Memed, com isso, o script é carregado a cada vez que o usuário clica nesse botão. Este fato pode gerar um problema na comunicação da integração, pois haverá duplicação dos iframes.

**Recomendação de ajuste:** Quando o usuário prescritor clicar no botão para abrir a prescrição da Memed, deixar este botão bloqueado até a [identificação do carregamento completo do script](https://doc.memed.com.br/docs/frontend/eventos-mdhub/modulo-terminou-carregar).

Após o módulo ter sido completamente carregado, habilitar o botão novamente. Caso o usuário clique no botão de abrir o módulo da prescriçao da Memed novamente, executar apenas o comando de abertura do módulo `MdHub.module.show('plataforma.prescricao');`.

Isso fará com que não tenha um delay na abertura da Memed e também removerá a possibilidade de erro de comunicação entre os iframes.

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-abre -->
## Módulo da Memed não abre

#### Token do prescritor inválido

Outra questão que pode afetar o acesso à Memed é o token do prescritor. Caso o parceiro esteja armazenando o token no banco de dados e utilizando-o para iniciar a integração com a plataforma, é possível que ocorra um erro. Isso acontece porque o token não é fixo e pode mudar, por exemplo, caso os dados do prescritor sejam alterados. Por isso, é importante que o parceiro [recupere o token](https://doc.memed.com.br/docs/backend/usuario-prescritor#obtendo-o-token-do-usu%C3%A1rio-prescritor) sempre que for iniciar a integração com a Memed.

#### Cookies bloqueados

Além disso, a Memed pode estar bloqueada nos cookies do navegador, o que impede o seu funcionamento. É necessário verificar as configurações do navegador e permitir o acesso à plataforma para solucionar o problema. Mais detalhes são dados na página [Memed não carrega](https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-carrega#uso-de-cookies-negado).

#### Carregamento do script

Outras possíveis causas para a não abertura da Memed incluem problemas no carregamento do script da plataforma ou falhas na execução do comando de abertura do modal. A resolução para esses problemas podem ser encontradas com mais detalhes [aqui](https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-carrega).

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-carrega -->
## O módulo da Memed não carrega

O módulo da Memed pode não ser exibido para o usuário em várias situações, incluindo o fato de o código HTML não estar hospedado em um servidor web, o comando de abertura não ser executado, o usuário estar bloqueado ou ter bloqueado os cookies para o site da Memed.

#### Carregamento do HTML contendo o script da Memed

Se a mensagem `Failed to load resource: net::ERR_INVALID_URL` aparecer no console do navegador, o HTML contendo o script da Memed está tentando ser inicializado em um ambiente sem servidor, o que impede o carregamento dos módulos de prescrição. Para solucionar isso, é necessário criar um servidor e hospedar o código HTML.

Imagem do erro abaixo:

![modulo-nao-aparece](https://cdn.memed.com.br/doc/modulo-nao-aparece.png)

#### Mensagem de autofocusing

Se apenas uma mensagem de bloqueio de `autofocusing` for exibida, isso indica que os módulos da Memed foram carregados, mas o comando de abertura ainda não foi executado. Para resolver essa situação, o parceiro pode executar o comando `MdHub.module.show('plataforma.prescricao')` diretamente no console do navegador para exibir o modal da Memed.

![modulo-nao-aparece](https://cdn.memed.com.br/doc/autofocusing.png)

#### Token inválido

Se o console exibir vários erros 401 de requisições GET, isso indica que o usuário que está acessando a Memed está com um token inválido. O parceiro pode obter mais informações lendo esse artigo [aqui](https://doc.memed.com.br/docs/erros-comuns/cadastro-medico-nao-consigo-utilizar).

Veja um exemplo desse erro abaixo:

![erros-401-get](https://cdn.memed.com.br/doc/erros-401-get.png)

#### Uso de cookies negado

Se várias mensagens `Failed to read the ‘localStorage’ property from ‘Window’` aparecerem, isso pode ser devido ao bloqueio de uma URL para o uso de cookies nos navegadores modernos, o que resulta no bloqueio de todas as outras formas de armazenamento que a Memed utiliza, como Local Storage e Session Storage. Para solucionar esse problema, o parceiro deve seguir os passos para remover os cookies:

#### Passo 1

Clicar no cadeado ao lado da url e selecionar a opção “Cookies”.

![erros-401-get](https://cdn.memed.com.br/doc/cookie-1.png)

#### Passo 2

Clicar na aba “Bloqueado”, selecionar as urls da Memed, clicar no botão “Permitir” e depois em “Concluído”.

![erros-401-get](https://cdn.memed.com.br/doc/cookie-2.png)

#### Passo 3

Após realizar as etapas anteriores, recarregue da página e verifique se o módulo da Memed está sendo carregado corretamente.

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/nao-consigo-cadastrar-usuario -->
## Não consigo cadastrar o usuário

As solicitações da Memed retornam uma mensagem de erro que explica qual foi o problema encontrado. Para identificar o erro, o primeiro passo é recuperar a mensagem de erro.

### Situação 1:

```
{
  "errors": [
    {
      "title": "Erro",
      "detail": "O objeto enviado não contém a propriedade \"data\"."
    }
  ]
}
```

Se o código acima for retornado, significa que a aplicação da Memed não conseguiu receber uma estrutura JSON no corpo da solicitação. Isso pode ter duas possíveis causas:

- O cabeçalho Content-Type: application/json não foi adicionado à solicitação;
- Há um erro de sintaxe no JSON do corpo;
  - Uma vírgula está faltando;
  - Há comentários dentro do JSON;

### Situação 2:

A Memed valida alguns campos enviados na criação de usuários. Portanto, é possível que alguns dados enviados não sejam válidos, o que resulta em uma solicitação mal-sucedida.

```
{
  "errors": [
    {
      "code": "CPF",
      "title": "Erro de validação",
      "detail": "CPF precisa ser um CPF válido"
    }
  ]
}
```

---

<!-- fonte: https://doc.memed.com.br/docs/erros-comuns/ocorreu-erro-autenticacao -->
## Ocorreu um erro na autenticação

Um erro de autenticação pode ocorrer por conta de fatores ligados ao token do usuário prescritor, como status do cadastro.

![ops-ocorreu-erro-autenticacao](https://cdn.memed.com.br/doc/ops-ocorreu-erro-autenticacao.png)  
  

Se você estiver enfrentando problemas ao acessar os módulos da plataforma Memed e encontrar a imagem de erro de autenticação, indicando que o seu usuário prescritor está inativo, significa que o mesmo passou por algum problema e precisou ser invalidado. Caso isso ocorra, as seguintes ações são recomendadas:

1.  Confira o token do acesso do prescritor e se o mesmo está atualizado com os dados da sua base.
2.  Caso haja uma atualização de dados, um novo token para o usuário prescritor é gerado e ele será usado para as próximas utilizações.
3.  Caso o token esteja correto quando consultado via método de usuários e o status esteja inativo, entre em contato com o suporte Memed.
