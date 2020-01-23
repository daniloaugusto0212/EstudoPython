'''Cáculo de quantidade de tinta necessária, levando em conta que precisamos de 1 litro de tinta para cada 2 m²'''
larg = float(input('Largura da parede: '))
altur = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {larg} x {altur} e sua área é de {larg*altur}m².\n'
      f'para pintar essa parede, você vai precisar de {(larg*altur)/2}l de tinta.')