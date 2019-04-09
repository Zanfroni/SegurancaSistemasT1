import os, sys, time

from getKeySize import countChars
from getKeySize import alphabet

charList = []

def decipher(cipFile,keySize):
    
    global charList
    
    for i in range(keySize):
        charList.clear()
        for j in cipFile[i::keySize]:
            charList.append(j)
        for char in charList:
            alphabet[char] = alphabet.get(char) + 1
        print('lista teste ' + str(i) + ' Tamanho ' + str(charList))
        print()
        print()
        print()
        print('frequencia teste ' + str(alphabet))
        print()
        print()
        print()
        print()
        print()
        print()
        print()

# Agora, é hora de shiftar,quarta-feira acabo ceerto essa bosta!!
