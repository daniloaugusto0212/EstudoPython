nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split() #Split divide a frase através dos espaços
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')
