def mostrarNaTela(): #define a função
    print('Olá, Mundo!')
    

mostrarNaTela() #chama a função

def soma2Numeros(n1, n2):
    print(f'A soma dos números é {n1 + n2}')

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro número: '))
soma2Numeros(numero1, numero2)

#função que retorna os valores dentro de uma lista com a quantidade de parâmetros indefinida
def retornaMaior(*list):
    print('O maior valor da lista é: ', end='')
    print(max(list))

retornaMaior(1,2,3,4,50,90,30,80)