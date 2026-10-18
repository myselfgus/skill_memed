# Comandos MdHub (MdHub.command.send)

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- Adicionar item a Prescrição (addItem) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/add-item`
- Definir alertas de condição (categoriesConditions) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/categories-condition`
- Opções de Receituario (Find) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/find`
- Esconder o módulo (hide) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/hide`
- Sair do sistema (Logout) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/logout`
- Nova Prescrição (newPrescription) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/new-prescription`
- Adicionar dados (setAdditionalData) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-additional-data`
- Definir alergia no paciente (setAllergy) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-allergy`
- Definir o nome do modulo (setDictionary) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-dictionary`
- Configurar funcionalidades da prescrição (setFeatureToggle) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle`
- Configurar Paciente (setPaciente) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient`
- Configurar local físico de trabalho do prescritor (setWorkplace) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-workplace`
- Reimpressão e edição de uma prescrição (viewPrescription) — `https://doc.memed.com.br/docs/frontend/comandos-mdhub/view-prescription`

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/add-item -->
## Adicionar item a Prescrição (addItem)

Com o comando `addItem` é possível manipular os itens da prescrição digital.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "addItem";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "addItem", {
  propriedade: "valor",
});
```

##### Propriedades do comando Add Item

| Propriedade | Valor padrão | Obrigatório/Opcional | Descrição |
|---|---|---|---|
| id | null | opcional | ID do medicamento na Memed (quando não informado, se transforma em texto livre) |
| nome | null | opcional | Nome do medicamento (utilizado em caso de texto livre). |
| posologia | null | opcional | Posologia descrição do uso. |
| quantidade | null | opcional | Quantidade do medicamento que será adicionado à prescrição (opcional, valor padrão é 1) informe quantidade 0 para uso contínuo |
| unit | null | opcional | Os valores válidos para o campo unit são: " \| embalagem \| embalagens \| form_units.singular \| form_units.plural" . |
| fabricante | null | opcional | Forma física relacionada à quantidade (opcional, valor padrão é 'embalagem'). Os valores válidos para o campo unit são: " \| embalagem \| embalagens \| form_units.singular \| form_units.plural" . |
| titularidade | null | opcional | Titularidade do medicamento |
| preco | null | opcional | Preço do medicamento |
| descricao | null | opcional | Descrição do medicamento |

#### Medicamento com ID

Para adicionar um medicamento você precisa passar o ID desse medicamento da base de dados da Memed.

```
await MdHub.command.send("plataforma.prescricao", "addItem", {
  id: "a123123123",
  posologia: "<p>HTML da posologia</p>",
  quantidade: 2,
  unit: "embalagens",
});
```

#### Fórmulas com ID

```
await MdHub.command.send("plataforma.prescricao", "addItem", {
  id: "f123123123",
  posologia: "<p>HTML da posologia</p>",
  quantidade: 2,
  unit: "embalagens",
});
```

#### Exame com ID

```
await MdHub.command.send("plataforma.prescricao", "addItem", {
  id: "e123123123",
  indicacoes: "<p>HTML da indicação</p>",
});
```

#### Texto Livre

```
await MdHub.command.send("plataforma.prescricao", "addItem", {
  nome: "Vitamina C, comprimido (100un)",
  posologia: "<p>HTML da posologia</p>",
  quantidade: 1,
  fabricante: "Nome do fabricante",
  titularidade: "Similar",
  preco: 1.99,
  descricao: "Ácido Ascórbico",
});
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/categories-condition -->
## Definir alertas de condição (categoriesConditions)

A Memed atualmente disponibiliza alertas personalizados em casos de pacientes específicos, como aeronautas e dopagem. Para utilizar estes alertas, eles devem ser definidos através do comando setPaciente, junto com as informações de paciente necessárias na prescrição conforme modelo acima.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

As opções dos alertas de condição são definidas através de ids, os ids estão listados abaixo

