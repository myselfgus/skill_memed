https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-workplace/

# Configurar local físico de trabalho do prescritor (setWorkplace)

É comum que o prescritor atenda em diferentes lugares durante sua jornada de trabalho.
Com o comando `setWorkplace` é possível preencher o endereço do prescritor que sairá no receituário.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setWorkplace";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "setWorkplace", {
  propriedade: "valor",
});
```

CNES e nome do estabelecimento obrigatórios em novos onboardings

Para novos onboardings de parceiros, os campos `cnes` e `local_name` passam a ser **obrigatórios**.
Isso permite identificar de forma estruturada o estabelecimento de saúde responsável por cada
prescrição.

#### Propriedades do comando setWorkplace

| Propriedade | Tipo | Obrigatório/Opcional | Descrição |
| --- | --- | --- | --- |
| city | string | opcional | Cidade do local de trabalho |
| state | string | opcional | UF do local de trabalho |
| cnes | string | obrigatório \* | Cadastro Nacional de Estabelecimentos de Saúde |
| local\_name | string | obrigatório \* | Nome do local de trabalho |
| address | string | opcional | Endereço completo com número |
| phone | string | opcional | Telefone do prescritor |

\* Obrigatório para novos onboardings de parceiros. Ver diretrizes de aplicação abaixo.

### Exemplo

```js
await MdHub.command.send("plataforma.prescricao", "setWorkplace", {
  city: "Cidade Teste",
  state: "TS",
  cnes: 0000, // obrigatório em novos onboardings
  local_name: "Clinica Teste", // obrigatório em novos onboardings
  address: "Rua teste, 123",
  phone: 0000000000,
});
```

Caso o número do telefone seja "0800", o valor do atributo phone deve ser uma `string`.

### Diretrizes de aplicação da regra

* **Novos onboardings de parceiros:** o envio de `cnes` e `local_name` é obrigatório a partir do
  início da integração. Parceiros que iniciarem o processo de onboarding a partir desta atualização
  devem enviar ambos os campos preenchidos no comando `setWorkplace`.
* **Integrações legadas:** parceiros já integrados anteriormente **não terão o envio bloqueado
  imediatamente** por ausência de `cnes` ou `local_name`. A obrigatoriedade vale para novas
  integrações; a migração de integrações existentes deve ser tratada separadamente, sem
  quebra de compatibilidade retroativa.
