from tkinter import  *
from tkinter import ttk

janela = Tk()
janela.title('Curso de Python')

tree = ttk.Treeview(janela, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

tree.column('column1', width=200, minwidth=50, stretch=NO)
tree.heading('#1', text='Nome')

tree.column('column2', width=100, minwidth=50, stretch=NO)
tree.heading('#2', text='Idade')

tree.column('column3', width=300, minwidth=50, stretch=NO)
tree.heading('#3', text='Endereço')

tree.column('column4', width=50, minwidth=50, stretch=NO)
tree.heading('#1', text='ID')

elementos = ['Joaquim', '13', '13 esquina com a 16', 1]
for i in range(0, 4):
    tree.insert('', END, values=elementos, tag='1')

tree.grid(row=0, column=0)


janela.mainloop()