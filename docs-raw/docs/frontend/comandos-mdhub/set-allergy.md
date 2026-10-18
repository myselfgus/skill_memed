https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-allergy/

# Definir alergia no paciente (setAllergy)

Com o comando `setAllergy` é possível definir as alergias do seu paciente dentro da plataforma Memed
para que o prescritor usufrua da funcionalidade "Alerta de Alergias",
e proporcione maior segurança ao paciente no momento de prescrever.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

![Exemplo Alergia da Plataforma](https://cdn.memed.com.br/doc/exemplo-alergias.png "João tem 3 alergias definidas")   
Na integração de exemplo de acima, o paciente **João Silva** possui alergia nas seguintes **substancias**:

* dipirona (622)
* losartana-potassica (2584)
* amoxicilina (174)

### Sintaxe do comando:

```js
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  nome: "João Silva",
  // ...restante dos campos
});

// Agora vamos definir que o paciente acima, tem alergia as alergias: `dipirona`, `losartana-potassica`, `amoxicilina`.
await MdHub.command.send("plataforma.prescricao", "setAllergy", [
  622, // Principio Ativo: (dipirona)
  2584, // Principio Ativo: (losartana-potassica)
  174, // Principio Ativo: (amoxicilina)
]);
```

Para consultar o principio ativo e fazer um `De/Para` com o seu sistema é possivel utilizar esse [endpoint](/docs/backend/prescricao#consultar-princ%C3%ADpios-ativos).
