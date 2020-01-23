distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.')
'''if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45'''
preco = 0.5 * distancia if distancia <= 200 else distancia * 0.45 #Usando if ternário
print(f'E o preço de sua passagem será de R${preco:.2f}')
