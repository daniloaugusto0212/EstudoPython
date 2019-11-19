'''Programa que lê o ângulo e calcula o seno, cosseno e tangente'''
import math
angulo = float(input("Digite o ângulo: "))
radianos = math.radians(angulo)
print(f"O ângulo de {angulo} tem o SENO de {math.sin(radianos):.2f}")
print(f"O ângule de {angulo} tem o COSSENO de {math.cos(radianos):.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {math.tan(radianos):.2f}")
