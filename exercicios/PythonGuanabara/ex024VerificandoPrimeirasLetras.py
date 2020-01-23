cidade = str(input('Em que cidade você nasceu? '))
cidade = cidade.upper()
cidade = cidade.strip()
if 'SANTO' in cidade[:5]:
    print(f'A cidade de {cidade} começa com a palavra Santo.')
else:
    print(f'A cidade de {cidade} não começa com a palavra Santo.')


