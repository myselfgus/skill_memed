https://doc.memed.com.br/docs/backend/configuracoes/

# Configurações

As configurações aqui propostas são apenas sugestões para
facilitar a sua integração com a prescrição digital Memed.

Dica

Aproveite para ver detalhes das configurações do [**frontend**](/docs/frontend/configuracoes).

## Variáveis de ambiente

Sugerimos a criação de algumas **variáveis de ambiente** para facilitar
a alteração dos valores das chaves e das urls entre os ambientes
de **homologação** e **produção**

```dotenv
#envs
API_KEY=
SECRET_KEY=
MEMED_API_URL=
```

## Par de chaves

### Ambiente de homologação

**API\_KEY**

```dotenv
iJGiB4kjDGOLeDFPWMG3no9VnN7Abpqe3w1jEFm6olkhkZD6oSfSmYCm
```

**SECRET\_KEY**

```dotenv
Xe8M5GvBGCr4FStKfxXKisRo3SfYKI7KrTMkJpCAstzu2yXVN4av5nmL
```

### Ambiente de produção

Nota

Para ambientes de **produção** só é possível obter o par de chaves após o preenchimento da Autorização para Credenciais de Produção.
Assim que você realizar todos os procedimentos da integração,
você poderá solicitar uma [Autorização para Credenciais de Produção](/docs/obter-credenciais)

## URLs

### URLs de homologação

**MEMED\_API\_URL**

```dotenv
https://integrations.api.memed.com.br/v1
```

### URLs de produção

**MEMED\_API\_URL**

```dotenv
https://api.memed.com.br/v1
```
