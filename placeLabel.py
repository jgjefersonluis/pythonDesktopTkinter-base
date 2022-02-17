from tkinter import *

#cores
cor1='#bdc2db' #cinza

janela = Tk()
janela.title('Place Label')
janela.geometry('350x250')
janela.config(background=cor1) # color picker no google

janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.resizable(width=False, height=False)

label_nome = Label(janela, width=10, height=2, text='Nome.:', font=('Arial 15 bold'), fg='white', bg='orange')
label_nome.place(x=10,y=10)
nome = Label(janela, width=10, height=2, text='João Futi', font=('Arial 15 bold'), fg='white', bg='orange')
nome.place(x=150,y=10)

label_idade = Label(janela, width=10, height=2, text='Idade.:' , font=('Arial 15 bold'), fg='white', bg='orange')
label_idade.place(x=10,y=80)
idade = Label(janela, width=10, height=2, text='50' , font=('Arial 15 bold'), fg='white', bg='orange')
idade.place(x=150,y=80)

label_pais = Label(janela, width=10, height=2, text='Pais.:', font=('Arial 15 bold'), fg='white', bg='orange')
label_pais.place(x=10,y=150)
pais = Label(janela, width=10, height=2, text='Angola', font=('Arial 15 bold'), fg='white', bg='orange')
pais.place(x=150,y=150)

janela.mainloop()