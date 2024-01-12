import time, os
from sys import platform

def insertion_sort(lista:list):
    print('\nExemplo de Ordenação utilizando o Método INSERTION SORT...\n')
    bar = "\\" if platform.endswith("win32") else "/"
    # ----------------------------------------------------------------------
    # Montando a lista de valores a partir de um arquivo

    lstValores = lista 
    # ----------------------------------------------------------------------
    # Ordenando a lista usando o algoritmo INSERTION SORT
    print('\nIniciando a Ordenação...\n')
    tInicial = time.time()

    for i in range(1, len(lstValores)):
        key = lstValores[i]
        j = i - 1
        while j >= 0 and lstValores[j] > key:
            lstValores[j + 1] = lstValores[j]
            j -= 1
        lstValores[j + 1] = key

    tFinal = time.time()
    dTime  = tFinal - tInicial

    # ----------------------------------------------------------------------
    # Excrevendo a lista em um arquivo
    DIRATUAL      = os.path.dirname(os.path.abspath(__file__)) 
    ARQUIVO_OUTPUT = DIRATUAL + bar +'valores_ordenados_InsertionSort.txt'
    arquivo        = open(ARQUIVO_OUTPUT, 'w')
    for i in lstValores: arquivo.write(f'{i}\n')
    arquivo.close()


    print(f'\nTempo de Execução InsertionSort: {dTime} segundos\n')
