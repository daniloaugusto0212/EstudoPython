from tkinter import *
import pymysql
from tkinter import messagebox


class AdminJanela():

    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN')
        self.root.geometry('500x500')

        self.root.mainloop()


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
                resultado = cursor.fetchall()
        except:
            print('Erro ao fazer a consulta.')

        for linha in resultado:
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

        Button(self.root, text='Visualizar Cadastros', bg='white').grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

JanelaLogin()
