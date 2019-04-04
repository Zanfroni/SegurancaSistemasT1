import os, sys

def error(index):
    os.system('clear')
    print('ERRO!!!')
    if index == 1:
        print('Entrada de arquivo inválida!')
        print('Reinicie o programa e tente novamente!\n')
    if index == 2:
        print('Tamanho de texto invalido!')
        print('Texto deve ter no minimo mais de 6 caracteres!\n')
    
    sys.exit()
