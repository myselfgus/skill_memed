https://doc.memed.com.br/docs/frontend/comandos-mdhub/categories-condition/

# Definir alertas de condição (categoriesConditions)

A Memed atualmente disponibiliza alertas personalizados em casos de pacientes específicos, como aeronautas e dopagem. Para utilizar estes alertas, eles devem ser definidos através do comando setPaciente, junto com as informações de paciente necessárias na prescrição conforme modelo acima.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

As opções dos alertas de condição são definidas através de ids, os ids estão listados abaixo

| ID | Condição | Descrição |
| --- | --- | --- |
| 1 | Aeronautas | Alertas relacionados a medicamentos que podem gerar problemas ao paciente em conduzir aeronaves |
| 2 | Atletas | Alertas relacionados a medicamentos que podem gerar alterações em exames de dopagem ligados a competições esportivas |
| 3 | Gestantes | Alertas relacionados a medicamentos contraindicados ou que exigem precaução durante a gestação |
| 4 | Lactantes | Alertas relacionados a medicamentos contraindicados ou que exigem precaução durante a amamentação |

### Sintaxe do comando:

```js
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  nome: "João Silva",
  // ...restante dos campos
  categoriesConditions: [1]
});
```
