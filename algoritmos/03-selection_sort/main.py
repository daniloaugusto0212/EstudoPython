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