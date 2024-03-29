# ------------------------------------------------------------------------------------------
# Programa de geraçao de passwords entre 4 e 16 caracteres e que,
# para além de mostrar as passwords na consola, cria ficheiro .txt de output
# NC
# V1.0.0 23-10-2013 : criaçao da primeira versão do programa. Mostra passwords na consola
# V1.0.1 19-07-2019 : grava ficheiro .txt com passwords geradas
#                      1a Versao para o GitHub
# ------------------------------------------------------------------------------------------
__author__ = 'Nelson Cerqueira'
__maintainer__ = "NC PySoft <nelsonfvc@hotmail.com>"
__version__ = "V1.0.1 2019-07-19"

import string
import random


class Parametros(object):
    """Classe para definição de variáveis globais"""
    STR_ASCII = string.digits + string.ascii_letters+'!$%#?*'


def cria_string(NumCaracteres):
    '''Define uma string com numeros e letras, maiusculas e minusculas,
        que servira para criar a password.
    '''
    str_out = ""
    for i in range(NumCaracteres):
        str_out += gera_password(Parametros.STR_ASCII)
    return str_out


def gera_password(str_ascii):
    '''Devolve um caractere aleatorio da lista fornecida.'''
    return random.choice(str_ascii)


def cria_ficheiro(lpass=[], ficheiro=None):
    '''Recebe a lista com as passwords e grava um ficheiro passw.txt.'''
    fich = open(ficheiro, 'w')
    [fich.write(lpass[i] + '\n') for i in range(len(lpass))]
    fich.close()


def main_loop():
    try:
        str = input("[0 - Abandona] Numero de caracteres da Password [4 - 16]: ")
        if ((int(str) >= 4) and (int(str) <= 16)):
            num = input("Número de Passwords a gerar: ")
            lista = [cria_string(int(str)) for i in range(int(num))]
            [print(password) for password in lista]
            cria_ficheiro(lista, "./passw.txt")
        elif int(str) == 0:
            exit()
        else:
            print("O numero informado deve estar compreendido entre 4 e 16!", "\n")
            main_loop()
    except (ValueError) as e:
        print(" ERRO! Caractere não suportado ... ", e, "\n")
        main_loop()


if __name__ == '__main__':
    while True:
        main_loop()
