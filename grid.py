from tkinter import *

#cores
cor1='#bdc2db' #cinza

janela = Tk()
janela.title('Grid')
janela.geometry('350x250')
janela.config(background=cor1) # color picker no google

janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.resizable(width=False, height=False)

label_nome = Label(janela, width=10, height=2, text='Nome.:', font=('Arial 15 bold'), fg='white', bg='orange')
label_nome.grid(row=0, column=0)
nome = Label(janela, width=10, height=2, text='João Futi', font=('Arial 15 bold'), fg='white', bg='orange')
nome.grid(row=0, column=1, padx=5, pady=10)


label_idade = Label(janela, width=10, height=2, text='Idade.:' , font=('Arial 15 bold'), fg='white', bg='orange')
label_idade.grid(row=1, column=0)
idade = Label(janela, width=10, height=2, text='50' , font=('Arial 15 bold'), fg='white', bg='orange')
idade.grid(row=1, column=1, padx=5, pady=10)

label_pais = Label(janela, width=10, height=2, text='Pais.:', font=('Arial 15 bold'), fg='white', bg='orange')
label_pais.grid(row=2, column=0)
pais = Label(janela, width=10, height=2, text='Angola', font=('Arial 15 bold'), fg='white', bg='orange')
pais.grid(row=2, column=1, padx=5, pady=10)

janela.mainloop()