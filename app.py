''' 
AVISO: O codigo DEVE ser executado usando Python3 (python3 app.py)
OBSERVACAO: Se existir um arquivo chamado "output.txt" no diretorio, o mesmo sera apagado
'''

# Bibliotecas nativas do Python importadas
import os
from time import sleep

# Chamada de funcoes do programa
from processText import read
from processText import verifySize
from processText import getClearText
from processText import write
from errorMessages import error
from getKeySize import getKeySize
from decipher import decipher


# Este e a funcao que inicia tudo. Serve como interface para o usuario
# fazer escolhas da linguagem do texto (portugues ou ingles), assim
# como dar algumas advertencias sobre o escopo do codigo
# Passos:
# 1 - Recebe o texto cifrado como input e o processa para uma string (processText --> read)
# 2 - Manda essa string para a funcao que encontra o tamanho da chave (getKeySize)
# 3 - Manda o tamanho da chave e a string para uma funcao que encontra a chave (decipher)
# 4 - Manda a chave e o texto cifrado para uma funcao que decodifica e escrever num .txt como output (processText --> write)
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
    
    print('\n\nDigite agora a linguagem (portugues, digite 1 e ingles, digite 2): ', end = '')
    language = int(input())
    
    keySize = getKeySize(cipFile,language)
    
    os.system('clear')
    print('CHAVE ENCONTRADA!!!')
    print('Tamanho da chave = ' + str(keySize))
    sleep(1)
    os.system('clear')
    
    key = decipher(cipFile,keySize,language)
    os.system('clear')
    
    print('Chave encontrada: ' + key)
    sleep(1)
    os.system('clear')
    
    text = getClearText(cipFile,key)
    write(text)
    print('Texto salvo em arquivo!!')

# Inicio
if __name__ == "__main__":
    app()
