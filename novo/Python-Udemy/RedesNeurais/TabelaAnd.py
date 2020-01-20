from random import *

pesoInicial1 = random()
pesoInicial2 = random()

entrada1 = int(input('Digite a entrada 1 [0 ou 1]:'))
entrada2 = int(input('Digite a entrada 2 [0 ou 1]:'))

erro = 1

while erro != 0:
    if entrada1 == 1 and entrada2 == 0:
        resultadpEsperado = 1
    else:
        resultadpEsperado = 0

    somatoria = pesoInicial1 * entrada1
    somatoria += pesoInicial2 * entrada2
    
    if somatoria < 1:
        resultado = 0
    elif somatoria >= 1:
        resultado = 1

    print(f'resultado {resultado}')

    erro = resultadpEsperado - resultado

    print(f'p1 {pesoInicial1}')
    print(f'p1 {pesoInicial1}')

    pesoInicial1 = pesoInicial1 + (0.1 * entrada1 * erro)
    pesoInicial2 = pesoInicial2 + (0.1 * entrada2 * erro)

    print(f'erro {erro}')
