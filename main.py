
import Fuction
import tkinter as ttk
from tkinter import filedialog
import os

pasta = ''


def get_diretorio():
    global pasta
    pasta = str(filedialog.askdirectory(title='selecione'))
    Label02['text'] = pasta
    Label03['text'] = "Diretório selecionado!"


def organizar():
    global pasta
    try:
        Fuction.arquivos_in(pasta)
        Label03['text'] = 'Pasta organizada ;)'
    except:
        Label03['text'] = "Você precisa selecionar um diretório"


def desorganizar():
    global pasta
    try:
        Fuction.arquivos_out(pasta)
        Label03['text'] = 'Ufa! Baguncei tudo para você'
    except:
        Label03['text'] = "Você precisa selecionar um diretório"


def apagarpastas():
    global pasta
    try:
        Fuction.apagar_pastas(pasta)
        Label03['text'] = 'Todas as pastas vázias foram apagadas'
    except:
        Label03['text'] = "Você precisa selecionar um diretório"


janela = ttk.Tk()
janela.title('Organizador de Arquivos')


frame01 = ttk.Frame(janela)
frame02 = ttk.Frame(janela)
frame03 = ttk.Frame(janela)


brand = ttk.PhotoImage(file="image1.gif")
label_img = ttk.Label(frame01, image=brand)


label01 = ttk.Label(
    frame02, text='SELECIONE UM DIRETÓRIO', font=('helvetica', 15))
Label02 = ttk.Label(frame02, text='', width='30',
                    relief='groove')
Label03 = ttk.Label(frame02, text='')

botao01 = ttk.Button(frame02, text='SELECIONAR',
                     command=get_diretorio)
botao02 = ttk.Button(
    frame03, text='Organizar', command=organizar)
botao03 = ttk.Button(
    frame03, text='Desorganizar', command=desorganizar)
botao04 = ttk.Button(
    frame03, text='Apagar Pastas vazias', command=apagarpastas)

botao01.grid(column=3, row=2, padx='5', sticky='w')
botao02.grid(column=0, row=0, padx='5')
botao03.grid(column=1, row=0, padx='5')
botao04.grid(column=2, row=0, padx='5')

frame01.grid(column=1, row=0)
frame02.grid(column=1, row=1, pady='5')
frame03.grid(column=1, row=2, pady='5', sticky='w')

label_img.grid(column=0, row=0, sticky='n')
label01.grid(column=0, row=0, sticky='w')
Label02.grid(column=0, row=2)
Label03.grid(column=0, row=3)


janela.mainloop()

