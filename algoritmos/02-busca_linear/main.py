
numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(0, tamanho):
    valor = int(input(f"Digite um número do vetor na posição {i}: "))
    numeros.append(valor)
print(f"Vetor: {numeros}")


#Busca Linear
numero_pesquisar = int(input("Digite o valor a ser pesquisado no vetor: "))
posicao_resultado = -1
for i in range(tamanho):
    if numeros[i] == numero_pesquisar:
        print(f"Número {numero_pesquisar} encontrado na posição {i}")
        break
if posicao_resultado < 0:
    print(f'O número {numero_pesquisar} não foi encontrado no vetor!')
#FIM Busca Linear
