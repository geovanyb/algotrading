
##################################################################################
### Main
##################################################################################
def main():
    
    import time
    
    start_time = time.time()
    print("\n*** Processo iniciado!")
    
    import cotacoes
    
    # Escolher abaixo a o universo de interesse para atualizar. Os códigos válidos está na pasta 'carteiras'
#    codigos_da_carteira_b3_acoes_eod = cotacoes.carregar_codigos(['IBOV.sa'])
#    codigos_da_carteira_b3_acoes_eod = cotacoes.carregar_codigos(['IBRA.sa'])
#    codigos_da_carteira_b3_acoes_eod = cotacoes.carregar_codigos(['FII.sa'])
#    codigos_da_carteira_b3_acoes_eod = cotacoes.carregar_codigos(['IBRA.sa','FII.sa','BOVA11.sa'])
    codigos_da_carteira_b3_acoes_eod = cotacoes.carregar_codigos(['ALL.sa','FII.sa','BOVA11.sa'])
#    codigos_da_carteira_b3_acoes_eod = cotacoes.carregar_codigos(['ALL.sa'])

    codigos_da_carteira_nyse_nasdaq_acoes_eod = cotacoes.carregar_codigos(['NYSE','NASDAQ'])

    atualizar_cotacoes_e_descricoes_b3_acoes_eod(codigos_da_carteira_b3_acoes_eod)
    atualizar_cotacoes_yahoo_acoes_eod(codigos_da_carteira_b3_acoes_eod)
    atualizar_cotacoes_yahoo_acoes_eod(codigos_da_carteira_nyse_nasdaq_acoes_eod)
    
    elapsed_time = time.time() - start_time    
    print("\n*** Processo concluído em %.2f minutos!" %(elapsed_time/60))

    return

##################################################################################
### atualizar_descricoes_b3_acoes_eod
##################################################################################
def atualizar_cotacoes_yahoo_acoes_eod(codigos_da_carteira):

    import pandas as pd
    from datetime import datetime as dt
    import datetime
    import os
    import yfinance as yf
    
    # As cotações do Yahoo são ajustadas. Logo, não se pode fazer uso de atualização incremental.
    
    for codigo in codigos_da_carteira:
        filename_csv = 'dados/yahoo/cotacoes_diarias/'+codigo+'.csv';
        print("[",codigo,"] Buscando cotações...")
        df_cotacoes = pd.DataFrame(columns=('date','open','high','low','close','adj close','vol','dividends','splits'))
        # sem informação de data, baixa todo o historico
#        df_cotacoes = yf.download(codigo) 
        ticker = yf.Ticker(codigo)
        if len(ticker.info)>0:
            try:
                # Como são dados EOD, essa atualização não pode incluir a data de hoje, 
                # se for feito antes das 20:00
                if datetime.datetime.now().hour<20:
                    end_date = datetime.datetime.today()-datetime.timedelta(days=1)
                    end_date = end_date.replace(hour=20, minute=00)
                else:
                    end_date = datetime.datetime.today()
                df_cotacoes = ticker.history(period="max",auto_adjust=False,end=end_date)
                # cria coluna com data
                df_cotacoes['date'] = df_cotacoes.index
                # renomea as demais colunas para compatibilidade
                df_cotacoes.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Adj Close': 'adj close', 'Volume': 'vol','Dividends':'dividends','Stock Splits':'splits'}, inplace=True)
                # muda a ordem para manter compatibilidade com o formato de arquivo CSV usado até então
                df_cotacoes = df_cotacoes[['date','open','high','low','close','adj close','vol','dividends','splits']] 
                # muda as datas para o formato brasileiro
                df_cotacoes['date'] = df_cotacoes['date'].dt.strftime('%d/%m/%Y')
            except:
                print("[",codigo,"] Erro no download de dados historicos")
                df_cotacoes = pd.DataFrame(columns=('date','open','high','low','close','adj close','vol','dividends','splits'))
        # imprime informação
        if len(df_cotacoes.index) > 0:
            min_date = min(pd.to_datetime(df_cotacoes['date'],format='%d/%m/%Y'))
            max_date = max(pd.to_datetime(df_cotacoes['date'],format='%d/%m/%Y'))
            print("[",codigo,"] Foram extraídas cotações de",min_date.strftime("%d/%m/%Y"),"a",max_date.strftime("%d/%m/%Y"))
            # gera arquivo csv
            df_cotacoes.to_csv (filename_csv, index = None, header=True)
        else:
            print("[",codigo,"] Não há cotações disponíveis")
            # ok, não há cotações disponíveis. Se não tiver um arquivo de dados, iniciar com um vazio.
            # se houver arquivo, melhor preservar
            if os.path.isfile(filename_csv)<=0:
                df_cotacoes.to_csv (filename_csv, index = None, header=True)
                print("[",codigo,"] Criando arquivo de dados mesmo assim")

    return

