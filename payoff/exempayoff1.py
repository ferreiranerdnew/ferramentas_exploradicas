# pip install opstrat

import opstrat as op
import funcaoConexaoBancoSQl as ConectSQL
import pandas as pd
import yfinance as yf

def opcoes_estrategia():
    
    tabela_2 = 'OPERACOES'  # verificar esta planilah pdoe modificar
    # chamada da conexão
    cnxn6 = ConectSQL.conexao_banco_sqlServer()
    #curs = cnxn5.cursor()
    # Montagem script sql para execução no banco de dados
    comando = f"""SELECT * FROM OPCOES_TRAVAS
                    where status = 'A'
                    --and papel ='ABEV3'
                    --group by pedido, papel
                    order by pedido
                    """

    # executando script na conexão do banco de dados que foi aberta
    df_opcoes = pd.read_sql(comando, cnxn6)

    # Resetando o index por uma questão organizacional
    df_opcoes = df_opcoes.reset_index()

    return df_opcoes   
#######################################################################################
########################### Função matriz do carregamento da sinformações##############
#######################################################################################


df_opcoes = ""
df_opcoes = opcoes_estrategia()
df_agrupado = df_opcoes.groupby(['papel', 'pedido','price_montagem', 'data_compra']).size().reset_index(name='count')

for index, row in df_agrupado.iterrows():

    primeira_passagem = True
    empresas = row['papel']    
    data_compra =row['data_compra']  
    ondens_position= row['count']
    preco_mont= row['price_montagem']
    dados_empresa = df_opcoes[df_opcoes['papel'] == empresas]

    ticker_symbol = empresas+".SA" 
    # Obtenha os dados do ticker
    ticker = yf.Ticker(ticker_symbol)
    # Obtenha o histórico de preços
    historico = ticker.history(period="1d")  # Obtém o histórico para o último dia
    # Obtenha o valor da última cotação (último preço)
    ultima_cotacao = historico['Close'].iloc[-1]

    if ondens_position == 2:
        for index, row_1 in dados_empresa.iterrows():
            if primeira_passagem:
                op1 = {
                    'op_type': row_1['op_type'],
                    'strike': row_1['strike'],
                    'tr_type': row_1['tr_type'],
                    'op_pr': row_1['op_pr']
                }
                primeira_passagem = False
            elif 'op2' not in locals():
                op2 = {
                    'op_type': row_1['op_type'],
                    'strike': row_1['strike'],
                    'tr_type': row_1['tr_type'],
                    'op_pr': row_1['op_pr']
                }
            elif 'op3' not in locals():
                op3 = {
                    'op_type': row_1['op_type'],
                    'strike': row_1['strike'],
                    'tr_type': row_1['tr_type'],
                    'op_pr': row_1['op_pr']
                }
            else:
                op4 = {
                    'op_type': row_1['op_type'],
                    'strike': row_1['strike'],
                    'tr_type': row_1['tr_type'],
                    'op_pr': row_1['op_pr']
                }

            title_1 = f'''{empresas} DATA INICIO {data_compra}'''
               
            if ondens_position == 2:
                op_list=[op1, op2]
            else:
                op_list=[op1, op2, op3, op4]
            op.multi_plotter(spot=preco_mont,spot_range=10, op_list=op_list, title_1=title_1,spotInicial = preco_mont)
            # Limpar os dicionários
            # del op1
            # del op2
            # del op3
            # del op4
            if 'op1' in locals():
                # Destruir op1
                del op1
            if 'op2' in locals():
                # Destruir op1
                del op2
            if 'op3' in locals():
                # Destruir op1
                del op3
            if 'op4' in locals():
                # Destruir op1
                del op4
            
    # for index, row_1 in dados_empresa.iterrows():     

    #     if primeira_passagem:
    #         op1 = {
    #             'op_type': row_1['op_type'],
    #             'strike': row_1['strike'],
    #             'tr_type': row_1['tr_type'],
    #             'op_pr': row_1['op_pr']
    #         }
    #         primeira_passagem = False
    #     elif 'op2' not in locals():
    #         op2 = {
    #             'op_type': row_1['op_type'],
    #             'strike': row_1['strike'],
    #             'tr_type': row_1['tr_type'],
    #             'op_pr': row_1['op_pr']
    #         }
    #     elif 'op3' not in locals():
    #         op3 = {
    #             'op_type': row_1['op_type'],
    #             'strike': row_1['strike'],
    #             'tr_type': row_1['tr_type'],
    #             'op_pr': row_1['op_pr']
    #         }
    #     else:
    #         op4 = {
    #             'op_type': row_1['op_type'],
    #             'strike': row_1['strike'],
    #             'tr_type': row_1['tr_type'],
    #             'op_pr': row_1['op_pr']
    #         }
    

    # title_1 = f'''{empresas} DATA INICIO {data_compra}'''

    # if ondens_position == 1:
    #     op_list=[op1]
        
    # elif ondens_position == 2:
    #     op_list=[op1, op2]
    # elif ondens_position == 3:
    #     op_list=[op1, op2, op3]
    # else:
    #     op_list=[op1, op2, op3, op4]
    # op.multi_plotter(spot=preco_mont,spot_range=10, op_list=op_list, title_1=title_1,spotInicial = preco_mont)
    # # Limpar os dicionários
    # # del op1
    # # del op2
    # # del op3
    # # del op4
    # if 'op1' in locals():
    #     # Destruir op1
    #     del op1
    # if 'op2' in locals():
    #     # Destruir op1
    #     del op2
    # if 'op3' in locals():
    #     # Destruir op1
    #     del op3
    # if 'op4' in locals():
    #     # Destruir op1
    #     del op4



