import os


def arquivos_in(diretorio):

    os.chdir(diretorio)
    lista_arquivos = os.listdir()

    for arquivos in lista_arquivos:
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
    lista_pastas = os.listdir()

    for pasta in lista_pastas:

        if pasta.split('.')[-1] != 'py':
            lista_arquivos = os.listdir(os.getcwd() + '/' + pasta)
            for arquivos in lista_arquivos:
                os.rename(os.getcwd() + '/' + pasta + '/' +
                          arquivos, os.getcwd() + '/' + arquivos)
            os.rmdir(pasta)
