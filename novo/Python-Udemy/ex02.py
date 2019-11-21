'''Faça um programa que receba o peso de 7 pessoas, calcule e mostre:
    a quantidade de pessoas acima de 90kg
    a media dos pesos das pessoas'''

pessoas = []
acima  = 0

for i in range(1, 8):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    pessoas.append(peso)    
    media = sum(pessoas) / 7 
    if peso > 90:
        acima += 1
print(f'A quantidade de pessoas acima do peso é {acima}\nA média dos pesos é {media:.2f}')