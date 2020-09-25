

numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(0, tamanho):
    valor = int(input(f"Digite um número do vetor na posição {i}: "))
    numeros.append(valor)
print(f"Vetor: {numeros}")

#SELECTION SORT
# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1
for i in range(tamanho):
    indice_menor = i
    for j in range((i + 1), tamanho):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("Vetor: ", numeros)

#FIM SELECTION SORT

# BUSCA BINÁRIA
#necessário ordenar primeiro o vetor
resultado = -1
inicio = 0
fim = tamanho -1
meio = 0
alvo = int(input("Digite o elemento a ser encontrado: "))
while inicio <= fim:
    meio = int((inicio + fim) / 2)
    if(numeros[meio] < alvo):
        inicio = meio + 1
    elif (numeros[meio] > alvo):
        fim = meio - 1
    else:
        resultado = meio
        break
if(resultado < 0):
    print("Elemento não encontrado")
else:
    print(f"O elemento {alvo} está na posição {resultado}")
# FIM BUSCA BINÁRIA