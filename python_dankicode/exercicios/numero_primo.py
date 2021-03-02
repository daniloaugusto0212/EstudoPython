num = int(input("Digite um número inteiro para saber se ele é primo: \n"))
primo = False
if num > 1:
    for i in range(2, num):
        print(i, "\n")
        if (num % i) == 0:
            primo = False
            break
    else:
        primo = True
if primo:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")




