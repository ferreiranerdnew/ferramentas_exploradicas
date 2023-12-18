# pip install opstrat

import opstrat as op
import funcaoConexaoBancoSQl as ConectSQL
import pandas as pd

def opcoes_estrategia():
    
    tabela_2 = 'OPERACOES'  # verificar esta planilah pdoe modificar
    # chamada da conexão
    cnxn6 = ConectSQL.conexao_banco_sqlServer()
    #curs = cnxn5.cursor()
    # Montagem script sql para execução no banco de dados
    comando = '''SELECT 
                        '{
                            "op_type": "' + op_type + '",
                            "strike": "' + CAST(strike AS VARCHAR) + '",
                            "tr_type": "' + tr_type + '",
                            "op_pr": "' + CAST(op_pr AS VARCHAR) + '"
                        }' AS ops_1,
                        *
                    FROM OPCOES_TRAVAS
                    '''

    # executando script na conexão do banco de dados que foi aberta
    df_opcoes = pd.read_sql(comando, cnxn6)

    # Resetando o index por uma questão organizacional
    df_opcoes = df_opcoes.reset_index()

    return df_opcoes   
#######################################################################################
########################### Função matriz do carregamento da sinformações##############
#######################################################################################
# Inicializando os dicionários
# op1 = {}
# op2 = {}
# op3 = {}
# op4 = {}
# op1 = {
#     'op_type': 0,
#     'strike': 0,
#     'tr_type': 0,
#     'op_pr': 0
# }
# op2 = {
#     'op_type': 0,
#     'strike': 0,
#     'tr_type': 0,
#     'op_pr': 0
# }
# op3 = {
#     'op_type': 0,
#     'strike': 0,
#     'tr_type': 0,
#     'op_pr': 0
# }
# op4= {
#     'op_type': 0,
#     'strike': 0,
#     'tr_type': 0,
#     'op_pr': 0
# }

df_opcoes = ""
df_opcoes = opcoes_estrategia()
df_agrupado = df_opcoes.groupby(['papel', 'pedido','price_montagem']).size().reset_index(name='count')

for index, row in df_agrupado.iterrows():

    primeira_passagem = True
    empresas = row['papel']
    ondens_position= row['count']
    preco_mont= row['price_montagem']
    dados_empresa = df_opcoes[df_opcoes['papel'] == empresas]


    
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
    

    # title_1 = f'''{empresas} IRON 18/12/2023'''
    # if ondens_position == 2:
    #     op_list=[op1, op2]
    # else:
    #     op_list=[op1, op2, op3, op4]
    # op.multi_plotter(spot=preco_mont,spot_range=10, op_list=op_list, title_1=title_1,spotInicial = preco_mont)
            
    # Limpar os dicionários
    # op1.clear()
    # op2.clear()
    # op3.clear()
    # op4.clear()



# op1={'op_type': 'c', 'strike': 36.77, 'tr_type': 's', 'op_pr': 0.76}
# op2={'op_type': 'c', 'strike': 37.27, 'tr_type': 'b', 'op_pr': 0.60}
# op3={'op_type': 'p', 'strike': 34.52, 'tr_type': 's', 'op_pr': 0.51}
# op4={'op_type': 'p', 'strike': 34.02, 'tr_type': 'b', 'op_pr': 0.41}

# title_1 = 'PETR4 IRON 18/12/2023'

# op_list=[op1, op2, op3, op4]
# op.multi_plotter(spot=35.84,spot_range=10, op_list=op_list, title_1=title_1)


