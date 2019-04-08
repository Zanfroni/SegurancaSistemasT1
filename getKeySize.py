import os, sys, time

targetIc = 0.072723
size = 10
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
    

def getKeySize(cipFile):
    
    global size

    for m in range(1,size+1):
        
        i = 0
        for i in range(m):
            
            countChars(cipFile,i,m)
        
        average = Average(icList)
        icList.clear()
        
        probableKeySize[m] = average
        average = 0       
    
    return bestSize()
    
def countChars(cipFile,i,m):
    
    global alphabet, icList
    
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

def Average(icList):
    return sum(icList) / len(icList)

def bestSize():
    
    global probableKeySize
    
    # https://stackoverflow.com/questions/18197359/python-dict-find-value-closest-to-x
    key, value = min(probableKeySize.items(), key=lambda kv : abs(kv[1] - targetIc))
    return key
