from random import randint
from time import sleep

print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
numeroComputador = randint(0, 5)
numero = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if numeroComputador == numero:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print(f'Você perdeu! Eu pensei no número {numeroComputador}, não no {numero}')