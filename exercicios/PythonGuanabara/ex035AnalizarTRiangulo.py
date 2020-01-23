print('-=' *20)
print('Analisador de triângulos')
print('-='*20)
lado1 =float(input('Primeiro Segmento: '))
lado2 =float(input('Segundo Segmento: '))
lado3 =float(input('Terceiro Segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÂO PODEM formar um triângulo.')