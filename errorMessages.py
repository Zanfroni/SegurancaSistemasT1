''' 
AVISO: O codigo DEVE ser executado usando Python3 (python3 app.py)
OBSERVACAO: Se existir um arquivo chamado "output.txt" no diretorio, o mesmo sera apagado
'''

# Bibliotecas nativas do Python importadas
import os, sys

# Esta funcao serve como tratamento basico de erros caso o usuario
# faca alguma malandragem. Ele recebe o index do erro e imprime
# a mensagem desse index. Da um shutdown final depois da mensagem
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
    
    # SHUTDOWN
    sys.exit()
