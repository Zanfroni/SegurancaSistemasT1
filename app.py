import os

from processText import read
from processText import verifySize
from processText import getClearText
from processText import write
from errorMessages import error
from getKeySize import getKeySize
from decipher import decipher

def app():
    os.system('clear')
    print('***Digite o arquivo de entrada***\n')
    print('- O arquivo deve estar no diretorio da execucao do programa')
    print('- A extensao do mesmo deve ser digitada junto')
    print('- O arquivo NAO deve conter espacamentos, pontuacoes e caracteres incomuns')
    print('- Garanta que nao exista um arquivo chamado output.txt no diretorio. Se existir, o mesmo sera excluido\n')
    rawFile = read(input())
    cipFile = rawFile.lower()
    if not verifySize(cipFile): error(2)
    keySize = getKeySize(cipFile)
    print('Keysize = ' + str(keySize))
    print('\n\nDigite agora a linguagem (portugues, digite 1 e ingles, digite 2): ', end = '')
    language = int(input())
    key = decipher(cipFile,keySize,language)
    print('Chave encontrada: ' + key)
    text = getClearText(cipFile,key)
    write(text)
    print('Texto salvo em arquivo!!')

if __name__ == "__main__":
    app()
