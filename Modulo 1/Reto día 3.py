#Reto día 3

nombre=input("Ingresa tu nombre de usuario: ")
nacimiento=int(input("Ingresa tu fecha de nacimiento: "))

videojuegos_string = input("Ingresa tus tres videojuegos favoritos (en una misma línea separados por una coma): ")
perfil = [nombre]
edad=2025 - nacimiento
perfil.append(edad)
#videojuegos_string_sinespacios = videojuegos_string.replace(" ", "")
juegos=videojuegos_string.replace(" ", "").split(',')
perfil.extend(juegos)
perfil.insert(0, True)
juego_favorito=perfil.pop(3)

es_mayor_de_edad = perfil[2] >= 18
nombre_largo = len(perfil[1]) > 10
es_gamer_retro = "pacman" in juegos

print("Perfil del jugador: ",perfil)
print(f"Su juego favorito es {juego_favorito}")
print(f"¿Es mayor de edad? {es_mayor_de_edad}. ¿Tiene nombre largo? {nombre_largo}. ¿Es gamer retro? {es_gamer_retro}")