| ID | Condição | Descrição |
|---|---|---|
| 1 | Aeronautas | Alertas relacionados a medicamentos que podem gerar problemas ao paciente em conduzir aeronaves |
| 2 | Atletas | Alertas relacionados a medicamentos que podem gerar alterações em exames de dopagem ligados a competições esportivas |
| 3 | Gestantes | Alertas relacionados a medicamentos contraindicados ou que exigem precaução durante a gestação |
| 4 | Lactantes | Alertas relacionados a medicamentos contraindicados ou que exigem precaução durante a amamentação |

#### Sintaxe do comando:

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  nome: "João Silva",
  // ...restante dos campos
  categoriesConditions: [1]
});
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/find -->
## Opções de Receituario (Find)

Com o comando `find` é possível ativar um dos quatro temas configurados nas opções de receituário.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.sdk";
nome_do_comando = "find";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.sdk", "find", {
  propriedade: "valor",
});
```

##### Propriedades do comando find

| Propriedade | Valor padrão | Obrigatório/Opcional | Descrição |
|---|---|---|---|
| resource | opcoes-receituario/ativar/2 | obrigatório | Endpoint que ativa o receituário |
| cache | false | obrigatório | Flag que força a limpeza do cache de opções de receituário |

#### Exemplo

```
await MdHub.command.send("plataforma.sdk", "find", {
  resource: "opcoes-receituario/ativar/2",
  cache: false,
});
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/hide -->
## Esconder o módulo (hide)

A Memed disponibiliza um comando via MdHub para fechar um módulo. A sintaxe do comando é essa:

`MdHub.module.hide('nome_do_modulo');`

Um exemplo comum de uso é fechar o módulo da plataforma prescricao. Segue um exemplo abaixo:

`MdHub.module.hide('plataforma.prescricao');`

A Memed também disponibiliza uma forma de capturar o evento de quando um módulo é encerrado (fechado). Para saber mais leia esse [artigo](https://doc.memed.com.br/docs/frontend/mdsinapseprescricao-mdhub#quando-o-m%C3%B3dulo-%C3%A9-encerrado).

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/logout -->
## Sair do sistema (Logout)

A limpeza do local storage do navegador é necessária quando prescritores compartilham a mesma máquina (notebook/pc). Ela deve ser implementada OBRIGATORIAMENTE para evitar conflitos de informações entre os cadastros e consequentemente falhas de segurança. Com o comando `logout` é possível executar essa limpeza.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.sdk";
nome_do_comando = "logout";
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.sdk", "logout");
```

#### Exemplo

```
await MdHub.command.send("plataforma.sdk", "logout");
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/new-prescription -->
## Nova Prescrição (newPrescription)

Com o comando `newPrescription` é possível ter a mesma ação do botão "Nova Prescrição" da plataforma da Memed.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "newPrescription";
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "newPrescription");
```

#### Exemplo

```
await MdHub.command.send("plataforma.prescricao", "newPrescription");
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-additional-data -->
## Adicionar dados (setAdditionalData)

Com o comando `setAdditionalData` é possível adicionar informações extras no cabeçalho e rodapé.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setAdditionalData";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "setAdditionalData", {
  propriedade: "valor",
});
```

##### Propriedades do comando setAdditionalData

| Propriedade | Tipo | Obrigatório/Opcional | Descrição |
|---|---|---|---|
| header | Array [Object] | opcional | O Atributo header é um array de objetos que você pode passar informações para o cabeçalho da prescrição |
| footer | string | opcional | O footer é do tipo string e você pode passar informações adicionais para o rodapé da prescrição |

#### Exemplo

Cada item do array do atributo `header` se transforma em 1 linha no cabeçalho da prescrição.

Você pode usar `\n` para quebrar linha na string do atributo `footer` no rodapé

```
await MdHub.command.send("plataforma.prescricao", "setAdditionalData", {
  header: [
    {
      Registro: "2911116",
    },
    {
      Sexo: "Masculino",
      "Estado Civil": "Solteiro",
      "Data de Nasc": "17/09/1991",
    },
    {
      Endereço: "Rua  Arthur prado, 513",
    },
    {
      Profissional: "Dra. Emilia Reis(CRM: 123456SP)",
    },
  ],
  footer:
    "Informações adicionais na primeira linhad do rodapé \n Segunda linha do rodapé",
});
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-allergy -->
## Definir alergia no paciente (setAllergy)

