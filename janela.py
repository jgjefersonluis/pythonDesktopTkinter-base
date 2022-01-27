from tkinter import *

# cores
cor1 = '#bdc2bd'  # cinza

janela = Tk()
janela.title('Hello, world!')
janela.geometry('600x300')
janela.config(background=cor1)  # color picker no google

janela.iconphoto(False, PhotoImage(file='icon.png'))
janela.resizable(width=False, height=False)

janela.mainloop()
