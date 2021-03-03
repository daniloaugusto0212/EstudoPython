#escreva um programa que leia 5 valores e mostre o maior e o menor entre eles
num = num = int(input(f"Digite o 1° valor: "))
menor = num
maior = num
for x in range(2, 6):
    num = int(input(f"Digite o {x}° valor: "))
    if menor < num:
        menor = menor
    else:
        menor = num

    if maior > num:
        maior = maior
    else:
        maior = num

print(f'O maior número digitado é {maior}, e o menor é {menor}')