Com o comando `setAllergy` é possível definir as alergias do seu paciente dentro da plataforma Memed para que o prescritor usufrua da funcionalidade "Alerta de Alergias", e proporcione maior segurança ao paciente no momento de prescrever.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

![Exemplo Alergia da Plataforma](https://cdn.memed.com.br/doc/exemplo-alergias.png "João tem 3 alergias definidas")  
Na integração de exemplo de acima, o paciente **João Silva** possui alergia nas seguintes **substancias**:

- dipirona (622)
- losartana-potassica (2584)
- amoxicilina (174)

#### Sintaxe do comando:

```
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

Para consultar o principio ativo e fazer um `De/Para` com o seu sistema é possivel utilizar esse [endpoint](https://doc.memed.com.br/docs/backend/prescricao#consultar-princ%C3%ADpios-ativos).

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-dictionary -->
## Definir o nome do modulo (setDictionary)

Com o comando `setDictionary` você tem a possibilidade de customizar alguns textos da prescrição digital. O botão que chamamos de "Protocolos" pode ser personalizado com o nome que o parceiro desejar. Ex: Modelos de Receita. Para alterar o nome de onde tiver escrito "Protocolo", basta usar o comando abaixo:

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setDictionary";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "setDictionary", {
  propriedade: "valor",
});
```

#### Propriedades de dicionário que você pode modificar

| Propriedade | Tipo | Obrigatório/Opcional | Valor Padrão |
|---|---|---|---|
| protocolPlural | string(255) | opcional | 'Protocolos' |
| protocolSingular | string(255) | opcional | 'Protocolo' |
| protocolSaved | string(255) | opcional | 'Protocolo salvo com sucesso!' |

### Exemplos

Veja abaixo um exemplo de implementação do comando `setDictionary`

```
await MdSinapsePrescricao.command.send("hub", "core:setDictionary", {
  protocolPlural: "Padrões de receitas",
  protocolSingular: "Padrão de receita",
  protocolSaved: "Modelo de Receita salvo!",
});
```

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle -->
## Configurar funcionalidades da prescrição (setFeatureToggle)

Com o comando `setFeatureToggle` é possível ativar e desativar alguns recursos e características da prescrição digital.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setFeatureToggle";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
  propriedade: true | false,
});
```

#### Funcionalidades que podem ser ativadas/desativadas

| Funcionalidade | Valor padrão | Descrição |
|---|---|---|
| deletePatient | false | Permite que o prescritor exclua o paciente da base de dados. |
| removePatient | false | Permite que o prescritor remova o paciente da prescrição. |
| editPatient | false | Permite que o prescritor edite os dados do paciente na base de dados. |
| setAllowedSignatureProviders | false | Permite configurar a lista de provedores de assinatura digital que ficarão disponíveis ao prescritor. |
| forceSign | false | Força que o prescritor tenha que assinar digitalmente para seguir o fluxo de prescrição. |
| historyPrescription | true | Permite a visualização do histórico na tela de prescrição. |
| optionsPrescription | true | Permite a exibição das opções de receituário no módulo. |
| removePrescription | true | Permite que o prescritor exclua a prescrição do histórico. |
| setPatientAllergy | true | Permite que o prescritor registre alergias conhecidas do paciente. |
| autocompleteManipulated | true | Permite que o prescritor visualize a lista de "Fórmulas". |
| autocompleteCompositions | true | Permite que o prescritor visualize a lista de "Nomes Genéricos. |
| autocompletePheripherals | true | Permite que o prescritor visualize a lista de produtos periféricos ("Outros"). |
| copyMedicalRecords | true | Permite que o prescritor copie os dados do receituário para o clipboard. |
| buttonClose | true | Permite que o prescritor visualize o botão de fechar o módulo. |
| newFormula | true | Permite que o prescritor adicione novas formulas. |
| allowShareModal | true | Permite que o prescritor seja capaz de compartilhar o link da prescrição via WhatsApp ou sms. |
| guidesOnboarding | true | Define se o guia de apresentação do módulo será exibido na primeira vez que o prescritor acessa a plataforma. |
| conclusionModalEdit | true | Permite que o prescritor edite uma prescrição gerada. |
| dropdownSync | true | Permite que o prescritor vincule o usuário gerado via parceiro com o usuário criado na plataforma da Memed. |
| showProtocol | true | Permite que o prescritor visualize o botão de protocolos. |
| showHelpMenu | true | Permite que o prescritor visualize o botão de ajuda. |
| editIdentification | true | Controla se é permitido editar ou não os dados já preenchidos nos campos da tela de identificação de prescritor e paciente no fluxo de prescrição. |
| addPrescriptionDrug | true | Permite que o prescritor utilize o botão de adicionar medicamentos. |
| removePrescriptionDrug | true | Permite que o prescritor utilize o botão de excluir medicamentos. |
| editPrescriptionDrugTitle | true | Permite ao prescritor a edição do nome do medicamento quando este for texto livre. |
| editPosology | true | Permite ao prescritor a edição da posologia do medicamento. |
| editQuantity | true | Permite ao prescritor a edição da quantidade do medicamento. |
| enableAlerts | true | Permite ao prescritor o aparecimento das mensagems de alertas sobre alergias e de condições. |

#### Exemplos

Você pode desativar/ativar várias ou apenas uma funcionalidade da prescrição.

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    historyPrescription: true,
    deletePatient:false,
    removePrescription: false
});
```

