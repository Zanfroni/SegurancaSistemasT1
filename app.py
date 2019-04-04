import os

from processText import read
from processText import verifySize
from errorMessages import error

def app():
    os.system('clear')
    print('***Digite o arquivo de entrada***\n')
    print('- O arquivo deve estar no diretorio da execucao do programa')
    print('- A extensao do mesmo deve ser digitada junto\n')
    cipFile = read(input())
    print(cipFile)                                                            #DEBBUGING THINGS N' SHIT
    if not verifySize(cipFile): error(2)
    print('passei')

if __name__ == "__main__":
    app()



# TODO

'''
- Em segundo lugar, preciso percorrer com três caracteres o texto encontrando padrões cujo tamanho divida pela distância
- Se der com sucesso, reparte nas colunas
- Beleza, realiza análise de frequência (ainda vou ver mais a fundo)
- Display o texto claro. Se estiver insatisfeito, pode daí aumentar pra tentar decifrar com maior tamanho
- Se chegar ao fim do texto, termina com resultado falho!
'''
