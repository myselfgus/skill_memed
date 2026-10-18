https://doc.memed.com.br/docs/duvidas-frequentes/outras-duvidas/

# Outras Dúvidas

### Quero automatizar as configurações de cabeçalho e rodapé com o logo do plano de saúde do paciente para cada atendimento. Como faço?

Basta consultar a seção [**Impressão**](/docs/backend/impressao). Através dessas opções de impressão é possível definir uma rotina de atualização para o prescritor.

### Já atualizei os dados de cadastro do prescritor, mas o endereço ou telefone continua saindo errado no receituário especial.

Os dados no receituário especial são definidos através do [**setWorkplace**](/docs/como-fazer/gestao-do-prescritor#setworkplace).

### Quais são as estilizações disponíveis na Memed?

As personalizações disponíveis podem ser consultadas na seção [Estilização da prescrição](/docs/frontend/estilizar-front).

### O status do prescritor está em análise e não consigo deixar como ativo. Como faço?

O status retornado nas consultas e cadastro de prescritores são apenas utilizados em outros sistemas da Memed. O status "Em análise" não impede o prescritor de utilizar a Memed.

### Como faço para desabilitar o nome do laboratório nas prescrições do prescritor?

O parametro responsável pelo nome do laboratório é o `mostrar_nome_fabricante` nas opções de [**receituário**](/docs/backend/impressao), ele deve ser setado como `false`.

### Não vejo necessidade de manter o mini histórico da Memed, pois já tenho uma cópia no meu prontuário. Qual o impacto de desabilitar?

Não haverá impacto algum. O mini histórico da Memed é util para uma reemissão na abertura do módulo, porém,
caso deseje desabilita-lo, é possível realizar através das opções de Ativar ou desativar
[**funcionalidades**](/docs/frontend/comandos-mdhub).

### Quero mandar a especialidade médica estruturada, mas não encontrei as mesmas especialidades que tenho na minha base (subespecialidades). O que posso fazer?

Sabemos que os profissionais da saúde podem ser de diferentes especialidades.

Contudo, no momento, é possível cadastrar apenas uma especialidade por prescritor e parceiro na Memed. A lista de especialidades é curada por um time de inteligencias clinicas e atualizada regularmente, caso a sua especialidade principal não esteja listada, você pode entrar em contato com o nosso suporte para solicitação, e iremos avaliar a inclusão da especialidade conforme os conselhos de prescritores.

### Como consigo subir modelos favoritos de receita para os prescritores de maneira massiva com texto livre?

Para protocolos de prescritores, consulte a seção [**Protocolos**](/docs/backend/protocolos).

### Seria possível criar um login teste no Memed Standalone para que eu (parceiro) possa fazer demonstrações comerciais com meus clientes? Se não, como posso permitir que colaboradores consigam acessar a Memed?

Não, para uso de demonstrações para clientes, sugerimos que utilizem o ambiente de homologação. Para isso, é necessário uma minima integração com o ambiente.

### O que devo fazer quando a API retorna que há um cadastro duplicado?

As chaves de API de homologação são de uso compartilhado, portanto, um dado utilizado no cadastro pode ter sido utilizado antes e acusar duplicidade. Nesse caso, sugerimos que utilize outros dados para seu teste.

Caso a duplicidade aconteça em ambiente de produção, sugerimos que recupera o cadastro duplicado e utilize o mesmo afim de evitar novas tentativas de cadastro duplicado.

### Como saber se a receita foi assinada ou não?

Para usuários prescritores, essa informação ficará disponível na receita emitida, no seu rodapé, indicando que a receita possui assinatura e informações para validação da mesma.

Para pacientes, a prescrição digital também recebe essa informação.

Para fins de desenvolvimento, no evento da prescrição [**prescricaoImpressa**](/docs/frontend/eventos-mdhub/prescricao-impressa) será devolvido o objeto `signed` com valor `true` ou `false` indicando o status da assinatura no documento.
