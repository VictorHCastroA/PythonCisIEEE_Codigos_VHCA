#Reto dia 2
x= int(input("Ingresa un valor 'x': "))
y= int(input("Ingresa un valor 'y': "))

print(f"La suma de {x} y {y} es: {x+y}")
print(f"La resta de {x} y {y} es: {x-y}")
print("La multiplicacion de", x, "y", y, "es:",x*y)
print("La división de " + str(x) + " y " + str(y) + " es: " + str(x/y))
print(f"El módulo 2 de {x} y {y} es:", x%2, "y", y%2)
print(f"La potencia cúbica de {x} y {y} es:", x**3, "y", y**3)

p=int(input("Ingresa un valor 'p': "))
q=int(input("Ingresa un valor 'q': "))
p += 2
q += 2
print(f"Asignación suma +2 para 'p' es {p} y para 'q' es {q}")
p -= 13
q -= 13
print(f"Asignación resta -13 para 'p' es {p} y para 'q' es {q}")
print(f"¿'p' es igual que 'q'? {p == q}")
print("¿'p' es diferente que 'q'?", p != q)
print("¿'p' es mayor que 'q'? " + str(p > q))
print("¿'p' es menor que 'q'?", p < q)

#AND
a = False
b = False
print("El AND de 0 y 0 es:", a and b)
a = False
b = True
print("El AND de 0 y 1 es:", a and b)
a = True
b = False
print("El AND de 1 y 0 es:", a and b)
a = True
b = True
print("El AND de 1 y 1 es:", a and b)
#OR
a = False
b = False
print("El OR de 0 y 0 es:", a or b)
a = False
b = True
print("El OR de 0 y 1 es:", a or b)
a = True
b = False
print("El OR de 1 y 0 es:", a or b)
a = True
b = True
print("El OR de 1 y 1 es:", a or b)
#NOT
a = False
b = True
print("El NOT de 0 es:", not a)
print("El NOT de 1 es:", not b)