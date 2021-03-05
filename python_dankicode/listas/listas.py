lista = ['chicago', 'queens', 'salvador', 'pernambuco']
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista4 = [True, False]
print(lista4)

lista5 = [True, 'chicago', 2.5, False, 4]
print(type(lista5))

print(lista5[1])

print(lista5[-2])

print(lista5[:3])

lista2 += lista3 #Junção das duas listas
print(lista2)

print(len(lista5)) #tamanho da lista

print(sum(lista2)) #soma de todos os dados da lista numérica
print(max(lista2)) #mostra o maior valor existente na lista
print(min(lista2)) #mostra o menos valor existente na lista

nome = "Curso de Python"
valor = range(10)

lista7 = list(range(10))
print(lista7)

lista8 = list(nome)
print(lista8)

elemento = 8

if elemento in lista7:
    print('O elemento está na lista')
else:
    print('O elemento não está na lista')


