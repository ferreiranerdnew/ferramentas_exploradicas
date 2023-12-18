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
    comando = f"""SELECT * FROM OPCOES_TRAVAS
                    where status = 'A'
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
df_agrupado = df_opcoes.groupby(['papel', 'pedido']).size().reset_index(name='count')

for index, row in df_agrupado.iterrows():
    empresas = row['papel']
    dados_empresa = df_opcoes[df_opcoes['papel'] == empresas]
    print(dados_empresa)




    print(empresas)

# op1={'op_type': 'c', 'strike': 36.77, 'tr_type': 's', 'op_pr': 0.76}
# op2={'op_type': 'c', 'strike': 37.27, 'tr_type': 'b', 'op_pr': 0.60}
# op3={'op_type': 'p', 'strike': 34.52, 'tr_type': 's', 'op_pr': 0.51}
# op4={'op_type': 'p', 'strike': 34.02, 'tr_type': 'b', 'op_pr': 0.41}

# title_1 = 'PETR4 IRON 18/12/2023'

# op_list=[op1, op2, op3, op4]
# op.multi_plotter(spot=35.84,spot_range=10, op_list=op_list, title_1=title_1)


