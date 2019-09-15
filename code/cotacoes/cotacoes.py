##################################################################################
### _testar_modulo: função interna para testar o módulo
##################################################################################
def _testar_modulo():

#    str_code = 'print(carregar_codigos([\'IBOV.sa\'],cotacoes_path=\'../cotacoes\'))'
#    print('\nExecutando "'+str_code+'":')
#    exec(str_code)
#    
#    str_code = 'print(carregar_codigos([\'PETR4.sa\'],cotacoes_path=\'../cotacoes\'))'
#    print('\nExecutando "'+str_code+'":')
#    exec(str_code)

    carteira = iniciar_carteira(carregar_codigos(['PETR4.sa','VALE3.sa','BOVA11.sa']), verbose=False)
    carteira = carregar_cotacoes_eod(carteira, fonte='b3', verbose=True)
#    print(carteira)
    
##################################################################################
### carregar_codigos
##################################################################################
def iniciar_carteira(codigos_da_carteira, verbose=False):

    carteira = []
    for codigo in codigos_da_carteira:
        carteira.append({'codigo':codigo})
        
    return carteira

##################################################################################
### carregar_codigos
##################################################################################
def carregar_cotacoes_eod(carteira, fonte='b3', cotacoes_path='.', verbose=False):

    import os
    import pandas as pd
#    import datetime
    
    if verbose:
        print("*** Carregando cotações EOD...")
    for ncarteira in range(len(carteira)):
        filename_csv = cotacoes_path+'/dados/'+fonte+'/cotacoes_diarias/'+carteira[ncarteira]['codigo']+'.csv'
        if os.path.isfile(filename_csv):
            carteira[ncarteira]['cotacoes_diarias'] = pd.read_csv(filename_csv) 
            if verbose:
                if len(carteira[ncarteira]['cotacoes_diarias']['date'].index)>0:
                    min_date = min(pd.to_datetime(carteira[ncarteira]['cotacoes_diarias']['date'],format='%d/%m/%Y'))
                    max_date = max(pd.to_datetime(carteira[ncarteira]['cotacoes_diarias']['date'],format='%d/%m/%Y'))
                    print('    ['+carteira[ncarteira]['codigo']+'] Carregadas cotações EOD base de dados "'+fonte+'" de',min_date.strftime("%d/%m/%Y"),'a',max_date.strftime("%d/%m/%Y"))
                else:
                    carteira[ncarteira]['cotacoes_diarias'] = pd.DataFrame(columns=('date','open','high','low','close','neg','vol'))
                    if verbose:
                        print('    ['+carteira[ncarteira]['codigo']+'] Não havia cotações disponíveis na base de dados "'+fonte+'"')
        else:
            carteira[ncarteira]['cotacoes_diarias'] = pd.DataFrame(columns=('date','open','high','low','close','neg','vol'))
            if verbose:
                print('    ['+carteira[ncarteira]['codigo']+'] Não havia cotações disponíveis na base de dados "'+fonte+'"')

        
#        carteira[ncarteira]['cotacoes_diarias'] = 0
        
#    print(carteira)
    
    return carteira

##################################################################################
### carregar_codigos
##################################################################################
def carregar_codigos(lista_de_nomes_da_carteira, cotacoes_path='.'):

    import os
    
    tickers = []
    for nome_da_carteira in lista_de_nomes_da_carteira:
#        print(nome_da_carteira)
        filename = cotacoes_path+"/carteiras/"+nome_da_carteira+'.txt'
        if os.path.isfile(filename):
            # Se existe lista de carteira, incluir conteúdo da lista
            file = open(filename, "r")
            next(file)
            for line in file:
                if line.strip() not in tickers:
                    tickers.append(line.strip())
            file.close()
        else:
            # Se não existe lista de carteira, incluir o nome pois representa um papel específico
            tickers.append(nome_da_carteira)

    return tickers


##################################################################################
### rotinas de teste
##################################################################################
if __name__== "__main__":
    _testar_modulo()
