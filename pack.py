from tkinter import *

# cores
cor1 = '#bdc2db'  # cinza

janela = Tk()
janela.title('Pack')
janela.geometry('800x250')
janela.config(background=cor1)  # color picker no google

janela.iconphoto(False, PhotoImage(file='icon.png'))
janela.resizable(width=False, height=False)

label_nome = Label(janela, width=10, height=2, text='Nome.:',
                   font=('Arial 15 bold'), fg='white', bg='orange')
label_nome.pack(side=LEFT)

nome = Label(janela, width=10, height=2, text='João Futi',
             font=('Arial 15 bold'), fg='white', bg='orange')
nome.pack(side=LEFT)


label_idade = Label(janela, width=10, height=2, text='Idade.:',
                    font=('Arial 15 bold'), fg='white', bg='orange')
label_idade.pack(side=LEFT)

idade = Label(janela, width=10, height=2, text='50',
              font=('Arial 15 bold'), fg='white', bg='orange')
idade.place(x=150, y=80)
idade.pack(side=LEFT)

label_pais = Label(janela, width=10, height=2, text='Pais.:',
                   font=('Arial 15 bold'), fg='white', bg='orange')
label_pais.pack(side=LEFT)

pais = Label(janela, width=10, height=2, text='Angola',
             font=('Arial 15 bold'), fg='white', bg='orange')
pais.place(x=150, y=150)
pais.pack(side=LEFT)

janela.mainloop()
