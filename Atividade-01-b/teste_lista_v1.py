from class_Lista_v1 import Lista

lstTeste = Lista(5, 1, 1000)
buble = lstTeste.Ordena_Bubble()
insert = lstTeste.Ordena_Insertion()
quick1 = lstTeste.Ordena_Quick()
selec = lstTeste.Ordena_Selection()
quick = lstTeste.Ordena_Quick()

variaveis_lista = {nome: valor for nome, valor in locals().items() if type(valor) == list}.items()
[print(d) for d in variaveis_lista]
