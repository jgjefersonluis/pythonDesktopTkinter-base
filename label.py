from tkinter import *

# cores
cor1 = '#bdc2bd'  # cinza

janela = Tk()
janela.title('Label')
janela.geometry('350x250')
janela.config(bg=cor1)  # color picker no google

janela.iconphoto(False, PhotoImage(file='icon.png'))
janela.resizable(width=False, height=False)

label_nome = Label(janela, width=10, height=2, text='Nome.: ',
                   font=('Arial 15 bold'), bg='orange', fg='black')
label_nome.grid(row=0, column=0, pady=10)

label_idade = Label(janela, width=10, height=2, text='Idade.: ',
                    font=('Arial 15 bold'), bg='orange', fg='black')
label_idade.grid(row=1, column=0, pady=10)

label_pais = Label(janela, width=10, height=2, text='País.: ',
                   font=('Arial 15 bold'), bg='orange', fg='black')
label_pais.grid(row=2, column=0, pady=10)


janela.mainloop()
