salario = float(input('Qual é o salário do funcionário? R$'))
salAumento = salario + (10 / 100 * salario) if salario > 1250 else salario + (15 / 100 * salario)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salAumento:.2f} agora.')