#### deletePatient

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    deletePatient: true
});
```

Permite que o prescritor seja capaz de excluir o paciente da base de dados.

![excluir-paciente](https://cdn.memed.com.br/doc/excluir-paciente.webp)

#### removePatient

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    removePatient: true
});
```

Permite que o prescritor seja capaz de remover o paciente da prescrição.

![remove-patient](https://cdn.memed.com.br/doc/remove-patient.webp)

#### editPatient

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    editPatient: true
});
```

#### setAllowedSignatureProviders

Lista de provedores de assinatura digital disponíveis para o prescritor:  

| Nome do provedor | Valor |
|---|---|
| Certisign | 'certisign' |
| Evaltec | 'evaltec' |
| Lacuna | 'lacuna' |
| Soluti | 'soluti' |
| Dinamo | 'dinamo' |
| Vidaas | 'vidaas' |
| Safeid | 'safeid' |

No exemplo abaixo, estamos habilitando os provedores `certisign` e `vidaas` para o prescritor.

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    setAllowedSignatureProviders: ['certisign', 'vidaas']
});
```

O valor padrão dessa propriedade é `false`. Para habilitar a lista de provedores de assinatura digital,  
é necessário enviar uma lista em formato de array para a propriedade `setAllowedSignatureProviders`.  
com os valores que deseja habilitar.

#### forceSign

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    forceSign: true
});
```

Ao ativar, só é possível seguir o fluxo de prescrição após autenticação com o provedor de assinatura digital do prescritor.

#### historyPrescription

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    historyPrescription: true
});
```

Permite que o prescritor visualize o histórico de prescrições geradas para o paciente.

Se você já possui um local habitual para armazenar o histórico de prescrições dentro do prontuário, é possível desabilitar essa opção na Memed. Assim o prescritor continua a consultar o histórico em um local centralizado.

Essa funcionalidade é utilizada por prescritor que utilizam a plataforma Stand Alone (fora do prontuário). É importante desativá-lo em integrações, pois não tem nenhuma função.

