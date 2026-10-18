https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-excluida/

# Prescrição excluída

Quando uma prescrição é excluída, enviamos o evento `prescricaoExcluida`.
Esse evento retorna os dados da prescrição excluída.

Veja um exemplo de implementação para escutar o evento:

```js
MdSinapsePrescricao.event.add('core:moduleInit', (memedModule) => {
  if (memedModule.name === 'plataforma.prescricao') {
    /**
     * @param {number} prescriptionId Id da prescrição excluída
     */
    MdHub.event.add('prescricaoExcluida', (prescriptionId) => {
    });
  }
});
```
