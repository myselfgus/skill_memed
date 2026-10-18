https://doc.memed.com.br/docs/primeiros-passos/

# Primeiros passos

Integrar com a prescrição digital Memed é simples e rápido.
Siga o passo a passo e ao final desse módulo de primeiros passos, você já será capaz de utilizar
vários recursos da nossa prescrição digital.

Atenção

Lembre-se que todo o passo a passo dessa documentação estará apontando
para o **ambiente de homologação (testes)** da Memed. No momento em que você obtiver
as **chaves de produção (api-key e secret-key)**, você precisará reconfigurar os endpoints de
[BACKEND](/docs/backend/configuracoes#urls-de-produ%C3%A7%C3%A3o)
e [FRONTEND](/docs/frontend/configuracoes#urls-de-produ%C3%A7%C3%A3o) da sua aplicação para apontar
para o **ambiente de produção** da Memed.

## Fluxo de integração

Segue abaixo um desenho do fluxo simplifiacado da integração com a prescrição digital memed.
![fluxo](https://cdn.memed.com.br/doc/simplified-integration-flux.png)

## Configurações básica

Atenção

O nosso ambiente de **homologação** estará **indisponível** das 0h às 6h, de segunda a sexta-feira, e ao longo de **todo o fim de semana**.

### Obtendo o par de chaves (homologação)

O par de chaves utilizados no ambiente de **homologação** é fixo.

**API\_KEY**

```dotenv
iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm
```

**SECRET\_KEY**

```dotenv
Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
```

Atenção

**Nunca** deixe o seu par de chaves **visíveis** no **front-end**.

### URLs Memed (homologação)

**API URL**

Essa url abaixo é utilizada para fazer as requisições do tipo `HTTP Rest` para o back-end da api da Memed.

**MEMED\_API\_URL**

```dotenv
https://integrations.api.memed.com.br/v1
```

**Script URL**

Essa url abaixo é utilizada para baixar os scripts da Memed.

**MEMED\_SCRIPT\_URL**

```dotenv
https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js
```

Recomendamos

Recomendamos que você veja no detalhe as nossas recomendações de como configurar o seu
[**backend**](/docs/backend/configuracoes) e o seu [**frontend**](/docs/frontend/configuracoes)
para uma integração mais completa com a prescrição digital memed.

## Backend

A integração com a prescrição digital Memed é baseada na perspectiva do usuário prescritor (profissional de saúde).
Por isso, para renderizar a prescrição digital Memed dentro do seu software, você precisa efetuar o cadastro do prescritor
e obter o token de acesso dele.

### Cadastrando o prescritor via API

Para obter o Token do usuário prescritor (`data-token`), temos as seguintes opções:

* [Cadastrar um usuário prescritor novo](/docs/como-fazer/cadastrar-prescritor)
* [Obter dados do usuário prescritor](/docs/como-fazer/obter-dados-usuario)

Veja mais detalhes

Para o nosso exemplo de integração não vamos utilizar todas as **funcionalidades** disponíveis
na **api da Memed**.
Para mais detalhes de todas as **ações disponíveis entre o seu backend e a API Memed**  [clique aqui](/docs/backend-api)

## Frontend

Agora que você já tem o token do usuário (`data-token`), podemos seguir com a implementação no frontend.

### Configurando o Frontend

A primeira etapa que você precisa fazer é carregar o script de prescrição digital informando
a ***MEMED\_SCRIPT\_URL*** junto com o ***TOKEN*** de acesso
do usuário prescritor. Estes dois você já obteve via backend na requisição de [obter](/docs/como-fazer/obter-dados-usuario)
ou [cadastrar](/docs/como-fazer/cadastrar-prescritor) o prescritor.

Atenção

*MEMED\_SCRIPT\_URL* que vamos utilizar neste exemplo é a **URL** de **homologação** da Memed.

Agora um exemplo de uma pagina em HTML + javascript no seu frontend passando os seguintes atributos:

```text
src="MEMED_SCRIPT_URL"
data-token="TOKEN_DO_USUARIO_OBTIDO_NO_CADASTRO_VIA_API"
```

#### Exemplo da página completa com o script da **MEMED\_SCRIPT\_URL** junto com o **TOKEN**:

```html
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Meu sistema de Saúde</title>
  </head>
  <body>
    <script
      type="text/javascript"
      src="https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js"
      data-token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I"
    ></script>
    <!-- Proximo passo é acionar os comandos do modulo da prescrição -->
  </body>
</html>
```

Resultado:
![Integração rodando, pagina em branco](https://cdn.memed.com.br/doc/integracao_exemplo_page_0.png)

Como resultado temos a tela em branco que já está disponivel para executar comandos para acionar os comandos do modulo da prescrição.  
Outro ponto é que o console avisa em qual ambiente a integração da Memed está rodando:

```text
ENVIRONMENT integrations
we are all set!!!
```

Veja mais detalhes

Você também pode carregar o script dinâmicamente.
Para mais detalhes de todas as formas de carregar o script da Memed [clique aqui](/docs/modos-de-carregamento#carregamento-din%C3%A2mico).

### Exibindo a prescrição digital

Agora que já adicionou o script de prescrição digital Memed no seu frontend, já podemos
começar a acionar os comandos, ouvir eventos e habilitar ou desabilitar os módulos para a renderização da prescrição.

Para mostrar a prescrição digital na tela do usuário, você precisará utilizar o método `show` do módulo
`plataforma.prescricao`.
Porém, se você tentar acessar alguma propriedade do módulo antes que o mesmo esteja completamente disponível, isso
acarretará em vários erros.

Erros comuns

Caso esteja enfrentando algum problema favor verificar nossa seção de [erros comuns](/docs/erros-comuns)

Então, antes de utilizar qualquer comando do módulo de prescrição, você precisa garantir que
o módulo esteja devidamente carregado (e disponível).
Para isso, vamos utilizar o evento `core:moduleInit` que retornar em seu segundo parâmetro uma função de callback
contendo algumas informações sobre o módulo.

```js
MdSinapsePrescricao.event.add("core:moduleInit", callbackFunction);
```

Veja mais detalhes

Existem vários eventos que você pode escutar durante a interação com a prescrição da Memed.
Para mais detalhes sobre os eventos da prescrição digital da Memed [clique aqui](/docs/frontend/eventos-mdhub).

Veja um exemplo de como ficaria essa estrutura com o evento mais a verificação se o módulo de prescrição está devidamente carregado.

```js
// Evento que fica escutando o carregamento do core:moduleInit
// que contém o dentre outros o módulo de prescrição
MdSinapsePrescricao.event.add("core:moduleInit", function (module) {
  // aqui você verifica se o módulo que retornou nesse callback é o 'plataforma.prescricao'
  if (module.name === "plataforma.prescricao") {
    // aqui você aciona os comandos
    // ativa e desativa funcionalidades
    // renderiza a prescrição na tela do usuário
  }
});
```

Agora que você já entende o funcionamento básico dos módulos da prescrição digital, vamos
ver um exemplo mais completo que adiciona os dados do paciente e mostra na tela do usuário
a prescrição digital da Memed.

Fique atento!

Dados de paciente enviados via MdHub não podem ser alterados na prescrição manualmente! Veja a seção
[dados do paciente](/docs/frontend/comandos-mdhub/set-patient) para mais detalhes.

Fluxo completo de integração

Este snippet cobre apenas o comando `setPaciente`. Para a implementação de referência completa — carregamento do script, eventos LGPD e abertura do módulo — consulte [Boas Práticas de Integração](/docs/boas-praticas-integracao).

```js
// Enviar dados do paciente (await obrigatório — comando assíncrono)
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  // Campos obrigatórios
  idExterno: "parceiro-demo-pac-a1b2c3d4",
  nome: "Maria Souza",
  sexo: "Feminino",

  // Campos opcionais (obrigatórios para LME)
  cpf: "39053344705",
  data_nascimento: "15/05/1985",
  telefone: "11987654321",
  email: "paciente.exemplo@email.com",
  raca: "branca",
  peso: 75,
  altura: 1.75,
  endereco: "Rua das Flores, 100",
  cidade: "São Paulo",
  nome_mae: "Nome da mãe",
  dificuldade_locomocao: false,
});
```

Após `setPaciente`, abra o módulo com `await MdHub.module.show("plataforma.prescricao")` — preferencialmente no clique do botão, e não dentro de `core:moduleInit`.

Implementação de referência

O exemplo acima cobre apenas o comando `setPaciente`. Para o fluxo completo de integração — carregamento do script, eventos LGPD, `setWorkplace` e abertura do módulo — consulte [Boas Práticas de Integração](/docs/boas-praticas-integracao).

Veja mais detalhes

No exemplo acima, estamos utilizando apenas o **comando** de `setPaciente` para setar os dados do paciente na prescrição e a função `show` do módulo de prescrição para mostrar a tela de prescrição.
Existem vários comandos e funções relacionados aos módulos.
Para mais detalhes sobre os comandos e módulos da prescrição Memed [clique aqui](/docs/frontend/comandos-mdhub/set-patient).

### Veja como ficaria o seu frontend após implementar a prescrição Memed

Veja mais detalhes

Para o nosso exemplo simplificado acima, não utilizamos todas as funcionalidades disponíveis no frontend da Memed.
Para mais detalhes de todas as funcionalidades, voce pode consultar nosso guia de [clique aqui](/docs/frontend).

## Garantindo uma integração robusta

A Memed disponibiliza uma documentação completa sobre nossas APIs e scripts.
Temos também alguns tutoriais e exemplos de implementação em algumas linguagens.

Para garantir que todas as funcionalidades estejam implementadas, você pode conferir através da tabela abaixo as principais funcionalidades e caminhos para a implantação:

* Ao cadastrar o prescritor, estou definindo os principais dados
  + ID Externo do prescritor
  + Nome
  + Sobrenome
  + CPF
  + Registro profissional + UF
  + Especialidade
  + Cidade
* Ao informar o paciente, estou definindo os principais dados
  + Nome completo
  + ID Externo do paciente
  + CPF
  + Telefone
  + Data de nascimento
* Recupero o retorno de informações da prescrição gerada
* Setar alergias do paciente
* Setar alertas de condições
* Definir configurações de impressão
* Definir cores conforme meu sistema
* Salvo uma cópia do PDF gerado na prescrição
* Salvo o link da receita digital
* Definir locais de atendimento do profissional
* Setar Feature Toggles no atendimento
* Cadastro os meus protocolos
* Campos adicionais no documento de impressão

## O que fazer a seguir?

Com a experiencia completa, você pode ainda explorar nossas documentações para mais informações adicionais!

* Se aprofunde nas [funcionalidades da API Memed](/docs/backend-api)
* Entenda as diferentes formas de [renderizar a prescrição Memed](/docs/modos-de-carregamento)
* Saiba como funciona para [habilitar e desabilitar funcionalidades da prescrição](/docs/frontend/comandos-mdhub)
* Garanta agilidade ao prescritor e segurança de prescrição com [alertas de alergias](/docs/frontend/comandos-mdhub/set-allergy) e [condições](/docs/docs/frontend/comandos-mdhub/categories-condition)
