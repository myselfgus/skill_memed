# Tabelas de referência: cidades e especialidades

Extraído de https://doc.memed.com.br/docs em 2026-10-18.

## Páginas neste arquivo

- Cidades — `https://doc.memed.com.br/docs/backend/cidades`
- Especialidades — `https://doc.memed.com.br/docs/backend/especialidades`

---

<!-- fonte: https://doc.memed.com.br/docs/backend/cidades -->
## Cidades

### Onde é usado?

A cidade é necessária para identificação do usuário prescritor no momento do cadastro, isso auxilia em campos de LME e na identificação do conselho regional para qual o usuário prescritor está cadastrado.

### Como usar

Para consultar as cidades disponíveis na Memed, basta fazer uma requisição **GET** na API Memed na rota de cidades. A autenticação **não é necessária** neste método.

**Atenção!**

Você pode filtrar utilizando o parâmetro **filter**.  
Ex: Filtrar por cidades que possuem a palavra 'Campinas' **filter\[q\]=Campinas**  
Ou filtrar todos os estados do 'RJ', **filter\[uf\]=RJ**

#### Rota para consultar cidades

```
GET: MEMED_API_URL/cidades
```

#### cURL para consultar cidades

Abaixo segue um exemplo da requisição para consultar as cidades.

- cURL
- cURL com filtro
- Sucesso
- Erro

**Requisição GET**

```
    curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/cidades' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

**Requisição GET**

```
    curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/cidades?filter[q]=Campinas' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

**Retorno: Http status 200 - OK**

