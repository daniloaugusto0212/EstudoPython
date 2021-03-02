palpite = 0
numero = 9

while True:
    palpite = int(input("Adivinhe qual o número correto: "))
    if palpite == numero:
        print("Parabéns você acertou")
        break
    else:
        print("Você errou!")
