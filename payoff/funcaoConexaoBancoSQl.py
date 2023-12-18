import pyodbc  #utilizado para acesso ao sql

def conexao_banco_sqlServer():
    server = "DESKTOP-9UBEH2T"
    database = "mql5_b3"
    username = "sa"
    password = "Zocca171416"

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn
