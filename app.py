import os

from processText import read
from processText import verifySize
from errorMessages import error
from getKeySize import getKeySize
from decipher import decipher

def app():
    os.system('clear')
    print('***Digite o arquivo de entrada***\n')
    print('- O arquivo deve estar no diretorio da execucao do programa')
    print('- A extensao do mesmo deve ser digitada junto\n')
    cipFile = read(input())
    if not verifySize(cipFile): error(2)
    keySize = getKeySize(cipFile)
    print('Keysize = ' + str(keySize))
    decipher(cipFile,keySize)

if __name__ == "__main__":
    app()



# TODO

'''
- Imprimir as coincidências das chaves
- Implementar a análise de frequência
- Decifrar o texto
- Escrever o texto decifrado em um .txt
'''

'''
- lowercase everything? even the extension
'''
