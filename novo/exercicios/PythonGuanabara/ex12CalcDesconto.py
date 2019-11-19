'''Cálculo de desconto no produto'''
valor = float(input('Qual é o preço do produto? R$'))
desc = 5 / 100 * valor
novo = valor - desc
print(f'O produto que custava R${valor:.2f}, na promoção com 5% de desconto vai custar R${novo:.2f} ')