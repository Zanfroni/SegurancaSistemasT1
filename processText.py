import os
from time import sleep

from errorMessages import error
from charConverter import converter
from charConverter import undo

def read(inp):
    try:
        f = open(inp, "r")
        data = f.read().replace('\n', '')
        f.close()
        return data
    except:
        error(1)

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

def verifySize(text):
    if len(text) <= 30: return False
    return True

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
    
