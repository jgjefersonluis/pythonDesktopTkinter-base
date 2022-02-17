import tkinter


from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry('400x400')

frame_1 = Frame(janela, width=200, height=100, bg='blue')
frame_1.grid(row=0, column=0, pady=2, padx=2)

frame_2 = Frame(janela, width=200, height=100, bg='yellow')
frame_2.grid(row=0, column=1, pady=2, padx=2)

frame_3 = Frame(janela, width=200, height=100, bg='red')
frame_3.grid(row=1, column=0, pady=2, padx=2)

frame_4 = Frame(janela, width=200, height=100, bg='green')
frame_4.grid(row=1, column=1, pady=2, padx=2)

frame_5 = Frame(frame_1, width=150, height=80, bg='gray')
frame_5.grid(row=3, column=0, pady=2, padx=2)

janela.mainloop()
