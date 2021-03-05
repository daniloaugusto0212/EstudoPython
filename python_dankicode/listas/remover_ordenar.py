lista = ['carro', 'barco', 'avião', 'moto']
print(lista)

#del lista #apaga toda a lista e gera um erro
#lista.clear() #apaga todos os elementos da lista e a deixa vazia
del lista[0]  #elimina o elemento com o indice escolhido

lista.pop() #elimina o último elemento
lista.pop(1) #elimina o elemento com o indice escolhido
#lista.remove("carro") #elimina o elemento escolhido
print(lista)

compras = ['pã0', 'carne', 'verduras']
print(compras)
compras.sort() #ordena a lista em ordem alfabético ou numérica crescente
print(compras)