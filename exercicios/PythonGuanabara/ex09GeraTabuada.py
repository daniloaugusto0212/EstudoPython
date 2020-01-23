'''Gera tabuada'''
number = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(0,11):
    print(f'{number} x {c:2} = {number*c}')

print('-'*12)