from class_Lista_v2 import Lista

range_num = 100
algoritmos = ["abc", 'Bubble', 'Selection', 'Insertion', 'Quick']

for alg in algoritmos:
    lstTeste = Lista(range_num, 1, 10)
    lstTeste.Ordena(metodo_ordenacao=alg)
    print(lstTeste.ListaValores)
