velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Multado! Você excedeu o limite permitido que é de 80Km/h\n'
          f'Você deve pagar uma multa de R${multa:.2f}')
print('Dirija com segurança!')
