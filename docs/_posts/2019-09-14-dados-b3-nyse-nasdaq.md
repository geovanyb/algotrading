---
layout: post
title: Obtenção de cotações diárias da B3, NYSE e NASDAQ
tags: b3, byse, nasdaq, dados
---

A obtenção de dados de cotações é uma constante do algotrader. Enquanto ele está testando suas estratégias, ele não precisa de cotações atualizadas. É apenas quando ele vai operacionalizar sua estratégia que ele precisa ter os dados atualizados.

No caso aqui, vamos abordar a optenção de dados diários, ou dados End-Of-Day (EOD), de fonte gratuitas. A obtenção de fonte pagas já é bem coberto nos tópicos de ajuda dos provedores.

### 1. Tipos de cotações

As cotações diárias apresentam normalmente os campos DATE, OPEN, HIGH, LOW, CLOSE, NEG, VOL, ADJ, a saber:
- DATE: data da cotação, na forma de um string. Essa data pode ser convertida para um formato binário de data, conforme a base de data escolhida;
- OPEN: preço de abertura, que é a cotação da primeira negociação realizada naquela data, no leilão de abertura;
- HIGH: preço mais alto, que é a mais alta cotação negociada naquela data;
- LOW: preço mais baixo, que é a mais baixa cotação negociada naquela data;
- CLOSE: preço de fechamento, que é a cotação negociada no leilão de fechamento daquela data;
- NEG: número de papéis negociados;
- VOL: volume financeiro dos papéis negociados;
- ADJ CLOSE: ajuste, que é um coeficiente que indica o percentual de ajuste dos preços em decorrência do pagamnto de proventos. Esse parâmetro está presente apenas em cotações ajustadas.
- DIVIDENDS: proventos em dinheiro pagos naquela data, por ação, para o detentor do papel. Esse parâmetro está presente apenas em cotações ajustadas. 
- SPLITS: fator que corresponde a um evento de agrupamento/desdobramento. Esse parâmetro está presente apenas em cotações ajustadas.

Logo, as cotações obtidas podem ser as ajustadas e as não ajustadas a eventos/dividendos. Nas cotações não-ajustadas os preços apresentados são os que foram negociados naquela data.
Essas cotações são interessantes para avaliar o interesse do mercado pelo papel, já que os papéis de maior interesse têm suas cotações aumentadas com o passar do tempo. Não é incomum encontrar papéis que pagam bons dividendos apresentarem suas cotações não-ajustadas com pouca evolução nos últimos anos.
Também, para quem avalia estratégias com opções, as cotações não-ajustadas estão casadas com os strikes das opções. Como o pagamento de dividendos altera o valor de strike das opções, nas cotações não-ajustadas o pagamento de dividendos resulta em uma redução da cotação na data ex-dividendos, e também no strike das opções. Quem usa cotações não-ajustadas para análise de estratégias com opções deve manter uma série histórica do strike das opções. Assim, a lógica a ser aplicada na data de exercício deve levar em conta o strike da opção e a cotação não ajustada, conforme as regras em vigor.

As cotações ajustadas refletem a evolução de valor de um papel. Isso porque, quando se paga dividendos, isso corresponde a valor retornado para o acionista, na forma de uma parte do patrimônio da empresa. Por essa razão a cotação sore um desconto da data ex-dividendos. Da mesma forma, cotações ajustadas não apresentam saltos devidos a eventos de grupamento/desdobramento. Isso porque esses eventos, quando ocorrem, não implicam em alteração de valor, tendo impacto apenas na quantidade de papéis o investidor possui. Mas para que o investidor possa produzir o mesmo resultado em termos de valorização, ele precisa usar os proventos para comprar mais ações.

Mas uma comparação entre cotações ajustadas e cotações não-justadas pode permitir separar o percentual da valorização do papel foi em decorrência do pagamento de proventos, e qual percentual vem do interesse de mercado, que implica em aumento de capital acumulado devido ao aumento da cotação. Claro que é preciso para isso aplicar às cotações não-ajustadas um ajuste para grupamento/desdobramento, para, quando comparar com cotações ajustadas, restar apenas o efeito dos proventos.

Cotações ajustadas são geralmente usadas em gráficos de históricos de preços de ativos financeiros em sites abertos.

Por exemplo, na figura a seguir vemos em um só gráfico as cotações ajustadas e não ajustadas de WEGE3. De acordo com o site [da empresa WEGE na B3](http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/ResumoEventosCorporativos.aspx?codigoCvm=5410&tab=3&idioma=pt-br), houve eventos de bonificação em ações no dia 24/04/2018 e desdobramento em 31/03/2015. 
Ambos os eventos se refletem nas cotações não ajustadas (curva em azul) como saltos nas cotações, enquanto que o mesmo não se observa nas cotações ajustadas.

&nbsp;
<a href="{{site.baseurl}}/images/wege3_cotacoes_ajustadas_nao_ajustadas.png"><img src="{{site.baseurl}}/images/wege3_cotacoes_ajustadas_nao_ajustadas.png" alt="drawing" width="100%">
</a>
&nbsp;

Já no caso do papel ALSC3, com o qual não houve grupamento, desdobramento ou bonificação nos últimos 10 anos, não se espera ver saltos nas cotações não-ajustadas. E se tivesse havido saltos, teria sido em decorrência de alguma notícia ou evento externo. 
A figura a seguir mostra então ambas as cotações, em que a diferença entre elas se deu pelo pagamento de proventos em dinheiro.

&nbsp;
<a href="{{site.baseurl}}/images/alsc3_cotacoes_ajustadas_nao_ajustadas.png"><img src="{{site.baseurl}}/images/alsc3_cotacoes_ajustadas_nao_ajustadas.png" alt="drawing" width="100%">
</a>
&nbsp;

 
### 2. Cotações B3

A B3 fornece gratuitamente (até a data desse artigo) arquivos com séries de cotações não-ajustadas no link [Cotações históricas](http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/cotacoes-historicas/).
Nessa mesma página tem um documento que descreve o formato do arquivo de dados. Nesse arquivo tem informações completas sobre ações, FIIs e opções. 

Já para cotações ajustadas, uma fonte gratuita é o site [Yahoo Finance!](https://finance.yahoo.com/). Nesse site, basta buscar por um papel e aparecerá uma página com informações sobre ele. Em uma aba "Historical Data" é possível baixar as cotações.
Para quem conhece de programação, é possível ver o comando com o link para baixar os dados, e implementar rapidamente um código para baixar os dados em qualquer liguagem de programação moderna. 

Há quem coloque em dúvida a qualidade de dados gratuitos do site Yahoo Finance. Logo, pode valer a pena comparar com outras bases. Pessoalmente eu assino um provedor de dados no Brasil para obter tais cotações.

### 3. Cotações NYSE/Nasdaq

Para as maiores bolsas do mundo, há algumas fontes de dados diários gratuitas, entre eles o próprio [Yahoo Finance!](https://finance.yahoo.com/).

### 4. Scripts em Python

No repositório deste blog foi disponibilizado [código em Python para baixar dados](https://github.com/geovanyb/algotrading/code/cotacoes) das bases citadas acima e armazenar na forma de arquivos .CSV em pasta local. 
Uma descrição dos scripts é apresentada no arquivo [README.md](https://github.com/geovanyb/algotrading/code/cotacoes/README.md).

Arquivos CSV são facilmente importáveis em programas proprietários ou em códigos próprios, apesar de serem pouco eficientes em termos de espaço em disco.
  
