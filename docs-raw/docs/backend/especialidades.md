https://doc.memed.com.br/docs/backend/especialidades/

# Especialidades

## Onde é usado?

As especialidades são utilizadas para identificar no cadastro do usuário prescritor qual a sua principal área de atuação. Essa informação também é emitida no receituário gerado pela Memed

![speciality-example](https://cdn.memed.com.br/doc/speciality-example.png)

Alem disso, a informacão de especialidade é exibida na receita digital.

## Como usar

Para consultar as especialidades disponíveis na Memed, basta fazer
uma requisição **GET** na API Memed na rota de consulta de especialidades. A autenticação
**não é necessária** neste método.

Atenção!

Você pode filtrar utilizando o parâmetro **filter**.   
Ex: Filtrar por especialidades que possuem a palavra 'Generalista' **filter[q]=Generalista**

### Rota para consultar especialidades

```text
GET: MEMED_API_URL/especialidades
```

### cURL para consultar especialidades

Abaixo segue um exemplo da requisição para consultar as especialidades.

* cURL
* cURL com filtro
* Sucesso
* Erro

**Requisição GET**

```js
    curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/especialidades' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

**Requisição GET**

```js
    curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/especialidades?filter[q]=Generalista' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

**Retorno: Http status 200 - OK**

```json
{
    "data": [
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Acupuntura",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/1"
            },
            "id": 1
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Alergia e Imunologia",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/63"
            },
            "id": 63
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Alergia e imunopatologia",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/2"
            },
            "id": 2
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Anestesia",
                "grupo": "Anestesiologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/64"
            },
            "id": 64
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Anestesiologia",
                "grupo": "Anestesiologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/3"
            },
            "id": 3
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Angiologia e cirurgia vascular",
                "grupo": "Cirurgia vascular"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/4"
            },
            "id": 4
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Atendimento domiciliar",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/65"
            },
            "id": 65
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Canabinologia",
                "grupo": "Clínica Médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/57"
            },
            "id": 57
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cardiologia",
                "grupo": "Cardiologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/5"
            },
            "id": 5
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia cardiovascular",
                "grupo": "Cardiologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/6"
            },
            "id": 6
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia da mão",
                "grupo": "Ortopedia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/7"
            },
            "id": 7
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia de cabeça e pescoço",
                "grupo": "Cirurgia geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/8"
            },
            "id": 8
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia digestiva",
                "grupo": "Gastroenterologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/9"
            },
            "id": 9
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia endocrinológica",
                "grupo": "Endocrinologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/51"
            },
            "id": 51
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia geral",
                "grupo": "Cirurgia geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/10"
            },
            "id": 10
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia oncológica",
                "grupo": "Oncologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/50"
            },
            "id": 50
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia pediátrica",
                "grupo": "Pediatria"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/11"
            },
            "id": 11
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia plástica",
                "grupo": "Dermatologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/12"
            },
            "id": 12
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Cirurgia torácica",
                "grupo": "Cirurgia geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/13"
            },
            "id": 13
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Clínica médica",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/14"
            },
            "id": 14
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Coloproctologia",
                "grupo": "Gastroenterologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/15"
            },
            "id": 15
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Dermatologia",
                "grupo": "Dermatologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/16"
            },
            "id": 16
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Endocrinologia e metabologia",
                "grupo": "Endocrinologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/17"
            },
            "id": 17
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Endoscopia digestiva",
                "grupo": "Gastroenterologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/18"
            },
            "id": 18
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Gastroenterologia",
                "grupo": "Gastroenterologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/19"
            },
            "id": 19
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Generalista",
                "grupo": "Clínica Médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/59"
            },
            "id": 59
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Genética médica",
                "grupo": "Clínica médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/56"
            },
            "id": 56
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Geriatria e gerontologia",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/20"
            },
            "id": 20
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Ginecologia e obstetrícia",
                "grupo": "Ginecologia e obstetrícia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/21"
            },
            "id": 21
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Hematologia, hemoterapia e terapia celular",
                "grupo": "Null"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/22"
            },
            "id": 22
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Hepatologia",
                "grupo": "Gastroenterologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/23"
            },
            "id": 23
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Homeopatia",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/24"
            },
            "id": 24
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Infectologia",
                "grupo": "Null"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/25"
            },
            "id": 25
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Mastologia",
                "grupo": "Ginecologia e obstetrícia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/26"
            },
            "id": 26
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina de emergência",
                "grupo": "Clínica Geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/60"
            },
            "id": 60
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina de família e comunidade",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/27"
            },
            "id": 27
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina de tráfego",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/28"
            },
            "id": 28
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina do exercício e do esporte",
                "grupo": "Ortopedia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/29"
            },
            "id": 29
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina do trabalho",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/30"
            },
            "id": 30
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina física e reabilitação",
                "grupo": "Ortopedia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/31"
            },
            "id": 31
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina intensiva",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/32"
            },
            "id": 32
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina legal",
                "grupo": "Clínica geral"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/33"
            },
            "id": 33
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina nuclear",
                "grupo": "Null"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/34"
            },
            "id": 34
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina ortomolecular",
                "grupo": "Clínica médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/54"
            },
            "id": 54
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Medicina preventiva e social",
                "grupo": "Clínica Médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/55"
            },
            "id": 55
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Nefrologia",
                "grupo": "Nefrologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/35"
            },
            "id": 35
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Neurocirurgia",
                "grupo": "Neurologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/36"
            },
            "id": 36
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Neurologia",
                "grupo": "Neurologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/37"
            },
            "id": 37
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Neurologia pediátrica",
                "grupo": "neurologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/62"
            },
            "id": 62
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Nutrição parenteral e enteral",
                "grupo": "Nutrologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/38"
            },
            "id": 38
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Nutrologia",
                "grupo": "Nutrologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/39"
            },
            "id": 39
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Oftalmologia",
                "grupo": "Oftalmologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/40"
            },
            "id": 40
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Oncologia",
                "grupo": "Oncologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/41"
            },
            "id": 41
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Ortopedia e traumatologia",
                "grupo": "Ortopedia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/42"
            },
            "id": 42
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Otorrinolaringologia e cirurgia cérvico-facial",
                "grupo": "Otorrinolaringologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/43"
            },
            "id": 43
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Patologia",
                "grupo": "Clínica médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/52"
            },
            "id": 52
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Patologia clínica",
                "grupo": "Clínica médica"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/53"
            },
            "id": 53
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Pediatria",
                "grupo": "Pediatria"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/44"
            },
            "id": 44
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Pneumologia e tisiologia",
                "grupo": "Pneumologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/45"
            },
            "id": 45
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Pneumologia pediátrica",
                "grupo": "Pediatria"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/61"
            },
            "id": 61
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Psiquiatria",
                "grupo": "Psiquiatria"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/46"
            },
            "id": 46
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Radiologia",
                "grupo": "Null"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/47"
            },
            "id": 47
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Radioterapia",
                "grupo": "Radioterapia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/58"
            },
            "id": 58
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Reumatologia",
                "grupo": "Reumatologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/48"
            },
            "id": 48
        },
        {
            "type": "especialidades",
            "attributes": {
                "nome": "Urologia",
                "grupo": "Nefrologia"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/especialidades/49"
            },
            "id": 49
        }
    ],
    "links": {
        "self": "https://integrations.api.memed.com.br/especialidades"
    },
    "meta": {
        "total": 65
    }
}
```

**Retorno: Http status 400 - BAD REQUEST**

```json
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
