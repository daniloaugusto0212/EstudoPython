
lista = ['a', 'b', 'c']
'''lista2 = [1, 4, 6]

lista.extend(lista2)
print(lista)

for x in lista2:
    lista.append(x)

print(lista)'''

lista2 = lista.copy()
lista2.append("d")
lista.append("e")
print(lista)
print(lista2)