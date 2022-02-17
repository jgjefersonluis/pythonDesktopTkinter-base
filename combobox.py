from tkinter.ttk import *
from tkinter import *
from tkinter import font


janela = Tk()
janela.title('Combobox')
janela.geometry('300x250')


# Nome ---------------------------
label_nome = Label(janela, width=15, height=2,
                   text='Faça a sua escolha', font=('Arial 10'), anchor=W)
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


def obter():
    resultado = combo.get()
    print(resultado)


# criando a combobox
combo = Combobox(janela)

# definindo valores para combobox
combo['values'] = ('Brasil', 'Argentina', 'Uruguai', 'Itália',
                   'Alemanha', 'França', 'Inglaterra', 'Espanha')
combo.current(0)
combo.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)


botao = Button(janela, command=obter, width=10, height=1, text='Ver resposta',
               relief='raised', bg='white')
botao.grid(row=2, column=0, padx=5, pady=20)

janela.mainloop()
