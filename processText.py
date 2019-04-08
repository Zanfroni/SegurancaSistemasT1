import os

from errorMessages import error

def read(inp):
    try:
        f = open(inp, "r")
        data = f.read().replace('\n', '')
        f.close()
        return data
    except:
        error(1)

def verifySize(text):
    if len(text) <= 30: return False
    return True
