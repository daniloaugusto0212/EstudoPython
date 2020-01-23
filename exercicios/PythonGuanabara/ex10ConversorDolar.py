'''Converte real em dólar usando a cotação de 4.20'''
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${dinheiro} você pode comprar US${dinheiro/4.2:.2f}')