![history-prescription](https://cdn.memed.com.br/doc/history-prescription.webp)

#### optionsPrescription

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    optionsPrescription: true
});
```

Permite que o prescritor seja capaz de acessar e editar as opções do receituário. Se a impressão for pré-definida e for configurada via API, é possível desativar essa função para que os prescritores não tenham possibilidade de editar as configurações.

![options-prescription](https://cdn.memed.com.br/doc/options-prescription.webp)![options-prescription-screen.webp](https://cdn.memed.com.br/doc/options-prescription-screen.webp.webp)

#### removePrescription

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    removePrescription: true
});
```

Permite que o prescritor seja capaz de remover uma prescrição do histórico de prescrições do paciente.

![remove-prescription](https://cdn.memed.com.br/doc/remove-prescription.webp)

#### setPatientAllergy

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    setPatientAllergy: true
});
```

Permite que o prescritor seja capaz de adicionar alergias conhecidas ao paciente.

![set-patient-allergy](https://cdn.memed.com.br/doc/set-patient-allergy.webp)![set-patient-allergy-screen](https://cdn.memed.com.br/doc/set-patient-allergy-screen.webp)

#### autocompleteManipulated

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    autocompleteManipulated: true
});
```

Permite que o prescritor visualizar a lista de "Fórmulas".

![autocomplete-manipulated](https://cdn.memed.com.br/doc/autocomplete-manipulated.png)

#### autocompleteCompositions

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    autocompleteCompositions: true
});
```

Permite que o prescritor visualize a lista de "Nomes Genéricos"

![autocomplete-compositions](https://cdn.memed.com.br/doc/autocomplete-compositions.webp)

#### autocompletePeripherals

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    autocompletePeripherals: true
});
```

Permite que o prescritor visualize a lista de produtos periféricos ("Outros")

![autocomplete-peripherals](https://cdn.memed.com.br/doc/autocomplete-peripherals.webp)

#### copyMedicalRecords

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    copyMedicalRecords: true
});
```

Permite que o prescritor copie os dados da prescrição para a área de transferência (clipboard).

![copy-medical-records](https://cdn.memed.com.br/doc/copy-medical-records.webp)

#### buttonClose

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    buttonClose: true
});
```

Permite que o prescritor seja capaz de fechar o módulo da Memed. Se por algum motivo não for permitido no sistema que o prescritor feche a prescrição uma vez aberta, é possível desabilitar o botão.

![button-close](https://cdn.memed.com.br/doc/button-close.png)

#### newFormula

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    newFormula: true
});
```

Permite que o prescritor seja capaz de adicionar uma nova fórmula.

![new-formula](https://cdn.memed.com.br/doc/new-formula.webp)

#### allowShareModal

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    allowShareModal: true
});
```

Permite que o prescritor seja capaz de compartilhar o link da prescrição através do WhatsApp e também via SMS.

![allow-share-modal](https://cdn.memed.com.br/doc/allow-share-modal.png)

#### guidesOnboarding

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    guidesOnboarding: true
});
```

Controla se a guia para primeiro acesso do prescritor será exibida quando ele acessar o módulo pela primeira vez.

![guides-onboarding](https://cdn.memed.com.br/doc/guides-onboarding.webp)

#### conclusionModalEdit

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    conclusionModalEdit: true
});
```

Permite que o prescritor edite uma receita após a sua emissão.

![conclusion-modal-edit](https://cdn.memed.com.br/doc/conclusion-modal-edit.png)

#### dropdownSync

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    dropdownSync: true
});
```

Permite que ao prescritor vincular a conta criada através do parceiro com sua conta standalone.

![dropdown-sync](https://cdn.memed.com.br/doc/dropdown-sync.webp)

#### showProtocol

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    showProtocol: true
});
```

Permite que o prescritor visualize os protocolos.

