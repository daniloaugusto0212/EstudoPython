import pandas as pd

data = {
        'Alunos': ['Danilo', 'Solange', 'Sophia', 'Kévyn'],
        'Idade': [16, 15, 7, 15],
        'Nota': [8, 9, 10, 9]
        
        }


df = pd.DataFrame(data, columns=['Alunos', 'Idade', 'Nota'])

df.describe()

df = df.drop([0])