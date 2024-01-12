import time, os
from sys import platform


def buble_sort(lista:list):
    print('\nExemplo de Ordenação utilizando o Método BUBBLE SORT...\n')
    bar = "\\" if platform.endswith("win32") else "/"
    # ----------------------------------------------------------------------
    # Montando a lista de valores a partir de um arquivo
    lstValores = lista
    # ----------------------------------------------------------------------
    # Ordenando a lista usando o algoritmo BUBBLE SORT
    print('\nIniciando a Ordenação...\n')
    tInicial = time.time()

    intSize = len(lstValores)
    for i in range(intSize):
        for j in range(intSize - i - 1):
            if lstValores[j] > lstValores[j + 1]:
                lstValores[j], lstValores[j + 1] = lstValores[j + 1], lstValores[j]

    tFinal = time.time()
    dTime  = tFinal - tInicial

    # ----------------------------------------------------------------------
    # Excrevendo a lista em um arquivo
    DIRATUAL      = os.path.dirname(os.path.abspath(__file__)) 
    ARQUIVO_OUTPUT = DIRATUAL + bar +'valores_ordenados_Bubble.txt'

    arquivo        = open(ARQUIVO_OUTPUT, 'w')
    for i in lstValores: arquivo.write(f'{i}\n')
    arquivo.close()

    print(f'\nTempo de Execução BubbleSort: {dTime} segundos\n')