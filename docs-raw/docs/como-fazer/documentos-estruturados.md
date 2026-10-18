https://doc.memed.com.br/docs/como-fazer/documentos-estruturados/

# Documentos estruturados

## Visão geral

Esta página explica como *estruturar* documentos de texto livre dentro da prescrição, com possibilidade de classificação e associação a diagnósticos **CID-10**. Essa estruturação melhora relatórios clínicos, integrações e rastreabilidade.

Nova funcionalidade disponível!

A nova versão do módulo de prescrição médica traz uma funcionalidade essencial: **categorização de documentos de texto livre** e **inclusão de CIDs (Classificação Internacional de Doenças)**.

Essa funcionalidade moderniza o fluxo de prescrição, organizando melhor documentos como:

* **Atestado**
* **Encaminhamento**
* **Laudo**
* **Relatório**
* **Outro documento**

Essas categorias são selecionadas diretamente no item de texto livre da prescrição.

Vantagens desta melhoria

Esta nova melhoria visa facilitar a estruturação de documentos médicos, oferecendo:

* Interface mais intuitiva e robusta
* Inclusão formal de diagnósticos com CID
* Melhor organização clínica e rastreabilidade de informações

---

## Como utilizar

### Na interface (Canvas de Prescrição)

1. No campo de busca da prescrição, digite o nome ou trecho do documento desejado (ex.: "atesta").
2. Clique na aba **Documentos** para visualizar os modelos disponíveis, já organizados por categoria (*Atestado*, *Encaminhamento*, *Laudo*, *Relatório* ou *Outro documento*).
3. Selecione o modelo desejado na lista (ex.: "Atestado de afastamento de atividades laborais") para inseri-lo na prescrição já com o tipo de documento associado.
4. (Opcional) Abra a guia **CID**, pesquise pelo código ou descrição e selecione um ou mais diagnósticos.
5. (Opcional) Utilize **Salvar como protocolo** para reutilizar este documento em futuras prescrições.
6. Finalize ou imprima a prescrição normalmente.

Atenção

A aba de busca **CID** só será habilitada para inclusão se constar um documento ou medicamento no documento.

Dica

O tipo de documento será exibido na impressão e pode ser usado para classificar melhor os documentos clínicos.

---

## Inclusão de CID

Após escolher o tipo de documento, a busca por CID será liberada na guia específica:

![Busca por CID](/assets/images/inclusao-cid-ad8d4ee5ec2da1080c58abdab70493cc.png)

Digite parte do nome ou código CID (ex: B16, C34, etc) e selecione a entrada desejada.

Atenção

A aba CID só aparecerá quando houver **conteúdo textual preenchido** no item.

## CIDs selecionados

Os CIDs adicionados aparecerão abaixo do documento:

> O paciente pode optar por **compartilhar ou ocultar** o CID no documento impresso.

---

## Resumo do fluxo

1. Insira um item em texto livre.
2. Escolha o tipo de documento (Atestado, Laudo, etc).
3. Digite o nome ou código do CID.
4. Clique na aba "CID" e selecione o diagnóstico.
5. Verifique se os CIDs foram listados abaixo corretamente.

Benefícios

Essa funcionalidade permite padronizar documentos clínicos e associá-los com diagnósticos (CID), oferecendo mais clareza e rastreabilidade para instituições de saúde.

---

## Exemplo de estrutura de dados

Abaixo, um exemplo de como as informações de CID e categoria do documento podem ser estruturadas em um objeto de integração:

```json
{
  "cids": [
    {
      "id": "c171555",
      "code": "B16",
      "name": "CID",
      "description": "B16 - Hepatite aguda B",
      "category": "cid_atestado",
      "observation": "Paciente solicitou compartilhamento do CID no documento",
      "is_cid": true
    }
  ],
  "medicamentos": [
    {
      // ... outros campos do medicamento ...
      "custom_categoria": "atestado"
    }
  ]
}
```

> **Nota:**  
> O campo `custom_categoria` indica a categoria selecionada para o documento (ex: "atestado").  
> O array `cids` traz os diagnósticos associados, incluindo observações relevantes.

---

## Busca e favoritos de modelos por CID

Nova funcionalidade disponível!

Os modelos de prescrição (protocolos) agora também podem ser encontrados por CID e marcados como favoritos direto no painel de Modelos da prescrição, facilitando a reutilização dos modelos mais relevantes para cada diagnóstico.
