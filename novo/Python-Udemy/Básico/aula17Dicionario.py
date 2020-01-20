dicionario = {'nome': 'Danilo', 'idade': 33, 'peso': 79.1} #{} ou dict() para inicializar um dicionário


print(dicionario['nome']) #mostra o valor atribuido ao índice 'nome'
print(f"Tem {dicionario['idade']} anos")

dicionario.pop('peso') # remove indice e valor do 'peso'
print(dicionario)