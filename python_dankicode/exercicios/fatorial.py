num = int(input("Digite um número positivo para ver o seu fatorial: "))
fatorial = num

if num == 0:
    fatorial = 1
else:
    for i in range(num - 1, 1, -1):
        fatorial *= i

print(f"O fatorial de {num} é {fatorial}")