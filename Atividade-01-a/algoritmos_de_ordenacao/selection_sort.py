import time, os
from sys import platform

def selection_sort(lista:list): 
    print('\nExemplo de Ordenação utilizando o Método SELECTION SORT...\n')
    bar = "\\" if platform.endswith("win32") else "/"  
    # ----------------------------------------------------------------------
    # Montando a lista de valores a partir de um arquivo
    print('\nMontando a lista...\n')
    lstValores = lista
    # ----------------------------------------------------------------------
    # Ordenando a lista usando o algoritmo SELECTION SORT
    print('\nIniciando a Ordenação...\n')
    tInicial = time.time()

    for i in range(len(lstValores)):
        min_idx = i
        for j in range(i + 1, len(lstValores)):
            if lstValores[j] < lstValores[min_idx]:
                min_idx = j
        lstValores[i], lstValores[min_idx] = lstValores[min_idx], lstValores[i]

    tFinal = time.time()
    dTime  = tFinal - tInicial

    # ----------------------------------------------------------------------
    # Excrevendo a lista em um arquivo
    DIRATUAL      = os.path.dirname(os.path.abspath(__file__)) 
    ARQUIVO_OUTPUT = DIRATUAL + bar +'valores_ordenados_SelectionSort.txt'
    arquivo        = open(ARQUIVO_OUTPUT, 'w')
    for i in lstValores: arquivo.write(f'{i}\n')
    arquivo.close()


    print(f'\nTempo de Execução SelectionSort: {dTime} segundos\n')
