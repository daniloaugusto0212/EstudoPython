import carro, moto

uno_vermelho = carro.Carro("Vermelho", "Flex", 1.0, 4)
#help(uno_vermelho.abastecer) #Imprime o conteúdo da DocString
uno_vermelho.ligar()
#help(carro.Carro)
uno_vermelho.abastecer(10)
uno_vermelho.abastecer(20)
uno_vermelho.ligar()
uno_vermelho.acelerar(50)
uno_vermelho.pintar("Azul")

print(f'A quantidade de combustível do carro é ')


moto_preta = moto.Moto("Vermelha", "Gasolina", 125, 2)

moto_preta.ligar()
