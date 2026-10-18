https://doc.memed.com.br/docs/frontend/eventos-mdhub/prescricao-impressa/

# Prescrição impressa

Quando uma prescrição é emitida pelo usuário prescritor, enviamos o evento `prescricaoImpressa`.
Esse evento retorna os dados da prescrição gerada pelo usuário.

Veja um exemplo de implementação para escutar o evento:

```js
MdSinapsePrescricao.event.add('core:moduleInit', function(moduleData){
    if (moduleData.name === 'plataforma.prescricao') {
        // O módulo da prescrição foi iniciado.
        MdHub.event.add('prescricaoImpressa', function(prescriptionData) {
            // No objeto "prescriptionData", são retornadas as informações da prescrição gerada.
            // Implementar ações, callbacks, etc.
        });
    }
});
```

**Dados retornados**

A Memed retorna todos os dados da prescrição na variável `prescriptionData`,
conforme exemplo acima, sendo possível identificar dados do paciente, prescritor e medicamento.
Logo, escutando o evento, o parceiro tem uma infinidade de possibilidades com a informação retornada. Ex.:

* Atualizar dados de prescritor/paciente no sistema do parceiro;

  + Verificar se houve alguma informação alterada pelo prescritor durante o uso da Memed.
    Ex.: trocou o número de telefone do paciente;
* Analisar dados dos itens da prescrição:

  + Quantas vezes o medicamento X foi prescrito?
  + Quantos antibióticos/exames foram prescritos?
  + Qual é o preço médio das minhas prescrições?
  + etc.

**Medicamentos**

No objeto `prescriptionData`, existe o atributo `medicamentos` que é um array de objetos com todos os itens da prescrição
(medicamentos, exames, atestados, etc.). Abaixo iremos detalhar os seus principais atributos.

**Características básicas de um item**

```js
{
    "id": "w6589",
    "nome": "Dipirona sódica 500mg, Comprimido",
    "descricao": "Dipirona sódica 500mg",
    "posologia": "<p>Tomar 1 comprimido até de 6 em 6 horas, se necessário.</p>",
    "quantidade": 1
    "sanitized_posology": "Tomar 1 comprimido até de 6 em 6 horas, se necessário."
    "unit": "comprimido",
    ...
}
```

