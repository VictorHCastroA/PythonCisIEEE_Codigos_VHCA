#Ejercicio tipo entrevista 1
import string

palabra1="Dostoievski".casefold()
palabra2="sinónimos".casefold()
palabra3="Horiki".casefold()
palabra4="humanos".casefold()
palabra5="miedo".casefold()
palabra6="palabras".casefold()

def Conteo(nombre_texto, pal1, pal2, pal3, pal4, pal5, pal6):
    pal1=palabra1
    pal2=palabra2
    pal3=palabra3
    pal4=palabra4
    pal5=palabra5
    pal6=palabra6
    diccionario={pal1:0, pal2:0, pal3:0, pal4:0, pal5:0, pal6:0}
    with open(nombre_texto, "r", encoding="utf-8") as f:
        for linea in f:
            contenido = linea.strip()
            contenido_normalizado=normalizar(contenido)
            for palabra in diccionario:
                if palabra in contenido_normalizado:
                    diccionario[palabra]=diccionario[palabra]+1
        for palabra in diccionario:
            print(f"La palabra '{palabra}' aparece {diccionario[palabra]} veces")
    print("-"*50)
    with open("conteo.txt", "w") as f:
        f.write("----- Conteo de palabras -----\n")
        for palabra in diccionario:
            f.write(f"La palabra '{palabra}' aparece {diccionario[palabra]} veces.\n")
        f.write("\n--- Resumen ---\n")
        f.write(f"{diccionario}\n")

def normalizar(texto):
    tabla_traduccion = str.maketrans('', '', string.punctuation)
    return texto.translate(tabla_traduccion).casefold()


try:
    nombre_texto = "Fragmento_Indigno_de_ser_humano.txt"
    Conteo(nombre_texto, palabra1, palabra2, palabra3, palabra4, palabra5, palabra6)

except FileNotFoundError:
    print("El archivo de texto con ese nombre no existe. Intentar de nuevo.")

