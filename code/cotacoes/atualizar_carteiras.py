from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from subprocess import check_output
from PIL import Image
import re
import datetime, time
import random
import os, shutil

##################################################################################
### Main
##################################################################################
def main():
    
    print("\n*** Atualização das carteiras!")
    atualizar_do_arquivo_b3_titulos_negociaveis('ALL.sa')
    atualizar_do_arquivo_b3_titulos_negociaveis('FII.sa')
    atualizar_do_arquivo_b3_indices('BDRX.sa');
    atualizar_do_arquivo_b3_indices('IBOV.sa');
    atualizar_do_arquivo_b3_indices('IBRA.sa'); 
    atualizar_do_arquivo_b3_indices('IBXL.sa'); 
    atualizar_do_arquivo_b3_indices('IBXX.sa'); 
    atualizar_do_arquivo_b3_indices('ICO2.sa'); 
    atualizar_do_arquivo_b3_indices('ICON.sa'); 
    atualizar_do_arquivo_b3_indices('IDIV.sa'); 
    atualizar_do_arquivo_b3_indices('IEEX.sa'); 
    atualizar_do_arquivo_b3_indices('IFIX.sa'); 
    atualizar_do_arquivo_b3_indices('IFNC.sa'); 
    atualizar_do_arquivo_b3_indices('IGCT.sa'); 
    atualizar_do_arquivo_b3_indices('IGCX.sa'); 
    atualizar_do_arquivo_b3_indices('IGNM.sa'); 
    atualizar_do_arquivo_b3_indices('IMAT.sa'); 
    atualizar_do_arquivo_b3_indices('IMOB.sa'); 
    atualizar_do_arquivo_b3_indices('INDX.sa'); 
    atualizar_do_arquivo_b3_indices('ISEE.sa'); 
    atualizar_do_arquivo_b3_indices('ITAG.sa'); 
    atualizar_do_arquivo_b3_indices('IVBX.sa'); 
    atualizar_do_arquivo_b3_indices('MLCX.sa'); 
    atualizar_do_arquivo_b3_indices('SMLL.sa');
    atualizar_do_arquivo_b3_indices('UTIL.sa');
#    atualizar_da_internet_b3_etf('ETF.sa'); # a implementar

    atualizar_do_arquivo_quandl_titulos_negociaveis('NYSE')
    atualizar_do_arquivo_quandl_titulos_negociaveis('NASDAQ')

    print("\n*** Processo concluído!")

    return

##################################################################################
### atualizar_do_arquivo_b3_titulos_negociaveis
##################################################################################
def atualizar_do_arquivo_quandl_titulos_negociaveis(nome_da_carteira):

    print('Atualizando carteira '+nome_da_carteira+'...')

    import pandas as pd
    
    fout = open('carteiras/'+nome_da_carteira+'.txt', 'wt')
    
    tables = pd.read_csv('fontes/quandl/titulos_negociaveis/ticker_list.csv')
    contador = 0
    for i, row in tables.iterrows():
        exchange = row['Exchange'] 
        if row['Exchange']==nome_da_carteira:
            contador += 1
            codename = row['Ticker']
            codename = codename.replace(' ','');
            codename = codename.upper();
            print('  Encontrado código '+codename)
            fout.write(codename+'\n')                

     
    fout.close()
     
    return

##################################################################################
### atualizar_do_arquivo_b3_titulos_negociaveis
##################################################################################
def atualizar_do_arquivo_b3_indices(nome_da_carteira):

    print('Atualizando carteira '+nome_da_carteira+'...')

    import pandas as pd
    
    fout = open('carteiras/'+nome_da_carteira+'.txt', 'wt')
    
    nome_da_carteira = nome_da_carteira.replace('.sa','')
    tables = pd.read_html('fontes/b3/indices/AcoesIndices.MaiAgo.2019.xls',header=0, skiprows=2) # Returns list of all tables on page
    tb = tables[0] # Select table of interest    
    contador = 0
    for row in tb[nome_da_carteira]:
        if isinstance(row, str):
            if row[0].isalpha():
                contador += 1
                codename = row
                codename = codename.replace(' ','');
                codename = codename.upper();
                print('  Encontrado código '+codename)
                fout.write(codename+'.sa\n')                

     
    fout.close()
     
    return

##################################################################################
### atualizar_do_arquivo_b3_titulos_negociaveis
##################################################################################
def atualizar_do_arquivo_b3_titulos_negociaveis(nome_da_carteira):

    print('Atualizando carteira '+nome_da_carteira+'...')
    contador = 0
    fin  = open('fontes/b3/titulos_negociaveis/TITULOS_NEGOCIAVEIS.TXT', 'rt')
    fout = open('carteiras/'+nome_da_carteira+'.txt', 'wt')
    for line in fin:
        if len(line.strip())>140:
            flag = True
            if nome_da_carteira=='ALL.sa':
                flag = flag & (line.strip().find('02',0,2)>=0)
                flag = flag & ( (line.strip().find('LOTE PADRAO',21,32)>=0) | (line.strip().find('RECUPERACAO JUDICIAL/EXTRAJUDICIAL',21,55)>=0) )
                flag = flag & ( (line.strip().find('ON',133,135)>=0) | (line.strip().find('PN',133,135)>=0) | (line.strip().find('UNT',133,136)>=0) )
            if nome_da_carteira=='FII.sa':
                flag = flag & (line.strip().find('02',0,2)>=0)
                flag = flag & (line.strip().find('FUNDOS IMOBILIARIOS',21,40)>=0)
                
            if flag:
                contador += 1
                codename = line.strip()[2:13]
                codename = codename.replace(' ','');
                codename = codename.upper();
                print('  Encontrado código '+codename)
                fout.write(codename+'.sa\n')
            

    fin.close()
    fout.close()

    print("\n*** Foram carregados ",contador," códigos")
    
    return


##################################################################################
### Chamada de main()
##################################################################################
if __name__== "__main__":
    main()