#Ejercicio tipo entrevista 2
def nuevalista(lista):
    lista_repetidos = []
    for i in lista:
        if i not in lista_repetidos:
            lista_repetidos.append(i)
        else:
            continue
    return lista_repetidos

lista=[1, 8 , 9, 7, 52, 78, 37, 13, 32, 2, 3, 8, 1, 44, 2, 9, 53, 54, 52, 7, 2, 1, 37, 13, 0, 1, 2, 3]
lista_sin_duplicados=nuevalista(lista)
print(lista_sin_duplicados)