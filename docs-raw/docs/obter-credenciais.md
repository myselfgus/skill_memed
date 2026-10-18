https://doc.memed.com.br/docs/obter-credenciais/

# Autorização para Credenciais de Produção

**Último passo antes de colocar a integração em produção**

Neste [formulário](https://forms.gle/Z3M6TGhf2GMVmzH56), procederemos ao registro das informações necessárias para que sua empresa se torne nossa parceira, assegurando o cumprimento das boas práticas descritas em nossa documentação e o seguimento dos passos essenciais para uma integração bem-sucedida.

# Requisitos Obrigatórios

**IMPORTANTE:**  Antes de realizar o preenchimento do formulário, certifique-se que os seguintes passos foram implementados:

# 1) Cadastro do Usuario Prescritor

Verifique se o cadastro do prescritor foi realizado contendo todas as informações listadas abaixo:

* Nome e Sobrenome
* Registro Profissional + UF (O Registro pode ser o número de registro CRM, CRO, COREN, CRMV, CRF, CRN, CREFITO, CRP, CRFa ou CREF)
* E-mail
* Especialidade
* Data de Nascimento
* CPF

# 2) Configurando o Paciente

O comando é `setPaciente` utilizado para enviar os dados do paciente para a prescrição da Memed. Verifique se o comando `setPaciente` foi implementado contendo todas as informações listadas abaixo:

* Nome e Sobrenome
* E-mail
* Telefone celular (Exemplo: 11999999999)
* Data de Nascimento
* CPF

Confira [Comandos Mdhub](/docs/frontend/comandos-mdhub)

# 3) Eventos

Caso esteja salvando a receita gerada no prontuário do paciente, implementar os eventos:

* [`prescricaoImpressa`](/docs/frontend/eventos-mdhub/prescricao-impressa) (para capturar o momento em que a prescrição foi emitida e recuperar os dados para o prontuário)
* [`prescricaoExcluida`](/docs/frontend/eventos-mdhub/prescricao-excluida) (para evitar que prescritor tente acessar um documento que foi excluído).
* Obs: a receita pode ser excluída pelo prescritor no histórico ou ao editá-la, e se ele tentar abrir uma receita salva no prontuário que foi excluída, vai dar erro.

  Confira [Eventos Mdhub](/docs/frontend/eventos-mdhub)

# 4) Termo de Responsabilidade

A Memed se resguarda o direito de avaliar a sua Integração em até 180 dias após a liberação das Chaves de Produção serem enviadas e de, eventualmente, revogar as mesmas em caso de não-cumprimento das Boas Práticas apontadas na documentação e validadas neste [formulário](https://forms.gle/mjPRJpaJ1EsKZp18A).

# 5) A permissão será revogada caso:

* O cadastro do prescritor não esteja completo.
* Sejam identificadas falhas de segurança no front-end do parceiro, como deixar as credenciais  **API-KEY**  e  **SECRET-KEY**  visíveis.
* Features desativadas com o comando [setFeatureToggle](/docs/frontend/comandos-mdhub/set-feature-toggle) estejam em funcionamento inadequadamente.
* Revisaremos o fluxo de [capturar uma prescrição](/docs/frontend/eventos-mdhub/prescricao-impressa).
