import matplotlib.pyplot as plt
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

def listarProdutos():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()

    except:
        print('Erro ao conectar ao banco de dados')

    for i in produtosCadastrados:
        produtos.append(i)

    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum produto cadastrado!')

def excluirProdutos():
    idDeletar = int(input('Digite o ID referente ao produto que deseja apagar: \n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletar))
            print('Produto {} excluído com sucesso!')
    except:
        print('Erro ao excluir o produto!')

def listarPedidos():
    pedidos = []
    decision = 0

    while decision != 2:
        pedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listaPedidos = cursor.fetchall()
        except:
            print('Erro no banco de dados! ')

        for i in listaPedidos:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('Não há pedidos! ')

        decision = int(input('[1] Produto entregue\n[2] Voltar\n'))

        if decision == 1:
            idDeletar = int(input('Digite o ID do pedido entregue: '))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print('Produto entregue.')
            except:
                print('Erro ao dar baixa no pedido! ')

def gerarEstatistica():
    nomeProdutos = []
    nomeProdutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except:
        print('Erro ao consultar o banco de dados. ')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatiticaVendido')
            vendido = cursor.fetchall()
    except:
        print('Error ao consultar o banco de dados. ')

    estado = int(input('[0] SAIR\n[1] PESQUISAR POR NOME\n[2] PESQUISAR POR GRUPO\n'))

    if estado == 1:
        decisao3 = int(input('[1] PESQUISAR POR VALOR\n[2] PESQUISAR POR QUANTIDADE\n'))
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append(i['nome'])

            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['nome'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Quantidade vendida em Reais')
            plt.xlabel('Produtos')
            plt.show()


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
            decisaoUsuario = int(input('[0] SAIR\n[1] CADASTRAR\n[2] LISTAR PRODUTOS CADASTRADOS\n[3] LISTAR PEDIDOS\n[4] VISUALIZAR ESTATISTICAS\n'))

            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('[1] Excluir um produto\n[2] Sair\n'))
                if delete == 1:
                    excluirProdutos()
            elif decisaoUsuario == 3:
                listarPedidos()
            elif decisaoUsuario == 4:
                gerarEstatistica()

