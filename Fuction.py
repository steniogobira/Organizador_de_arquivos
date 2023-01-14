import os


def arquivos_in(diretorio):

    os.chdir(diretorio)
    lista_arquivos = os.listdir()

    for arquivos in lista_arquivos:
        if os.path.isfile(arquivos):
            extensoes = arquivos.split('.')[-1]
            if extensoes != 'py':
                if os.path.exists(os.getcwd() + '/' + extensoes):
                    os.rename(arquivos, os.getcwd() + '/' +
                              extensoes + '/' + arquivos)
                else:
                    os.mkdir(arquivos.split('.')[-1])
                    os.rename(arquivos, os.getcwd() + '/' +
                              extensoes + '/' + arquivos)


def arquivos_out(diretorio):

    os.chdir(diretorio)
    lista_arquivos = os.listdir()

    for pasta in lista_arquivos:
        if os.path.isdir(pasta):
            lista_arquivos_pasta = os.listdir(os.getcwd() + '/' + pasta)
            for arquivos in lista_arquivos_pasta:
                os.rename(os.getcwd() + '/' + pasta + '/' +
                          arquivos, os.getcwd() + '/' + arquivos)
            os.rmdir(pasta)


def apagar_pastas(diretorio):

    os.chdir(diretorio)
    lista_arquivos = os.listdir()
    lista_pasta = [i for i in lista_arquivos if os.path.isdir(i)]

    for pastas in lista_pasta:
        if len(os.listdir(pastas)) == 0:
            os.rmdir(pastas)
