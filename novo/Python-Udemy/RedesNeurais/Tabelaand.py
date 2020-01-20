from random import *

pesoInicial1 =random()
pesoInicial2 = random()
pesoBias = random()

entrada1 =int(input('Digite a entrada 1:'))
entrada2 = int(input('Digite a entrada 2:'))
bias =1

erro = 1

while erro != 0:
    if entrada1 == 1 and entrada2 == 1:
        resultadoEsperado = 1
    else:
        resultadoEsperado = 0

    somatoria = pesoInicial1 * entrada1
    somatoria += pesoInicial2 * entrada2
    somatoria += pesoBias * bias

    if somatoria < 0:
        resultado = 0
    elif somatoria >= 0:
        resultado = 1

    print(f'Resultado: {resultado}')

    erro = resultadoEsperado - resultado

    print(f'p1 {pesoInicial1}')
    print(f'p2 {pesoInicial2}')
    print(f'pb {pesoBias}')

    pesoInicial1 = pesoInicial1 + (0.1 * entrada1 * erro)
    pesoInicial2 = pesoInicial2 + (0.1 * entrada2 * erro)
    pesoBias = pesoBias + (0.1 * bias * erro)

    print(f'erro {erro}')