https://doc.memed.com.br/docs/como-fazer/gestao-paciente/

# Gestão do paciente

A Memed disponibiliza os seguintes comandos para realizar a gestão do paciente:

* [setPacient](/docs/como-fazer/gestao-paciente#setpacient)
* [setAllergy](/docs/como-fazer/gestao-paciente#setallergy)
* [categoryConditions](/docs/como-fazer/gestao-paciente#categoryconditions)
* [addItem](/docs/como-fazer/gestao-paciente#additem)
* [setFeatureToggle](/docs/como-fazer/gestao-paciente#setfeaturetoggle)

### Definir Pacientes (setPacient)

Este comando possibilita ao parceiro configurar o envio previamente dos dados do paciente para a plataforma de prescrição
da Memed.
Ou seja, assim que a plataforma de prescrição for carregada, os dados do paciente estarão previamente preenchidos,
e o usuário prescritor não precisará preenchê-los.

Para saber como implementar esse comando leia este artigo [aqui](/docs/frontend/comandos-mdhub/set-patient)

### setAllergy

Este comando possibilita ao parceiro configurar o envio previamente das alergias do seu paciente à Memed
para que o usuário prescritor. Assim este não precisa cadastrar as alergias do paciente dentro da plataforma,
e proporciona maior segurança ao paciente no momento de prescrever. Ou seja, assim que a plataforma de prescrição for
carregada, essas alergias já estarão cadastradas no paciente.

Para saber como implementar esse comando leia este artigo [aqui](/docs/frontend/comandos-mdhub/set-allergy)

### categoryConditions

Este comando possibilita ao usuário prescritor receber alertas após inserir um determinado medicamento na plataforma,
e caso este medicamento oferecer algum risco ao paciente com condições específicas, como exemplo
aeronautas e pacientes com risco de dopagem, um alerta irá aparecer na plataforma.

Para saber como implementar esse comando leia este artigo [aqui](/docs/frontend/comandos-mdhub/set-patient#category-condition)

### addItem

Este comando possibilita ao parceiro configurar o envio previamente dos medicamentos ou exames
que serão receitados para o paciente na plataforma de prescrição da Memed. Ou seja,
assim que a plataforma de prescrição for carregada, esses medicamentos já estarão no receituario do paciente.

Para saber como implementar esse comando leia este artigo [aqui](/docs/frontend/comandos-mdhub/add-item)

### setFeatureToggle

Este comando possibilita ao parceiro realizar configurações que habilite ou não algumas ações
do usuário prescritor sobre os dados do paciente.
Por exemplo:

* `deletePatient` Permite que o prescritor exclua o paciente da base de dados.
* `removePatient` Permite que o prescritor remova o paciente da prescrição.
* `editPatient` Permite que o prescritor edite os dados do paciente na base de dados.
* `setPatientAllergy` Permite que o prescritor registre alergias conhecidas do paciente.
* `conclusionModalEdit` Permite que o prescritor visualize o botão de protocolos.
* `editIdentification` Controla se é permitido editar ou não os dados já preenchidos nos campos da tela de
  identificação de prescritor e paciente no fluxo de prescrição
* `addPrescriptionDrug` Permite que o prescritor utilize o botão de adicionar medicamentos
* `removePrescriptionDrug` Permite que o prescritor utilize o botão de excluir medicamentos
* `editPrescriptionDrugTitle` Permite ao prescritor a edição do nome do medicamento quando este for texto livre

Para saber como implementar esse comando leia este artigo [aqui](/docs/frontend/comandos-mdhub/set-feature-toggle)

### Veja como ficaria um exemplo após implementar esses 5 comandos ao mesmo tempo:
