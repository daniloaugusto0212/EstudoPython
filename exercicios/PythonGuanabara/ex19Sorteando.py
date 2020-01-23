'''Sorteia um aluno entre os digitados'''
import random
aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
lista = [aluno1, aluno2, aluno3]
print(f'O aluno escolhido foi {random.choice(lista)}')

