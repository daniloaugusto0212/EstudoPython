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

        Button(self.root, text='Login', bg='green3', width=10, command=self.VerificaLogin).grid(row=3, column=0, padx=5, pady=5)

        Button(self.root, text='Cadastrar', bg='orange3', width=10).grid(row=3, column=1, padx=5, pady=5)

        Button(self.root, text='Visualizar Cadastros', bg='white').grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

JanelaLogin()
