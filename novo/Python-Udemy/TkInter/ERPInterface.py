from tkinter import *

def mostrar():
    armazenarLabel['text'] = 'Botão foi clicado'

janela = Tk()
janela.title('Curso de Python')
janela.geometry('300x300')
janela.resizable(False, False)

# Label(janela, text='Hello World', bg='black', fg='white', padx=30, pady=30).grid(row=0, column=0) edição da janela
# Entry(janela, bg='black', fg='orange', show='*').grid(row=0, column=0)

Button(janela, text='Clique aqui', bg='black', fg='white', height=10, width=20, command=mostrar).grid(row=0, column=0)
armazenarLabel = Label(janela, text='Ainda não foi clicado')
armazenarLabel.grid(row=1, column=0)

janela.mainloop()