# Programa para sacar la CURP de una persona
# Sigue las reglas de la practica: primeras 4 letras, fecha, sexo, estado,
# consonantes internas, homoclave aleatoria y digito verificador
import random

def ejecutar_curp():
    nombre = input("Ingresa tu nombre (o nombres):   ").upper()
    apellido_paterno = input("Ingresa tu primer apellido:   ").upper()
    apellido_materno = input("Ingresa tu segundo apellido (si no tienes, solo Enter):   ").upper()
    anio = input("Anio de nacimiento (4 digitos, ej. 2006):   ")
    mes = input("Mes de nacimiento (2 digitos, ej. 09):   ")
    dia = input("Dia de nacimiento (2 digitos, ej. 05):   ")
    sexo = input("Sexo (H = hombre, M = mujer):   ").upper()
    estado = input("Estado de nacimiento (2 letras, ej. BC):   ").upper()

    # ---------- Partes para las primeras 4 letras ----------

    # Lista de particulas que NO se deben considerar en los apellidos
    particulas = ["DE LA ", "DE LOS ", "DE LAS ", "DE ", "DEL ", "LA ", "LAS ",
                  "LOS ", "MC ", "MAC ", "VON ", "VAN ", "Y "]

    # Se quitan las particulas del inicio del apellido paterno
    paterno_limpio = apellido_paterno
    for particula in particulas:
        if paterno_limpio.startswith(particula):
            paterno_limpio = paterno_limpio[len(particula):]

    # Se quitan las particulas del inicio del apellido materno
    materno_limpio = apellido_materno
    for particula in particulas:
        if materno_limpio.startswith(particula):
            materno_limpio = materno_limpio[len(particula):]

    # 1. Primera letra del primer apellido
    inicial_paterno = paterno_limpio[0]

    # 2. Primera vocal interna (no la inicial) del primer apellido
    vocal_paterno = "X"
    posicion = 1
    while posicion < len(paterno_limpio):
        if paterno_limpio[posicion] in "AEIOU":
            vocal_paterno = paterno_limpio[posicion]
            break
        posicion = posicion + 1

    # 3. Primera letra del segundo apellido (X si no hay)
    if materno_limpio == "":
        inicial_materno = "X"
    else:
        inicial_materno = materno_limpio[0]

    # 4. Primera letra del nombre
    # Si el primer nombre es JOSE o MARIA y tiene otro nombre, se usa el segundo
    inicial_nombre = nombre[0]
    if nombre.startswith("JOSE "):
        inicial_nombre = nombre[5]
    elif nombre.startswith("MARIA "):
        inicial_nombre = nombre[6]

    letras = inicial_paterno + vocal_paterno + inicial_materno + inicial_nombre

    # Palabras altisonantes: si las 4 letras forman una, se cambia el 2do caracter por X
    prohibidas = ["BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO",
                  "COGE", "COJA", "COJE", "COJI", "COJO", "CULO", "FETO", "GUEY",
                  "JOTO", "KACA", "KACO", "KAGA", "KAGO", "KOGE", "KOJO", "KAKA",
                  "KULO", "MAME", "MAMO", "MEAR", "MEAS", "MEON", "MION", "MOCO",
                  "MULA", "PEDA", "PEDO", "PENE", "PUTA", "PUTO", "QULO", "RATA",
                  "RUIN"]

    if letras in prohibidas:
        letras = inicial_paterno + "X" + inicial_materno + inicial_nombre

    # ---------- Consonantes internas (posiciones 14, 15 y 16) ----------

    # Primera consonante interna (no la inicial) de cada palabra
    consonantes = "BCDFGHJKLMNPQRSTVWXYZ"

    # Consonante interna del primer apellido
    consonante_paterno = "X"
    posicion = 1
    while posicion < len(paterno_limpio):
        if paterno_limpio[posicion] in consonantes:
            consonante_paterno = paterno_limpio[posicion]
            break
        posicion = posicion + 1

    # Consonante interna del segundo apellido
    consonante_materno = "X"
    posicion = 1
    while posicion < len(materno_limpio):
        if materno_limpio[posicion] in consonantes:
            consonante_materno = materno_limpio[posicion]
            break
        posicion = posicion + 1

    # Consonante interna del nombre (se usa la palabra del nombre elegido)
    nombre_consonante = nombre
    if nombre.startswith("JOSE "):
        nombre_consonante = nombre[5:]
    elif nombre.startswith("MARIA "):
        nombre_consonante = nombre[6:]

    consonante_nombre = "X"
    posicion = 1
    while posicion < len(nombre_consonante):
        if nombre_consonante[posicion] in consonantes:
            consonante_nombre = nombre_consonante[posicion]
            break
        posicion = posicion + 1

    # ---------- Fecha de nacimiento (posiciones 5 a 10) ----------
    anio_corto = anio[2:4]

    # ---------- Homoclave (posicion 17) ----------
    # Si nacio antes del 2000 es un numero 0-9; del 2000 en adelante una letra A-J
    if int(anio) < 2000:
        homoclave = str(random.randint(0, 9))
    else:
        homoclave = random.choice("ABCDEFGHIJ")

    # Digito verificador (posicion 18), se deja en 0 para simplificar
    verificador = "0"

    curp_final = (letras + anio_corto + mes + dia + sexo + estado +
                  consonante_paterno + consonante_materno + consonante_nombre +
                  homoclave + verificador)

    print(f"\nTu CURP es: {curp_final}")

# Si se corre este archivo directo, se ejecuta la funcion
if __name__ == "__main__":
    ejecutar_curp()