![show-protocol](https://cdn.memed.com.br/doc/show-protocol.webp)

#### showHelpMenu

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    showHelpMenu: true
});
```

Permite que o prescritor visualize o menu de ajuda.

![show-help-menu.webp](https://cdn.memed.com.br/doc/show-help-menu.webp)

#### editIdentification

```
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    editIdentification: true
});
```

Controla se é permitido editar ou não os dados já preenchidos nos campos da tela de identificação de prescritor e paciente no fluxo de prescrição

**Valor padrão:** `true` . Permite a edição dos campos já preenchidos.

![edit-identification.webp](https://cdn.memed.com.br/doc/edit-identification.webp)

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient -->
## Configurar Paciente (setPaciente)

O comando `setPaciente` é utilizado para configurar os dados do paciente antes de iniciar uma prescrição médica na Memed. Este comando envia informações cadastrais e demográficas essenciais para diferentes tipos de prescrições.

### Quando usar

Este comando é necessário para:

- **Prescrições digitais**: Dados básicos do paciente
- **LME (Laudo Médico de Exame)**: Informações obrigatórias para emissão
- **Receitas de controle especial**: Dados necessários para medicamentos controlados

**Importante**

Este comando deve ser executado **antes** de abrir o módulo de prescrição para garantir que todos os dados do paciente estejam disponíveis durante o processo de prescrição.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setPaciente";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  propriedade: "valor",
});
```

#### Propriedades do paciente que podem ser definidas via comando

##### Campos Obrigatórios

| Propriedade | Tipo | Observações |
|---|---|---|
| idExterno | int/string(255) | Recomendável ser do tipo UUID, pois é um campo único |
| nome | string(255) | Nome completo do paciente |
| sexo | string(255) | Aceita "Masculino", "Feminino", "M", "F", "m", "f". Se ausente, preenche automaticamente com "Não informado" |

##### Campos Opcionais - Dados Pessoais

| Propriedade | Tipo | Observações |
|---|---|---|
| nome_social | string(255) | Nome social do paciente |
| cpf | string(11) | Apenas dígitos |
| passaporte | string(15) | Apenas dígitos |
| data_nascimento | string(255) | Formatado no padrão: dd/mm/YYYY |
| nome_mae | string(255) | Nome da mãe do paciente |
| telefone | string(16) | Apenas dígitos ou formatado (DDD) XXXXX-XXXX |
| email | string(255) | Deve conter formato válido de e-mail. Utilizado no formulário LME |

##### Campos Opcionais - Dados Demográficos

| Propriedade | Tipo | Observações |
|---|---|---|
| raca | string(255) | Aceita "branca", "preta", "parda", "amarela", "indígena". Padronizada para minúsculas com fallback entre raca e race |

##### Campos Opcionais - Dados Físicos e Localização

| Propriedade | Tipo | Observações |
|---|---|---|
| peso | int(10) | Peso em quilogramas |
| altura | float(10) | Altura em metros |
| endereco | string(255) | Endereço completo |
| cidade | string(255) | Cidade de residência |
| dificuldade_locomocao | bool | Valor padrão: false |

##### Campos Opcionais - Documentos Estruturados (Mention)

| Propriedade | Tipo | Observações |
|---|---|---|
| historia_clinica | string(2000) | Texto livre com a história clínica do paciente. Suporta múltiplas linhas (multiline). Limite de 2000 caracteres — ao exceder, o comando rejeita o payload com erro descritivo (sem truncamento silencioso). Coexiste com outros campos de documentos estruturados / mention (ex.: endereco , cidade ) numa mesma chamada, sem sobrescrita entre eles |

##### Campos Especiais

| Propriedade | Tipo | Observações |
|---|---|---|
| categoriesConditions | array | [1] Aeronautas, [2] Atletas (alerta antidoping), [3] Gestante, [4] Lactante |

**Normalização Automática de Dados**

O sistema normaliza automaticamente alguns dos valores enviados para melhorar a consistência dos dados, como exemplo:

**Campo Sexo:** Se não informado, preenche automaticamente com "Não informado"

**Campo Raça:**

- Normalização: Todos os valores são convertidos para minúsculas
- Aceita tanto "raca" quanto "race" como nome da propriedade

