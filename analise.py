import pandas as pd

def calcular_roi(investimento, receita):
    if investimento == 0:
        return 0
    roi = ((receita - investimento) / investimento) * 100
    return roi

tabela = pd.read_csv('dados_campanha.csv')

tabela['roi_percentual'] = ((tabela['receita'] - tabela['investimento']) / tabela['investimento']) * 100

print("--- Resultado das Campanhas ---")
print(tabela)