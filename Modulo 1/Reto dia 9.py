#Reto dia 9
"""
Crea una herramienta de terminal simple para registrar y revisar tus notas de laboratorio
"""

TIPOS_ENTRADA_VALIDOS=("Observacion", "Prueba", "Error", "Mantenimiento")
bucle = True

def registrar_entrada():
    tipo_entrada = input("Ingrese un tipo de entrada: ")
    tipo_entrada_estandar = tipo_entrada.capitalize()
    if tipo_entrada_estandar not in TIPOS_ENTRADA_VALIDOS:
        print("El tipo de entrada no es válido. Intentelo de nuevo.")
        print("-"*50)
        return "continue"
    else:
        descripcion=input("Ingrese la descripcion de la entrada:\n")
        with open("laboratorio.log", "a") as f:
            f.writelines(f"Tipo: {tipo_entrada_estandar} - {descripcion}\n")
        print("-"*50)
        return "continue"


def ver_log():
    try:
        with open("laboratorio.log", "r") as f:
            for linea in f:
                contenido= linea.strip()
                print(contenido)
                print("-"*20)
    except:
        print("ERROR: No se encontró el archivo. Ejecuta el script de escritura primero.")
        return "continue"
    print("-"*50)

def salir():
    print("Confirmado\nFinalizando programa...\nAdios")
    print("-"*50)

def input_invalido():
    print("Valor invalido.\nIngrese un valor del menu de opciones.")
    print("-"*50)

def main():
    if opciones == 1:
        registrar_entrada()
        return "continue"
    elif opciones == 2:
        ver_log()
        return "continue"
    elif opciones == 3:
        salir()
        return "break"
    else:
        input_invalido()
        return "continue"

while bucle:
    try:
        opciones = int(input("Ingrese una opción del menu:\n(1)Registrar entrada. (2)Ver apunte. (3)Salir\n"))
        resultado = main()
        if resultado == "continue":
            continue
        else:
            break
    except:
        print("Entrada invalida. Ingrese un número del menu de opciones")
        continue