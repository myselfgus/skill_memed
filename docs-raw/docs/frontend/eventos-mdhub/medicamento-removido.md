https://doc.memed.com.br/docs/frontend/eventos-mdhub/medicamento-removido/

# Medicamento removido

Quando o medicamento é removido da receita pelo usuário prescritor,
disparamos o evento `medicamentoRemovido` , veja no exemplo abaixo;

```js
MdSinapsePrescricao.event.add('core:moduleInit', function moduleInitHandler(module) {

     MdHub.event.add('medicamentoRemovido', function callback(idDoMedicamento) {
          console.log(idDoMedicamento);
     });
});
```

O parametro `idDoMedicamento` da função `callback` contém o id do medicamento excluído.
