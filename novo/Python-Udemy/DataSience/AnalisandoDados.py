import pandas as pd


#ANALISANDO UM DOCUMENTO CSV
df = pd.read_csv('servicos.csv')

df.describe()

df.columns


#ANALISANDO DADOS DE UMAS PLANILHA DE EXCEL
excel = pd.ExcelFile('Controles Firma 2018.xls')
planilha = pd.read_excel(excel, 'FOUR ONE')

planilha['À RECEBER'].sum() #somar

planilha.shape
