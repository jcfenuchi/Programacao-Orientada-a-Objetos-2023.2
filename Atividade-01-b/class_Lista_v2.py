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
    __ORDENACOES = ['Bubble', 'Selection', 'Insertion', 'Quick']

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
                    if not (valor := arquivo.readline()[:-1]):
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
        def inner_func(self, *args, **kargs):
            t1 = time()
            execute = func(self, *args, **kargs)
            t2 = time()
            print(f"a função {func.__name__} usando {kargs['metodo_ordenacao']} demorou {t2-t1}s Para Ordernar.")
            return execute
        return inner_func

    # ----------------------------------------------------------------------
    @time_it
    def Ordena(self, metodo_ordenacao: str):
        if metodo_ordenacao.title() not in self.__ORDENACOES:
            return "Erro Metodo Invalido!"
        elif metodo_ordenacao.title() == "Bubble":
            self.__bubble()

        elif metodo_ordenacao.title() == "Selection":
            self.__selection()

        elif metodo_ordenacao.title() == "Insertion":
            self.__insertion()

        elif metodo_ordenacao.title() == "Quick":
            self.__quick()

    # ----------------------------------------------------------------------
    def __bubble(self):
        intSize = len(self.__lstValores)
        for i in range(intSize):
            for j in range(intSize - i - 1):
                if self.__lstValores[j] > self.__lstValores[j + 1]:
                    self.__lstValores[j], self.__lstValores[j + 1] = self.__lstValores[j + 1], self.__lstValores[j]
    # --------------------------------------------------------------------------
    def __insertion(self):
        for i in range(1, len(self.__lstValores)):
            key = self.__lstValores[i]
            j = i - 1
            while j >= 0 and self.__lstValores[j] > key:
                self.__lstValores[j + 1] = self.__lstValores[j]
                j -= 1
            self.__lstValores[j + 1] = key

    # ----------------------------------------------------------------------
    def __selection(self):
        for i in range(len(self.__lstValores)):
            min_idx = i
            for j in range(i + 1, len(self.__lstValores)):
                if self.__lstValores[j] < self.__lstValores[min_idx]:
                    min_idx = j
            self.__lstValores[i], self.__lstValores[min_idx] = self.__lstValores[min_idx], self.__lstValores[i]   
    # ---------------------------------------------------------------------
    def __quick(self):
        def quick_sort_algorithm(lista, inicio=0, fim=None):
            if fim is None: # se nao for passado o fim ele assume a lista toda
                fim = len(lista) - 1
            if inicio < fim:
                p = partition(lista, inicio, fim) # divide a lista em 2 partes entre o pivot
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
            lista[i], lista[fim] = lista[fim], lista[i]
            if doc:  # apenas doc
                print(lista, "---- FIM DE UMA ITERACAO")
            return i
        self.__lstValores = quick_sort_algorithm(self.__lstValores[:])
