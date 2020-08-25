import pandas as pd

data = {
        'Alunos': ['Danilo', 'Solange', 'Sophia', 'Kévyn', 'Eliana'],
        'Idade': [16, 15, 7, 15, 30],
        'Nota': [8, 9, 10, 9, 6]
        
        }


df = pd.DataFrame(data, columns=['Alunos', 'Idade', 'Nota'])

df.describe()

df = df.drop([0]) #Exclui dados da lista na posição 0

df = df.drop('Idade', axis=1) #Exclui coluna Idade

df.count()

df.columns #Mostra as colunas inseridas

df.shape #Mostra quantidade de linhas e colunas

df.max() #Mostra valor máximo de cada lista

df['Idade'].max() #MOstra a maior Idade

df.min()#Mostra valor mínimo de cada lista

df['Nota'].min() #Mostra a menor Nota

df.mean() #Mostra a média das listas numéricas

df.median() #Mostra a mediana das listas numéricas

df.sum() #soma os numéricos e concatena as strings

df['Nota'].add(10) #Soma 10 em todas as Notas

df['Idade'].sub(2) #Subtrai 2 em todas as Idades

df.mul(2) #Multiplica por 2

df['Idade'].div(2) #Divide idade por 2
 
df.head() #Mostra as 5 primeiras linhas

df.tail() #Mostra as 5 útimas linhas

df.loc[df['Nota'] <= 6] #mostra os Alunos com nota menor ou igual a 6

