import math, os, sys, time

from getKeySize import countChars
from getKeySize import alphabet

from charConverter import alph
from charConverter import converter
from charConverter import undo
from charConverter import x2back

from errorMessages import error

from time import sleep

charList = []
finalKey = []
x2 = x2back

freqList = alphabet

portuguese = {'a':0.1463,'b':0.0104,'c':0.0388,'d':0.0499,'e':0.1257,
              'f':0.0102,'g':0.013,'h':0.0078,'i':0.0618,'j':0.039,
              'k':0.001,'l':0.0277,'m':0.0473,'n':0.0444,'o':0.0973,
              'p':0.0252,'q':0.012,'r':0.0653,'s':0.068,'t':0.0433,
              'u':0.0363,'v':0.0157,'w':0.0003,'x':0.0025,'y':0.0006,'z':0.0047}
english = {'a':0.0816,'b':0.0149,'c':0.0278,'d':0.0425,'e':0.1270,
           'f':0.0222,'g':0.0201,'h':0.0609,'i':0.0696,'j':0.0015,
           'k':0.0077,'l':0.0402,'m':0.024,'n':0.0674,'o':0.075,
           'p':0.0192,'q':0.009,'r':0.0598,'s':0.0632,'t':0.0905,
           'u':0.0275,'v':0.0097,'w':0.0236,'x':0.015,'y':0.0197,'z':0.007}
language = {}

def decipher(cipFile,keySize,languageIndex):
    
    global charList, key, freqList
    
    index = 0
    
    for i in range(keySize):
        finalKey.append('0')
    
    if languageIndex == 1: language = portuguese
    elif languageIndex == 2: language = english
    else: error(4)
    
    while index != -1:
        print('Escolha o index da chave para avaliar (0..tamanho da chave-1)')
        print('Digite -1 para finalizar')
        index = int(input())
        if index < -1 or index >= keySize: print('Key Index invalido!')
        elif index == -1:
            print('\n\nRetornando chave...')
            sleep(2)
            index = -1
        else:
            charList.clear()
            for i in cipFile[index::keySize]:
                charList.append(i)
           
            for letter in alph:
                x = 0
                
                auxList = []
                for char in charList:
                    newChar = undo((converter(char) - converter(letter)) % 26)
                    auxList.append(newChar)
                for char in auxList:
                    freqList[char] = freqList.get(char) + 1

                sizeF = len(auxList)
                for freqLetter in alph:
                    f = freqList[freqLetter]/sizeF
                    x += (math.pow((f - language[freqLetter]),2) / language[freqLetter])
                
                x2[letter] = x
                
                for letter in alph:
                    freqList[letter] = 0
                
            xsort=[]
            for key,value in x2.items():
                temp = key,value
                xsort.append(temp)
                x2[key] = 0
            xsort.sort(key=lambda tup: tup[1])
            xlist = [item[0] for item in xsort]
            
            os.system('clear')
            print('AVALIADO!!')
            sleep(1)
            print('\n\n')
            done = 0
            while done != 1 and done != 2:
                print('Melhor concorrente foi ' + xlist[0])
                print('Digite 1 para escolher e 0 para negar e ir para o proximo melhor')
                choice = int(input())
                if choice == 1:
                    finalKey[index] = xlist[0]
                    done = 2
                elif choice == 0: done = 1
                else:
                    os.system('clear')
                    print('Escolha invalida. Tente novamente.\n')
                 
            i = 1
            os.system('clear')
            while (i < len(xlist)) and (done != 2):
                print('Proximo concorrente foi ' + xlist[i])
                print('Digite 1 para escolher e 0 para negar e ir para o proximo melhor')
                choice = int(input())
                if choice == 1:
                    finalKey[index] = xlist[i]
                    done = 2
                elif choice == 0:
                    i += 1
                else:
                    os.system('clear')
                    print('Escolha invalida. Tente novamente.\n')
            
            os.system('clear')
        
    return ''.join(finalKey)
                
