
idade = [] #inicializando lista vazia

idade.append(18) #adiciona o valor 18 à lista
idade.append(50)
idade.append(35)
idade.append(48)
idade.append(40) #adiciona o valor 18 ao final da lista

idade.insert(1, 30) #adiciona o valor 30 na posição 1 da lista
idade.pop() #remove o valor da última posição da lista
idade.pop(1) #remove o valor da posição 1 da lista

idade.remove(50) #remove o valor especificado

len(idade) #mostra a quantidade de elementos que está dentro da lista

idade.sort() #ordena a lista
idade.sort(reverse = True) #ordena a lista em ordem decrescente
idade.reverse() #inverte a ordem da lista

max(idade) #mostra o maior valor dentro da lista
min(idade) #mostra o menor valor dentro da lista
sum(idade) #soma todos os valores dentro da lista

print(idade)