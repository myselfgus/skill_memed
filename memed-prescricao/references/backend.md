# Backend / API REST da Memed

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- Par de Chaves — `https://doc.memed.com.br/docs/backend/chaves`
- Configurações — `https://doc.memed.com.br/docs/backend/configuracoes`
- Impressão — `https://doc.memed.com.br/docs/backend/impressao`
- Prescrição — `https://doc.memed.com.br/docs/backend/prescricao`
- Protocolos — `https://doc.memed.com.br/docs/backend/protocolos`
- Usuário Prescritor — `https://doc.memed.com.br/docs/backend/usuario-prescritor`

---

<!-- fonte: https://doc.memed.com.br/docs/backend/chaves -->
## Par de Chaves

### Sobre pares de chaves

Os pares de chave são o principal atributo para realizar a integração Memed, sem ele, não é possível cadastrar um prescritor e inciar as integrações com a plataforma de fato. A seguir, você pode usar o nosso endpoint de validação para entender se a chave de produção recebida é valida para realizar uma integração.

#### Consultar se o par de chaves está ativo e funcional:

```
PATCH: MEMED_API_URL/v1/sinapse-prescricao/check-key
```

- cURL
- Sucesso
- Erro

**Requisição GET**  
Query Parameters:

- api-key
- secret-key

Abaixo segue um **exemplo** da requisição na api apontando para o ambiente de **integrations** (QA/Testes).  
Nessa rota é possivel consultar se a chave está funcional.

**Atenção**

