from tkinter import *

#cores
cor1='#bdc2db' #cinza

janela = Tk()
janela.title('Place')
janela.geometry('350x250')
janela.config(background=cor1) # color picker no google

janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.resizable(width=False, height=False)

label_1 = Label(janela, width=20, text="Nome.: ")
label_1.place(x=10,y=10)

label_2 = Label(janela, width=20, text="Idade.: ")
label_2.place(x=10,y=40)

label_3 = Label(janela, width=20, text="País.: ")
label_3.place(x=10,y=70)


janela.mainloop()