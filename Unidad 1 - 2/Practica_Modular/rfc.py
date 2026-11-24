# Modulo: calcula el RFC de una persona (sin homoclave real)
import random

def ejecutar_rfc():
    nombre = input("Ingresa tu nombre (o nombres):   ").upper()
    apellido_paterno = input("Ingresa tu apellido paterno:   ").upper()
    apellido_materno = input("Ingresa tu apellido materno (si no tienes, solo Enter):   ").upper()
    dia = input("Dia de nacimiento (2 digitos, ej. 05):   ")
    mes = input("Mes de nacimiento (2 digitos, ej. 09):   ")
    anio = input("Anio de nacimiento (4 digitos, ej. 2006):   ")
    anio_corto = anio[2:4]

    # Primera letra del apellido paterno
    inicial_paterno = apellido_paterno[0]

    # Primera vocal interna del apellido paterno
    vocal_paterno = "X"
    posicion = 1
    while posicion < len(apellido_paterno):
        if apellido_paterno[posicion] in "AEIOU":
            vocal_paterno = apellido_paterno[posicion]
            break
        posicion = posicion + 1

    # Primera letra del apellido materno (X si no hay)
    if apellido_materno == "":
        inicial_materno = "X"
    else:
        inicial_materno = apellido_materno[0]

    # Primera letra del nombre (JOSE y MARIA usan el segundo nombre)
    inicial_nombre = nombre[0]
    if nombre.startswith("JOSE "):
        inicial_nombre = nombre[5]
    elif nombre.startswith("MARIA "):
        inicial_nombre = nombre[6]

    letras = inicial_paterno + vocal_paterno + inicial_materno + inicial_nombre

    # Palabras prohibidas por el gobierno (SAT)
    prohibidas = ["BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO",
                  "COGE", "COJA", "COJE", "COJI", "COJO", "CULO", "FETO", "GUEY",
                  "JOTO", "KACA", "KACO", "KAGA", "KAGO", "KOGE", "KOJO", "KAKA",
                  "KULO", "MAME", "MAMO", "MEAR", "MEAS", "MEON", "MION", "MOCO",
                  "MULA", "PEDA", "PEDO", "PENE", "PUTA", "PUTO", "QULO", "RATA",
                  "RUIN"]

    # Si las 4 letras forman una palabra prohibida, la ultima letra se cambia por X
    if letras in prohibidas:
        letras = inicial_paterno + vocal_paterno + inicial_materno + "X"

    # Letras y numero aleatorios al final
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra1 = random.choice(abecedario)
    letra2 = random.choice(abecedario)
    numero_aleatorio = random.randint(0, 9)
    aleatorio = letra1 + letra2 + str(numero_aleatorio)

    rfc_final = letras + anio_corto + mes + dia + aleatorio
    print(f"\nTu RFC es: {rfc_final}")
