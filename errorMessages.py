import os, sys

def error(index):
    os.system('clear')
    print('ERRO!!!')
    if index == 1:
        print('Entrada de arquivo inválida!')
        print('Reinicie o programa e tente novamente!\n')
    if index == 2:
        print('Tamanho de texto invalido!')
        print('Texto deve ter no minimo mais de 30 caracteres!\n')
    if index == 3:
        print('Erro durante escrita do texto em arquivo!')
        print('Verifique o texto de entrada e tente novamente!\n')
    if index == 4:
        print('Linguagem invalida!')
        print('Digite corretamente da proxima vez!\n')
    
    sys.exit()
