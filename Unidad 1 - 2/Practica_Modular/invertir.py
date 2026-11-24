# Modulo: muestra una palabra al reves
def ejecutar_invertir():
    palabra = input("Escribe una palabra:   ")
    invertida = ""
    posicion = len(palabra) - 1

    # Se recorre la palabra desde el ultimo caracter hasta el primero
    while posicion >= 0:
        invertida = invertida + palabra[posicion]
        posicion = posicion - 1

    print(f"Al reves: {invertida}")
