'''Faça um programa que receba varias idades e calcule a media entre elas.
O programa deverá ser finalizado quando for digitado -1'''
soma = cont = media = 0
while True:
    idade = int(input(f"Digite a {cont + 1}° idade: "))
    if idade == -1:
        break
    soma += idade
    cont += 1
    media = soma / cont

print(f'A média entre as idades digitas é {media}.')


