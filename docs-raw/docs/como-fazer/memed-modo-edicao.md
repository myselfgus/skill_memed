https://doc.memed.com.br/docs/como-fazer/memed-modo-edicao/

# Abrir modulo da Memed em modo de edição

Abrir o modo de edição de prescrição é muito simples, você precisará chamar o comando responsável por exibir o preview através do `MdHub` e passar as seguintes informações:

* Nome do modulo `plataforma.prescricao`
* Nome do comando `viewPrescription`
* Id da prescrição

Quando o comando `viewPrescription` é executado, uma prévia da prescrição selecionada é exibida, conforme
exemplo abaixo, e as ações que podem ser executadas são a reemissão ou criação de uma cópia da prescrição.

![tela-impressao.png](https://cdn.memed.com.br/doc/tela-impressao.png)

## Como executar o comando

Abaixo temos um exemplo de como pode ser feita a chamada do comando `viewPrescription`.
Recuperando o botão com o id `btnViewPrescription`, escutamos o evento de `click` e passamos a chamada para o modulo de prescrição enviando o comando de visualização da prescrição através do `MdHub`.

A resposta desse comando é assincrona e retorna `true` quando o preview é aberto.
Caso seja passado um `id` inexistente na nossa base, o preview ainda irá abrir, mas exibirá a mensagem de id não encontrado.

Segue o exemplo da execução do comando.

```js
document
  .getElementById("btnViewPrescription")
  .addEventListener("click", function() {
    MdHub.command.send(
      'plataforma.prescricao',
      'viewPrescription',
      ID_DA_PRESCRICAO
    );
});
```
