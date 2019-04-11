''' 
AVISO: O codigo DEVE ser executado usando Python3 (python3 app.py)
OBSERVACAO: Se existir um arquivo chamado "output.txt" no diretorio, o mesmo sera apagado
'''

# Bibliotecas nativas do Python importadas
import os
from time import sleep

# Chamada de funcoes do programa
from errorMessages import error
from charConverter import converter
from charConverter import undo

# Esta funcao simplesmente recebe o file de entrada
# e usa o gerenciador de contexto para processar o
# texto no arquivo e salvar em uma String
# Trata erro de input
def read(inp):
    try:
        f = open(inp, "r")
        data = f.read().replace('\n', '')
        f.close()
        return data
    except:
        error(1)

# Funcao que primeiramente verifica se tem um "output.txt" existente
# no diretorio. Se tiver, apaga pra criar outro. Usa gerenciador de
# contexto para escrever o texto claro no arquivo e da output
# dele no diretorio onde o app.py foi executado
def write(clearText):
    if os.path.exists('output.txt'):
        print('\n')
        print('--> output.txt encontrado no diretorio')
        sleep(2)
        os.remove('output.txt')
        print('--> Apagado para criacao de um novo')
        print('\n')
        sleep(1)
    try:
        with open('output.txt', 'w') as f:
            f.write(clearText)
    except:
        error(3)

# Verifica se o texto tem pelo menos mais de 30 caracteres.
# Frases pequenas sao complicadas de serem decifradas em Vigenere
def verifySize(text):
    if len(text) <= 30: return False
    return True

# Funcao que usa a formular
# M_i = (C_i - K_i) mod 26
# para decifrar o texto
def getClearText(cipFile,key):
    
    clearText = []
    keyIndex = 0
    for char in cipFile:
        newChar = undo(((converter(char) - converter(key[keyIndex:keyIndex+1])) % 26))
        clearText.append(newChar)
        keyIndex += 1
        if keyIndex >= len(key): keyIndex = 0
     
    ''' Caso queiras visualizar o texto via terminal, descomente o print abaixo '''
    # print(''.join(clearText))
    return ''.join(clearText)
    
