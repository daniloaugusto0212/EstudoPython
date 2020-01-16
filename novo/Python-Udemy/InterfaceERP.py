from tkinter import *
import pymysql
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt


class AdminJanela():

    def CadastrarProduto(self):
        self.cadastrar = Tk()
        self.cadastrar.title('Cadastro de produtos')
        self.cadastrar['bg'] = '#524f4f'

        Label(self.cadastrar, text='Cadastre os produtos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        Label(self.cadastrar, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.ingredientes = Entry(self.cadastrar)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.cadastrar)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='preço', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.preco = Entry(self.cadastrar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.CadastrarProdutoBackEnd).grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.RemoverCadastrosBackEnd).grid(row=5, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.CadastrarProdutoBackEnd).grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar produtos', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.LimparCadastrosBackEnd).grid(row=6, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=200, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('column2', width=400, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column('column3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('column4', width=60, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()

    def CadastrarPedido(self):
        self.cadastrar = Tk()
        self.cadastrar.title('Pedidos em aberto')
        self.cadastrar['bg'] = '#524f4f'

        Label(self.cadastrar, text='Cadastre os pedidos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4,
                                                                                          padx=5, pady=5)

        Label(self.cadastrar, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5,
                                                                                  pady=5)
        self.ingredientes = Entry(self.cadastrar)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5,
                                                                           pady=5)
        self.grupo = Entry(self.cadastrar)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Local de Entrega', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5,
                                                                           pady=5)
        self.localEntrega = Entry(self.cadastrar)
        self.localEntrega.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Observações', bg='#524f4f', fg='white').grid(row=5, column=0, columnspan=1, padx=5,
                                                                                  pady=5)
        self.observacoes = Entry(self.cadastrar)
        self.observacoes.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f',
               command=self.CadastrarPedidoBackEnd).grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Entregue', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.PedidoEntregueBackEnd
               ).grid(row=6, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f'
               ).grid(row=7, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar todos pedidos', width=15, bg='gray', relief='flat',
               highlightbackground='#524f4f', command=self.LimparPedidosBackEnd).grid(row=7, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode='browse',
                                 column=('column1', 'column2', 'column3', 'column4', 'column5'), show='headings')

        self.tree.column('column1', width=200, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('column2', width=300, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column('column3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('column4', width=300, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Local de Entrega')

        self.tree.column('column5', width=100, minwidth=800, stretch=NO)
        self.tree.heading('#5', text='Observações')

        self.tree.grid(row=0, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        self.MostrarPedidosBackEnd()

        self.cadastrar.mainloop()


    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN')

        Button(self.root, text='Pedidos', width=20, bg='#2E4682', command=self.CadastrarPedido).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Cadastros', width=20, bg='#485A88', command=self.CadastrarProduto).grid(row=1, column=0, padx=10, pady=10)
        Button(self.root, text='Estatísticas', width=20, bg='#021F3D', fg='white', command=self.Estatisticas).grid(row=2, column=0, padx=10, pady=10)

        self.root.mainloop()

    def Estatisticas(self):
        self.root = Tk()
        self.root.title('ESTATÍSTICAS')

        Button(self.root, text='Por Nome', width=20, bg='#2E4682', command=self.PesquisaNome).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Por Grupo', width=20, bg='#2E4682', command=self.PesquisaGrupo).grid(row=1, column=0, padx=10, pady=10)
        
    def PesquisaNome(self):
        Button(self.root, text='Por Valor', width=20, bg='#2E4682', command=self.PequisaValor).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Por Quantidade', width=20, bg='#2E4682', command=self.PesquisaQuantidade).grid(row=1, column=0, padx=10, pady=10)
        
    def PequisaValor(self):
            nomeProdutos = []
            nomeProdutos.clear()

            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='681015',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('Erro ao conectar ao banco de dados.')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    produtos = cursor.fetchall()
            except:
                print('Erro ao consultar o banco de dados. ')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticaVendido')
                    vendido = cursor.fetchall()
            except:
                print('Error ao consultar o banco de dados. ')
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

    '''def PesquisaQuantidade(self):
        grupoUnico = []
        grupoUnico.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                grupo = cursor.fetchall()
        except:
            print('Erro na consulta.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from estatiticaVendido')
                vendidoGrupo = cursor.fetchall()
        except:
            print('Erro na consulta')
        for i in grupo:
            grupoUnico.append(i['nome'])

        grupoUnico = sorted(set(grupoUnico))
        qntFinal = []
        qntFinal.clear()

        for h in range(0, len(grupoUnico)):
            qntUnitaria = 0
            for i in vendidoGrupo:
                if grupoUnico[h] == i['nome']:
                    qntUnitaria += 1
            qntFinal.append(qntUnitaria)

        plt.plot(grupoUnico, qntFinal)
        plt.ylabel('Quantidade unitária vendida')
        plt.xlabel('Produtos')
        plt.show()

    def PesquisaGrupo(self):
        nomeProdutos = []
        nomeProdutos.clear()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                produtos = cursor.fetchall()
        except:
            print('Erro ao consultar o banco de dados. ')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from estatisticaVendido')
                vendido = cursor.fetchall()
        except:
            print('Error ao consultar o banco de dados. ')
        for i in produtos:
            nomeProdutos.append(i['grupo'])

        valores = []
        valores.clear()

        for h in range(0, len(nomeProdutos)):
            somaValor = -1
            for i in vendido:
                if i['grupo'] == nomeProdutos[h]:
                    somaValor += i['preco']
            if somaValor == -1:
                valores.append(0)
            elif somaValor > 0:
                valores.append(somaValor + 1)

        plt.plot(nomeProdutos, valores)
        plt.ylabel('Quantidade vendida em Reais')
        plt.xlabel('Produtos')
        plt.show()'''
    #Faltando finalizar a parte de Estatísticas.

    def MostrarProdutosBackEnd(self):
    
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultados = cursor.fetchall()
        except:
            print('Erro ao fazer a consulta.')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()

    def CadastrarProdutoBackEnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
                conexao.commit()
        except:
            print('Erro ao cadastrar.')

        self.MostrarProdutosBackEnd()

    def RemoverCadastrosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(


                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from produtos where id = {}'.format(idDeletar))
                conexao.commit()
        except:
            print('Erro ao fazer a consulta.')

        self.MostrarProdutosBackEnd()

    def LimparCadastrosBackEnd(self):
        if messagebox.askokcancel('Limpar dados CUIDADO!!!', 'DESEJA EXCLUIR TODOS OS DADOS DA TABELA? NÂO PODERÁ RECUPERAR.'):

            try:
                conexao = pymysql.connect(

                    host='localhost',
                    user='root',
                    password='681015',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor

                )
            except:
                print('Erro ao conectar ao banco de dados.')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('trancate table produtos:')
                    conexao.commit()
            except:
                print('Erro ao fazer a consulta.')

            self.MostrarProdutosBackEnd()

    def CadastrarPedidoBackEnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        localEntrega = self.localEntrega.get()
        observacoes = self.observacoes.get()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into pedidos(nome, ingredientes, grupo, localEntrega, observacoes) values (%s, %s, %s, %s, %s)',
                               (nome, ingredientes, grupo, localEntrega, observacoes))
                conexao.commit()
        except:
            print('Erro ao cadastrar pedido.')

        self.MostrarPedidosBackEnd()

    def MostrarPedidosBackEnd(self):

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                resultados = cursor.fetchall()
        except:
            print('Erro ao fazer a consulta.')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['localEntrega'])
            linhaV.append(linha['observacoes'])

            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()

    def PedidoEntregueBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                conexao.commit()
        except:
            print('Erro ao fazer a consulta.')

        self.MostrarPedidosBackEnd()

    def LimparPedidosBackEnd(self):
        if messagebox.askokcancel('Limpar pedidos. CUIDADO!!!', 'DESEJA EXCLUIR TODOS OS PEDIDOS DA TABELA? NÂO PODERÁ RECUPERAR.'):

            try:
                conexao = pymysql.connect(

                    host='localhost',
                    user='root',
                    password='681015',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor

                )
            except:
                print('Erro ao conectar ao banco de dados.')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('trancate table pedidos:')
                    conexao.commit()
            except:
                print('Erro ao fazer a consulta.')

            self.MostrarPedidosBackEnd()




class JanelaLogin():

    def VerificaLogin(self):
        autenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')

        usuario = self.login.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('Erro ao abrir a janela.')

        for linha in resultados:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('login', 'Email ou senha inválido.')

        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                AdminJanela()

    def CadastroBackEnd(self):
        codigoPadrao = '1234'

        if self.codigoSeguranca.get() == codigoPadrao:
            if len(self.login.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.login.get()

                    senha = self.senha.get()

                    try:
                        conexao = pymysql.connect(

                            host='localhost',
                            user='root',
                            password='681015',
                            db='erp',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor

                        )
                    except:
                        print('Erro ao conectar ao banco de dados.')

                    try:
                        with conexao.cursor() as cursor:
                            cursor.execute('insert into cadastros (nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                            conexao.commit()
                        messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso!')
                        self.root.destroy()
                    except:
                        print('Erro ao inserir dados.')
                else:
                    messagebox.showinfo('ERRO', 'Por favor, insira uma senha com 50 ou menos caracteres')
            else:
                messagebox.showinfo('ERRO', 'Por favor, insira um nome com 20 ou menos caracteres')
        else:
            messagebox.showinfo('ERRO', 'Erro no código de segurança')

    def Cadastros(self):
        Label(self.root, text='Chave de segurança').grid(row=3, column=0, pady=5, padx=5)
        self.codigoSeguranca = Entry(self.root, show='*')
        self.codigoSeguranca.grid(row=3, column=1, pady=5, padx=5)
        Button(self.root, text='Confirmar cadastro', width=15, bg='blue1', command=self.CadastroBackEnd).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

    def UpdateBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='681015',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('Erro ao conectar ao banco de dados.')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('Erro ao fazer a consulta.')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['id'])
            linhaV.append(linha['nome'])
            linhaV.append(linha['senha'])
            linhaV.append(linha['nivel'])


            self.tree.insert('', END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()


    def VisualizarCadastros(self):
        self.vc = Toplevel()
        self.vc.resizable(False, False)
        self.vc.title('Visualizar cadastros')

        self.tree = ttk.Treeview(self.vc, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=40, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column('column2', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Usuário')

        self.tree.column('column3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column('column4', width=40, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Nível')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.UpdateBackEnd()

        self.vc.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        Label(self.root, text='Faça o login').grid(row=0, column=0, columnspan=2)

        Label(self.root, text='Usuário').grid(row=1, column=0)

        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text='Senha').grid(row=2, column=0)

        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='Login', bg='green3', width=10, command=self.VerificaLogin).grid(row=5, column=0, padx=5, pady=5)

        Button(self.root, text='Cadastrar', bg='orange3', width=10, command=self.Cadastros).grid(row=5, column=1, padx=5, pady=5)

        Button(self.root, text='Visualizar Cadastros', bg='white', command=self.VisualizarCadastros).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

JanelaLogin()
