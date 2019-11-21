nome = str(input('Digite o nome do Aluno: '))
idade = int(input('Digite a idade: '))
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
if (media >= 6 and idade >= 18):
    status = 'Aprovado!'
else:
    status = 'Reprovado!'

print(f'{nome.title()} foi {status}') 