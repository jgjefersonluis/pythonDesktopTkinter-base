from tkinter import *

#cores
cor1='#bdc2db' #cinza

janela = Tk()
janela.title('Olá, mundo!')
janela.geometry('600x300')
janela.config(background=cor1) # color picker no google

janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.resizable(width=False, height=False)

janela.mainloop()
