# Modulo: cuenta cuantas vocales tiene una palabra
def ejecutar_vocales():
    palabra = input("Escribe una palabra:   ").lower()
    vocales = 0

    # Se recorre letra por letra
    for letra in palabra:
        if letra in "aeiou":
            vocales = vocales + 1

    print(f"{palabra} tiene {vocales} vocales")
