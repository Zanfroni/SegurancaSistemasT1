import os, sys, time

from getKeySize import countChars
from getKeySize import alphabet
from charConverter import converter
from charConverter import undo

from errorMessages import error

charList = []

highest = -1
keyword = ''
keyChars = []

decList = alphabet

portuguese = ['a','e','o','s','r','i','n','d','m','u','t','c','l','p','v','g','h','q','b','f','z','j','x','k','w','y']
english = ['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']
language = []

def decipher(cipFile,keySize,languageIndex):
    
    global charList
    
    if languageIndex == 1: language = portuguese
    elif languageIndex == 2: language = english
    else: error(4)
    
    for i in range(keySize):
        highest = -1
        charList.clear()
        for j in cipFile[i::keySize]:
            charList.append(j)
        for char in charList:
            alphabet[char] = alphabet.get(char) + 1
            
        dictlist = []
        for key, value in alphabet.items():
            temp = [key,value]
            dictlist.append(temp)
        # https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
        dictlist.sort(key=lambda tup: tup[1], reverse=True)
        
        for letter in language:
            for char in charList:
                newChar = undo((converter(char) - converter(letter)) % 26)
                decList[newChar] = decList.get(newChar) + 1
            
            auxlist=[]
            for key,value in decList.items():
                temp = [key,value]
                auxlist.append(temp)
                decList[key] = 0
            auxlist.sort(key=lambda tup: tup[1], reverse=True)
            
            comparation = [item[0] for item in auxlist]
            
            count = 0
            for i in range(len(language)):
                if comparation[i] == language[i]: count += 1
            
            if count > highest:
                highest = count
                keyword = letter
            
            
        # Insere a chave
        keyChars.append(keyword)
            
    key = ''.join(str(e) for e in keyChars)
    return key
