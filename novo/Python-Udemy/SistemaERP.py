import pymysql.cursors

conexao = pymysql.connect(

    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor


)
autentico = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False
    if decisao == 1:
        nome = input('Nome: ')
        senha = input('Senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        if not autenticado:
            print('Usuário ou Senha incorretos!')

    elif decisao == 2:
        print("Faça seu Cadastro")
        nome = input('Nome: ')
        senha = input('Senha: ')

        for linha in resultado:
            if nome == linha['nome']:
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('Usuário já Cadastrado! Tente um nome diferente.')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                print("Usuário cadastrado com sucesso!")
            except:
                print('Erro ao inserir os dados!')
    return autenticado, usuarioMaster

def cadastrarProdutos():
    nome = input('Nome do Produto: ')
    ingredientes = input('Ingredientes: ')
    grupo = input('Grupo: ')
    preco = float(input('Valor do produto: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
            conexao.commit()
            print('Produto cadastrado com sucesso!')

    except:
        print('Erro ao inserir dados!')

while not autentico:
    decisao = int(input('Digite:\n[1] LOGAR\n[2]CADASTRAR\n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()

    except:
        print('Erro ao conectar ao banco de dados.')

    autentico, usuarioSupremo = logarCadastrar()

if autentico == True:
    print('Autenticado')

    if usuarioSupremo == True:

        decisaoUsuario = 1


        while decisaoUsuario != 0:
            decisaoUsuario = int(input('[1] CADASTRAR\n[0] SAIR\n'))

            if decisaoUsuario == 1:
                cadastrarProdutos()