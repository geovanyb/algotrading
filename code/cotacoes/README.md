# Cotações B3, NYSE e NASDAQ

O código disponibilizado permite a atualização de dados das bolsas B3, NYSE e NASDAQ.

Na B3 são obtidas cotações ajustadas e não-ajustadas, além de uma descrição de cada papel. No caso da NYSE e da NASDAQ obtém-se apenas cotações ajustadas a proventos e eventos corporativos.

Esse código é disponibilizado para servir de base de desenvolvimento para outras bolsas e ativos. Ele não será atualizado com frequência. 

# Estrutura das pastas

Há três pastas de base: *carteiras*, *fontes* e *dados*.

A pasta *carteiras* contém arquivos de texto com universos de interesse. Em cada universo de interesse existe um conjunto de ações. Por exemplo, no caso do Índice Bovespa da B3, o arquivo *IBOV.sa.txt* contém todos os códigos de papéis que compõem o índice. 
Da mesma forma existem outros universos de interesse que agrupam papéis por setores ou por índices ou fundos imobiliários. Quando vai testar uma estratégia, o algotrader o aplica a todos os papéis de um universo de interesse, de acordo com a liquidez ou amplitude da cobertura. *ALL.sa.txt* contém todos os papéis da B3. 
*NYSE.txt* e *NASDAQ.txt* contém o mesmo para as bolsas NYSE e NASDAQ, respectivamente. Já *FII.sa.txt* contém a listagem de papéis de fundos imobiliários.

A pasta *fontes* contém arquivos grandes que são baixados de uma só vez, para depois serem processados no sentido de gerar os arquivos da pasta *dados*. 

Para a B3, estão sendo atualizados apenas ações e FIIs. A fonte de dados não-ajustados contém também cotações históricas para opções. A extração de cotações para opções ainda não está implementada nessa versão. O algotrader pode consultar o arquivo *fontes\b3\series_historicas\SeriesHistoricas_Layout.pdf* para ver como é feita a extração de dados e implementar a leitura de opções. 

# Uso indicado

Sempre que for necessário atualizar a base de dados, é necessário primeiro atualizar a base de fontes rodando o script *atualizar_bases.py*. 
Essencialmente esse script vai baixar o arquivo de dados históricos da B3, e os títulos negociáveis da B3, NYSE e NASDAQ.
No caso de dados históricos da B3, a linha *atualizar_b3_series_historicas(2019)* atualiza apenas o ano de 2019, sendo 2019 o ano atual. Claro que no ano seguinte, já se deve alterar esse número paa 2020. Cuidado deve-se ter para a primeira atualização do ano, quando se deve antes atualizar do ano anterior para se ter certeza que a base de fontes vai ter os dados das últimas negociações do ano anterior. Para o primeiro uso, sugere-se atualizar a base de 1986 até o ano presente. Esse arquivo de fontes da B3 é atualizado pela bolsa, normalmente, até as 21:00. No entanto, já se percebeu que essa atualização não foi feita até esse horário, chegando a ficar até um dia sem atualizar. Fique atento!

Para atualizar a base de dados, basta executar o script *atualizar_dados.py*. A base de dados e seu universo de interesse estão explícitos na função *main*. Caso deseja atualizar apenas os dados de uma bolsa em específico ou de outro universo de interesse, basta comentar ou alterar o código dessa função. A atualização da base de dados somente será afetiva se a base de fontes tiver sido atualizada.

Já com menos frequência, talvez mensalmente, pode-se atualizar a base de universos de interesse da pasta *carteiras*. Isso é feito pelo script *atualizar_carteiras.py*.
 
# Módulo cotacoes.py

Esse módulo tem como objetivo fornecer funções para inicialização da lista de papéis de um determinado universo de interesse, ou de uma lista de universos de interesse. Há ainda uma função que, a partir de uma lista de papéis, retorna uma matriz de pandas com as cotações.

O seguinte trecho de código mostra como montar um pandas com cotações de papéis que compõem o Índice Brasil Amplo (IBRA):

    fonte_dos_dados = 'b3'
    cotacoes_path = '.'
    codigos_da_carteira = cotacoes.carregar_codigos(['IBRA.sa'],cotacoes_path=cotacoes_path)
    carteira = cotacoes.iniciar_carteira(codigos_da_carteira,verbose=True)
    carteira = cotacoes.carregar_cotacoes_eod(carteira, fonte=fonte_dos_dados, cotacoes_path=cotacoes_path, verbose=True)
 
