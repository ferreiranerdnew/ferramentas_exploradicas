import yfinance as yf
import numpy as np

# def optionsbidask (ticker, dataVencimento,strike):
#     # ativoTiker = yf.Ticker("mglu3.sa")
#     #opt = ativoTiker.option_chain('2021-11-19') #data de vencimento da opção
#     ativoTiker = yf.Ticker(ticker)
#     opt = ativoTiker.option_chain(dataVencimento) #data de vencimento da opção
#     ##Converter coluna em indice 
#     opt.puts.set_index('contractSymbol',inplace=True) #trasformando a primeira coluna coluna em indice
#     df1 = opt.puts
#     dadosStrikePut = df1[(df1.strike == strike)] #strike da put a ser analisado
#     putbidInter = dadosStrikePut['bid'][-1]
#     putaskInter = dadosStrikePut['ask'][-1]
    
#     return putbidInter,putaskInter

# def optionsbidaskCalls (ticker, dataVencimento,strike):
#     ativoTikercalls = yf.Ticker(ticker)
#     optcalls = ativoTikercalls.option_chain(dataVencimento) #data de vencimento da opção
#     ##Converter coluna em indice 
#     optcalls.calls.set_index('contractSymbol',inplace=True) #trasformando a primeira coluna coluna em indice
#     df1calls = optcalls.calls
#     dadosStrikecalls = df1calls[(df1calls.strike == strike)] #strike da put a ser analisado
#     callsbidInter = dadosStrikecalls['bid'][-1]
#     callskInter = dadosStrikecalls['ask'][-1]
    
#     return callsbidInter,callskInter

ticker = "MSFT"
dataVencimento = "2024-01-19"
# ativoTiker = yf.Ticker("mglu3.sa")
#opt = ativoTiker.option_chain('2021-11-19') #data de vencimento da opção
ativoTiker = yf.Ticker(ticker)
opt = ativoTiker.option_chain(dataVencimento) #data de vencimento da opção
##Converter coluna em indice 
# opt.puts.set_index('contractSymbol',inplace=True) #trasformando a primeira coluna coluna em indice
# df1 = opt.puts
# dadosStrikePut = df1[(df1.strike == strike)] #strike da put a ser analisado
# putbidInter = dadosStrikePut['bid'][-1]
# putaskInter = dadosStrikePut['ask'][-1]