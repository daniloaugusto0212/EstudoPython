
numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(0, tamanho):
    valor = int(input(f"Digite um número do vetor na posição {i}: "))
    numeros.append(valor)
print(f"Vetor: {numeros}")
