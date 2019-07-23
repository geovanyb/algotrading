---
layout: post
title: O que penso sobre algotrading
tags: algotrading
---

Algotrading (trading algorítmico ou ainda trading quantitativo) é uma modalidade de trading que é feita com forte ajuda de algoritmos. Não se trata de retirar a componente emocional do processo de trading, mas sim de buscar fazer melhor. Também não se trata (apenas) de fazer um robô que vai trabalhar por você para seu patrimônio financeiro crescer enquanto dorme.

Algotrading implica em muito esforço e estudo, até que um algoritmo de negociação se mostre consistente e possa ser empregado no mercado. O algotrader é alguém que desenvolve suas próprias estratégias, que podem ser aplicadas a qualquer mercado. Ele estuda aquele mercado, faz ensaios e testes, desenvolve suas ferramentas e faz mais testes. É um ciclo contínuo, de aprimoramento e de estudo. Mas os resultados, pelo menos para mim, mostram que vale a pena seguir esse caminho. 

Não seja preguiçoso. Gosta de reaproveitar códigos de terceiros? Boa sorte! Não se esqueça que um grande tombo no mercado pode ser fatal. Por isso é importante você entender de todo o processo. Se ainda está com preguiça, então algotrading não é para você.

É fácil? Não, assim como qualquer atividade profissional é necessário se preparar. Por onde começar? Comece sendo trader, e entenda como o mercado funciona. Se tiver um mínimo de habilidade com cálculo, computação ou engenharia, já é boa parte do caminho. 

Precisa entender de machine learning? Bom, faço pesquisa com robótica há mais de 20 anos, e raras vezes recorri a esse tipo de técnica. Sou de uma vertente de modelagem caixa cinza e estimação Bayesiana, pois gosto de partir de um conhecimento a priori ou de uma estrutura inicial, e encontrar os parâmetros que melhor explicam os dados. Embora seja também considerado machine learning, não é o tipo que mais se encontra nos livros. Claro que você pode usar machine learning, assim como pode usar um simples regressor linear para prever o que vai ocorrer com os preços de um ativo. Leve em conta que em tempo de execução não há muito "tempo para pensar".

Preciso saber de Python? Pra ser sincero, qualquer linguagem de programação já serve, embora C/C++ e Python sejam as mais comumente empregadas. Matlab e R são excelentes companheiros para prototipagem rápida. Metatrader é outra ferramenta interessante. Na figura abaixo temos um preditor de faixas de preços para o período seguinte e um indicador de probabilidade de sucesso de reversão à média computado usando histórico de dados. 

&nbsp;
<a href="{{site.baseurl}}/images/mt5-indicadores.png"><img src="{{site.baseurl}}/images/mt5-indicadores.png" alt="drawing" width="100%">
</a>
&nbsp;

Tem algotrader que usa planilhas. Eu mesmo usei por um bom tempo! Desenvolvi uma ferramenta para operar opções com cotações em tempo real fornecidas por DDE. Com um simples click de botão apareciam as melhores estratégias obtidas avaliando um grande número de combinações de papéis. Aprendi a programar em VBA para fazer esse projeto. 

Tem gente que usa até mapa astral (sério!). O que importa é usar um algoritmo, e verificar se ele funciona. 

Um algotrader entende o que é um candle e o que é gerenciamento de risco. Entender o fluxo de caixa de uma operação é ser essencial. Dados podem enganar, entenda bem o que eles significam. Entenda o que são cotações ajustadas e cotações não-ajustadas. Entenda o efeito de proventos e eventos corporativos no preço de uma ação. 

Gosta de alavancagem? Cuidado, o precipício está bem aí. Prefere ativos bastante voláteis, acreditando que é o melhor? Pode até ser que funcione, por um tempo, até algo dar errado (nem precisa ser um cisne negro). Somente gerenciamento de risco vai te manter no jogo, por muito tempo. Quando se aplica gerenciamento de risco, o tipo de mercado passa a ter menos importância. Mercado bom é aquele que você conhece bem e tem os meios de operar.

Entenda métricas, tais como índice de Sharpe, e crie suas variantes. Entenda o que é um outlier ou uma simples distribuição t de Student. Se não gosta de teoria das probabilidades, sem problema, tem espaço para todos. Que tal explorar combinações de regras usando os preços de fechamento dos últimos dias?

Desconfie de fórmulas mágicas e de propostas tentadoras. Isso não existe! E se existe, e eu um dia encontrar, não vou revelar. Pra quê ganhar com a venda de algo que por si só me deixará multi-bilionário? (entendeu a ironia?) E se você encontrar uma estratégia realmente boa em ambiente controlado, veja se não está cometendo overfitting ou usando alguma informação futura. Há formas de incluir no código testes que te permitem minimizar essa chance.

Não se prenda a um ativo, o mercado está cheio de oportunidades. Se o objetivo é lucro, e no fim é o que importa, estabeleça seu nível de tolerância a volatilidade. Pra mim, ativo financeiro é um parâmetro como qualquer outro.

Não se prenda a uma linguagem de programação ou a moda qualquer de algoritmos. Fixe-se nos conceitos e busque imaginar algo novo. Algotrading é um processo de descoberta. Backtesting e análise walkforward são seus amigos íntimos! Eles é que vão te ajudar a confirmar se há fortes chances de uma estratégia funcionar. Isso depende, claro, das condições estresse às quais o algoritmo foi exposto durante os testes.

E conte comigo para compartilhar ideias e conhecimentos. Só não compartilho minhas estratégias! Por quê não? O que funciona pra mim não funciona pra você. Não quero ser responsabilizado pelo que não posso garantir. Só eu sei o que fazer se algo der errado, e vez ou outra vai dar errado (estatisticamente). Você não saberá como resolver, mas eu sim, porque fui eu quem fez. Mas o que vou compartilhar? Aquilo que sei que fará a diferença. O restante é aprendizado.

Por último, não se esqueça das pessoas. Família e amigos são nossa sustentação. Sua profissão principal não precisa ser penalizada por causa de trading. Comece a desenvolver uma estratégia que se encaixa no seu estilo de vida e nas suas possibilidades. Não tenha pressa! Quanto mais pressa, mais risco se corre, e mais cedo a festa pode acabar. Não busque no trading uma renda extra da qual dependa para pagar as contas. Não faça empréstimo para fazer trading; não se usa renda variável para cobrir uma dívida de taxa fixa. Todos os estudos que fiz nesse sentido apontam que o melhor é começar com pouco e ir fazendo aportes (sim, tentei me convencer que não valia a pena!). No início, mesmo que tenha uma excelente taxa de retorno, seus aportes muito provavelmente serão maiores do que a rentabilidade mensal.

Swing trading pode ser muito rentável, acredite! Fazer trading uma vez por semana ou uma vez por mês também pode dar bons resultados. Já ouviu a expressão ["sell May and go away!"](https://www.investopedia.com/terms/s/sell-in-may-and-go-away.asp)? Faça uma simples análise histórica com diferentes ativos e verá que todos os meses há boas oportunidades (viva a sazonalidade!). 
