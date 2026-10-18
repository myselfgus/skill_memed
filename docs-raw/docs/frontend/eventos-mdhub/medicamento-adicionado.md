https://doc.memed.com.br/docs/frontend/eventos-mdhub/medicamento-adicionado/

# Medicamento adicionado

Quando um medicamento é adicionado dentro da plataforma ou pela api,
disparamos o evento `medicamentoAdicionado` , veja no exemplo abaixo;

```js
MdSinapsePrescricao.event.add('core:moduleInit', (moduleData) => {
  if (moduleData.name === 'plataforma.prescricao') {
    MdHub.event.add('medicamentoAdicionado', (medicine) => {});
  }
});
```

O objeto `medicamentoAdicionado` contém os atributos relacionados ao medicamento adicionado.
Abaixo iremos detalhar os seus atributos.

```js
medicine = {
  alto_custo: false,
  composicao: 'Princípio Ativo 1 + Princípio Ativo 2',
  controle_especial: false,
  descricao: 'Ácido Ascórbico',
  fabricante: 'Sundown Vitaminas',
  forma_fisica: 'Cápsula',
  id: 'a123123123',
  nome: 'Vitamina C, comprimido (100un)',
  quantidade: 1,
  tipo: 'dermocosmético',
}
```
