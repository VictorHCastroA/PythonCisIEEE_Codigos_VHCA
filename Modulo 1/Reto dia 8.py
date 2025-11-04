#Reto dia 8
base_de_partes = {}
"""
Diccionario principal: {"clave1":{dict1}, "clave2":{dict2}, ...}
Diccionario secundario: {"Tipo de componente": "s1", "Resultado de pruebas": [#, #, #], "Estado":"Pendiente"}
"""
COMPONENTES_VALIDOS = ("Motor", "Sensor", "Batería", "Chasis")
bucle = True

def registrar():
    id=input("Ingrese el número de serie (S/N): ")
    id_registro=base_de_partes.get(id) #Comprueba si está registrado
    if id_registro == None:
        componente=input("Ingrese el componente: ")
        componente_estandar=componente.capitalize()
        if componente_estandar not in COMPONENTES_VALIDOS:
            print("Componente invalido. Escribe correctamente el nombre del componente.")
            print("-"*50)
        else:
            print("Ingrese 3 resultados de pruebas (0-100):")
            try:
                prueba1=int(input("Prueba 1: "))
                prueba2=int(input("Prueba 2: "))
                prueba3=int(input("Prueba 3: "))
                if prueba1>=0 and prueba1<=100 and prueba2>=0 and prueba2<=100 and prueba3>=0 and prueba3<=100:
                    resultado_pruebas=[prueba1, prueba2, prueba3]
                    nuevo_componente={"Tipo de componente":componente_estandar,"Resultado de pruebas": resultado_pruebas, "Estado": "Pendiente"}
                    base_de_partes[id]=nuevo_componente
                    print("Registro exitoso")
                    print("-"*50)
                else:
                    print("Valor de la prueba invalido. Ingrese un valor entre 0-100")
            except:
                print("Error. Ingrese un numero para cada prueba.")
                print("-"*50)
    else:
        print("Error. El número de serie ya está registrado")
        print("-"*50)

def buscar():
    id=input("Ingrese el numero de serie (S/N): ")
    id_registro=base_de_partes.get(id)
    if id_registro == None:
        print("Numero de serie no registrado. Verifique.")
        print("-"*50)
    else:
        registro=base_de_partes[id]#Diccionario secundario
        lista_pruebas=registro["Resultado de pruebas"]#Lista de resultados
        print("Tipo de componente: ", registro["Tipo de componente"])
        print(f"Resultado de pruebas:\nPrueba 1: {lista_pruebas[0]}. Prueba 2: {lista_pruebas[1]}. Prueba 3: {lista_pruebas[2]}")
        print("Estado: ", registro["Estado"])
        print("-"*50)

def evaluar():
    id=input("Ingrese el numero de serie: ")
    id_registro=base_de_partes.get(id)
    if id_registro == None:
        print("Numero de serie no registrado. Verifique.")
        print("-"*50)
    else:
        registro=base_de_partes[id]
        lista_pruebas=registro["Resultado de pruebas"]
        print("Tipo de componente: ", registro["Tipo de componente"])
        suma = lista_pruebas[0] + lista_pruebas[1] + lista_pruebas[2]
        promedio = suma/3
        print(f"Promedio de pruebas: {promedio}")
        print("-"*50)

def ver_inventario():
    vacio = len(base_de_partes)
    if vacio == 0:
        print("La base está vacío")
        print("-"*50)
    else:
        for user_id, user_info in base_de_partes.items():
            print(f"Numero de registro: {user_id} - Tipo de componente: {user_info.get("Tipo de componente")} - Estado: {user_info.get("Estado")}")
            print("-"*10)
        print("-"*50)

def contar_componentes(lista_componentes, componente_buscado, indice=0):
    if indice >= len(lista_componentes):
        return 0
    componente_actual = lista_componentes[indice]
    if componente_actual.get("Tipo de componente") == componente_buscado:
        return 1 + contar_componentes(lista_componentes, componente_buscado, indice + 1)
    else:
        return contar_componentes(lista_componentes, componente_buscado, indice + 1)

def conteo():
    if len(base_de_partes) == 0:
        print("La base de datos está vacía.")
        print("-" * 50)
    else:
        componente = input("Ingrese un tipo de componente: ")
        componente_estandar = componente.capitalize()
        if componente_estandar not in COMPONENTES_VALIDOS:
            print(f"Ingrese un componente válido.")
            print(f"Componentes válidos: {COMPONENTES_VALIDOS}")
            print("-" * 50)
        else:
            lista_componentes = list(base_de_partes.values()) #Lista de componentes
            cantidad = contar_componentes(lista_componentes, componente_estandar)
            print(f"\nTotal de componentes de tipo '{componente_estandar}': {cantidad}")
            print("-" * 50)


def salir():
    print("Confirmado\nFinalizando programa...\nAdios")
    print("-"*50)

def error():
    print("Valor invalido.\nIngrese un valor del menu de opciones.")
    print("-"*50)

while bucle:
    try:
        opciones=int(input("Menu de opciones:\n(1)Registrar. (2)Buscar. (3)Evaluar. (4)Ver_inventario. (5)Conteo. (6)Salir\n"))
        if opciones == 1:
            registrar()
            continue
        elif opciones == 2:
            buscar()
            continue
        elif opciones == 3:
            evaluar()
            continue
        elif opciones == 4:
            ver_inventario()
            continue
        elif opciones == 5:
            conteo()
            continue
        if opciones == 6:
            salir()
            break
        else:
            error()
            continue
    except:
        print("Entrada invalida. Intentalo de nuevo ingresando un número.")
        print("-"*50)
        continue