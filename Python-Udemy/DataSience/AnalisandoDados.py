import pandas as pd


#ANALISANDO UM DOCUMENTO CSV
df = pd.read_csv('servicos.csv')

df.describe()

df.columns

df.count()

df.shape

df.head()


#ANALISANDO DADOS DE UMAS PLANILHA DE EXCEL
excel = pd.ExcelFile('Controles Firma 2020.xlsx')
planilha = pd.read_excel(excel, 'FOUR ONE')

planilha['À RECEBER'].sum() #somar

planilha.shape
