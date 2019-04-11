''' 
AVISO: O codigo DEVE ser executado usando Python3 (python3 app.py)
OBSERVACAO: Se existir um arquivo chamado "output.txt" no diretorio, o mesmo sera apagado
'''

''' Bibliotecas nativas do Python importadas '''
import os
from time import sleep

# ESTE E A FUNCAO QUE APLICA INDICE DE COINCIDENCIA E RETORNA O TAMANHO DA CHAVE,
# ESCOLHIDO PELO USUARIO

''' VARIAVEIS GLOBAIS '''
# Indices de Coincidencia das linguagens
# targetIc vira o indice de acordo com a
# escolha do usuario em app.py
portuguese = 0.072723
english = 0.0686
targetIc = 0

# Listas e Dicionarios auxiliares usados para calcular os indices
icList = []
alphabet = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    
# Este dicionario ira conter os indices finais
# para medir e escolher o tamanho da chave
probableKeySize = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 0,
        23: 0,
        24: 0,
        25: 0,
        26: 0,
    }
    
# Tamanho maximo de chave que este algoritmo trabalha e 26
# size serve como restritor, logo, apenas o definiu como o
# tamanho do alfabeto em questao mesmo
size = len(alphabet)
   
    
    
    
    
''' ALGORITMO DE ENCONTRAR O TAMANHO DA CHAVE '''

# Inicio
def getKeySize(cipFile,languageIndex):
    
    global size, targetIc
    
    # Define a linguagem
    if languageIndex == 1: targetIc = portuguese
    elif languageIndex == 2: targetIc = english
    else: error(4)
    
    # Aqui ele conta os indices por cada coset
    # Faz a media dos indices usando Average()
    # Finalmente, retorna o candidato escolhido
    # pelo usuario no bestSize()
    for m in range(1,size+1):
        
        i = 0
        for i in range(m):
            
            countChars(cipFile,i,m)
        
        average = Average(icList)
        icList.clear()
        
        probableKeySize[m] = average
        average = 0       
    
    return bestSize()
    
# Funcao que conta os caracteres do intervalo coset
# definido. Aproveita e aplica a formula do indice de coincidencia
# e insere a soma para a chave de tamanho m na lista,
# faltando apenas fazer a media para ter o indice, que sera
# feita pelo Average()
def countChars(cipFile,i,m):
    
    global alphabet
    
    n = 0
    charSum = 0
    for char in cipFile[i::m]:
        alphabet[char] = alphabet.get(char) + 1
        n+=1
    
    for letter in alphabet:
        charSum += alphabet.get(letter)*(alphabet.get(letter)-1)
        alphabet[letter] = 0
        
    ic = charSum/(n*(n-1))
    icList.append(ic)

# Apenas faz a media do indice para o coset.
# Por exemplo, se o coset e 3 (ABC DEF GHI)
# ele faz a media destes todos, obtendo
# o indice de coincidencia. Retorna ele
# que sera guardado na lista de indices
# que sera escolhida pelo usuario no bestSize()
def Average(icList):
    return sum(icList) / len(icList)

# Funcao mais interface, que vai pegando os melhores candidatos
# do indice de coincidencia e dando a opcao do usuario escolher
# ele ou descartar e seguir para o proximo melhor
# Pensou-se em implementar esta escolha, ja que Vigenere nem
# sempre e um processo consistente dependendo do texto, ja que
# ele trabalha com possibilidade, entao nem sempre o melhor candidato
# e o correto
def bestSize():
    
    global probableKeySize
    
    os.system('clear')
    print('AVALIADO!!')
    sleep(1)
    print('\n\n')
    done = 0
    best = ''
    
    while done != 1 and done != 2:
        
        # https://stackoverflow.com/questions/18197359/python-dict-find-value-closest-to-x
        key, _ = min(probableKeySize.items(), key=lambda kv : abs(kv[1] - targetIc))
        
        print('Melhor concorrente foi ' + str(key))
        print('Digite 1 para escolher e 0 para negar e ir para o proximo melhor')
        choice = int(input())
        if choice == 1:
            done = 2
            break
        elif choice == 0:
            done = 1
            del probableKeySize[key]
        else:
            os.system('clear')
            print('Escolha invalida. Tente novamente.\n')
    
    i = 1
    os.system('clear')
    while (i < len(alphabet)) and (done != 2):
        
        # https://stackoverflow.com/questions/18197359/python-dict-find-value-closest-to-x
        key, _ = min(probableKeySize.items(), key=lambda kv : abs(kv[1] - targetIc))
        
        print('Proximo concorrente foi ' + str(key))
        print('Digite 1 para escolher e 0 para negar e ir para o proximo melhor')
        choice = int(input())
        if choice == 1:
            done = 2
            break
        elif choice == 0:
            i += 1
            del probableKeySize[key]
        else:
            os.system('clear')
            print('Escolha invalida. Tente novamente.\n')
            
    os.system('clear')
    return key
