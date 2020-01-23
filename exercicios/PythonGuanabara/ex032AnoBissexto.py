from datetime import date

ano = int(input('Que ano deseja analizar? Digite 0 para o ano atual: '))
atual = date.today().year
ano = atual if ano == 0 else ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano de {ano} não é Bissexto. ')
