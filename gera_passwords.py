# --------------------------------------------------------------------
# Programa de geraçao de passwords entre 4 e 16 caracteres
# NC  22-10-2013
# V1.0.0a 23-10-2013 : criaçao do esqueleto do programa em consola
# V1.0.1a 19-07-2019 : grava ficheiro .txt com passwords geradas
#                      1a Versao para o GitHub
# --------------------------------------------------------------------
__author__ = 'Nelson Cerqueira'
__maintainer__ = "NC PySoft"
__version__ = "V1.0.1a"


import string
import random


def cria_string(NumCaracteres):
    '''Define uma string com numeros e letras, maiusculas e minusculas,
        que servira para criar a password.
    '''
    # simbolos = '!Ã¢â‚¬â€œ$%#?_*'
    simbolos = '!$%#?*'
    str_ascii = string.digits + string.ascii_letters + simbolos
    str_out = ""
    for i in range(NumCaracteres):
        str_out += gera_password(str_ascii)
        # print(str_out)
    return str_out


def gera_password(str_ascii):
    '''Devolve um caractere aleatorio da lista fornecida.'''
    return random.choice(str_ascii)


def cria_ficheiro(lpass=[], ficheiro=None):
    '''Recebe a lista com as passwords e grava um ficheiro passw.txt.'''
    # print("lista criada=", l)
    fich = open(ficheiro, 'w')
    for i in range(len(lpass)):
        fich.write(lpass[i] + '\n')
    fich.close()


def main_loop():
    lista = []
    try:
        str = input("[0 - Abandona] Numero de caracteres da Password [4 - 16]: ")
        if ((int(str) >= 4) and (int(str) <= 16)):
            num = input("Número de Passwords a gerar: ")
            for i in range(int(num)):
                lista.append(cria_string(int(str)))
                print(lista[i])
            print("\n")
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
