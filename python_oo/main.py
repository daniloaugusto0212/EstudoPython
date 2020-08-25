import carro

uno_vermelho = carro.Carro("Vermelho", 4, "Flex", 1.0, 0, False)
uno_vermelho.ligar()
uno_vermelho.abastecer()
uno_vermelho.abastecer()
print(f'A quantidade de combustível do carro é {uno_vermelho.qtd_combustivel} litros\n')


uno_preto= carro.Carro("Preto", 2, "Flex", 1.4, 0, True)
uno_preto.desligar()
print(f'\nA quantidade de combustível do Uno Preto é {uno_preto.qtd_combustivel} litros')