##################################################################################
### atualizar_descricoes_b3_acoes_eod
##################################################################################
def atualizar_cotacoes_e_descricoes_b3_acoes_eod(codigos_da_carteira):

    import pandas as pd
    from datetime import datetime as dt
    import datetime
    import os
    
    # As cotações de séries historicas da bovespa não são ajustadas. Logo, os valores
    # passados não são alterados com o passar do tempo, e assim a atualização pode ser feito de
    # forma incremental, a partir da última data disponível na base de dados
    
    for codigo in codigos_da_carteira:
        codigo = codigo.replace('.sa','')
        filename_csv = 'dados/b3/cotacoes_diarias/'+codigo+'.sa.csv';
        print("[",codigo,"] Buscando cotações...")
        if os.path.isfile(filename_csv):
            df_cotacoes = pd.read_csv(filename_csv)
            if len(df_cotacoes['date'])>0:
                start_date = max(pd.to_datetime(df_cotacoes['date'],format='%d/%m/%Y')) + datetime.timedelta(days=1)
                n = len(df_cotacoes.index)
                min_date = min(pd.to_datetime(df_cotacoes['date'],format='%d/%m/%Y'))
                max_date = max(pd.to_datetime(df_cotacoes['date'],format='%d/%m/%Y'))
                print("    [",codigo,"] Partindo de cotações da base de dados de",min_date.strftime("%d/%m/%Y"),"a",max_date.strftime("%d/%m/%Y"))
            else:
                start_date = dt.strptime('01/01/1986','%d/%m/%Y')
                df_cotacoes = pd.DataFrame(columns=('date','open','high','low','close','neg','vol'))
                n = 0
                print("    [",codigo,"] Não há dados prévios na base")
#            return
        else:
            start_date = dt.strptime('01/01/1986','%d/%m/%Y')
            df_cotacoes = pd.DataFrame(columns=('date','open','high','low','close','neg','vol'))
            n = 0
            print("    [",codigo,"] Não há dados prévios na base")
        df_propriedades = pd.DataFrame(columns=('nome','especificação','mercado'))
        for year in range(max(1986,start_date.year),dt.today().year+1):
            print("    [",codigo,"] Processando dados do ano", year)
            file = open("fontes/b3/series_historicas/COTAHIST_A"+str(year)+".TXT", "r")
            next(file) # descarta primeira linha
            for line in file:
                line_stock_symbol = line.strip()[12:23].replace(' ','')
                if line_stock_symbol==codigo:
                    line_date = dt(int(line.strip()[2:6]), int(line.strip()[6:8]), int(line.strip()[8:10]))
#                    print(line_date)
                    if line_date >= start_date:
#                        print(line.strip())
                        line_open  = float(line.strip()[56:69].replace(' ',''))/100.0
                        line_high  = float(line.strip()[69:82].replace(' ',''))/100.0
                        line_low   = float(line.strip()[82:95].replace(' ',''))/100.0
                        line_close = float(line.strip()[108:121].replace(' ',''))/100.0
                        line_neg = int(line.strip()[147:152].replace(' ',''))
                        line_vol = int(line.strip()[170:188].replace(' ',''))
                        df_cotacoes.loc[n] = [line_date.strftime("%d/%m/%Y"), line_open, line_high, line_low, line_close, line_neg, line_vol]
                        n += 1
                        if n==1:
                            min_date = line_date
                            max_date = line_date
                        else:
                            min_date = min(line_date,min_date)
                            max_date = max(line_date,max_date)
                        # Propriedades: colocar sempre na posição inicial, para reter as propriedades da ultima cotação
                        nome = line.strip()[27:39].rstrip()
                        especificacao = line.strip()[39:49].split(' ')[0] # Pega apenas as primeira sequencia antes do primeiro espaço em branco
                        mercado_num = int(line.strip()[24:27].replace(' ',''))
                        if mercado_num==10:
                            mercado = 'VISTA'
                        elif mercado_num==12 :
                            mercado = 'EXERCÍCIO DE OPÇÕES DE COMPRA'
                        elif mercado_num==13 :
                            mercado = 'EXERCÍCIO DE OPÇÕES DE VENDA'
                        elif mercado_num==17 :
                            mercado = 'LEILÃO'
                        elif mercado_num==20 :
                            mercado = 'FRACIONÁRIO'
                        elif mercado_num==30 :
                            mercado = 'TERMO'
                        elif mercado_num==50 :
                            mercado = 'FUTURO COM RETENÇÃO DE GANHO'
                        elif mercado_num==60 :
                            mercado = 'FUTURO COM MOVIMENTAÇÃO CONTÍNUA'
                        elif mercado_num==70 :
                            mercado = 'OPÇÕES DE COMPRA'
                        elif mercado_num==80 :
                            mercado = 'OPÇÕES DE VENDA'
                        else:
                            mercado = ""
                        df_propriedades.loc[0] = [nome, especificacao, mercado]
            file.close()            
#        print(df_cotacoes.to_string())
        df_cotacoes.to_csv (filename_csv, index = None, header=True)
        if len(df_cotacoes.index) > 0:
            print("[",codigo,"] Foram extraídas cotações de",min_date.strftime("%d/%m/%Y"),"a",max_date.strftime("%d/%m/%Y"))
        else:
            print("[",codigo,"] Não há cotações disponíveis")
        if len(df_propriedades.index) > 0:
            print("[",codigo,"] O papel tem nome resumido \""+nome+"\" especificação \""+especificacao+"\" e mercado \""+mercado+"\"")
            df_propriedades.to_csv (filename_csv.replace('cotacoes_diarias','propriedades'), index = None, header=True)
        else:
            print("[",codigo,"] Não há atualização de propriedades")

    return

##################################################################################
### Chamada de main()
##################################################################################
if __name__== "__main__":
    main()