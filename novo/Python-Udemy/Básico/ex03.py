'''faça um programa que mostre o resultado de n!(fatorial)
5! = 5 * 4 * 3 * 2 * 1'''

n = int(input('Digite um valor para calcular o seu Fatorial: '))
resultado = n
for i in range(n-1, 0, -1):
    resultado *= i

print(f'O fatorial de {n} é {resultado}')