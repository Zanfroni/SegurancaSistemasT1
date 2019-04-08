import os, sys

def getKeySize(cipFile):
    
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
    
    for letter in cipFile:
        print(letter)
        alphabet[letter] = alphabet.get(letter) + 1
    
    
    print('\n\n\n\n\n\n')

    for shit in alphabet:
        print(shit + ' ' + str(alphabet.get(shit)))
    
    print('\n\n\n\n\n\n')
    print('beleza')
    
    print('to fazendo essa porra do caralho inicialmente só pra m=1')
    
    n = len(cipFile)*(len(cipFile)-1)
    totalSum = 0
    
    for letter in alphabet:
        totalSum += alphabet.get(letter)*(alphabet.get(letter)-1)
    
    ic = totalSum/n
    
    print('%.5f' % ic)
    
    return 0;
