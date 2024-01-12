import random
import os
import sys
from sys import platform
from time import time


class Lista:
    # ----------------------------------------------------------------------
    # Atributos
    __lstValores = None
    __DIRATUAL = os.path.dirname(os.path.abspath(__file__))

    # ----------------------------------------------------------------------
    # Método Construtor
    def __init__(self, *args):
        if len(args) == 3 and isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int):
            self.__lstValores = [random.randint(args[1], args[2]) for _ in range(args[0])]
        elif len(args) == 1 and isinstance(args[0], str):
            try:
                if platform == "Linux":
                    arquivo = open(self.__DIRATUAL + '/' + args[0], 'r')
                else:
                    arquivo = open(self.__DIRATUAL + '\\' + args[0], 'r')
            except FileNotFoundError:
                self.__lstValores = 'ERRO: Arquivo Não Encontrado...'
            except Exception:
                self.__lstValores = f'ERRO: {sys.exc_info()[0]}...'
            else:
                self.__lstValores = list()
                while True:
                    valor = arquivo.readline()[:-1]
                    if not valor:
                        break
                    self.__lstValores.append(int(valor))
                arquivo.close()
        else:
            self.__lstValores = 'ERRO: Argumentos Inválidos ou Incompletos'

    # ----------------------------------------------------------------------
    @property
    def ListaValores(self):
        return self.__lstValores

    def time_it(func):
        def inner_func(*args, **kargs):
            t1 = time()
            execute = func(*args, **kargs)
            t2 = time()
            print(f"a função {func.__name__} demorou {t2-t1}s Para Ordernar.")
            return execute
        return inner_func

    # ----------------------------------------------------------------------
    @time_it
    def Ordena_Bubble(self, lista_valores: list = None):
        lista_valores = self.__lstValores[:]
        intSize = len(lista_valores)
        for i in range(intSize):
            for j in range(intSize - i - 1):
                if lista_valores[j] > lista_valores[j + 1]:
                    lista_valores[j], lista_valores[j + 1] = lista_valores[j + 1], lista_valores[j]
        return lista_valores

    # ----------------------------------------------------------------------
    @time_it
    def Ordena_Selection(self, lista_valores: list = None):
        lista_valores = self.__lstValores[:]
        for i in range(len(lista_valores)):
            min_idx = i
            for j in range(i + 1, len(lista_valores)):
                if lista_valores[j] < lista_valores[min_idx]:
                    min_idx = j
            lista_valores[i], lista_valores[min_idx] = lista_valores[min_idx], lista_valores[i]
        return lista_valores

    # ----------------------------------------------------------------------
    @time_it
    def Ordena_Insertion(self, lista_valores: list = None):
        lista_valores = self.__lstValores[:]
        for i in range(1, len(lista_valores)):
            key = lista_valores[i]
            j = i - 1
            while j >= 0 and lista_valores[j] > key:
                lista_valores[j + 1] = lista_valores[j]
                j -= 1
            lista_valores[j + 1] = key
        return lista_valores

    # ----------------------------------------------------------------------
    @time_it
    def Ordena_Quick(self, lista_valores: list = None):
        lista_valores = self.__lstValores[:]

        def quick_sort_algorithm(lista, inicio=0, fim=None):
            if fim is None:  # se nao for passado o fim ele assume a lista toda
                fim = len(lista) - 1
            if inicio < fim:
                p = partition(lista, inicio, fim)  # divide a lista em 2 partes entre o pivot
                quick_sort_algorithm(lista, inicio, p-1)  # trata os valores da esqueda
                quick_sort_algorithm(lista, p+1, fim)  # trata valores da direita 
            return lista

        def partition(lista, inicio, fim):
            # Ativar doc=True => para entender. o metodo é i = 0, quando ele encontra um valor menor que o pivot
            # ele troca os valores de posicao o i coloca no j e o j no i  e soma +1 no I 
            # porque no fim basta saber que o pivot está no lugar certo ai aplica afuncao recursivamente para antes e depois do pivot atual.
            doc = False
            pivot = lista[fim]
            i = inicio
            if doc:  # apenas doc
                print(f"inicio={i}, fim={fim}, pivot={pivot}")
            for j in range(inicio, fim):
                if lista[j] <= pivot:
                    lista[j], lista[i] = lista[i], lista[j]
                    i += 1
                if doc:  # apenas doc
                    print(lista, "DENTRO DO da Iteracao!")
            lista[i], lista[fim] = lista[fim],lista[i]
            if doc:  # apenas doc
                print(lista, "---- FIM DE UMA ITERACAO")
            return i

        return quick_sort_algorithm(lista_valores)
