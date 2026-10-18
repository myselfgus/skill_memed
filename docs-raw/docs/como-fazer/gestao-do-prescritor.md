https://doc.memed.com.br/docs/como-fazer/gestao-do-prescritor/

# Gestão do prescritor

Para executar os comandos do paciente é necessário que o módulo da Memed seja [completamente carregado](/docs/primeiros-passos#renderizando-a-prescri%C3%A7%C3%A3o-digital),
após isso temos acesso ao MdHub para a execução de nosso comandos.

# Set Workplace

É possível resgatar o endereço do prescritor de seu sistema para preenchê-lo no receituário Memed.
Dessa forma, o prescritor não precisa escrever manualmente seu endereço nas opções de receituário.
É comum que o prescritor atenda em diferentes lugares durante sua jornada de trabalho.
Pensando nessa situação, criamos o comando Javascript setWorkplace.

Através desse comando é possível adicionar dados do prescritor como:

* Cidade do local de trabalho;
* UF do local de trabalho
* Cadastro Nacional de Estabelecimentos de Saúde
* Nome do local de trabalho
* Endereço completo com número
* Telefone do prescritor

Com isso, o prescritor não precisará preencher os seus dados quando for prescrever um medicamento controlado, pois
eles já foram preenchidos com esse comando.

Abaixo há um exemplo de como ficaria o PDF da receita com os dados do prescritor preenchidos:

![pdf-impresso](https://cdn.memed.com.br/doc/pdf-impresso.webp)

Veja um exemplo de código utilizando o comando `setWorkPlace` abaixo:

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/frontend/comandos-mdhub/set-workplace)

# setAdditionalData

Com esse comando é possível adicionar informações extras no cabeçalho e rodapé da receita digital,
como dados do paciente, do prescritor, e local do atendimento.

Aqui está um exemplo de como ficaria os dados no cabecalho e rodapé no PDF da receita.

![exemplo-dados-header-footer](https://cdn.memed.com.br/doc/exemplo-dados-header-footer.png)

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/frontend/comandos-mdhub/set-additional-data).

# Formulário de Alto Custo

CNES do estabelecimento (pode ser alterado de acordo com o local de atendimento do prescritor)

![formulario-alto-custo](https://cdn.memed.com.br/doc/formulario-alto-custo.webp)

# Trocar usuário (SPA)

Caso sua aplicação seja do tipo SPA (Single Page Application) e não faça refresh após a ação de login/logout, você pode redefinir o token do usuário logado utilizando o código abaixo

```js
MdSinapsePrescricao.setToken('TOKEN_DO_NOVO_USUARIO');
```

# Ativar tema nas opções de receituário

Agora que você já [sabe cadastrar um tema](/docs/backend/impressao#configurar-impress%C3%A3o), podemos chavear qual é o tema ativo ao iniciar a prescrição.

```js
MdHub.command.send('plataforma.sdk', 'find', {
    resource: 'opcoes-receituario/ativar/2',
    cache: false,
});
```

Com esse comando, será enviada uma requisição para nosso backend, ativando o tema 2 cadastrado nas opções de receituário.

info

É importante que valor de cache sempre seja `false` para esse comando

**Limpar o local storage do navegador web** 
A limpeza do local storage do navegador é necessária quando prescritores compartilham a mesma máquina (notebook/pc). Ela deve ser implementada OBRIGATORIAMENTE para evitar conflitos de informações entre os cadastros e consequentemente falhas de segurança.
Através do objeto `MdHub`, pode-se chamar o método abaixo para realizar a limpeza do local storage:

```js
MdHub.command.send('plataforma.sdk', 'logout');
```
