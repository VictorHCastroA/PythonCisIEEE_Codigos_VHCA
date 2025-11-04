#Reto día 5

Cantidad = int(input("Ingrese la cantidad de alumnos: "))
Nombres = []
Calificaciones = []

for i in range(Cantidad):
    N = input("Nombre de alumno: ")
    C = float(input("Calificacion obtenida: "))
    Nombres.append(N)
    Calificaciones.append(C)

Aprobados = []
Reprobados = []
Excelentes = []
suma = 0

for j in Calificaciones:
    suma=suma + j

promedio = suma / len(Calificaciones)
for k, l in enumerate(Calificaciones):
    if l == 10:
        Excelentes.append(Nombres[k])
    elif l >= 6:
        Aprobados.append(Nombres[k])
    else:
        Reprobados.append(Nombres[k]) 

Calificaciones.sort()
CalificacionesOrdenadas = Calificaciones.copy()
print("Reporte completo")
print(f"La cantidad de alumnos son: {Cantidad}")
print(f"El promedio del grupo es de {promedio}")
print("La calificacion más baja es: ", CalificacionesOrdenadas[0])
print("La calificación más alta es: ", CalificacionesOrdenadas[-1])
print(f"Los alumnos con una calificacion de 10 son los siguientes: \n{Excelentes}")
print(f"Los alumnos aprobados son los siguientes: \n{Aprobados}")
print(f"Los alumnos reprobados son los siguientes: \n{Reprobados}")