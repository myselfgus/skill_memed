https://doc.memed.com.br/docs/como-fazer/impressao-medico/

# Configurar impressão do prescritor

A Memed disponibiliza comandos via MdHub e API para configurar os dados que serão impressos no PDF da receita.

## Os seguintes comandos utilizam o MdHub:

# Set Workplace

É possível resgatar o endereço do prescritor de seu sistema para preenchê-lo no receituário Memed.
Dessa forma, o prescritor não precisa escrever manualmente seu endereço nas opções de receituário.
É comum que o prescritor atenda em diferentes lugares durante sua jornada de trabalho.
Pensando nessa situação, criamos o comando Javascript setWorkplace.

Através desse comando é possível adicionar dados do prescritor como:

* Cidade do local de trabalho;
* UF do local de trabalho
* Cadastro Nacional de Estabelecimentos de Saúde
* Nome do local de trabalho
* Endereço completo com número
* Telefone do prescritor

Com isso, o prescritor não precisará preencher os seus dados quando for prescrever um medicamento controlado, pois
eles já foram preenchidos com esse comando.

Abaixo há um exemplo de como ficaria o PDF da receita com os dados do prescritor preenchidos:

![pdf-impresso](https://cdn.memed.com.br/doc/pdf-impresso.webp)

Veja um exemplo de código utilizando o comando `setWorkPlace` abaixo:

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/frontend/comandos-mdhub/set-workplace)

# setAdditionalData

Com esse comando é possível adicionar informações extras no cabeçalho e rodapé da receita digital,
como dados do paciente, do prescritor, e local do atendimento.

Aqui está um exemplo de como ficaria os dados no cabecalho e rodapé no PDF da receita.

![exemplo-dados-header-footer](https://cdn.memed.com.br/doc/exemplo-dados-header-footer.png)

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/frontend/comandos-mdhub/set-additional-data).

### Find

Com esse comando é possível alterar o tema da prescrição do prescritor.
Cada prescritor possui até 4 temas, e cada tema tem personalizações diferentes.
Os temas podem ser trocados pelo prescritor dentro da plataforma de prescrição ou via comando MdHub.

Para saber mais sobre esse comando, leia esse artigo [aqui](/docs/frontend/comandos-mdhub/find)

### Estilizar a prescrição

É possível estilizar a cor primária da prescrição digital Memed para se adequar a cor primária do seu sistema.

Segue um exemplo de como mudar a cor da prescrição digital no modo de carregamento estático:

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/frontend/estilizar-front)

## Os seguintes comandos utilizam api da Memed:

# Configurar Impressão

Esse comando permite personalizar algumas configurações relacionadas à impressão do PDF da receita, como margens,
cabeçalho, rodapé, fonte, entre outros do PDF da receita.

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/backend/impressao#configurar-impress%C3%A3o)

# Importar um cabeçalho e/ou rodapé do PDF da receita

A Memed disponibiliza uma forma de importar um cabeçalho e/ou rodapé com base em um template (PDF).
Este é enviado para a Memed através da api, e assim será usado como imagem de fundo na prescrição.

Para mais informações sobre esse comando leia esse artigo [aqui](/docs/backend/impressao#importar-cabe%C3%A7alhorodap%C3%A9-de-um-pdf)

# Remover o cabeçalho e/ou rodapé do PDF da receita

É possível remover cabeçalho e/ou rodapé através da api da Memed.
Para saber como, leia esse artigo [aqui](/docs/como-fazer/removendo-cabecalho-rodape)
