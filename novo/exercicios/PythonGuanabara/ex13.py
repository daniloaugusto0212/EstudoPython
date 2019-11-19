salario = float(input('Qual é o salário do funcionário? R$'))
aumento = 15 / 100 * salario
novo = salario + aumento
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')