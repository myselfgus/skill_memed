https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-feature-toggle/

# Configurar funcionalidades da prescrição (setFeatureToggle)

Com o comando `setFeatureToggle` é possível ativar e desativar alguns recursos
e características da prescrição digital.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setFeatureToggle";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
  propriedade: true | false,
});
```

### Funcionalidades que podem ser ativadas/desativadas

| Funcionalidade | Valor padrão | Descrição |
| --- | --- | --- |
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

### Exemplos

Você pode desativar/ativar várias ou apenas uma funcionalidade da prescrição.

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    historyPrescription: true,
    deletePatient:false,
    removePrescription: false
});
```

### deletePatient

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    deletePatient: true
});
```

Permite que o prescritor seja capaz de excluir o paciente da base de dados.

![excluir-paciente](https://cdn.memed.com.br/doc/excluir-paciente.webp)

### removePatient

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    removePatient: true
});
```

Permite que o prescritor seja capaz de remover o paciente da prescrição.

![remove-patient](https://cdn.memed.com.br/doc/remove-patient.webp)

### editPatient

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    editPatient: true
});
```

### setAllowedSignatureProviders

Lista de provedores de assinatura digital disponíveis para o prescritor:

| Nome do provedor | Valor |
| --- | --- |
| Certisign | 'certisign' |
| Evaltec | 'evaltec' |
| Lacuna | 'lacuna' |
| Soluti | 'soluti' |
| Dinamo | 'dinamo' |
| Vidaas | 'vidaas' |
| Safeid | 'safeid' |

No exemplo abaixo, estamos habilitando os provedores `certisign` e `vidaas` para o prescritor.

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    setAllowedSignatureProviders: ['certisign', 'vidaas']
});
```

O valor padrão dessa propriedade é `false`. Para habilitar a lista de provedores de
assinatura digital,   
é necessário enviar uma lista em formato de array para a propriedade `setAllowedSignatureProviders`.  
com os valores que deseja habilitar.

### forceSign

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    forceSign: true
});
```

Ao ativar, só é possível seguir o fluxo de prescrição após autenticação com o provedor de assinatura digital do prescritor.

### historyPrescription

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    historyPrescription: true
});
```

Permite que o prescritor visualize o histórico de prescrições geradas para o paciente.

Se você já possui um local habitual para armazenar o histórico de prescrições dentro do prontuário,
é possível desabilitar essa opção na Memed. Assim o prescritor continua a consultar o histórico em um
local centralizado.

Essa funcionalidade é utilizada por prescritor que utilizam a plataforma Stand Alone (fora do prontuário).
É importante desativá-lo em integrações, pois não tem nenhuma função.

![history-prescription](https://cdn.memed.com.br/doc/history-prescription.webp)

### optionsPrescription

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    optionsPrescription: true
});
```

Permite que o prescritor seja capaz de acessar e editar as opções do receituário.
Se a impressão for pré-definida e for configurada via API, é possível desativar essa função para
que os prescritores não tenham possibilidade de editar as configurações.

![options-prescription](https://cdn.memed.com.br/doc/options-prescription.webp)![options-prescription-screen.webp](https://cdn.memed.com.br/doc/options-prescription-screen.webp.webp)

### removePrescription

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    removePrescription: true
});
```

Permite que o prescritor seja capaz de remover uma prescrição do histórico de prescrições do paciente.

![remove-prescription](https://cdn.memed.com.br/doc/remove-prescription.webp)

### setPatientAllergy

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    setPatientAllergy: true
});
```

Permite que o prescritor seja capaz de adicionar alergias conhecidas ao paciente.

![set-patient-allergy](https://cdn.memed.com.br/doc/set-patient-allergy.webp)![set-patient-allergy-screen](https://cdn.memed.com.br/doc/set-patient-allergy-screen.webp)

### autocompleteManipulated

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    autocompleteManipulated: true
});
```

Permite que o prescritor visualizar a lista de "Fórmulas".

![autocomplete-manipulated](https://cdn.memed.com.br/doc/autocomplete-manipulated.png)

### autocompleteCompositions

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    autocompleteCompositions: true
});
```

Permite que o prescritor visualize a lista de "Nomes Genéricos"

![autocomplete-compositions](https://cdn.memed.com.br/doc/autocomplete-compositions.webp)

### autocompletePeripherals

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    autocompletePeripherals: true
});
```

Permite que o prescritor visualize a lista de produtos periféricos ("Outros")

![autocomplete-peripherals](https://cdn.memed.com.br/doc/autocomplete-peripherals.webp)

### copyMedicalRecords

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    copyMedicalRecords: true
});
```

Permite que o prescritor copie os dados da prescrição para a área de transferência (clipboard).

![copy-medical-records](https://cdn.memed.com.br/doc/copy-medical-records.webp)

### buttonClose

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    buttonClose: true
});
```

Permite que o prescritor seja capaz de fechar o módulo da Memed.
Se por algum motivo não for permitido no sistema que o prescritor feche a prescrição uma vez aberta, é possível desabilitar o botão.

![button-close](https://cdn.memed.com.br/doc/button-close.png)

### newFormula

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    newFormula: true
});
```

Permite que o prescritor seja capaz de adicionar uma nova fórmula.

![new-formula](https://cdn.memed.com.br/doc/new-formula.webp)

### allowShareModal

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    allowShareModal: true
});
```

Permite que o prescritor seja capaz de compartilhar o link da prescrição através do WhatsApp e também via SMS.

![allow-share-modal](https://cdn.memed.com.br/doc/allow-share-modal.png)

### guidesOnboarding

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    guidesOnboarding: true
});
```

Controla se a guia para primeiro acesso do prescritor será exibida quando ele acessar o módulo pela primeira vez.

![guides-onboarding](https://cdn.memed.com.br/doc/guides-onboarding.webp)

### conclusionModalEdit

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    conclusionModalEdit: true
});
```

Permite que o prescritor edite uma receita após a sua emissão.

![conclusion-modal-edit](https://cdn.memed.com.br/doc/conclusion-modal-edit.png)

### dropdownSync

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    dropdownSync: true
});
```

Permite que ao prescritor vincular a conta criada através do parceiro com sua conta standalone.

![dropdown-sync](https://cdn.memed.com.br/doc/dropdown-sync.webp)

### showProtocol

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    showProtocol: true
});
```

Permite que o prescritor visualize os protocolos.

![show-protocol](https://cdn.memed.com.br/doc/show-protocol.webp)

### showHelpMenu

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    showHelpMenu: true
});
```

Permite que o prescritor visualize o menu de ajuda.

![show-help-menu.webp](https://cdn.memed.com.br/doc/show-help-menu.webp)

### editIdentification

```js
await MdHub.command.send("plataforma.prescricao", "setFeatureToggle", {
    editIdentification: true
});
```

Controla se é permitido editar ou não os dados já preenchidos nos campos da tela de
identificação de prescritor e paciente no fluxo de prescrição

**Valor padrão:**  `true` . Permite a edição dos campos já preenchidos.

![edit-identification.webp](https://cdn.memed.com.br/doc/edit-identification.webp)
