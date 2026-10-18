https://doc.memed.com.br/docs/frontend/comandos-mdhub/set-patient/

# Configurar Paciente (setPaciente)

O comando `setPaciente` é utilizado para configurar os dados do paciente antes de iniciar uma prescrição médica na Memed. Este comando envia informações cadastrais e demográficas essenciais para diferentes tipos de prescrições.

## Quando usar

Este comando é necessário para:

* **Prescrições digitais**: Dados básicos do paciente
* **LME (Laudo Médico de Exame)**: Informações obrigatórias para emissão
* **Receitas de controle especial**: Dados necessários para medicamentos controlados

Importante

Este comando deve ser executado **antes** de abrir o módulo de prescrição para garantir que todos os dados do paciente estejam disponíveis durante o processo de prescrição.

Atenção

Todos os comandos do **MdHub** são executados de forma **assíncrona**. Por esse motivo
recomendamos o uso de **async**/**await** como padrão de implementação para evitar
problemas de assincronicidade durante a execução dos comandos. Você também
pode utilizar o método **.then()** para saber quando o comando terminou sua execução.

### Estrutura do comando

```js
nome_do_modulo = "plataforma.prescricao";
nome_do_comando = "setPaciente";
parametro = { propriedade: valor };
```

### Sintaxe do comando

```js
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  propriedade: "valor",
});
```

### Propriedades do paciente que podem ser definidas via comando

#### Campos Obrigatórios

| Propriedade | Tipo | Observações |
| --- | --- | --- |
| **idExterno** | **int/string(255)** | Recomendável ser do tipo UUID, pois é um campo único |
| **nome** | **string(255)** | Nome completo do paciente |
| **sexo** | **string(255)** | Aceita "Masculino", "Feminino", "M", "F", "m", "f". Se ausente, preenche automaticamente com "Não informado" |

#### Campos Opcionais - Dados Pessoais

| Propriedade | Tipo | Observações |
| --- | --- | --- |
| nome\_social | string(255) | Nome social do paciente |
| cpf | string(11) | Apenas dígitos |
| passaporte | string(15) | Apenas dígitos |
| data\_nascimento | string(255) | Formatado no padrão: dd/mm/YYYY |
| nome\_mae | string(255) | Nome da mãe do paciente |
| telefone | string(16) | Apenas dígitos ou formatado (DDD) XXXXX-XXXX |
| email | string(255) | Deve conter formato válido de e-mail. Utilizado no formulário LME |

#### Campos Opcionais - Dados Demográficos

| Propriedade | Tipo | Observações |
| --- | --- | --- |
| raca | string(255) | Aceita "branca", "preta", "parda", "amarela", "indígena". Padronizada para minúsculas com fallback entre raca e race |

#### Campos Opcionais - Dados Físicos e Localização

| Propriedade | Tipo | Observações |
| --- | --- | --- |
| peso | int(10) | Peso em quilogramas |
| altura | float(10) | Altura em metros |
| endereco | string(255) | Endereço completo |
| cidade | string(255) | Cidade de residência |
| dificuldade\_locomocao | bool | Valor padrão: false |

#### Campos Opcionais - Documentos Estruturados (Mention)

| Propriedade | Tipo | Observações |
| --- | --- | --- |
| historia\_clinica | string(2000) | Texto livre com a história clínica do paciente. Suporta múltiplas linhas (multiline). Limite de 2000 caracteres — ao exceder, o comando rejeita o payload com erro descritivo (sem truncamento silencioso). Coexiste com outros campos de documentos estruturados / mention (ex.: `endereco`, `cidade`) numa mesma chamada, sem sobrescrita entre eles |

#### Campos Especiais

| Propriedade | Tipo | Observações |
| --- | --- | --- |
| categoriesConditions | array | **[1]** Aeronautas, **[2]** Atletas (alerta antidoping), **[3]** Gestante, **[4]** Lactante |

Normalização Automática de Dados

O sistema normaliza automaticamente alguns dos valores enviados para melhorar a consistência dos dados, como exemplo:

**Campo Sexo:** Se não informado, preenche automaticamente com "Não informado"

**Campo Raça:**

* Normalização: Todos os valores são convertidos para minúsculas
* Aceita tanto "raca" quanto "race" como nome da propriedade

História clínica e campos de documentos estruturados

O campo `historia_clinica` faz parte do conjunto de campos de documentos estruturados / mention que podem ser pré-populados via `setPaciente` (junto com `endereco`, `cidade`, entre outros). Esses campos coexistem numa mesma chamada, sem que um sobrescreva o outro.

**Limite de caracteres:** o valor de `historia_clinica` é limitado a 2000 caracteres. Ao exceder o limite, o comando rejeita a requisição e retorna um erro descritivo, ao invés de truncar o conteúdo silenciosamente:

```text
O campo história clínica excede o limite de 2000 caracteres.
```

**Normalização de quebras de linha:** quebras de linha no formato `\r\n` são normalizadas para `\n`, tanto na contagem do limite de 2000 caracteres quanto na persistência do valor. O campo aceita conteúdo multiline normalmente.

## Casos de Uso Comuns

### Prescrição Digital Básica

Para prescrições digitais simples, envie apenas os campos obrigatórios:

```js
await MdHub.command.send("plataforma.prescricao", "setPaciente", {
  idExterno: "uuid-do-paciente",
  nome: "João Silva",
  sexo: "Masculino",
  passaporte: "AB12930293345636" // ou cpf: "12345678901"
});
```

### Prescrição com LME

Para emissão de LME, inclua todos os campos obrigatórios:

```js
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

### Prescrição Completa

Para casos que requerem informações completas do paciente:

```js
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

### Prescrição com História Clínica e Documentos Estruturados

Para pré-popular a história clínica junto com outros campos de documentos estruturados / mention, sem que um sobrescreva o outro:

```js
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

Limite de historia\_clinica

Se o valor de `historia_clinica` exceder 2000 caracteres, o comando **não trunca** o conteúdo: a requisição é rejeitada com o erro:

```text
O campo história clínica excede o limite de 2000 caracteres.
```

## Exemplos

Fluxo completo

O snippet abaixo mostra apenas o payload de `setPaciente`. Para a implementação de referência completa, consulte [Boas Práticas de Integração](/docs/boas-praticas-integracao).

Veja abaixo um exemplo de implementação do comando `setPaciente`

Fluxo completo de integração

Este snippet cobre apenas o comando `setPaciente`. Para a implementação de referência completa — carregamento do script, eventos LGPD e abertura do módulo — consulte [Boas Práticas de Integração](/docs/boas-praticas-integracao).

```js
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

Campos Obrigatórios para LME:

Para emissão de LME (Laudo Médico de Exame), os seguintes campos são obrigatórios:

* **nome**: Nome completo do paciente
* **documento de identificação**: **Cpf** ou **passaporte** (apenas dígitos)
* **sexo**: Sexo do paciente ("Masculino" ou "Feminino")
* **raca**: Raça/cor do paciente ("branca", "preta", "parda", "amarela" ou "indígena")
* **telefone**: Telefone de contato do paciente
* **email**: E-mail válido do paciente
