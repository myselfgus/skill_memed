https://doc.memed.com.br/docs/frontend/configuracoes/

# Configurações

As configurações propostas logo abaixo são apenas sugestões para
facilitar a sua integração com a prescrição digital Memed.

Dica

Aproveite para ver detalhes das configurações do [**backend**](/docs/backend/configuracoes).

## Variáveis de ambiente

Sugerimos a criação de algumas **variáveis de ambiente** para facilitar
a alteração dos valores das chaves e das urls entre os ambientes
de **homologação** e **produção**

```dotenv
#envs
MEMED_SCRIPT_URL=
```

## URLs

### URLs de homologação

**MEMED\_SCRIPT\_URL**

```dotenv
https://integrations.memed.com.br/modulos/plataforma.sinapse-prescricao/build/sinapse-prescricao.min.js
```

### URLs de produção

**MEMED\_SCRIPT\_URL**

```dotenv
https://partners.memed.com.br/integration.js
```