```
{
    "data": [
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acrelândia",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1"
            },
            "id": 1
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Assis Brasil",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/2"
            },
            "id": 2
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Bujari",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/3"
            },
            "id": 3
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Brasiléia",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/4"
            },
            "id": 4
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Capixaba",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/5"
            },
            "id": 5
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Cruzeiro do Sul",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/6"
            },
            "id": 6
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Epitaciolândia",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/7"
            },
            "id": 7
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Feijó",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/8"
            },
            "id": 8
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Jordão",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/9"
            },
            "id": 9
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Mâncio Lima",
                "uf": "AC"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/10"
            },
            "id": 10
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Branca",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/23"
            },
            "id": 23
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Anadia",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/24"
            },
            "id": 24
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Arapiraca",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/25"
            },
            "id": 25
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Atalaia",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/26"
            },
            "id": 26
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Barra de Santo Antônio",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/27"
            },
            "id": 27
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Barra de São Miguel",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/28"
            },
            "id": 28
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Batalha",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/29"
            },
            "id": 29
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Belém",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/30"
            },
            "id": 30
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Belo Monte",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/31"
            },
            "id": 31
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Boca da Mata",
                "uf": "AL"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/32"
            },
            "id": 32
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Amapá",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/124"
            },
            "id": 124
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Calçoene",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/125"
            },
            "id": 125
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Cutias",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/126"
            },
            "id": 126
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Ferreira Gomes",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/127"
            },
            "id": 127
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Itaubal",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/128"
            },
            "id": 128
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Laranjal do Jari",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/129"
            },
            "id": 129
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Macapá",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/130"
            },
            "id": 130
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Mazagão",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/131"
            },
            "id": 131
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Oiapoque",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/132"
            },
            "id": 132
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Pedra Branca do Amaparí",
                "uf": "AP"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/133"
            },
            "id": 133
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alvarães",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/140"
            },
            "id": 140
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Amaturá",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/141"
            },
            "id": 141
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "namã",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/142"
            },
            "id": 142
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Anori",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/143"
            },
            "id": 143
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Apuí",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/144"
            },
            "id": 144
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Atalaia do Norte",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/145"
            },
            "id": 145
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Autazes",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/146"
            },
            "id": 146
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Barcelos",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/147"
            },
            "id": 147
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Barreirinha",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/148"
            },
            "id": 148
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Benjamin Constant",
                "uf": "AM"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/149"
            },
            "id": 149
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Abaíra",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/202"
            },
            "id": 202
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Abaré",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/203"
            },
            "id": 203
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acajutiba",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/204"
            },
            "id": 204
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Adustina",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/205"
            },
            "id": 205
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Fria",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/206"
            },
            "id": 206
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Aiquara",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/207"
            },
            "id": 207
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alagoinhas",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/208"
            },
            "id": 208
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alcobaça",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/209"
            },
            "id": 209
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Almadina",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/210"
            },
            "id": 210
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Amargosa",
                "uf": "BA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/211"
            },
            "id": 211
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Abaiara",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/617"
            },
            "id": 617
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acarapé",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/618"
            },
            "id": 618
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acaraú",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/619"
            },
            "id": 619
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acopiara",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/620"
            },
            "id": 620
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Aiuaba",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/621"
            },
            "id": 621
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alcântaras",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/622"
            },
            "id": 622
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Altaneira",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/623"
            },
            "id": 623
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Santo",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/624"
            },
            "id": 624
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Amontada",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/625"
            },
            "id": 625
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Antonina do Norte",
                "uf": "CE"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/626"
            },
            "id": 626
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Brasília",
                "uf": "DF"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/801"
            },
            "id": 801
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Afonso Cláudio",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/802"
            },
            "id": 802
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Doce do Norte",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/803"
            },
            "id": 803
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Águia Branca",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/804"
            },
            "id": 804
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alegre",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/805"
            },
            "id": 805
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alfredo Chaves",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/806"
            },
            "id": 806
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Rio Novo",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/807"
            },
            "id": 807
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Anchieta",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/808"
            },
            "id": 808
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Apiacá",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/809"
            },
            "id": 809
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Aracruz",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/810"
            },
            "id": 810
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Atilio Vivacqua",
                "uf": "ES"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/811"
            },
            "id": 811
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Abadia de Goiás",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/879"
            },
            "id": 879
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Abadiânia",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/880"
            },
            "id": 880
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acreúna",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/881"
            },
            "id": 881
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Adelândia",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/882"
            },
            "id": 882
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Fria de Goiás",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/883"
            },
            "id": 883
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Limpa",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/884"
            },
            "id": 884
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Águas Lindas de Goiás",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/885"
            },
            "id": 885
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alexânia",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/886"
            },
            "id": 886
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Aloândia",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/887"
            },
            "id": 887
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Horizonte",
                "uf": "GO"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/888"
            },
            "id": 888
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Açailândia",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1121"
            },
            "id": 1121
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Afonso Cunha",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1122"
            },
            "id": 1122
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Doce do Maranhão",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1123"
            },
            "id": 1123
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alcântara",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1124"
            },
            "id": 1124
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Aldeias Altas",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1125"
            },
            "id": 1125
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Altamira do Maranhão",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1126"
            },
            "id": 1126
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Alegre do Maranhão",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1127"
            },
            "id": 1127
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Alegre do Pindaré",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1128"
            },
            "id": 1128
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Parnaíba",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1129"
            },
            "id": 1129
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Amapá do Maranhão",
                "uf": "MA"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1130"
            },
            "id": 1130
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Acorizal",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1338"
            },
            "id": 1338
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Água Boa",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1339"
            },
            "id": 1339
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alta Floresta",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1340"
            },
            "id": 1340
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Araguaia",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1341"
            },
            "id": 1341
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Boa Vista",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1342"
            },
            "id": 1342
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Garças",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1343"
            },
            "id": 1343
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Paraguai",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1344"
            },
            "id": 1344
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Alto Taquari",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1345"
            },
            "id": 1345
        },
        {
            "type": "cidades",
            "attributes": {
                "nome": "Apiacás",
                "uf": "MT"
            },
            "links": {
                "self": "https://integrations.api.memed.com.br/v1/cidades/1346"
            },
            "id": 1346
        }
    ],
    "links": {
        "next": "https://integrations.api.memed.com.br/v1/cidades?page[offset]=100",
        "last": "https://integrations.api.memed.com.br/v1/cidades?page[offset]=166",
        "self": "https://integrations.api.memed.com.br/cidades"
    },
    "meta": {
        "total": 266,
        "limit": 100
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

---

<!-- fonte: https://doc.memed.com.br/docs/backend/especialidades -->
## Especialidades

### Onde é usado?

As especialidades são utilizadas para identificar no cadastro do usuário prescritor qual a sua principal área de atuação. Essa informação também é emitida no receituário gerado pela Memed

![speciality-example](https://cdn.memed.com.br/doc/speciality-example.png)

Alem disso, a informacão de especialidade é exibida na receita digital.

### Como usar

Para consultar as especialidades disponíveis na Memed, basta fazer uma requisição **GET** na API Memed na rota de consulta de especialidades. A autenticação **não é necessária** neste método.

**Atenção!**

Você pode filtrar utilizando o parâmetro **filter**.  
Ex: Filtrar por especialidades que possuem a palavra 'Generalista' **filter\[q\]=Generalista**  

#### Rota para consultar especialidades

```
GET: MEMED_API_URL/especialidades
```

#### cURL para consultar especialidades

Abaixo segue um exemplo da requisição para consultar as especialidades.

- cURL
- cURL com filtro
- Sucesso
- Erro

**Requisição GET**

```
    curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/especialidades' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

**Requisição GET**

```
    curl --request GET \
    --url 'https://integrations.api.memed.com.br/v1/especialidades?filter[q]=Generalista' \
    --header 'Accept: application/vnd.api+json' \
    --header 'Cache-Control: no-cache' \
    --header 'Content-Type: application/json'
```

**Retorno: Http status 200 - OK**

```
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
