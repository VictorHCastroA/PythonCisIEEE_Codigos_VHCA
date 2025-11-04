#Reto día 4
ListaInicial = ["leche", "pan", "manzanas"]
print("La lista inicial contiene lo siguiente:", ListaInicial)
opcion=int(input("Opciones: Añadir (1). Quitar (2). Revisar(3): "))
if opcion == 1:
    NuevoArticulo=input("Agregue nuevo artículo: ")
    if NuevoArticulo not in ListaInicial: 
        ListaInicial.append(NuevoArticulo)
        print("Confirmado. \nLa lista actualizada contiene lo siguiente: ", ListaInicial)
    else:
        print("Este artículo ya está en la lista.\n", ListaInicial)
elif opcion == 2:
    ArticuloBorrar=input("Ingrese el artículo que quiere eliminar: ")
    if ArticuloBorrar in ListaInicial:
        ListaInicial.remove(ArticuloBorrar)
        print("Confirmado. \nLa lista contiene lo siguiente: ", ListaInicial)
    else:
        print("El artículo no está en la lista.\n", ListaInicial)
elif opcion == 3:
    print(f"La lista tiene los siguiente artículos: {ListaInicial}")
else:
    print("Error. Ingrese una opción válida.")
