import carro

uno_vermelho = carro.Carro("Vermelho", 4, "Flex", 1.0)
help(uno_vermelho.abastecer) #Imprime o conteúdo da DocString
uno_vermelho.ligar()
help(carro.Carro)
uno_vermelho.abastecer(10)
uno_vermelho.abastecer(20)
print(f'A quantidade de combustível do carro é {uno_vermelho.qtd_combustivel} litros\n')
#del uno_vermelho

uno_preto= carro.Carro("Preto", 2, "Gasolina", 1.4)
uno_preto.ligar()

print(f'\nA quantidade de combustível do Uno Preto é {uno_preto.qtd_combustivel} litros')
uno_preto.acelerar(120)
print(f'\nO carro está na velocidade de {uno_preto.velocidade} Km/h')