**História clínica e campos de documentos estruturados**

O campo `historia_clinica` faz parte do conjunto de campos de documentos estruturados / mention que podem ser pré-populados via `setPaciente` (junto com `endereco`, `cidade`, entre outros). Esses campos coexistem numa mesma chamada, sem que um sobrescreva o outro.

**Limite de caracteres:** o valor de `historia_clinica` é limitado a 2000 caracteres. Ao exceder o limite, o comando rejeita a requisição e retorna um erro descritivo, ao invés de truncar o conteúdo silenciosamente:

```
O campo história clínica excede o limite de 2000 caracteres.
```

**Normalização de quebras de linha:** quebras de linha no formato `\r\n` são normalizadas para `\n`, tanto na contagem do limite de 2000 caracteres quanto na persistência do valor. O campo aceita conteúdo multiline normalmente.

### Casos de Uso Comuns

#### Prescrição Digital Básica

Para prescrições digitais simples, envie apenas os campos obrigatórios:

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  idExterno: "uuid-do-paciente",
  nome: "João Silva",
  sexo: "Masculino",
  passaporte: "AB12930293345636" // ou cpf: "12345678901"
});
```

#### Prescrição com LME

Para emissão de LME, inclua todos os campos obrigatórios:

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  idExterno: "uuid-do-paciente",
  nome: "Maria Santos",
  cpf: "98765432100", // ou passaporte: "AB12930293345636"
  sexo: "Feminino",
  raca: "branca",
  telefone: "11999999999",
  email: "maria.santos@email.com"
});
```

#### Prescrição Completa

Para casos que requerem informações completas do paciente:

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  idExterno: "uuid-do-paciente",
  nome: "Pedro Costa",
  cpf: "11122233344", // ou passaporte: "AB12930293345636"
  sexo: "Masculino",
  data_nascimento: "15/03/1985",
  telefone: "11888888888", 
  email: "pedro.costa@email.com",
  endereco: "Rua das Flores, 123",
  cidade: "São Paulo",
  peso: 75,
  altura: 1.75,
  raca: "parda"
});
```

#### Prescrição com História Clínica e Documentos Estruturados

Para pré-popular a história clínica junto com outros campos de documentos estruturados / mention, sem que um sobrescreva o outro:

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  idExterno: "uuid-do-paciente",
  nome: "Ana Ferreira",
  sexo: "Feminino",
  cpf: "12345678901",
  historia_clinica: "Paciente relata dor lombar há 3 semanas.\nSem histórico de cirurgias prévias.",
  endereco: "Rua das Flores, 123",
  cidade: "São Paulo"
});
```

**Limite de historia_clinica**

Se o valor de `historia_clinica` exceder 2000 caracteres, o comando **não trunca** o conteúdo: a requisição é rejeitada com o erro:

```
O campo história clínica excede o limite de 2000 caracteres.
```

### Exemplos

**Fluxo completo**

