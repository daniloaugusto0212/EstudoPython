'''Calcula a hipotenusa'''
co = float(input('Qual é o valor do cateto oposto? '))
ca = float(input('Qual é o valor do cateto adjacente? '))
hipotenusa = pow((co**2) + (ca**2), 1/2)
print(f'A hipotenusa do triângulo é {hipotenusa:.2f}')
