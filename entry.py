from tkinter import *

janela = Tk()
janela.title('Entry')
janela.geometry('450x200')

# função OBTER


def obter():
    nome = enntry_nome.get()
    idade = enntry_idade.get()
    pais = enntry_pais.get()

    label_nome_re['text'] = nome
    label_idade_re['text'] = idade
    label_pais_re['text'] = pais

    enntry_nome.delete(0, END)
    enntry_idade.delete(0, END)
    enntry_pais.delete(0, END)


# Nome ---------------------------------------------------------
label_nome = Label(janela, width=10, height=2, text='Nome: ',
                   font=('Arial 10'), anchor='w')
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)
enntry_nome = Entry(janela, width=10, font=('Arial 10'))
enntry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = Label(janela, width=10, height=2,
                    text='Idade: ', font=('Arial 10'), anchor='w')
label_idade.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)
enntry_idade = Entry(janela, width=10, font=('Arial 10'))
enntry_idade.grid(row=1, column=1, padx=10, pady=5)

label_pais = Label(janela, width=10, height=2, text='País: ',
                   font=('Arial 10'), anchor='w')
label_pais.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)
enntry_pais = Entry(janela, width=10, font=('Arial 10'))  # , state='disable'
enntry_pais.grid(row=2, column=1, padx=10, pady=5)

# resposta -----------------------------------------
label_nome_re = Label(janela, width=15, height=2, text='', font=('Arial 10'))
label_nome_re.grid(row=0, column=2, padx=10, pady=5, sticky=NSEW)

label_idade_re = Label(janela, width=15, height=2, text='', font=('Arial 10'))
label_idade_re.grid(row=1, column=2, padx=10, pady=5, )

label_pais_re = Label(janela, width=15, height=2, text='', font=('Arial 10'))
label_pais_re.grid(row=2, column=2, padx=10, pady=5, sticky=NSEW)

botao = Button(janela, command=obter, width=12, height=1,
               text='Ver os dados', relief='raised', fg='#ffffff', bg='green')
botao.grid(row=3, column=0, padx=5, pady=10)


janela.mainloop()