O snippet abaixo mostra apenas o payload de `setPaciente`. Para a implementação de referência completa, consulte [Boas Práticas de Integração](https://doc.memed.com.br/docs/boas-praticas-integracao).

Veja abaixo um exemplo de implementação do comando `setPaciente`

**Fluxo completo de integração**

Este snippet cobre apenas o comando `setPaciente`. Para a implementação de referência completa — carregamento do script, eventos LGPD e abertura do módulo — consulte [Boas Práticas de Integração](https://doc.memed.com.br/docs/boas-praticas-integracao).

```
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

## Definir alertas de condição (categoriesConditions)

A Memed atualmente disponibiliza alertas personalizados em casos de pacientes específicos, como aeronautas e dopagem. Para utilizar estes alertas, eles devem ser definidos através do comando setPaciente, junto com as informações de paciente necessárias na prescrição conforme modelo acima.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

As opções dos alertas de condição são definidas através de ids, os ids estão listados abaixo

| ID | Condição | Descrição |
|---|---|---|
| 1 | Aeronautas | Alertas relacionados a medicamentos que podem gerar problemas ao paciente em conduzir aeronaves |
| 2 | Atletas | Alertas relacionados a medicamentos que podem gerar alterações em exames de dopagem ligados a competições esportivas |
| 3 | Gestantes | Alertas relacionados a medicamentos contraindicados ou que exigem precaução durante a gestação |
| 4 | Lactantes | Alertas relacionados a medicamentos contraindicados ou que exigem precaução durante a amamentação |

#### Sintaxe do comando:

```
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  nome: "João Silva",
  // ...restante dos campos
  categoriesConditions: [1]
});
```

**Campos Obrigatórios para LME:**

Para emissão de LME (Laudo Médico de Exame), os seguintes campos são obrigatórios:

- **nome**: Nome completo do paciente
- **documento de identificação**: **Cpf** ou **passaporte** (apenas dígitos)
- **sexo**: Sexo do paciente ("Masculino" ou "Feminino")
- **raca**: Raça/cor do paciente ("branca", "preta", "parda", "amarela" ou "indígena")
- **telefone**: Telefone de contato do paciente
- **email**: E-mail válido do paciente

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-workplace -->
## Configurar local físico de trabalho do prescritor (setWorkplace)

É comum que o prescritor atenda em diferentes lugares durante sua jornada de trabalho. Com o comando `setWorkplace` é possível preencher o endereço do prescritor que sairá no receituário.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setWorkplace";
parametro = { propriedade: valor };
```

#### Sintaxe do comando

```
await MdHub.command.send("plataforma.prescricao", "setWorkplace", {
  propriedade: "valor",
});
```

**CNES e nome do estabelecimento obrigatórios em novos onboardings**

Para novos onboardings de parceiros, os campos `cnes` e `local_name` passam a ser **obrigatórios**. Isso permite identificar de forma estruturada o estabelecimento de saúde responsável por cada prescrição.

##### Propriedades do comando setWorkplace

| Propriedade | Tipo | Obrigatório/Opcional | Descrição |
|---|---|---|---|
| city | string | opcional | Cidade do local de trabalho |
| state | string | opcional | UF do local de trabalho |
| cnes | string | obrigatório * | Cadastro Nacional de Estabelecimentos de Saúde |
| local_name | string | obrigatório * | Nome do local de trabalho |
| address | string | opcional | Endereço completo com número |
| phone | string | opcional | Telefone do prescritor |

\* Obrigatório para novos onboardings de parceiros. Ver diretrizes de aplicação abaixo.

#### Exemplo

```
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

#### Diretrizes de aplicação da regra

- **Novos onboardings de parceiros:** o envio de `cnes` e `local_name` é obrigatório a partir do início da integração. Parceiros que iniciarem o processo de onboarding a partir desta atualização devem enviar ambos os campos preenchidos no comando `setWorkplace`.
- **Integrações legadas:** parceiros já integrados anteriormente **não terão o envio bloqueado imediatamente** por ausência de `cnes` ou `local_name`. A obrigatoriedade vale para novas integrações; a migração de integrações existentes deve ser tratada separadamente, sem quebra de compatibilidade retroativa.

---

<!-- fonte: https://doc.memed.com.br/docs/frontend/comandos-mdhub/view-prescription -->
## Reimpressão e edição de uma prescrição (viewPrescription)

Com o comando `viewPrescription` é possível implementar a reimpressão e edição de uma prescrição já gerada.

**Atenção**

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo recomendamos o uso de **async**/**await** como padrão de implementação para evitar problemas de assincronicidade durante a execução dos comandos. Você também pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

#### Estrutura do comando

```
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "viewPrescription";
parametro = "string";
```

#### Sintaxe do comando

```
await MdHub.command.send(
  "plataforma.prescricao",
  "viewPrescription",
  "ID_DA_PRESCRICAO"
);
```

#### Exemplo

```
await MdHub.command.send("plataforma.prescricao", "viewPrescription", "1234");
```
