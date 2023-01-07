
import Fuction
import tkinter as ttk
from tkinter import filedialog
import os


def get_diretorio():
    pasta = str(filedialog.askdirectory(title='selecione'))
    Label02['text'] = pasta

    def organizar():
        Fuction.arquivos_in(pasta)
    botao02 = ttk.Button(
        frame02, text='Organizar', command=organizar)
    botao02.grid(column=0, row=6)

    def desorganizar():
        Fuction.arquivos_out(pasta)
    botao03 = ttk.Button(
        frame02, text='Desorganizar', command=desorganizar)
    botao03.grid(column=2, row=6)


janela = ttk.Tk()
janela.title('Organizador de Arquivos')


frame01 = ttk.Frame(janela)
frame01.grid(column=1, row=0)

frame02 = ttk.Frame(janela)
frame02.grid(column=1, row=2)


label01 = ttk.Label(
    frame01, text='SELECIONE UM DIRETÓRIO', font=('helvetica', 15))
label01.grid(column=0, row=0)

Label02 = ttk.Label(frame02, text='', borderwidth=2,
                    relief='groove', height='1', width='50')
Label02.grid(column=0, row=2)


botao01 = ttk.Button(frame02, text='SELECIONAR',
                     command=get_diretorio)
botao01.grid(column=3, row=2)


janela.mainloop()
