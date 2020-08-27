import carro, moto

uno_vermelho = carro.Carro("Vermelho", "Flex", 1.0, 4)
#help(uno_vermelho.abastecer) #Imprime o conteúdo da DocString
uno_vermelho.ligar()
#help(carro.Carro)
uno_vermelho.abastecer(10)
uno_vermelho.abastecer(20)
print(f'A quantidade de combustível do carro é {uno_vermelho.qtd_combustivel} litros\n')
#del uno_vermelho

moto_preta = moto.Moto("Vermelha", "Gasolina", 125, 2)
moto_preta.abastecer(30)
moto_preta.abastecer((10))
moto_preta.ligar()
print(moto_preta.is_ligado)