Para ambientes de **produção** a url deve ser: [https://api.memed.com.br/](https://api.memed.com.br/)

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/check-key?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

**Retorno: Http status 200**

```
{
    "success": [
        {
            "code": "chave-valida",
            "title": "Sucesso",
            "detail": "Código de acesso valido"
        }
    ]
}
```

**Retorno: Http status 401 - UNAUTHORIZED**

```
{
    "errors": [
        {
            "code": "token-invalido",
            "title": "Erro",
            "detail": "Token vazio"
        }
    ]
}
```

---

<!-- fonte: https://doc.memed.com.br/docs/backend/configuracoes -->
## Configurações

As configurações aqui propostas são apenas sugestões para facilitar a sua integração com a prescrição digital Memed.

**Dica**

Aproveite para ver detalhes das configurações do [**frontend**](https://doc.memed.com.br/docs/frontend/configuracoes).

### Variáveis de ambiente

Sugerimos a criação de algumas **variáveis de ambiente** para facilitar a alteração dos valores das chaves e das urls entre os ambientes de **homologação** e **produção**

```
#envs
API_KEY=
SECRET_KEY=
MEMED_API_URL=
```

### Par de chaves

#### Ambiente de homologação

**API_KEY**

```
iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm
```

**SECRET_KEY**

```
Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
```

#### Ambiente de produção

**Nota**

Para ambientes de **produção** só é possível obter o par de chaves após o preenchimento da Autorização para Credenciais de Produção. Assim que você realizar todos os procedimentos da integração, você poderá solicitar uma [Autorização para Credenciais de Produção](https://doc.memed.com.br/docs/obter-credenciais)

### URLs

#### URLs de homologação

**MEMED_API_URL**

```
https://integrations.api.memed.com.br/v1
```

#### URLs de produção

**MEMED_API_URL**

```
https://api.memed.com.br/v1
```

---

<!-- fonte: https://doc.memed.com.br/docs/backend/impressao -->
## Impressão

Quando um usuário é criado, são adicionados 4 (quatro) temas padrão para o usuário. Esses temas podem ser customizados via API.

### Configurar Impressão

A Memed permite personalizar algumas configurações relacionadas à impressão, como margens, cabeçalho, rodapé, fonte, entre outros. É possível capturar as configurações de impressão atuais e o PDF da prescrição para visualização. Segue um exemplo em cUrl abaixo:

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
            "type": "configuracoes-prescricao",
            "attributes": {
                "medicos_id": 123456,
                "indice": 1,
                "mostrar_label_nome_paciente": true,
                "mostrar_label_paciente_especial": 1,
                "mostrar_data": 1,
                "mostrar_data_controle_especial": 1,
                "fonte": "Helvetica",
                "tamanho_fonte": 14,
                "espacamento": 30,
                "mostrar_unidades": true,
                "mostrar_unidades_especial": true,
                "separar_por_uso": false,
                "mostrar_nome_fabricante": true,
                "separador_uso": 0,
                "separador_medicamento": 0,
                "largura_papel": 21,
                "altura_papel": 29.7,
                "margem_esquerda": 1.5,
                "margem_direita": 1.5,
                "margem_superior": 1,
                "margem_inferior": 1,
                "titulo_fonte": "Droid Serif Italic",
                "titulo_tamanho_fonte": 22,
                "titulo": "Dr. Teste da Silva Teste",
                "titulo_cor": "#20afd6",
                "subtitulo_fonte": "Proxima Nova",
                "subtitulo_tamanho_fonte": 14,
                "subtitulo": "CRM: 12345MG - Ginecologia e obstetrícia",
                "subtitulo_cor": "#8c8c8c",
                "tamanho_cabecalho": 2,
                "rodape_fonte": "Proxima Nova",
                "rodape_tamanho_fonte": 14,
                "rodape": "",
                "rodape_cor": "#8c8c8c",
                "tamanho_rodape": 8,
                "modelo_cabecalho_rodape": 1,
                "ativo": true,
                "imprimir_controle_especial": false,
                "imprimir_controle_especial_antibioticos": true,
                "imprimir_controle_especial_c4": false,
                "imprimir_lme": false,
                "nome_medico": "Teste da Silva Teste",
                "endereco_medico": "RUA MATO GROSSO, 1100 - SANTO AGOSTINHO",
                "cidade_medico": "São Paulo - MG",
                "telefone_medico": "(11) 99999-9999",
                "mostrar_cabecalho_rodape_simples": 1,
                "modelo_rodape": 0,
                "width_logo": 0,
                "height_logo": 0,
                "mostrar_cabecalho_rodape_especial": 1,
                "logo_nome": "",
                "logo_src": "",
                "zoom_logo": 0,
                "header_image": "parceiros\/templates\/parceiro-template-teste-header.jpeg",
                "footer_image": "parceiros\/templates\/parceiro-template-teste-footer.jpeg",
                "number_of_lme_copies": 1
            }
     }
}'
```

### Dados de impressão adicionais

É possível colocar dados extras no cabeçalho e rodapé da prescrição como, por exemplo: endereço, nome e registro do prescritor.

Veja [Gestão de prescritor](https://doc.memed.com.br/docs/como-fazer/gestao-do-prescritor).

## Recuperar as configurações das opções de receituário

Para recuperar as configurações cadastradas nas opções de receituário utilize a seguinte requisição abaixo:

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
```

### Importar cabeçalho/rodapé de um PDF

Como muitas ferramentas já possuem a opção de customização da impressão e que muitas vezes não se encaixam nas opções disponibilizadas pela Memed, criamos uma forma de importar o cabeçalho/rodapé com base em um template (PDF) enviado para a Memed, que será usado como imagem de fundo na prescrição.

Abaixo temos um exemplo de importar o cabeçalho e o rodapé com base em um template PDF enviado para a Memed:

![exemplo-importar-cabecalho.webp](https://cdn.memed.com.br/doc/exemplo-importar-cabecalho.webp)

- O PDF é enviado para a nossa API contendo somente o cabeçalho e rodapé do prescritor;
- A Memed converte para imagem e faz o recorte, identificando automaticamente onde começa e termina o cabeçalho/rodapé;
- As imagens são usadas como fundo da receita médica.

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/opcoes-receituario/upload-template?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzQ0MTQ2LCI0NDhkZDQyZDcwYTM2NjQ3ZmRmZDRlY2I0OGQzOWM5YyIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjU1Mi4zOTQ1NiJd.8Ap9NOH_M5o5XGbkf1-cb5wjo4ufCaiq0utFkr22cuE' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: multipart/form-data' \
  --form 'template=@'
```

Também é possível enviar apenas um template contendo o header ou o footer. Essa funcionalidade pode ajudar, por exemplo, em casos que o prescritor utilize papel timbrado. Nesse caso, a requisição retornará apenas o caminho do header ou do footer que foi encontrado no template.

**danger**

O PDF importado será cadastrado na configuração de impressão com índice 1 do prescritor. Caso essa configuração não possua os atributos **mostrar_cabecalho_rodape_simples** e **mostrar_cabecalho_rodape_especial** com valor igual a 1, as imagens recuperadas na requisição não irão aparecer no PDF, pois a configuração não está permitindo que o cabeçalho e rodapé sejam exibidos.

**info**

É importante lembrar que o processo acima precisará ser feito (uma única vez) para cada prescritor que utilizará o Sinapse Prescrição.

**info**

Tenha certeza que o tamanho do container onde ficará a imagem recortada tem o espaço necessário nos atributos **tamanho_cabecalho** e **tamanho_rodape** das opções de receituário cadastrada.

**Veja um vídeo demonstrando como fazer o upload do arquivo em PDF**

## An error occurred.

Unable to execute JavaScript.

---

<!-- fonte: https://doc.memed.com.br/docs/backend/prescricao -->
## Prescrição

### Capturar histórico de prescrições

É possível recuperar o histórico de prescrições do usuário prescritor. A seguinte requisição retorna as 10 últimas prescrições do usuário prescritor.

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

**Nota**

- É possível recuperar o histórico que abrangem mais do que as últimas 10 prescrições. Com o exemplo abaixo, você pode consultar qualquer período desejado e aplicar paginação caso o limite de 100 registros seja atingido.

- Exemplo de uso da paginação:

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/?page%5Blimit%5D=100&page%5Boffset%5D=0&token=<TOKEN-DO-MEDICO>&initialDate=2024-09-23&finalDate=2024-09-23' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

> **Importante:** Para recuperar prescrição com a estruturação de documentos (documentos estruturados) de uma prescrição via API, é necessário passar o parâmetro `structuredDocuments=true` na requisição. Isso garante que a resposta traga os dados estruturados dos documentos associados à prescrição.

**Exemplo de requisição com `structuredDocuments=true`:**

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/<id_prescription>?structuredDocuments=true' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <seu_token_aqui>'
```

### Remover uma prescrição

É possível remover via api uma prescrição informando o id da prescrição e o token do usuário prescritor. Veja um exemplo de requisição em cURL abaixo:

```
curl --request DELETE \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/{id_prescription}?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

### Consultar princípios ativos

É possível buscar/listar os princípios ativos dos medicamentos informando a api-key e secret-key como parametro da url (Query Parameters).

#### Veja um exemplo de requisição em cURL abaixo:

- cURL
- Resposta

**Requisição GET**

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/drugs/ingredients?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
  &terms=dipirona&limit=10&order[field]=name&order[sort]=ASC' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

**Resposta: Http status 200 - OK**

```
{
    "data": [
        {
            "type": "ingredient",
            "attributes": {
                "unii": "n.d.",
                "slug": "dipirona",
                "base": 1,
                "radical": null,
                "related": "Dipirona magnésica, Dipirona sódica, Dipirona mono-hidratada",
                "name": "Dipirona",
                "name_en": "Dipyrone"
            },
            "links": {
                "self": "https:\/\/integrations.api.memed.com.br\/v1\/ingredient\/622"
            },
            "id": 622
        }
    ],
    "links": {
        "self": "https:\/\/integrations.api.memed.com.br\/ingredient"
    },
    "meta": {
        "total": 1
    }
}
```

### Recuperar o link da Receita Digital

Para recuperar o link da receita digital enviado ao paciente, informe o id da prescrição e o token do usuário. Veja um exemplo de requisição em cURL abaixo:

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/{id_prescription}/get-digital-prescription-link?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

**Nota**

- O link da receita e o código de desbloqueio são fixos. Esses dados podem ser armazenados em banco de dados;

- Ao implementar essa opção, SEMPRE informe o código de desbloqueio para o paciente no local em que for exibir o link.

### Salvar o PDF da prescrição

Caso necessite salvar o PDF da prescrição em seu sistema, informe o id da prescrição e o token do usuário. Veja um exemplo de requisição em cURL abaixo:

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/prescricoes/{id_prescription}/url-document/full?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

---

<!-- fonte: https://doc.memed.com.br/docs/backend/protocolos -->
## Protocolos

### Medicamentos, exames e documentos

Para cadastrar um modelo de prescrição padrão, seja a nível de profissional prescritor ou instituição de saúde, deve se considerar, principalmente o uso do array de medicamento nas requisições de cadastro (POST). Ele é importante para definir comportamentos no pós prescrição, como uso do marketplace e dispensação correta de medicamentos. Abaixo temos exemplos de como o array `medicamentos` se comporta em cada caso:

Obs: o ID do medicamento/exame deve possuir correspondência correta com a Memed, caso contrario ocorrera a seguinte mensagem:

```
Apresentação especificada no medicamento não encontrada
```

**Fica a dica!**

Para facilitar o uso e criação, um protocolo pode ser cadastrado via frontEnd e recuperado com as rotas abaixo para replicar para outros profissionais.

#### Medicamentos

Para o cadastro correto de medicamentos, é necessário informar todas as medidas necessárias referente ao medicamento, abaixo temos um exemplo dos preenchimentos:

```
"medicamentos": [
{
  "id": "a1046503030027106379",
  "posologia": "Tomar de 6 em 6h",
  "nome": "Dipirona"
},
```

#### Exames

Para exames, é necessário informar somente os campos de ID e nome do exame, conforme catalogo da Memed.

```
"medicamentos": [
{
  "id": "e10",
  "posologia": "Jejum de 8 a 10 horas",
  "nome": "Hemograma"
},
```

#### Documentos

Para utilização de documentos, os campos de id são removidos do array, logo, toda inserção dentro do array de medicamentos sem um campo de ID será considerada texto livre.

```
"medicamentos": [
{
  "nome": "Atestado",
  "posologia": "<p>ATESTADO<br> Atesto que o(a) Sr.(a) ___________________________________________________________________<br> encontra-se sob meus cuidados profissionais ...."
}
```

**Sobre os ID's**

A Memed não possui uma rota direta para captura dos ID's de medicamento/exames, por favor, contate a Memed sobre como adquirir esses ID's

### Cadastrar protocolos para o usuário prescritor

É possível cadastrar protocolos de tratamento para o usuário através da API, informando o token do usuário prescritor e, dentro do array de medicamentos informando, os dados do medicamento.

Veja um exemplo de requisição em cURL abaixo:

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos?token=user_token' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": "string",
      "medicamentos": [
        {
          "nome": "string",
          "posologia": "string",
          "quantidade": 0,
          "composicao": "string",
          "fabricante": "string",
          "titularidade": "string",
          "preco": 0
        }
      ]
    }
  }
}'
```

**info**

- O campo `data.attributes.nome` possui um limite de 500 caracteres;
- Caso não tenha o ID, o item/medicamento será adicionado como texto livre na prescrição.

Após inserido, o usuário visualizará o protocolo no menu Protocolos, conforme print a seguir

![protocols-list.png](https://cdn.memed.com.br/doc/protocols-list.png)

### Recuperar protocolos de um prescritor

Para recuperar o protocolo do usuário prescritor, utilize o cURL abaixo, enviando o token do usuário prescritor na url como parametro (Query Parameters).

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/protocolos?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNTc5LCIwOTZiZDY5MDBhYjYxMTMyZTkzNzUzYjU2NDA5NWM0MSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjI1LjI2OTgxIl0.3i20Y7OZ3RSuyajuBlxGLxsjsMKqMB3egbNmjeKz5Y8' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

### Excluir protocolo de um prescritor

Para excluir o protocolo do usuário prescritor, utilize o cURL abaixo, enviando o token do usuário prescritor na url como parametro (Query Parameters).

```
curl --request DELETE \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/1367?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNTc5LCIwOTZiZDY5MDBhYjYxMTMyZTkzNzUzYjU2NDA5NWM0MSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjI1LjI2OTgxIl0.3i20Y7OZ3RSuyajuBlxGLxsjsMKqMB3egbNmjeKz5Y8' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

### Criar protocolo para todos os prescritores

Dentro de uma instituição/hospital é comum a padronização de protocolos para certo tipo de tratamento/doença. Pensando nisso, a Memed disponibiliza aos parceiros integrados a possibilidade de criar e gerenciar os protocolos que aparecerão a todos os seus prescritores.

Para criar um protocolo é preciso informar os seguintes dados:

- Nome do protocolo;
- Lista de item do protocolo, o item pode ser uma das opções abaixo:
  - Medicamento
  - Exame
  - Texto Livre

No exemplo abaixo, vamos adicionando um protocolo cujo o nome vai ser `NomeQueVaiAparecerParaTodosMedicos` e nesse protocolo vai possuir um medicamento dipirona e exame hemograma sendo exibido automaticamente para todos os prescritores do seu hospital.

**info**

Os protocolos cadastrados a nível de instituição são exibidos para todos os profissionais prescritores do par de chaves utilizado.

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": string,
      "medicamentos": [
        {
          "id": string,
          "posologia": string,
          "nome": string
        },
        {
          "id": string,
          "nome": string
        }
      ]
    }
  }
}'
```

Obs: o id do medicamento deve ser utilizado do ambiente correspondente (integrations ou produção), caso contrario ocorrera a seguinte mensagem de erro:

```
Apresentação especificada no medicamento não encontrada
```

#### Associar diagnósticos (CID) ao protocolo

Além dos dados acima, este mesmo endpoint (`POST /v1/protocolos/parceiros`) aceita o array `cids`, para associar um ou mais diagnósticos ao protocolo do parceiro. Cada código deve seguir o padrão CID-10 (ex.: `A10`, `J54`, `Z50`) e não pode se repetir dentro da mesma lista. Essa associação é o que permite que o modelo seja posteriormente encontrado por CID na busca de modelos (ver [Documentos estruturados](https://doc.memed.com.br/docs/como-fazer/documentos-estruturados#busca-e-favoritos-de-modelos-por-cid)).

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": "NomeQueVaiAparecerParaTodosMedicos",
      "cids": ["A10", "B29", "J54"],
      "medicamentos": [
        {
          "id": string,
          "posologia": string,
          "nome": string
        },
        {
          "id": string,
          "nome": string
        }
      ]
    }
  }
}'
```

O comportamento é o mesmo do cadastro sem `cids`: os diagnósticos informados ficam disponíveis para todos os prescritores vinculados ao par de chaves utilizado, e são retornados em `data.attributes.cids` na resposta (`201 Created`).

**Erros de validação de CID**

Se algum código não seguir o padrão CID-10 ou vier duplicado na lista, a API retorna `400` antes de criar o protocolo:

```
{
  "status": 400,
  "errors": [
    { "title": "invalid-cid", "detail": "Códigos CID incorretos: AA10, J9911" }
  ]
}
```

```
{
  "status": 400,
  "errors": [
    { "title": "invalid-cid", "detail": "Códigos CID duplicados: A10" }
  ]
}
```

### Consultar todos os protocolos

É possível consultar todos os protocolos de um determinado parceiro. Para isto, utilize a cURL abaixo enviando as chaves api-key e secret-key na url como parâmetro (Query Parameters).

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

Essa requisição retorna todos os protocolos que foram criados e estão sendo exibidos aos prescritores do parceiro.

### Consultar/Excluir protocolo por ID

Para a exclusão e consulta de um protocolo específico, o parceiro precisa informar o ID deste protocolo nas requisições. Esse ID pode ser recuperado de duas formas:

- Após a criação de um protocolo, o sistema retorna todos os dados do mesmo de forma estruturada, inclusive o ID;
- Consultando todos os protocolos do parceiro

## Consultar:

```
curl --request GET \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros/{protocolo_id}?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

## Excluir:

```
curl --request DELETE \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/parceiros/{protocolo_id}?api-key=NWJhMzEwNWUtYjJmMC00M2M0LWFlNmMtY2FjZDRhOTViMzNi&secret-key=YjdmNjUwZTUtZmE3My00OTJkLTkzNWMtMjg5NTRlMGU1MjIw' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json'
```

### Cadastrar múltiplos protocolos para o usuário

É possível cadastrar vários protocolos de tratamento para o usuário apenas com um REQUEST para a nossa API.

Veja um exemplo de requisição em cURL abaixo:

```
curl --request POST \
  --url 'https://integrations.api.memed.com.br/v1/protocolos/multiplos?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzMxNTc5LCIwOTZiZDY5MDBhYjYxMTMyZTkzNzUzYjU2NDA5NWM0MSIsIjIwMjMtMDItMDkiLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjI1LjI2OTgxIl0.3i20Y7OZ3RSuyajuBlxGLxsjsMKqMB3egbNmjeKz5Y8' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
    "type": "protocolos",
    "attributes": {
      "nome": "string",
      "medicamentos": [
        {
          "nome": "string",
          "posologia": "string",
          "quantidade": 0,
          "composicao": "string",
          "fabricante": "string",
          "titularidade": "string",
          "preco": 0
        }
      ]
    }
  }
}'
```

**info**

- O campo `data[].attributes.nome` possui um limite de 250 caracteres;

---

<!-- fonte: https://doc.memed.com.br/docs/backend/usuario-prescritor -->
## Usuário Prescritor

**Atenção: Obrigatoriedade de Dados (RDC n° 1000/25)**

A partir de **13/02/2026**, conforme exigência da **RDC n° 1000/25**, passará a ser **obrigatório** informar o CPF (ou passaporte, no caso de estrangeiros) e a Data de Nascimento nas emissões de prescrições.

Além disso, a data da prescrição considerada será sempre a **data da assinatura digital**. Certifique-se de que sua integração já esteja enviando esses parâmetros corretamente para evitar erros de validação na emissão.

### Tipos de usuário prescritor

A plataforma Memed permite a emissão de prescrições por diversos tipos de profissionais de saúde devidamente habilitados pelos seus respectivos conselhos profissionais:

- **Médicos** (CRM)
- **Dentistas** (CRO)
- **Enfermeiros** (COREN)
- **Médicos Veterinários** (CRMV)
- **Farmacêuticos** (CRF)
- **Nutricionistas** (CRN)
- **Fisioterapeutas** (CREFITO)
- **Psicólogos** (CRP)
- **Fonoaudiólogos** (CRFa)
- **Profissionais de Educação Física** (CREF)

A identificação do tipo de prescritor é realizada automaticamente durante o cadastro, com base no registro profissional informado (CRM, CRO, COREN, etc.).

**Base de Medicamentos Unificada**

A base de medicamentos da Memed é **única e compartilhada** entre todas as categorias profissionais. Cabe ao sistema integrado implementar o controle e validação dos medicamentos que podem ser prescritos por cada categoria profissional, respeitando suas respectivas competências e legislações vigentes.

#### Status do usuário prescritor

Cada prescritor cadastrado na Memed possui um **status** que determina se ele está autorizado a emitir prescrições. Este status indica o estado atual da validação do cadastro.

**Importante**

Prescritores com status "Inativo" **não podem** emitir prescrições e receberão um [erro de autenticação](https://doc.memed.com.br/docs/erros-comuns/ocorreu-erro-autenticacao) ao tentarem acessar a plataforma.

**Status possíveis:**

| Status | Descrição | Pode prescrever? |
|---|---|---|
| Ativo | Cadastro validado e aprovado | ✅ |
| Em análise | Cadastro em processo de validação interna | ✅ |
| Inativo | Cadastro bloqueado ou desativado | ❌ |

### Obtendo o token do usuário (prescritor)

O token de acesso do usuário prescritor é retornado junto com todos os outros dados do usuário. [Veja abaixo](#obtendo-os-dados-do-usu%C3%A1rio-prescritor) como recuperar os dados do usuário e o token de acesso.

**Atenção**

O **token** não é estático, portanto sempre que for fazer uma requisição na **API Memed**, você precisa recuperar o último token válido do usuário.

### Obtendo os dados do usuário prescritor

Para consultar os dados completos de um prescritor, incluindo seu **token de acesso**, realize uma requisição **GET** na API da Memed utilizando a rota de usuários.

**Parâmetros necessários:**

- **Identificador do usuário** (veja opções abaixo)
- **Par de chaves** (API Key + Secret Key)

**Token de Acesso**

O **token de acesso** do usuário prescritor é retornado automaticamente junto com todos os demais dados do usuário na resposta da requisição.

**Identificadores Válidos**

O **identificador do usuário** pode ser informado de três formas diferentes:

- **CPF:** Apenas números (11 dígitos)
- **External ID:** Identificador único definido pelo seu sistema
- **Registro + UF:** Número do registro profissional seguido da sigla do estado (Ex: `12345SP`, `01234MG`)

> **Tipos de registro aceitos:** CRM, CRO, COREN, CRMV, CRF, CRN, CREFITO, CRP, CRFa, CREF

#### Rota para obter os dados do usuário

```
GET: MEMED_API_URL/sinapse-prescricao/usuarios/{ID_USUARIO}?api-key=API_KEY&secret-key=SECRET_KEY
```

#### Exemplo de requisição

Abaixo está um exemplo completo de requisição para obter os dados e o **token de acesso** do usuário.

- cURL
- Sucesso
- Erro

##### Requisição GET

```
curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/1234?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL'\
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

##### ✅ Retorno de Sucesso - HTTP 200 OK

```
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "nome": "Jhon",
      "sobrenome": "Doe",
      "cpf": "84168858006",
      "email": "jhon@doe.com",
      "telefone": "(00) 00000-0000",
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I",
      "uf": "SP",
      "crm": "016964"
    }
  }
}
```

##### ❌ Retorno de Erro - HTTP 404 NOT FOUND

```
{
  "errors": [
    {
      "title": "Erro",
      "detail": "Nenhum usuário encontrado com este este CRM, CPF ou Id: 1234"
    }
  ]
}
```

### Cadastrando o prescritor

Para cadastrar um novo usuário prescritor, realize uma requisição **POST** na rota de usuários da API Memed, enviando os dados do profissional no corpo da requisição.

**Estrutura da Requisição**

**Formato obrigatório:** Os dados devem ser enviados no **corpo (body)** da requisição seguindo rigorosamente a estrutura de payload especificada pela API. A formatação correta garante o sucesso da operação e evita erros de validação.

**Relacionamentos opcionais:** Ao incluir as propriedades `cidade` e/ou `especialidade` no objeto `relationships`, os campos `type` e `id` dentro delas tornam-se **obrigatórios**.

**APIs de Consulta:**

- **Cidades:** Obtenha o ID da cidade em:  
  `https://integrations.api.memed.com.br/v1/cidades`

- **Especialidades:** Obtenha o ID da especialidade em:  
  `https://integrations.api.memed.com.br/v1/especialidades`

**💡 Dica:** Consulte essas APIs previamente e armazene os IDs mais utilizados em cache no seu sistema para otimizar o desempenho do processo de cadastro.

#### Rota de cadastro do usuário

```
POST: MEMED_API_URL/sinapse-prescricao/usuarios?api-key={API_KEY}&secret-key={SECRET_KEY}
```

#### Estrutura do payload de cadastro

**Estrutura Obrigatória**

A requisição deve seguir **exatamente** a estrutura de payload (contrato) especificada abaixo. Qualquer desvio desta estrutura resultará em erro de validação:

```
{
  // obrigatório
  "data": {
    "type": "usuarios",
    "attributes": {
      "external_id": "0753879b-362d-4126-9146-a16cf6eb14bd", // Obrigatório
      "nome": "Gustavo", // Obrigatório
      "sobrenome": "Ribeiro Sousa", // Obrigatório
      "cpf": "53076220403", // Obrigatório
      "board": {
            "board_code": "CRM", // Obrigatório
            "board_number": "315435435", // Obrigatório
            "board_state": "SP"}, // Obrigatório
      "email": "gustavo.ribeiro@meuhospital.com", // Opcional
      "telefone": "19938742708", // Opcional
      "sexo": "M", // Opcional
      "data_nascimento": "05/09/1972" // Obrigatório
    },

    // opcional
    "relationships": {
      "cidade": {
        "data": {
          "type": "cidades", // Obrigatório
          "id": 1 // Obrigatório
        }
      },
      "especialidade": {
        "data": {
          "type": "especialidades", // Obrigatório
          "id": 1 // Obrigatório
        }
      }
    }
  }
}
```

#### Dados do prescritor

| Propriedade | Tipo | Obrigatório | Observações |
|---|---|---|---|
| external_id | int/string(255) | ✅ | Recomendável ser do tipo UUID, pois é um campo único |
| nome | string(255) | ✅ |  |
| sobrenome | string(255) | ✅ |  |
| cpf | string(11) | ✅ | Apenas dígitos |
| board_code | string(5) | ✅ | CRM / CRO / COREN / CRMV / CRF / CRN / CREFITO / CRP / CRFa / CREF |
| board_number | string(255) | ✅ | Apenas dígitos |
| board_state | string(2) | ✅ | Siglas dos estados brasileiros |
| email | string(255) |  |  |
| telefone | string(16) |  | Apenas dígitos ou formatado (DDD) XXXXX-XXXX |
| sexo | string(1) |  | M / F |
| data_de_nascimento | date(10) | ✅ | dd/mm/YYYY |
| cidade | int(10) |  | O id da API https://integrations.api.memed.com.br/v1/cidades |
| especialidade | int(10) |  | O id da API https://integrations.api.memed.com.br/v1/especialidades |

**Melhores Práticas para Experiência do Usuário**

Embora diversos campos sejam marcados como opcionais na estrutura de cadastro, é importante compreender que **quanto mais completo for o cadastro inicial, melhor será a experiência** do prescritor na plataforma.

Dados não preenchidos durante a integração precisarão ser completados posteriormente pelo próprio usuário dentro da plataforma de prescrição da Memed, o que pode gerar interrupções no fluxo de trabalho e frustração.

**Recomendação:** Envie o máximo de informações disponíveis durante o processo de cadastro (CPF, e-mail, telefone, sexo, data de nascimento, cidade e especialidade). Esta prática resulta em:

- **Acesso imediato e completo** às funcionalidades da plataforma
- **Redução de etapas** para o prescritor após o primeiro login
- **Onboarding mais ágil** e sem interrupções
- **Dados mais completos** para análises e relatórios

#### Exemplo de requisição de cadastro

Abaixo está um exemplo completo de requisição para cadastrar um novo prescritor. O **token** do usuário será retornado na resposta de sucesso:

- cURL
- Sucesso
- Erro

**Requisição POST**

```
curl --location 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL' \
--header 'Accept: application/vnd.api+json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "type": "usuarios",
    "attributes": {
      "external_id": "0753879b-362d-4126-9146-a16cf6eb14bd",
      "nome": "Gustavo",
      "sobrenome": "Ribeiro Sousa",
      "cpf": "53076220403",
      "board": {
            "board_code": "CRM",
            "board_number": "315435435",
            "board_state": "SP"},
      "email": "gustavo.ribeiro@meuhospital.com",
      "telefone": "19938742708",
      "sexo": "M",
      "data_nascimento": "05/09/1972"
    },
    "relationships": {
      "cidade": {
        "data": {
          "type": "cidades",
          "id": 1
        }
      },
      "especialidade": {
        "data": {
          "type": "especialidades",
          "id": 1
        }
      }
    }
  }
}'
```

##### ✅ Retorno de Sucesso - HTTP 200 OK

```
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "nome": "Jhon",
      "sobrenome": "Doe",
      "cpf": "84168858006",
      "email": "jhon@doe.com",
      "telefone": "(00) 00000-0000",
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I",
      "uf": "MG",
      "crm": "016964"
    }
  }
}
```

##### ❌ Retorno de Erro - HTTP 400 BAD REQUEST

```
{
  "errors": [
    {
      "code": "codigo_do_erro",
      "title": "titulo do erro",
      "detail": "detalhes sobre o erro"
    }
  ]
}
```

**Tratamento de Erros**

As mensagens de erro são específicas para cada situação. Analise cuidadosamente o campo `detail` do erro retornado para identificar e corrigir o problema antes de reenviar a requisição.

**Principais causas de erro:**

- Dados em formato inválido (ex: CPF com letras, data mal formatada)
- Registro profissional não encontrado nos conselhos oficiais
- CPF inválido ou não cadastrado
- E-mail em formato inválido
- Campos obrigatórios ausentes ou vazios
- `external_id` já cadastrado para outro usuário

### Atualizando os dados do usuário prescritor

Para atualizar os dados de um prescritor existente, realize uma requisição **PATCH** na rota de usuários, informando:

- **Identificador do usuário** (CPF, External ID ou Registro+UF)
- **Par de chaves** (API Key + Secret Key)
- **Dados a atualizar** no corpo da requisição

**Atenção ao external_id**

**Importante:** Só inclua o campo `external_id` no payload se você realmente deseja **alterar** seu valor.

Se você enviar o `external_id` com o **mesmo valor atual**, a API retornará o erro:  
`"Prescritor já cadastrado para o parceiro com esse id externo"`

**Recomendação:** Para atualizações comuns (nome, e-mail, telefone, etc.), **não inclua** o campo `external_id` no payload.

#### Rota para atualizar os dados do usuário prescritor

```
PATCH: MEMED_API_URL/sinapse-prescricao/usuarios/{EXTERNAL_ID}?api-key=API_KEY&secret-key=SECRET_KEY
```

#### Exemplo de requisição de atualização

Exemplo de requisição para atualizar o CPF de um prescritor existente:

- cURL
- Sucesso
- Erro

**Requisição PATCH**

```
curl --request PATCH \
  --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/EXTERNAL_ID?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL' \
  --header 'Accept: application/vnd.api+json' \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
        "type": "usuarios",
        "attributes": {
            "cpf": "84587617008"
        }
    }
}'
```

**Retorno: Http status 200 - OK**

```
{
  "data": {
    "type": "usuarios",
    "attributes": {
      "nome": "Jhon",
      "sobrenome": "Doe",
      "cpf": "84168858006",
      "email": "jhon@doe.com",
      "telefone": "(00) 00000-0000",
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WzM2MzE3LCI2MTA0NGVkZThiMDg4YzdmMmIwMDlkNWM3NmJiMzJjMiIsIjIwMjItMTItMTciLCJzaW5hcHNlLnByZXNjcmljYW8iLCJwYXJ0bmVyLjMuMzE2NDkiXQ.Kv-VSTmXqCI-q6GPiPHF7Q8Prhz2RKy0sL0BWYfoM2I",
      "uf": "MG",
      "crm": "016964",
      "email": "novoemail@test.com"
    }
  }
}
```

**Retorno: Http status 400 - BAD REQUEST**

```
{
  "errors": [
    {
      "code": "codigo_do_erro",
      "title": "titulo do erro",
      "detail": "detalhes sobre o erro"
    }
  ]
}
```

### Excluindo usuário prescritor

Para excluir permanentemente um prescritor, realize uma requisição **DELETE** na rota de usuários, informando o **identificador do usuário** e o **par de chaves**.

**Ação Irreversível**

Ao excluir um prescritor, você estará:

- Removendo **permanentemente** todo o histórico de atividades
- Excluindo **todas as prescrições** associadas
- Apagando **todos os dados e configurações** do usuário

Mesmo recriando o cadastro com os mesmos dados, **não será possível** recuperar o histórico, prescrições ou configurações anteriores.

#### Rota para excluir o usuário prescritor

```
DELETE: MEMED_API_URL/sinapse-prescricao/usuarios/{ID_USUARIO}?api-key=API_KEY&secret-key=SECRET_KEY
```

#### Exemplo de requisição de exclusão

Exemplo de requisição para excluir permanentemente um prescritor:

- cURL
- Sucesso
- Erro

**Requisição DELETE**

```
    curl --request DELETE \
        --url 'https://integrations.api.memed.com.br/v1/sinapse-prescricao/usuarios/1234?api-key=iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm&secret-key=Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL'\
        --header 'Accept: application/vnd.api+json' \
        --header 'Cache-Control: no-cache' \
        --header 'Content-Type: application/json'
```

**Retorno: Http status 200 - OK**

```
no content
```

**Retorno: Http status 404 - NOT FOUND**

```
{
  "errors": [
    {
      "title": "titulo do erro",
      "detail": "detalhes do erro"
    }
  ]
}
```
