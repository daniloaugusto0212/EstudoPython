nome, idade, sobrenome = "João", 10, "Silva"

print(f'Olá, {nome} {sobrenome}, sua idade é {idade} anos')

if idade >= 18:
    print(f'{nome} é maior de idade')
else:
    print(f'{nome} é menor de idade')

idade2 = 1
while idade2 != 0:
    nome2 = input('Digite o seu nome: ')
    idade2 = int(input('Digite sua idade: '))
    sobrenome2 = input('Digite seu sobrenome: ')

    if idade2 == 99:
        break
    if idade2 == 98:
        continue

    print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2} anos")

    media_idades = (idade + idade2) / 2
    print(f"A média das idades é: {media_idades}")

    if idade2 <= 17:
        print(f"{nome2} é adolescente.")
    elif idade2 >= 18 and idade2 <= 50:
        print(f"{nome2} é adulto")
    else:
        print(f"{nome2} é idoso.")
else:
    print('O loop entrou no else')