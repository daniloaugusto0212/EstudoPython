for x in range(10):
    if x == 3:
        continue #pula o número 3
    print(x)

for x in range(10):
    if x == 3:
        pass #Só para não deixar a condição vazia(camufla o erro)
    print(x)