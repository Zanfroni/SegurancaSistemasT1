import math, os, sys, time

from getKeySize import countChars
from getKeySize import alphabet

from charConverter import alph
from charConverter import converter
from charConverter import undo
from charConverter import x2back

from errorMessages import error

from time import sleep

'''
    BASICAMENTE
    
    FAZ A MERDA DOS SHIFTS (implementado)
    CALCULA A FREQUENCIA DA MOTHERFUCKING COLUNA PARA A LETRA (FORMULA GAY)
    PEGA TODAS AS COLUNAS DAS LETRAS (f) E DIVIDE PELA FREQ TOTAL
    ORDENA POR MENOR NUM DICTZAO
    
'''

charList = []
finalKey = []
x2 = x2back

freqList = alphabet

portuguese = {'a':0.1463,'b':0.0104,'c':0.0388,'d':0.0499,'e':0.1257,
              'f':0.0102,'g':0.013,'h':0.0078,'i':0.0618,'j':0.039,
              'k':0.001,'l':0.0277,'m':0.0473,'n':0.0444,'o':0.0973,
              'p':0.0252,'q':0.012,'r':0.0653,'s':0.068,'t':0.0433,
              'u':0.0363,'v':0.0157,'w':0.0003,'x':0.0025,'y':0.0006,'z':0.0047}
#english = [,,,,,,,,,,,,,,,,,,,,,,,,,,,,,] #faco amanha

english = [['e',0.1270],['t',0.0905],['a',0.0816],['o',0.075],['i',0.0696],['n',0.0674],['s',0.0632],['h',0.0609],['r',0.0598],
           ['d',0.0425],['l',0.0402],['c',0.0278],['u',0.0275],['m',0.024],['w',0.0236],['f',0.0222],['g',0.0201],['y',0.0197],
           ['p',0.0192],['b',0.0149],['v',0.0097],['k',0.0077],['j',0.0015],['x',0.015],['q',0.009],['z',0.007]]
language = {}

def decipher(cipFile,keySize,languageIndex):
    
    global charList, key, freqList
    
    index = 0
    
    for i in range(keySize):
        finalKey.append('0')
        print(finalKey)
    
    if languageIndex == 1: language = portuguese
    elif languageIndex == 2: language = english
    else: error(4)
    
    while True or index != -1 :
        print('Escolha o index da chave para avaliar (0..tamanho da chave-1)')
        print('Digite -1 para finalizar')
        index = int(input())
        if index < 0 or index >= keySize: print('Key Index invalido!')
        elif index == -1:
            print('\n\nRetornando chave...')
            sleep(2)
            index = -1
        else:
            charList.clear()
            for i in cipFile[index::keySize]:
                charList.append(i)
            #Necessary?
            #for char in charList:
                #freqList[char] = freqList.get(char) + 1
                
            print(freqList)
            
            print('acima a freqlist')
            
            # Faz a substituicao e calcula as frequencias (ATE AQUI TA OK
            # LETTER É A LETRA QUE VOU SUBSTITUIR SHIFTAR
            for letter in alph:
                x = 0
                print(letter)
                
                auxList = []
                for char in charList:
                    print (char, end=' ')
                    newChar = undo((converter(char) - converter(letter)) % 26)
                    auxList.append(newChar)
                for char in auxList:
                    freqList[char] = freqList.get(char) + 1
                # temos a frequencia bugada 
                sizeF = len(auxList)
                print('SAIZE ' + str(sizeF))
                print(freqList)
                #Blz, PERFEITO
                
                # agora calcula logo essa merda
                # no language e facil, so botar language[letter]
                # nesse... freqlist[letter]??
                
                # pra LETTER, calcula a frequencia delas, na freqlist (foi), pega ela e divide pelo tamanho --> frequencia do coset da tal letra substituido pela LETTER
                for freqLetter in alph:
                    #calcula frequencia
                    f = freqList[freqLetter]/sizeF
                    print('DUTRA ' + str(f))
                    x += (math.pow((f - language[freqLetter]),2) / language[freqLetter])
                    print('LIXO' + str(language[freqLetter]))
                    print(x)
                # ELE SABE QUE VAI SER POR ORDEM ALFABETICA, NO WORRIES
                
                x2[letter] = x
                
                for letter in alph:
                    freqList[letter] = 0
                
                #tem que fazer com que o user ESCOLHA OU PASSE, como uma linkedlist
                
                # MAS, tem que organizar a porra da lista, de acordo com o caracter
                #melhor atirar em dicionario
                
            # caindo fora, terei uma LISTA de X_2s
            print('gimme a taste ' + str(x2))
                
            #AGORA, FAZ A SELECAO
            xsort=[]
            for key,value in x2.items():
                temp = key,value
                xsort.append(temp)
                x2[key] = 0
            xsort.sort(key=lambda tup: tup[1])
            xlist = [item[0] for item in xsort]
            
            print(xlist)
            print('FUCKING FUCK ' + str(finalKey))
            
            done = False
            while not done:
                print('Melhor concorrente foi ' + xlist[0])
                print('Digite 1 para escolher e 0 para negar e ir para o proximo melhor')
                choice = int(input())
                if choice == 1:
                    finalKey[index] = xlist[0]
                    done = True
                elif choice == 0: done = True
                else: print('Escolha invalida. Tente novamente.\n')
                 
            i = 1
            while i < len(xlist) or not done:
                done = False
                print('Proximo concorrente foi ' + xlist[i])
                print('Digite 1 para escolher e 0 para negar e ir para o proximo melhor')
                choice = int(input())
                if choice == 1:
                    finalKey[index] = xlist[i]
                    done = True
                elif choice == 0:
                    i += 1
                else: print('Escolha invalida. Tente novamente.\n')
        
        return ''.join(key)
                
