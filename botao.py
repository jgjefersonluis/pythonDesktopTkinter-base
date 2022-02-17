from tkinter import *

janela = Tk()
janela.title('Botao')
janela.geometry('400x250')

global contador
contador = 1

def executar():
    global contador
    texto_1 = 'Numero impar: '
    texto_2 = 'Numero par: '

    if (contador %2) == 0:
        resultado = texto_2 + str(contador)
        label['text'] = resultado
        label['fg'] = '#24851e'
    else:
        resultado = texto_1 + str(contador)
        label['text'] = resultado
        label['fg'] = '#2586c2'

    contador +=1

label = Label(janela, width=20, height=2, text='Texto sera apresentado', relief='flat', fg='white', bg='#121211')
label.grid(row=0, column=0, padx=5, pady=10)

botao = Button(janela, command=executar, width=8, height=1, text='Clica aqui', relief='raised', fg='#fcb603', bg='gray')
botao.grid(row=0, column=1, padx=5, pady=10)


janela.mainloop()