from tkinter import *


janela = Tk()
janela.title('Curso de Python')
janela.geometry('500x500')

frame = Frame(janela, width=300, height=300, bg='white').grid(row=0, column=0)
Label(frame, text='Hello World').grid(row=0, column=0)




janela.mainloop()