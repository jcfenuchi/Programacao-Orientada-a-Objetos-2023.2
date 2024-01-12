import random, os
from sys import platform

def gerar_lista(size:int, min_value:int, max_value:int):
    # ----------------------------------------------------------------------
    # Gerando uma lista com 100.000 elementos 
    # com valores entre 1 e 1.000.000 (pode haver números repetidos)
    SIZELISTA = size # tamanho da lista
    MINVALUE  = min_value # valor minimo
    MAXVALUE  = max_value # valor maximo
    lstValores = [random.randint(MINVALUE, MAXVALUE) for _ in range(SIZELISTA)]

    # ----------------------------------------------------------------------
    # Excrevendo a lista em um arquivo
    DIRATUAL    = os.path.dirname(os.path.abspath(__file__))
    if platform.startswith("linux"):  # para linux
        NOMEARQUIVO = DIRATUAL + '/valores_nao_ordenados.txt'  
    elif platform.startswith("win32"): # para windows
        NOMEARQUIVO = DIRATUAL + '\valores_nao_ordenados.txt'

    arquivo     = open(NOMEARQUIVO, 'w')
    for i in lstValores: arquivo.write(f'{i}\n')    
    arquivo.close()

    # retorna a lista na memoria
    with open(NOMEARQUIVO, "r") as file: 
        lista =  file.read().split("\n")
        lista = lista[:-1] if lista[-1] == "" else lista 
    return list(map(int, lista))
        