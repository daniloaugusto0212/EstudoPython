'''Faça um programa que verifique e mostre os numeros entre 1000 e 2000,
que quando dividido por 11 produz o resto 5'''

lista = []

for i in range(1000, 2001):
    if i % 11 == 5:
        lista.append(i)
print(lista)
