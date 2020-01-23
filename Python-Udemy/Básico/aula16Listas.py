lista = []

#adiciona a lista os valores de 1 até 1000
for i in range(1, 1001):
    lista.append(i)

lista = list(range(1, 1001)) #mesma função do código acima (mais simplificado)

print(lista)

#verifica se o valor digitado exista na lista para apagá-lo
apagar = int(input('Digite um número para apagar da lista: '))
if apagar in lista:
    lista.remove(apagar)
    print('O valor foi removido com sucesso.\n')
else:
    print('Não existe o valor digitado na lista.\n')

print(lista)
