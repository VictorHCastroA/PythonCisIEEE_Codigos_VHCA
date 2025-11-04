#Reto dia 7
diccionario_principal={}
materias_validas=("Resistencia de los materiales", "Control clásico", "Programación avanzada")
bucle=True
while bucle:
    try:
        opciones=int(input("Ingresa la opción:\n (1)Registrar. (2)Buscar. (3)Promedio. (4)Ver_todos. (5)Cursos_unicos. (6)Salir\n "))
        if opciones == 1:
            id=input("Ingrese un id de alumno: ")
            try:
                id_numero=int(id)
            except:
                print("El ID del alumno debe ser numérico.")
                print("-"*50)
                continue
            id_registro=diccionario_principal.get(id) #Comprueba si está registrado
            if id_registro == None:
                nombre=input("Ingrese nombre del alumno: ")
                materia=input("Ingrese materia: ")
                materia_estandar=materia.capitalize()
                if materia_estandar not in materias_validas:
                    print("Materia invalida. Escribe correctamente el nombre de la materia.")
                    print("-"*50)
                    continue
                else:
                    print("Ingrese 3 calificaciones:")
                    try:
                        calificacion1=int(input("Calificacion 1: "))
                        calificacion2=int(input("Calificacion 2: "))
                        calificacion3=int(input("Calificacion 3: "))
                        calificaciones=[calificacion1, calificacion2, calificacion3]
                        nuevo_alumno={"Nombre": nombre,"Calificacion_1": calificacion1, "Calificacion_2": calificacion2, "Calificacion_3":calificacion3}
                        diccionario_principal[id]=nuevo_alumno
                        print("Registro exitoso")
                        print("-"*50)
                        #print(diccionario_principal)
                        continue
                    except:
                        print("Error. Ingrese un numero para cada calificacion.")
                        print("-"*50)
                        continue
            else:
                print("Error. ID registrada")
                print("-"*50)
                continue
        elif opciones == 2:
            id=input("Ingrese el ID del alumno: ")
            id_registro=diccionario_principal.get(id)
            if id_registro == None:
                print("Alumno no registrado. Verifique el ID")
                print("-"*50)
                continue
            else:
                alumno=diccionario_principal[id]
                print("Nombre: ", alumno["Nombre"])
                print(f"Lista de calificaciones:\nCalificacion 1: {alumno["Calificacion_1"]}\nCalificacion 2: {alumno["Calificacion_2"]}\nCalificacion 3: {alumno["Calificacion_3"]}")
                print("-"*50)
                continue
        elif opciones == 3:
            id=input("Ingrese el ID del alumno: ")
            id_registro=diccionario_principal.get(id)
            if id_registro == None:
                print("Alumno no registrado. Verifique el ID")
                print("-"*50)
                continue
            else:
                alumno=diccionario_principal[id]
                print("Nombre: ", alumno["Nombre"])
                suma = alumno["Calificacion_1"] + alumno["Calificacion_2"] + alumno["Calificacion_3"]
                promedio = suma/3
                print(f"Promedio de calificaciones: {promedio}")
                print("-"*50)
                continue
        elif opciones == 4:
            vacio = len(diccionario_principal)
            if vacio == 0:
                print("El diccionario está vacío")
                print("-"*50)
                continue
            else:
                for user_id, user_info in diccionario_principal.items():
                    print("ID: ", user_id)
                    print(f"Nombre: {user_info.get("Nombre")}")
                    print("-"*10)
                print("-"*50)
                continue
        elif opciones == 5:
            print("Cursos únicos: ", materias_validas)
            print("-"*50)
            continue
        elif opciones == 6:
            print("Confirmado...\nFinalizando programa...\nNo repruebe a todos :))")
            break
        else:
            print("Opcion invalida. Escoge una opción del menú")
            print("-"*50)
            continue
    except:
        print("Opcion invalida. Ingrese un número")
        print("-"*50)
        continue