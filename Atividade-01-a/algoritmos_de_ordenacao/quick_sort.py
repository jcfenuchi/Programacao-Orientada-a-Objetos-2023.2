import time, os
from sys import platform

def quick_sort(lista:list):
    print('\nExemplo de Ordenação utilizando o Método Quick Sort...\n')
    bar = "\\" if platform.endswith("win32") else "/"
    lstValores = lista 
    print('\nIniciando a Ordenação...\n')
    tInicial = time.time()
    quick_sort_algorithm(lista) # quicksort
    tFinal = time.time()
    dTime  = tFinal - tInicial
        # ----------------------------------------------------------------------
    # Excrevendo a lista em um arquivo
    DIRATUAL      = os.path.dirname(os.path.abspath(__file__)) 
    ARQUIVO_OUTPUT = DIRATUAL + bar +'valores_ordenados_QuickSort.txt'
    arquivo        = open(ARQUIVO_OUTPUT, 'w')
    for i in lstValores: arquivo.write(f'{i}\n')
    arquivo.close()
    print(f'\nTempo de Execução QuickSort: {dTime} segundos\n')

def quick_sort_algorithm(lista,inicio=0,fim=None):
    if fim is None: # se nao for passado o fim ele assume a lista toda
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim) # divide a lista em 2 partes entre o pivot
        quick_sort_algorithm(lista, inicio, p-1) # trata os valores da esqueda
        quick_sort_algorithm(lista, p+1 , fim) # trata valores da direita 
    return lista

def partition(lista,inicio,fim):
    # Ativar doc=True => para entender. o metodo é i = 0, quando ele encontra um valor menor que o pivot
    # ele troca os valores de posicao o i coloca no j e o j no i  e soma +1 no I 
    # porque no fim basta saber que o pivot está no lugar certo ai aplica afuncao recursivamente para antes e depois do pivot atual.
    doc = False
    pivot = lista[fim]
    i = inicio
    if doc: # apenas doc
        print(f"inicio={i}, fim={fim}, pivot={pivot}")
    for j in range(inicio,fim):
        if lista[j] <= pivot:
            lista[j],lista[i] = lista[i],lista[j]
            i += 1
        if doc: # apenas doc
            print(lista, "DENTRO DO da Iteracao!")
    lista[i],lista[fim] = lista[fim],lista[i]
    if doc: # apenas doc
        print(lista,"---- FIM DE UMA ITERACAO")
    return i