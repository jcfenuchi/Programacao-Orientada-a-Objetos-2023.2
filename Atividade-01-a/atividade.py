from gerar_arquivo import gerar_lista
from algoritmos_de_ordenacao.bubble_sort import buble_sort
from algoritmos_de_ordenacao.selection_sort import selection_sort
from algoritmos_de_ordenacao.insertion_sort import insertion_sort
from algoritmos_de_ordenacao.quick_sort import quick_sort

class Lista:
    def __init__(self,data:str = None):
        self.__data = data
        if type((number_inputted := self.__data)) is int:
            self.__data = None if number_inputted < 0 else ([] if number_inputted == 0 else gerar_lista(size=number_inputted,min_value=1,max_value=1000))
        elif type((file := self.__data)) is str:
            try:
                with open(file, "r") as file:
                    lista = file.read().split("\n")
                    lista = lista[:-1] if lista[-1] == "" else lista
                    self.__data = list(map(int,lista))
                    
            except FileNotFoundError:
                print("Arquivo não encontrado")
                self.__data = list()
    @property
    def OUTPUT(self):
        print(type(self.__data), self.__data)
        return self.__data
    
    @OUTPUT.setter
    def OUTPUT(self,data):
        self.__data = data

    def buble_sort(self):
        buble_sort(self.__data)

    def selection_sort(self):
        selection_sort(self.__data)
    
    def insertion_sort(self):
        insertion_sort(self.__data)
    
    def quick_sort(self):
        quick_sort(self.__data)
    
        

lista = Lista(500)
lista.OUTPUT
lista.buble_sort()
lista.insertion_sort()
lista.selection_sort()
lista.quick_sort()


