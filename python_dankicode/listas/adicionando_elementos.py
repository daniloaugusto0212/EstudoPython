lista = ['carro', 'barco', 'avião']
print(lista)

lista.append('moto') #adiciona ao final da lista (somente um por append)
lista.append(['bicicleta', 'navio']) #adiciona lista dentro de uma lista

lista.insert(1, 'caminhão') #insere o elemento no indice escolhido

lista.extend(['motoneta', 'triciclo']) #adiciona novos elementos ao final da lista

#mostra os elementos
for x in lista:
    print(x)

#mostra os indices e os elementos
for x in range(len(lista)):
    print(x, lista[x])