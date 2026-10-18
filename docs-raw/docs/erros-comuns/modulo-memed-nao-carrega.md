https://doc.memed.com.br/docs/erros-comuns/modulo-memed-nao-carrega/

# O módulo da Memed não carrega

O módulo da Memed pode não ser exibido para o usuário em várias situações, incluindo o fato de o código HTML não estar hospedado em um servidor web, o comando de abertura não ser executado, o usuário estar bloqueado ou ter bloqueado os cookies para o site da Memed.

### Carregamento do HTML contendo o script da Memed

Se a mensagem `Failed to load resource: net::ERR_INVALID_URL` aparecer no console do navegador, o HTML contendo o script da Memed está tentando ser inicializado em um ambiente sem servidor, o que impede o carregamento dos módulos de prescrição.
Para solucionar isso, é necessário criar um servidor e hospedar o código HTML.

Imagem do erro abaixo:

![modulo-nao-aparece](https://cdn.memed.com.br/doc/modulo-nao-aparece.png)

### Mensagem de autofocusing

Se apenas uma mensagem de bloqueio de `autofocusing` for exibida, isso indica que os módulos da Memed foram carregados, mas o comando de abertura ainda não foi executado.
Para resolver essa situação, o parceiro pode executar o comando `MdHub.module.show('plataforma.prescricao')` diretamente no console do navegador para exibir o modal da Memed.

![modulo-nao-aparece](https://cdn.memed.com.br/doc/autofocusing.png)

### Token inválido

Se o console exibir vários erros 401 de requisições GET, isso indica que o usuário que está acessando a
Memed está com um token inválido.
O parceiro pode obter mais informações lendo esse artigo [aqui](/docs/erros-comuns/cadastro-medico-nao-consigo-utilizar).

Veja um exemplo desse erro abaixo:

![erros-401-get](https://cdn.memed.com.br/doc/erros-401-get.png)

### Uso de cookies negado

Se várias mensagens `Failed to read the ‘localStorage’ property from ‘Window’` aparecerem, isso pode ser devido ao bloqueio de uma URL para o uso de cookies nos navegadores modernos, o que resulta no bloqueio de todas as outras formas de armazenamento que a Memed utiliza, como Local Storage e Session Storage.
Para solucionar esse problema, o parceiro deve seguir os passos para remover os cookies:

### Passo 1

Clicar no cadeado ao lado da url e selecionar a opção “Cookies”.

![erros-401-get](https://cdn.memed.com.br/doc/cookie-1.png)

### Passo 2

Clicar na aba “Bloqueado”, selecionar as urls da Memed, clicar no botão “Permitir” e depois em “Concluído”.

![erros-401-get](https://cdn.memed.com.br/doc/cookie-2.png)

### Passo 3

Após realizar as etapas anteriores, recarregue da página e verifique se o módulo da Memed está sendo carregado corretamente.
