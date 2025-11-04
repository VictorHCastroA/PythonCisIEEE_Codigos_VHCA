#Reto día 6
menu = ["Paneles solares", "Tanques de oxigeno", "Cubiertos", "Agua", "Trajes espaciales"]
bucle = True
while bucle:
    try: 
        opciones=int(input("Ingrese el numero de la opcion que desee: \n(1) Añadir. (2)Quitar. (3)Ver. (4)Inspeccionar. (5)Salir\n "))
        if opciones == 1:
            nuevo_articulo=input("Ingrese nuevo artículo: ")
            articulo_estandar1=nuevo_articulo.capitalize()
            if articulo_estandar1 in menu:
                print("El artículo ya esté en el menu. Intentelo de nuevo")
                print("-"*50)
                continue
            else:
                menu.append(articulo_estandar1)
                print("Confirmado\nMenú actualizado:\n", menu)
                print("-"*50)
                continue
        elif opciones == 2:
            quitar_articulo=input("Ingrese el artículo que quiera quitar: ")
            articulo_estandar2=quitar_articulo.capitalize()
            if articulo_estandar2 not in menu:
                print("El artículo no se encuentra en el menu. Intentelo de nuevo")
                print("-"*50)
                continue
            else:
                menu.remove(articulo_estandar2)
                print("Confirmado\nMenú actualizado:\n", menu)
                print("-"*50)
                continue
        elif opciones == 3:
            print("El menú es el siguiente:\n", menu)
            print("-"*50)
            continue
        elif opciones == 4:
            try:
                item=int(input("Ingrese el numero de item que quiera inpeccionar: "))-1
                try:
                    articulo=menu[item]
                    print("El item con ese valor es: ", articulo)
                    print("-"*50)
                    continue
                except:
                    print("No existe ese valor de item. Intentelo de nuevo")
                    print("-"*50)
                    continue
            except:
                print("Item inválido. \nIntentelo de nuevo.")
                print("-"*50)
                continue
        elif opciones == 5:
            print("Saliendo...")
            print("Programa terminado")
            break
        else:
            print("La opción no está en el menú de opciones. \nIntentelo de nuevo")
            print("-"*50)
            continue
    except:
        print("Valor inválido. \nIntentelo de nuevo.")
        print("-"*50)
        continue