Os campos acima definem qual é o item, sua quantidade, unidade e posologia.
São os campos que podem ser alterados pelo prescritor durante a geração da prescrição e podem ser utilizados na
criação de um [protocolo](/docs/backend/protocolos#cadastrar-protocolos-para-o-usu%C3%A1rio).

**Tipos de itens da prescrição**

Os atributos "tipo" e "receituario" servem para indicar qual é o tipo de item da prescrição e seu respectivo
formato de receituário.

```js
{
    ...
    "prescrição": {
        ...
        "medicamentos": [
            {
                ...
                "tipo": "white-label",
                "receituario": "Simples",
                ...
            }
        ...
    }
    ...
}
```

**Os possíveis valores para os dois atributos são:**

* Tipo:

  + alopático
  + dermocosmético
  + exame
  + fitoterápico
  + homeopático
  + manipulado
  + periférico
  + white-label
  + custom -> Textos livres
* Receituários:

  + Notif. receita A (A1)
  + Notif. receita A (A2)
  + Notif. receita A (A3)
  + Notif. receita B (B1)
  + Notif. receita B (B2)
  + Especial-2 vias (C1)
  + Retinóides sist. (C2)
  + Talidomida-2 vias (C3)
  + Especial-2 vias (C4)
  + Especial-2 vias (C5)
  + Antibióticos-2 vias
  + Simples
  + Essencial
  + Especial-2 vias

**Códigos de exame**

Após identificar que o item da prescrição é um exame, é possível realizar um de/para no
sistema do parceiro através dos códigos SUS e TUSS. Segue abaixo um exemplo de retorno para uma
prescrição contendo um hemograma:

```js
{
    ...
    "prescrição": {
        ...
        "medicamentos": [
            {
                ...
                "id": "e10"
                "nome": "Hemograma completo"
                "exames_sus_codigo": "0202020380",
                "exames_tuss_codigo": "40304361"
                ...
            }
        ...
    }
    ...
}
```

**Dados adicionais**

Caso o parceiro tenha implementado os comandos [setWorkplace](/docs/como-fazer/gestao-do-prescritor#setworkplace)
e/ou [setAdditionalData](/docs/como-fazer/gestao-do-prescritor#metadados-e-informa%C3%A7%C3%B5es-de-impress%C3%A3o-adicionais-no-cabe%C3%A7alho-e-rodap%C3%A9), os atributos
workplace e additionalData terão os valores informados anteriormente.

**Documentos Estruturados**

Lista de dados Estruturados

* Atestados Gerais:

  + Restrição de atividades (Home Office)
  + Aptidão Física
  + Sanidade Mental
  + Uso de Piscina
* Atestados de Afastamento:

  + Atividades laborais
  + Atividades escolares
  + Home Office
* Declarações

  + Acompanhamento
  + Comparecimento
* Encaminhamento estruturado
* Relatório

Os dados relacionados a Documentos Estruturados podem ser obtidos a partir de dois campos: "additionalData" e "medicamentos".

Em "additionalData", o campo "mentions" estará presente fornecendo um conjunto de propriedades que definem o valor das mentions usada em cada documento estruturado.

Em "medicamentos", os campos que definem o tipo da prescrição como documento estruturado são "tipo" e "custom\_categoria".

Para mais detalhes sobre a interface dos campo, consulte o exemplo abaixo:

```js
{
    ...
    "prescrição": {
        "additionalData": {
            ...
            "mentions": {
                "nome": "João Silva",
                "cpf": "111.222.333-44",
                "endereco": "Rua Acre, 123",
                "cidade": "Rio de Janeiro",
                "gender": "Masculino",
                "data_afastamento": "01-01-2000",
                "dias_afastamento": "3",
                "horario_atendimento": "10:20:30",
                "grau_parentesco": "pai",
                "acompanhante": "Antônio Silva",
                "CID": "c638",
                "especialidade": "Otorrinolaringologista",
                "situacao_paciente": "apto com restrições"
            }
        },
        ...
        "medicamentos": [
            {
                ...
                "id": "c181503",
                "nome": "Atestado de Aptidão Física",
                "posologia": "Atesto, para os devidos fins, que André Silva, CPF 111.222.333-44, encontra-se apto(a) para a prática de atividades físicas, não havendo, no momento, contraindicações clínicas."
                "tipo": "custom",
                "custom_categoria": "atestado"
                ...
            }
        ]
        ...
    }
    ...
}
```

**Payload de exemplo e seus campos**

Você pode identificar os campos de um payload e seus significados através da tabela abaixo:

| Linha | Campo origem do payload de entrada | Conteúdo recebido no payload de entrada | Descrição do dado/campo de origem |
| --- | --- | --- | --- |
| 1 | { |  | Inicio do array |
| 2 | "alterada" | false, | Se a prescrição foi alterada |
| 3 | "prescricao" | { | Array da prescrição |
| 4 | "paciente" | { | Array do paciente |
| 5 | "id" | **id** | Id do paciente |
| 6 | "external\_id" | **id** | Id do paciente no sistema integrador |
| 7 | "category\_condition\_id" | 2 | Categoria de alertas de condições |
| 8 | "benefit\_member\_id" | null, | Não usado |
| 9 | "nome" | "João Silva", | Nome do paciente |
| 10 | "nome\_completo" | null, | Nome completo do paciente cadastrado, este dado é opcional e depende de preenchimento do prescritor. |
| 11 | "nome\_social" | null, | Nome social do paciente |
| 12 | "peso" | null, | Peso do paciente |
| 13 | "altura" | null, | Altura do paciente |
| 14 | "rg" | null, | RG do paciente |
| 15 | "cpf" | null, | CPF do paciente |
| 16 | "data\_nascimento" | null, | Data de nascimento do paciente |
| 17 | "nome\_mae" | null, | Nome da mãe do paciente |
| 18 | "dificuldade\_locomocao" | false, | Se o paciente possui dificuldade de locomoção |
| 19 | "nome\_responsavel" | null, | Nome do responsável pelo paciente |
| 20 | "email" | null, | Email do paciente |
| 21 | "telefone" | "11999999999", | Telefone do paciente |
| 22 | "cidade" | "São Paulo", | Cidade do paciente |
| 23 | "endereco" | "Rua da Saúde, 123", | Endereço completo do paciente |
| 24 | "accept\_terms" | 0 | Termo de aceite do paciente na abertura da prescrição digital |
| 25 | "total" | 4 | Total de prescrições geradas para o paciente pelo prescritor do atendimento |
| 26 | "type" | "pacientes", | Tipo de usuário |
| 27 | "\_relationships" | { | Array de relacionamentos do paciente |
| 28 | "allergy" | [ | Array de alergias do paciente |
| 29 | { |  | -- |
| 30 | "id" | 1286 | Id da alergia do paciente |
| 31 | "patient\_id" | **id** | Id Memed do paciente |
| 32 | "ingredient\_id" | 622 | ID do principio ativo |
| 33 | "created\_at" | "2023-05-16 16:37:11", | Data de cadastro da alergia |
| 34 | "deleted\_at" | null, | Exclusão do cadastro da alergia |
| 35 | "type" | "patient\_allergy", | Tipo do cadastro |
| 36 | "ingredient\_name" | "Dipirona", | Principio ativo alergico |
| 37 | "related" | "Dipirona magnésica, Dipirona sódica, Dipirona mono-hidratada" | Principio ativo relacionado |
| 38 | } |  | -- |
| 39 | ] |  | -- |
| 40 | }, |  | -- |
| 41 | "ultima" | "16/05/2023 16:37:17", | Ultima prescrição do paciente |
| 42 | "allergy" | [ | Array de alergias |
| 43 | { |  | -- |
| 44 | "id" | 1286 | Id da alergia da alergia |
| 45 | "patient\_id" | **id** | Id Memed do paciente |
| 46 | "ingredient\_id" | 622 | ID do principio ativo |
| 47 | "created\_at" | "2023-05-16 16:37:11", | Data de cadastro da alergia |
| 48 | "deleted\_at" | null, | Exclusão do cadastro da alergia |
| 49 | "type" | "patient\_allergy", | Tipo do cadastro |
| 50 | "ingredient\_name" | "Dipirona", | Principio ativo alergico |
| 51 | "related" | "Dipirona magnésica, Dipirona sódica, Dipirona mono-hidratada" | Principio ativo relacionado |
| 52 | } |  | -- |
| 53 | ] |  | -- |
| 54 | }, |  | -- |
| 55 | "pacienteId" | null, | Não usado |
| 56 | "screening" | "{\"total\":\"1... | Metadado que possui informações de triagem do paciente, tais como alergia a medicamentos. |
| 57 | "additionalData" | [], | Dados adicionais informados pela integração |
| 58 | "workplace" | [], | Informações de local de atendimento |
| 59 | "prescriptionDate" | "16/05/2023", | Data da prescrição |
| 60 | "prescriptionUuid" | **uuid** | UUID da prescrição |
| 61 | "medicamentos" | [ | Array de medicamentos |
| 62 | { |  | -- |
| 63 | "id" | "c35746", | Id do medicamento na Memed |
| 64 | "nome" | "Texto Livre", | Nome do medicamento |
| 65 | "descricao" | "", | Principios ativos do medicamento |
| 66 | "posologia" | " Campo do texto/posologia ", | Posologia do medicamento |
| 67 | "quantidade" | 0 | Quantidade do medicamento |
| 68 | "unit" | "Uso Contínuo", | Unidade do medicamento (Uso continuo, comprimido, gotas) |
| 69 | "formas\_fisicas\_unidades\_id" | null, | ID da forma física |
| 70 | "composicao" | "", | Composição da fórmula |
| 71 | "fabricante" | "", | Fabricante do medicamento |
| 72 | "titularidade" | "", | Titularidade do medicamento (Biosimilar, Genérico, Referencia...) |
| 73 | "controle\_especial" | false, | Medicamento de controle especial |
| 74 | "alto\_custo" | false, | Medicamento de alto custo |
| 75 | "quantidade\_mes\_1" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 1 |
| 76 | "quantidade\_mes\_2" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 2 |
| 77 | "quantidade\_mes\_3" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 3 |
| 78 | "quantidade\_mes\_4" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 4 |
| 79 | "quantidade\_mes\_5" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 5 |
| 80 | "quantidade\_mes\_6" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 6 |
| 81 | "anamnese" | "", | Campo que contém informações relevantes provenientes da avaliação do paciente |
| 82 | "tratamento\_previo" | false, | Campo que informa se há tratamento prévio ou não |
| 83 | "descricao\_tratamento" | "", | Campo que informa qual é o tipo de tratamento que o paciente está |
| 84 | "data\_solicitacao" | null, | Campo que traz a data da solicitação |
| 85 | "cid\_id" | 0 | ID Memed do CID do medicamento |
| 86 | "receituario" | "", | Tipo de receituário da Memed (Antibiotico 2 vias...) |
| 87 | "exames\_sus\_codigo" | "", | Código SUS do exame |
| 88 | "exames\_tuss\_codigo" | "", | Código TUSS do exame |
| 89 | "tipo\_exame\_selecionado" | "", | Campo traz o tipo de exame selecionado |
| 90 | "catmat\_codigo\_br" | "", | Não usado |
| 91 | "catmat\_descricao" | "", | Não usado |
| 92 | "cid\_descricao" | "", | Não usado |
| 93 | "cid\_numero" | "", | Nº do CID do medicamento |
| 94 | "preco" | null, | Preço do medicamento |
| 95 | "real\_id" | 92951 | Id interno Memed para mapeamento unico |
| 96 | "tarja" | "", | Tarja do medicamento (Vermelha, livre...) |
| 97 | "tipo" | "custom", | Tipo de medicamento (Exame, Simples, custom) |
| 98 | "custom\_categoria" | null, | Categoria do texto livre prescrito |
| 99 | "exames" | [], | Exames associados ao medicamento LME |
| 100 | "fabricante\_id" | "", | ID do fabricante do medicamento |
| 101 | "sanitized\_posology" | "Campo do texto/posologia", | Posologia do medicamento em string |
| 102 | "form\_units" | [], | Array de unidades do medicamento (Capsulas, gotas...) |
| 103 | "psp" | { | Array de PSP |
| 104 | "active" | false, | Se preço indicado pela industria está ativo |
| 105 | "tagline" | null, | Não usado |
| 106 | "link" | null | Não usado |
| 107 | }, |  | -- |
| 108 | "via" | null, | Indicação de uso do medicamento (Oral...) |
| 109 | "receituario\_id" | null, | ID identificador do receituario (Simples, 2-vias especial...) |
| 110 | "descontinuado" | false, | Se medicamento é descontinuado ou não |
| 111 | "status" | "", | Não usado |
| 112 | "categoria\_posologia" | "", | Não usado |
| 113 | "origem" | "Prescrição", | Origem do medicamento |
| 114 | "cid" | "c638", | CID associado |
| 115 | "mostrarDescricao" | false, | Organização interna do FrontEnd Memed (Não usado) |
| 116 | "subtitulo" | "", | Subtitulo do medicamento na prescrição |
| 117 | "titulo" | "Texto Livre" | Nome do medicamento |
| 118 | }, |  | -- |
| 119 | { |  | -- |
| 120 | "id" | "a510600605115312", | Id do medicamento na Memed |
| 121 | "nome" | "Amoxil 500mg, Cápsula (15un)", | Nome do medicamento |
| 122 | "descricao" | "Amoxicilina 500mg", | Principios ativos do medicamento |
| 123 | "posologia" | " 1 por dia ", | Posologia do medicamento |
| 124 | "quantidade" | 1 | Quantidade do medicamento |
| 125 | "unit" | "embalagem", | Unidade do medicamento prescrito(Uso continuo, comprimido, gotas) |
| 126 | "formas\_fisicas\_unidades\_id" | null, | ID da forma física |
| 127 | "composicao" | "", | Composição da fórmula |
| 128 | "fabricante" | "GSK - Glaxosmithkline", | Fabricante do medicamento |
| 129 | "titularidade" | "Referência", | Titularidade do medicamento (Biosimilar, Genérico, Referencia...) |
| 130 | "controle\_especial" | true, | Medicamento de controle especial |
| 131 | "alto\_custo" | false, | Medicamento de alto custo |
| 132 | "quantidade\_mes\_1" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 1 |
| 133 | "quantidade\_mes\_2" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 2 |
| 134 | "quantidade\_mes\_3" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 3 |
| 135 | "quantidade\_mes\_4" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 4 |
| 136 | "quantidade\_mes\_5" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 5 |
| 137 | "quantidade\_mes\_6" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 6 |
| 138 | "anamnese" | "", | Campo que contém informações relevantes provenientes da avaliação do paciente |
| 139 | "tratamento\_previo" | false, | Campo que informa se há tratamento prévio ou não |
| 140 | "descricao\_tratamento" | "", | Campo que informa qual é o tipo de tratamento que o paciente está |
| 141 | "data\_solicitacao" | null, | Campo que traz a data da solicitação |
| 142 | "cid\_id" | 0 | ID Memed do CID do medicamento |
| 143 | "receituario" | "Antibióticos-2 vias", | Tipo de receituário da Memed (Antibiotico 2 vias...) |
| 144 | "exames\_sus\_codigo" | "", | Código SUS do exame |
| 145 | "exames\_tuss\_codigo" | "", | Código TUSS do exame |
| 146 | "tipo\_exame\_selecionado" | "", | Campo traz o tipo de exame selecionado |
| 147 | "catmat\_codigo\_br" | "", | Não usado |
| 148 | "catmat\_descricao" | "", | Não usado |
| 149 | "cid\_descricao" | "", | Não usado |
| 150 | "cid\_numero" | "", | Nº do CID do medicamento |
| 151 | "preco" | 48 | Preço do medicamento |
| 152 | "real\_id" | 92952 | Id interno Memed para mapeamento unico |
| 153 | "tarja" | "Vermelho", | Tarja do medicamento (Vermelho, livre...) |
| 154 | "tipo" | "alopático", | Tipo de medicamento (Exame, Alopático, custom) |
| 155 | "custom\_categoria" | null, | Categoria do texto livre prescrito |
| 156 | "exames" | [], | Exames associados ao medicamento LME |
| 157 | "fabricante\_id" | "f100", | ID do fabricante do medicamento |
| 158 | "sanitized\_posology" | "1 por dia ", | Posologia do medicamento em string |
| 159 | "form\_units" | [ | Array de unidades do medicamento (Capsulas, gotas...) |
| 160 | { |  | -- |
| 161 | "id" | 16 | ID da forma do medicamento Memed |
| 162 | "singular" | "Cápsula", | Forma no singular |
| 163 | "plural" | "Cápsulas", | Forma no plural |
| 164 | "type" | "formas-fisicas-unidades" | Tipo da forma na Memed |
| 165 | } |  | -- |
| 166 | ], |  | -- |
| 167 | "psp" | { | Array de PSP |
| 168 | "active" | false, | Se preço indicado pela industria está ativo |
| 169 | "tagline" | null, | Não usado |
| 170 | "link" | null | Não usado |
| 171 | }, |  | -- |
| 172 | "via" | null, | Indicação de uso do medicamento (Oral...) |
| 173 | "receituario\_id" | 11 | ID identificador do receituario (Simples, 2-vias especial...) |
| 174 | "descontinuado" | false, | Se medicamento é descontinuado ou não |
| 175 | "status" | "", | Não usado |
| 176 | "categoria\_posologia" | "", | Não usado |
| 177 | "origem" | "Prescrição", | Origem do medicamento |
| 178 | "cid" | "c646", | CID associado |
| 179 | "mostrarDescricao" | true, | Organização interna do FrontEnd Memed (Não usado) |
| 180 | "subtitulo" | ", Cápsula (15un)", | Subtitulo do medicamento na prescrição |
| 181 | "titulo" | "Amoxil 500mg" | Nome do medicamento |
| 182 | }, |  | -- |
| 183 | { |  | -- |
| 184 | "id" | "w6589", | Id do medicamento na Memed |
| 185 | "nome" | "Dipirona sódica 500mg, Comprimido", | Nome do medicamento |
| 186 | "descricao" | "Dipirona sódica 500mg", | Principios ativos do medicamento |
| 187 | "posologia" | " Tomar 1 comprimido até de 6 em 6 horas, se necessário. ", | Posologia do medicamento |
| 188 | "quantidade" | null, | Quantidade do medicamento |
| 189 | "unit" | null, | Unidade do medicamento prescrito(Uso continuo, comprimido, gotas) |
| 190 | "formas\_fisicas\_unidades\_id" | null, | ID da forma física |
| 191 | "composicao" | "", | Composição da fórmula |
| 192 | "fabricante" | "", | Fabricante do medicamento |
| 193 | "titularidade" | "—", | Titularidade do medicamento (Biosimilar, Genérico, Referencia...) |
| 194 | "controle\_especial" | false, | Medicamento de controle especial |
| 195 | "alto\_custo" | false, | Medicamento de alto custo |
| 196 | "quantidade\_mes\_1" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 1 |
| 197 | "quantidade\_mes\_2" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 2 |
| 198 | "quantidade\_mes\_3" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 3 |
| 199 | "quantidade\_mes\_4" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 4 |
| 200 | "quantidade\_mes\_5" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 5 |
| 201 | "quantidade\_mes\_6" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 6 |
| 202 | "anamnese" | "", | Campo que contém informações relevantes provenientes da avaliação do paciente |
| 203 | "tratamento\_previo" | false, | Campo que informa se há tratamento prévio ou não |
| 204 | "descricao\_tratamento" | "", | Campo que informa qual é o tipo de tratamento que o paciente está |
| 205 | "data\_solicitacao" | null, | Campo que traz a data da solicitação |
| 206 | "cid\_id" | 0 | ID Memed do CID do medicamento |
| 207 | "receituario" | "Simples", | Tipo de receituário da Memed (Antibiotico 2 vias...) |
| 208 | "exames\_sus\_codigo" | "", | Código SUS do exame |
| 209 | "exames\_tuss\_codigo" | "", | Código TUSS do exame |
| 210 | "tipo\_exame\_selecionado" | "", | Campo traz o tipo de exame selecionado |
| 211 | "catmat\_codigo\_br" | "BR0267203", | Não usado |
| 212 | "catmat\_descricao" | "DIPIRONA SÓDICA, 500 MG", | Não usado |
| 213 | "cid\_descricao" | "", | Não usado |
| 214 | "cid\_numero" | "", | Nº do CID do medicamento |
| 215 | "preco" | 0 | Preço do medicamento |
| 216 | "real\_id" | 92953 | Id interno Memed para mapeamento unico |
| 217 | "tarja" | "Livre", | Tarja do medicamento (Vermelho, livre...) |
| 218 | "tipo" | "white-label", | Tipo de medicamento (Exame, Alopático, custom) |
| 219 | "custom\_categoria" | null, | Categoria do texto livre prescrito |
| 220 | "exames" | [], | Exames associados ao medicamento LME |
| 221 | "fabricante\_id" | "", | ID do fabricante do medicamento |
| 222 | "sanitized\_posology" | "Tomar 1 comprimido até de 6 em 6 horas, se necessário.", | Posologia do medicamento em string |
| 223 | "form\_units" | [ | Array de unidades do medicamento (Capsulas, gotas...) |
| 224 | { |  | -- |
| 225 | "id" | 27 | ID da forma do medicamento Memed |
| 226 | "singular" | "Comprimido", | Forma no singular |
| 227 | "plural" | "Comprimidos", | Forma no plural |
| 228 | "type" | "formas-fisicas-unidades" | Tipo da forma na Memed |
| 229 | } |  | -- |
| 230 | ], |  | -- |
| 231 | "psp" | { | Array de PSP |
| 232 | "active" | false, | Se preço indicado pela industria está ativo |
| 233 | "tagline" | null, | Não usado |
| 234 | "link" | null | Não usado |
| 235 | }, |  | -- |
| 236 | "via" | null, | Indicação de uso do medicamento (Oral...) |
| 237 | "receituario\_id" | 12 | ID identificador do receituario (Simples, 2-vias especial...) |
| 238 | "descontinuado" | false, | Se medicamento é descontinuado ou não |
| 239 | "status" | "", | Não usado |
| 240 | "categoria\_posologia" | "", | Não usado |
| 241 | "origem" | "Prescrição", | Origem do medicamento |
| 242 | "cid" | "c648", | CID associado |
| 243 | "mostrarDescricao" | false, | Organização interna do FrontEnd Memed (Não usado) |
| 244 | "subtitulo" | ", Comprimido", | Subtitulo do medicamento na prescrição |
| 245 | "titulo" | "Dipirona sódica 500mg" | Nome do medicamento |
| 246 | }, |  | -- |
| 247 | { |  | -- |
| 248 | "id" | "e166", | Id do medicamento na Memed |
| 249 | "nome" | "Raio X simples de abdômen", | Nome do medicamento/exame |
| 250 | "descricao" | null, | Principios ativos do medicamento |
| 251 | "posologia" | " HTML da indicação ", | Posologia do medicamento/indicação do exame |
| 252 | "quantidade" | null, | Quantidade do medicamento |
| 253 | "unit" | null, | Unidade do medicamento prescrito(Uso continuo, comprimido, gotas) |
| 254 | "formas\_fisicas\_unidades\_id" | null, | ID da forma física |
| 255 | "composicao" | "", | Composição da fórmula |
| 256 | "fabricante" | "", | Fabricante do medicamento |
| 257 | "titularidade" | "", | Titularidade do medicamento (Biosimilar, Genérico, Referencia...) |
| 258 | "controle\_especial" | false, | Medicamento de controle especial |
| 259 | "alto\_custo" | false, | Medicamento de alto custo |
| 260 | "quantidade\_mes\_1" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 1 |
| 261 | "quantidade\_mes\_2" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 2 |
| 262 | "quantidade\_mes\_3" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 3 |
| 263 | "quantidade\_mes\_4" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 4 |
| 264 | "quantidade\_mes\_5" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 5 |
| 265 | "quantidade\_mes\_6" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 6 |
| 266 | "anamnese" | "", | Campo que contém informações relevantes provenientes da avaliação do paciente |
| 267 | "tratamento\_previo" | false, | Campo que informa se há tratamento prévio ou não |
| 268 | "descricao\_tratamento" | "", | Campo que informa qual é o tipo de tratamento que o paciente está |
| 269 | "data\_solicitacao" | null, | Campo que traz a data da solicitação |
| 270 | "cid\_id" | 0 | ID Memed do CID do medicamento |
| 271 | "receituario" | "Simples", | Tipo de receituário da Memed (Antibiotico 2 vias...) |
| 272 | "exames\_sus\_codigo" | "", | Código SUS do exame |
| 273 | "exames\_tuss\_codigo" | "", | Código TUSS do exame |
| 274 | "tipo\_exame\_selecionado" | "", | Campo traz o tipo de exame selecionado |
| 275 | "catmat\_codigo\_br" | "", | Não usado |
| 276 | "catmat\_descricao" | "", | Não usado |
| 277 | "cid\_descricao" | "", | Não usado |
| 278 | "cid\_numero" | "", | Nº do CID do medicamento |
| 279 | "preco" | 0 | Preço do medicamento |
| 280 | "real\_id" | 92954 | Id interno Memed para mapeamento unico |
| 281 | "tarja" | "", | Tarja do medicamento (Vermelho, livre...) |
| 282 | "tipo" | "exame", | Tipo de medicamento (Exame, Alopático, custom) |
| 283 | "custom\_categoria" | null, | Categoria do texto livre prescrito |
| 284 | "exames" | [], | Exames associados ao medicamento LME |
| 285 | "fabricante\_id" | "fe1", | ID do fabricante do medicamento |
| 286 | "sanitized\_posology" | "HTML da indicação", | Posologia do medicamento em string |
| 287 | "form\_units" | [], | Array de unidades do medicamento (Capsulas, gotas...) |
| 288 | "psp" | { | Array de PSP |
| 289 | "active" | false, | Se preço indicado pela industria está ativo |
| 290 | "tagline" | null, | Não usado |
| 291 | "link" | null | Não usado |
| 292 | }, |  | -- |
| 293 | "via" | null, | Indicação de uso do medicamento (Oral...) |
| 294 | "receituario\_id" | null, | ID identificador do receituario (Simples, 2-vias especial...) |
| 295 | "descontinuado" | false, | Se medicamento/exame é descontinuado ou não |
| 296 | "status" | "", | Não usado |
| 297 | "categoria\_posologia" | "", | Não usado |
| 298 | "origem" | "Prescrição", | Origem do medicamento |
| 299 | "cid" | "c650", | CID associado |
| 300 | "mostrarDescricao" | false, | Organização interna do FrontEnd Memed (Não usado) |
| 301 | "subtitulo" | "", | Subtitulo do medicamento na prescrição |
| 302 | "titulo" | "Raio X simples de abdômen" | Nome do medicamento |
| 303 | }, |  | -- |
| 304 | { |  | -- |
| 305 | "id" | "m9103", | Id do medicamento na Memed |
| 306 | "nome" | "Intolerância a lactose, inulina (1un)", | Nome do medicamento |
| 307 | "descricao" | "Lactobacillus reuteri 1blh + Lactobacillus casei 2blh + Inulina q.s.p. 1un", | Principios ativos do medicamento |
| 308 | "posologia" | " Tomar 1 vez ao dia - Manipulado - Formula ", | Posologia do medicamento |
| 309 | "quantidade" | 1 | Quantidade do medicamento |
| 310 | "unit" | "embalagem", | Unidade do medicamento prescrito(Uso continuo, comprimido, gotas) |
| 311 | "formas\_fisicas\_unidades\_id" | null, | ID da forma física |
| 312 | "composicao" | "Lactobacillus reuteri .................................................. | Composição da fórmula |
| 313 | "fabricante" | "", | Fabricante do medicamento |
| 314 | "titularidade" | "Manipulado", | Titularidade do medicamento (Biosimilar, Genérico, Referencia...) |
| 315 | "controle\_especial" | false, | Medicamento de controle especial |
| 316 | "alto\_custo" | false, | Medicamento de alto custo |
| 317 | "quantidade\_mes\_1" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 1 |
| 318 | "quantidade\_mes\_2" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 2 |
| 319 | "quantidade\_mes\_3" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 3 |
| 320 | "quantidade\_mes\_4" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 4 |
| 321 | "quantidade\_mes\_5" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 5 |
| 322 | "quantidade\_mes\_6" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 6 |
| 323 | "anamnese" | "", | Campo que contém informações relevantes provenientes da avaliação do paciente |
| 324 | "tratamento\_previo" | false, | Campo que informa se há tratamento prévio ou não |
| 325 | "descricao\_tratamento" | "", | Campo que informa qual é o tipo de tratamento que o paciente está |
| 326 | "data\_solicitacao" | null, | Campo que traz a data da solicitação |
| 327 | "cid\_id" | 0 | ID Memed do CID do medicamento |
| 328 | "receituario" | "Simples", | Tipo de receituário da Memed (Antibiotico 2 vias...) |
| 329 | "exames\_sus\_codigo" | "", | Código SUS do exame |
| 330 | "exames\_tuss\_codigo" | "", | Código TUSS do exame |
| 331 | "tipo\_exame\_selecionado" | "", | Campo traz o tipo de exame selecionado |
| 332 | "catmat\_codigo\_br" | "", | Não usado |
| 333 | "catmat\_descricao" | "", | Não usado |
| 334 | "cid\_descricao" | "", | Não usado |
| 335 | "cid\_numero" | "", | Nº do CID do medicamento |
| 336 | "preco" | 0 | Preço do medicamento |
| 337 | "real\_id" | 92955 | Id interno Memed para mapeamento unico |
| 338 | "tarja" | "", | Tarja do medicamento (Vermelho, livre...) |
| 339 | "tipo" | "manipulado", | Tipo de medicamento (Exame, Alopático, custom) |
| 340 | "custom\_categoria" | null, | Categoria do texto livre prescrito |
| 341 | "exames" | [], | Exames associados ao medicamento LME |
| 342 | "fabricante\_id" | "f347", | ID do fabricante do medicamento |
| 343 | "sanitized\_posology" | "Tomar 1 vez ao dia - Manipulado - Formula", | Posologia do medicamento em string |
| 344 | "form\_units" | [ | Array de unidades do medicamento (Capsulas, gotas...) |
| 345 | { |  | -- |
| 346 | "id" | 294 | ID da forma do medicamento Memed |
| 347 | "singular" | "Frasco", | Forma no singular |
| 348 | "plural" | "Frascos", | Forma no plural |
| 349 | "type" | "formas-fisicas-unidades" | Tipo da forma na Memed |
| 350 | } |  | -- |
| 351 | ], |  | -- |
| 352 | "psp" | { | Array de PSP |
| 353 | "active" | false, | Se preço indicado pela industria está ativo |
| 354 | "tagline" | null, | Não usado |
| 355 | "link" | null | Não usado |
| 356 | }, |  | -- |
| 357 | "via" | "21", | Indicação de uso do medicamento (Oral...) |
| 358 | "receituario\_id" | 12 | ID identificador do receituario (Simples, 2-vias especial...) |
| 359 | "descontinuado" | false, | Se medicamento é descontinuado ou não |
| 360 | "status" | "", | Não usado |
| 361 | "categoria\_posologia" | "", | Não usado |
| 362 | "origem" | "Prescrição", | Origem do medicamento |
| 363 | "cid" | "c652", | CID associado |
| 364 | "mostrarDescricao" | false, | Organização interna do FrontEnd Memed (Não usado) |
| 365 | "subtitulo" | ", inulina (1un)", | Subtitulo do medicamento na prescrição |
| 366 | "titulo" | "Fórmula" | Nome do medicamento/exame/formula |
| 367 | }, |  | -- |
| 368 | { |  | -- |
| 369 | "id" | "p8", | Id do medicamento na Memed |
| 370 | "nome" | "Similac 2", | Nome do medicamento |
| 371 | "descricao" | "Carboidratos 55g, Proteínas 12g, Gorduras totais ... | Principios ativos do medicamento |
| 372 | "posologia" | " Tomar 1 vez ao dia ", | Posologia do medicamento |
| 373 | "quantidade" | 1 | Quantidade do medicamento |
| 374 | "unit" | "embalagem", | Unidade do medicamento prescrito(Uso continuo, comprimido, gotas) |
| 375 | "formas\_fisicas\_unidades\_id" | null, | ID da forma física |
| 376 | "composicao" | "", | Composição da fórmula |
| 377 | "fabricante" | "Alcon", | Fabricante do medicamento |
| 378 | "titularidade" | "Categoria 3", | Titularidade do medicamento (Biosimilar, Genérico, Referencia...) |
| 379 | "controle\_especial" | false, | Medicamento de controle especial |
| 380 | "alto\_custo" | false, | Medicamento de alto custo |
| 381 | "quantidade\_mes\_1" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 1 |
| 382 | "quantidade\_mes\_2" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 2 |
| 383 | "quantidade\_mes\_3" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 3 |
| 384 | "quantidade\_mes\_4" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 4 |
| 385 | "quantidade\_mes\_5" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 5 |
| 386 | "quantidade\_mes\_6" | null, | Campo que informa a quantidade por mês que o medicamento foi prescrito no mês 6 |
| 387 | "anamnese" | "", | Campo que contém informações relevantes provenientes da avaliação do paciente |
| 388 | "tratamento\_previo" | false, | Campo que informa se há tratamento prévio ou não |
| 389 | "descricao\_tratamento" | "", | Campo que informa qual é o tipo de tratamento que o paciente está |
| 390 | "data\_solicitacao" | null, | Campo que traz a data da solicitação |
| 391 | "cid\_id" | 0 | ID Memed do CID do medicamento |
| 392 | "receituario" | "Simples", | Tipo de receituário da Memed (Antibiotico 2 vias...) |
| 393 | "exames\_sus\_codigo" | "", | Código SUS do exame |
| 394 | "exames\_tuss\_codigo" | "", | Código TUSS do exame |
| 395 | "tipo\_exame\_selecionado" | "", | Campo traz o tipo de exame selecionado |
| 396 | "catmat\_codigo\_br" | "", | Não usado |
| 397 | "catmat\_descricao" | "", | Não usado |
| 398 | "cid\_descricao" | "", | Não usado |
| 399 | "cid\_numero" | "", | Nº do CID do medicamento |
| 400 | "preco" | 23 | Preço do medicamento |
| 401 | "real\_id" | 92956 | Id interno Memed para mapeamento unico |
| 402 | "tarja" | "", | Tarja do medicamento (Vermelho, livre...) |
| 403 | "tipo" | "periférico", | Tipo de medicamento (Exame, Alopático, custom) |
| 404 | "custom\_categoria" | null, | Categoria do texto livre prescrito |
| 405 | "exames" | [], | Exames associados ao medicamento LME |
| 406 | "fabricante\_id" | "f9", | ID do fabricante do medicamento |
| 407 | "sanitized\_posology" | "Tomar 1 vez ao dia", | Posologia do medicamento em string |
| 408 | "form\_units" | [], | Array de unidades do medicamento (Capsulas, gotas...) |
| 409 | "psp" | { | Array de PSP |
| 410 | "active" | false, | Se preço indicado pela industria está ativo |
| 411 | "tagline" | null, | Não usado |
| 412 | "link" | null | Não usado |
| 413 | }, |  | -- |
| 414 | "via" | null, | Indicação de uso do medicamento (Oral...) |
| 415 | "receituario\_id" | null, | ID identificador do receituario (Simples, 2-vias especial...) |
| 416 | "descontinuado" | false, | Se medicamento é descontinuado ou não |
| 417 | "status" | "", | Não usado |
| 418 | "categoria\_posologia" | "", | Não usado |
| 419 | "origem" | "Prescrição", | Origem do medicamento |
| 420 | "cid" | "c655", | CID associado |
| 421 | "mostrarDescricao" | false, | Organização interna do FrontEnd Memed (Não usado) |
| 422 | "subtitulo" | "", | Subtitulo do medicamento na prescrição |
| 423 | "titulo" | "Similac 2" | Nome do medicamento/exame/formula |
| 424 | } |  | -- |
| 425 | ], |  | -- |
| 426 | "reprint" | false, | Primeira emissão ou se reimpresso |
| 427 | "prescriptionTimer" | { | Array de timer da prescrição |
| 428 | "hasStarted" | true, | ID da forma física |
| 429 | "startTime" | 1684265915330 | Não usado |
| 430 | }, |  | -- |
| 431 | "id" | **id** | ID da prescrição |
| 432 | "medicos\_id" | **id** | Id do prescritor na Memed |
| 433 | "prescricao\_editada\_id" | null, | Não usado |
| 434 | "lme" | false, | Se a prescrição é LME |
| 435 | "opcoes\_receituario\_id" | 1 | Opção de receituráio usada na impressão |
| 436 | "nome\_medico" | "Médico teste", | Nome do prescritor |
| 437 | "endereco\_medico" | "Rua Arthur Prado, 513", | Endereço do prescritor |
| 438 | "cidade\_medico" | "", | Cidade do prescritor |
| 439 | "telefone\_medico" | "(11) 96046-7098", | Telefone do prescritor |
| 440 | "checksum" | null, | Não usado |
| 441 | "created\_at" | "16/05/2023 16:37:17", | Data de criação da prescrição |
| 442 | "source" | "", | Não usado |
| 443 | "signed" | 0 | Se documento está assinado digitalmente |
| 444 | "renew" | 0 | Não usado |
| 445 | "version" | 1 | Versão usada para geração da prescrição |
| 446 | "data" | "16/05/2023", | Data da prescrição |
| 447 | "horario" | "16:37:17", | Horario da prescrição |
| 448 | "print\_config" | "{\"simple\":{\"all\":{\"print\":true,\"showDate\":true,\"copies\":{\"16\/0... | Configurações de impressão |
| 449 | "prescriptionDateOriginal" | "2023-05-16 16:37:17", | Data da prescrição Original |
| 450 | "clinica" | null, | Nome da clinica definida no módulo |
| 451 | "medicos" | { | Array de prescritores |
| 452 | "id" | "**id**", | ID do prescritor na Memed |
| 453 | "especialidades\_id" | 59 | ID da especialidade na Memed |
| 454 | "cidades\_id" | 5213 | ID da cidade na memed |
| 455 | "nome\_completo" | "prescritor teste", | Nome do prescritor |
| 456 | "cns" | "1234567890", | CNS do prescritor |
| 457 | "crm" | "0000", | CRM do prescritor |
| 458 | "uf" | "SP", | Estado do prescritor |
| 459 | "estudante" | 0 | Se estudante |
| 460 | "telefone" | "(11) 96046-7098", | Telefone do prescritor |
| 461 | "type" | "medicos", | Tipo do cadastro |
| 462 | "cpf" | "33643594070" | CPF do prescritor |
| 463 | }, |  | -- |
| 464 | "documents" | [ | Array de documentos |
| 465 | { |  | -- |
| 466 | "id" | **id** | ID do documento gerado |
| 467 | "uuid" | **uuid** | UUID do documento gerado |
| 468 | "type" | "full", | Tipo do documento gerado |
| 469 | "status" | "saved", | Status do documento |
| 470 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 471 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 472 | "prescription\_origin" | null, | Não usado |
| 473 | "prescription\_item\_id" | null, | Não usado |
| 474 | "signed" | 0 | Se documento está assinado digitalmente |
| 475 | "signed\_by" | null, | Não usado |
| 476 | "file\_name" | "**uuid**\_FULL.pdf", | Nome do documento |
| 477 | "file\_size" | null, | Tamanho do documento |
| 478 | "file\_hash" | **uuid** | Hash do documento |
| 479 | "keywords" | { | Array de keywords |
| 480 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 481 | "uuid" | **uuid** | UUID do documento gerado |
| 482 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 483 | }, |  | -- |
| 484 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 485 | "updated\_at" | "2023-05-16 16:39:04", | Ultima atualização do documento |
| 486 | "deleted\_at" | null | Data de exclusão do documento |
| 487 | }, |  | -- |
| 488 | { |  | -- |
| 489 | "id" | **id** | ID do documento gerado |
| 490 | "uuid" | **uuid** | UUID do documento gerado |
| 491 | "type" | "individual", | Tipo do documento gerado |
| 492 | "status" | "saved", | Status do documento |
| 493 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 494 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 495 | "prescription\_origin" | null, | Não usado |
| 496 | "prescription\_item\_id" | **id** | Não usado |
| 497 | "signed" | 0 | Se documento está assinado digitalmente |
| 498 | "signed\_by" | null, | Não usado |
| 499 | "file\_name" | **uuid** | Nome do documento |
| 500 | "file\_size" | null, | Tamanho do documento |
| 501 | "file\_hash" | **uuid** | Hash do documento |
| 502 | "keywords" | { | Array de keywords |
| 503 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 504 | "uuid" | **uuid** | UUID do documento gerado |
| 505 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 506 | }, |  | -- |
| 507 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 508 | "updated\_at" | "2023-05-16 16:39:04", | Ultima atualização do documento |
| 509 | "deleted\_at" | null | Data de exclusão do documento |
| 510 | }, |  | -- |
| 511 | { |  | -- |
| 512 | "id" | **id** | ID do documento gerado |
| 513 | "uuid" | **uuid** | UUID do documento gerado |
| 514 | "type" | "individual", | Tipo do documento gerado |
| 515 | "status" | "saved", | Status do documento |
| 516 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 517 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 518 | "prescription\_origin" | null, | Não usado |
| 519 | "prescription\_item\_id" | **id** | Não usado |
| 520 | "signed" | 0 | Se documento está assinado digitalmente |
| 521 | "signed\_by" | null, | Não usado |
| 522 | "file\_name" | "**uuid**.pdf", | Nome do documento |
| 523 | "file\_size" | null, | Tamanho do documento |
| 524 | "file\_hash" | **uuid** | Hash do documento |
| 525 | "keywords" | { | Array de keywords |
| 526 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 527 | "uuid" | **uuid** | UUID do documento gerado |
| 528 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 529 | }, |  | -- |
| 530 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 531 | "updated\_at" | "2023-05-16 16:39:04", | Ultima atualização do documento |
| 532 | "deleted\_at" | null | Data de exclusão do documento |
| 533 | }, |  | -- |
| 534 | { |  | -- |
| 535 | "id" | **id** | ID do documento gerado |
| 536 | "uuid" | **uuid** | UUID do documento gerado |
| 537 | "type" | "individual", | Tipo do documento gerado |
| 538 | "status" | "saved", | Status do documento |
| 539 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 540 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 541 | "prescription\_origin" | null, | Não usado |
| 542 | "prescription\_item\_id" | **id** | Não usado |
| 543 | "signed" | 0 | Se documento está assinado digitalmente |
| 544 | "signed\_by" | null, | Não usado |
| 545 | "file\_name" | "**uuid**.pdf", | Nome do documento |
| 546 | "file\_size" | null, | Tamanho do documento |
| 547 | "file\_hash" | **uuid** | Hash do documento |
| 548 | "keywords" | { | Array de keywords |
| 549 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 550 | "uuid" | **uuid** | UUID do documento gerado |
| 551 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 552 | }, |  | -- |
| 553 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 554 | "updated\_at" | "2023-05-16 16:39:04", | Ultima atualização do documento |
| 555 | "deleted\_at" | null | Data de exclusão do documento |
| 556 | }, |  | -- |
| 557 | { |  | -- |
| 558 | "id" | **id** | ID do documento gerado |
| 559 | "uuid" | **uuid** | UUID do documento gerado |
| 560 | "type" | "individual", | Tipo do documento gerado |
| 561 | "status" | "saved", | Status do documento |
| 562 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 563 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 564 | "prescription\_origin" | null, | Não usado |
| 565 | "prescription\_item\_id" | **id** | Não usado |
| 566 | "signed" | 0 | Se documento está assinado digitalmente |
| 567 | "signed\_by" | null, | Não usado |
| 568 | "file\_name" | "**uuid**.pdf", | Nome do documento |
| 569 | "file\_size" | null, | Tamanho do documento |
| 570 | "file\_hash" | **uuid** | Hash do documento |
| 571 | "keywords" | { | Array de keywords |
| 572 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 573 | "uuid" | **uuid** | UUID do documento gerado |
| 574 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 575 | }, |  | -- |
| 576 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 577 | "updated\_at" | "2023-05-16 16:39:04", | Ultima atualização do documento |
| 578 | "deleted\_at" | null | Data de exclusão do documento |
| 579 | }, |  | -- |
| 580 | { |  | -- |
| 581 | "id" | **id** | ID do documento gerado |
| 582 | "uuid" | **uuid** | UUID do documento gerado |
| 583 | "type" | "individual", | Tipo do documento gerado |
| 584 | "status" | "saved", | Status do documento |
| 585 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 586 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 587 | "prescription\_origin" | null, | Não usado |
| 588 | "prescription\_item\_id" | **id** | Não usado |
| 589 | "signed" | 0 | Se documento está assinado digitalmente |
| 590 | "signed\_by" | null, | Não usado |
| 591 | "file\_name" | "**uuid**.pdf", | Nome do documento |
| 592 | "file\_size" | null, | Tamanho do documento |
| 593 | "file\_hash" | **uuid** | Hash do documento |
| 594 | "keywords" | { | Array de keywords |
| 595 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 596 | "uuid" | **uuid** | UUID do documento gerado |
| 597 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 598 | }, |  | -- |
| 599 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 600 | "updated\_at" | "2023-05-16 16:39:05", | Ultima atualização do documento |
| 601 | "deleted\_at" | null | Data de exclusão do documento |
| 602 | }, |  | -- |
| 603 | { |  | -- |
| 604 | "id" | **id** | ID do documento gerado |
| 605 | "uuid" | **uuid** | UUID do documento gerado |
| 606 | "type" | "individual", | Tipo do documento gerado |
| 607 | "status" | "saved", | Status do documento |
| 608 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 609 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 610 | "prescription\_origin" | null, | Não usado |
| 611 | "prescription\_item\_id" | **id** | Não usado |
| 612 | "signed" | 0 | Se documento está assinado digitalmente |
| 613 | "signed\_by" | null, | Não usado |
| 614 | "file\_name" | "**uuid**.pdf", | Nome do documento |
| 615 | "file\_size" | null, | Tamanho do documento |
| 616 | "file\_hash" | **uuid** | Hash do documento |
| 617 | "keywords" | { | Array de keywords |
| 618 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 619 | "uuid" | **uuid** | UUID do documento gerado |
| 620 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 621 | }, |  | -- |
| 622 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 623 | "updated\_at" | "2023-05-16 16:39:05", | Ultima atualização do documento |
| 624 | "deleted\_at" | null | Data de exclusão do documento |
| 625 | }, |  | -- |
| 626 | { |  | -- |
| 627 | "id" | **id** | ID do documento gerado |
| 628 | "uuid" | **uuid** | UUID do documento gerado |
| 629 | "type" | "signature", | Tipo do documento gerado |
| 630 | "status" | "saved", | Status do documento |
| 631 | "prescription\_id" | **id** | ID da prescrição associado ao documento |
| 632 | "prescription\_uuid" | **uuid** | UUID da prescrição associado ao documento |
| 633 | "prescription\_origin" | null, | Não usado |
| 634 | "prescription\_item\_id" | null, | Não usado |
| 635 | "signed" | 0 | Se documento está assinado digitalmente |
| 636 | "signed\_by" | null, | Não usado |
| 637 | "file\_name" | "**uuid**\_SIGNATURE.pdf", | Nome do documento |
| 638 | "file\_size" | null, | Tamanho do documento |
| 639 | "file\_hash" | null, | Hash do documento |
| 640 | "keywords" | { | Array de keywords |
| 641 | "prescriptionUuid" | **uuid** | UUID da prescrição associado ao documento |
| 642 | "uuid" | **uuid** | UUID do documento gerado |
| 643 | "date" | "16/05/2023 16:37:17" | Data da emissão da prescrição |
| 644 | }, |  | -- |
| 645 | "created\_at" | "2023-05-16 16:38:10", | Criação do documento |
| 646 | "updated\_at" | "2023-05-16 16:39:05", | Ultima atualização do documento |
| 647 | "deleted\_at" | null | Data de exclusão do documento |
| 648 | } |  | -- |
| 649 | ] |  | -- |
| 650 | }, |  | -- |
| 651 | "reimpressao" | true | Se documento é uma reimpressão |
| 652 | } |  | -- |
