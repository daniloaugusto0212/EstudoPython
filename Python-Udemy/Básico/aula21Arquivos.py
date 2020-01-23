arquivo = open('aula.txt', 'w') #cria um arquivo, se ele já existir, somente abre para edição, todo texto existente é sobrescrevido

texto = ' Olá, tudo bem? Python'
#texto = arquivo.readlines()

arquivo.write(texto)



arquivo.close

