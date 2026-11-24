import random

def par_impar():
    num = int(input("Ingresa un numero entero:   "))
    if (num % 2 == 0):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")


def tabla_multiplicar():
    numero = int(input("Ingresa el numero de la tabla:   "))
    print(f"\nTabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i

        if resultado % 2 == 0:
            tipo = "par"
        else:
            tipo = "impar"

        print(f"{numero} x {i} = {resultado} ({tipo})")

def es_primo():
    numero = int(input("Ingresa un numero para verificar:   "))
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1

    if divisores == 2:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} NO es primo")

def primos_1_al_100():
    print("Numeros primos del 1 al 100:")

    for num in range(1, 101):
        divisores = 0

        for i in range(1, num + 1):
            if num % i == 0:
                divisores = divisores + 1

        if divisores == 2:
            print(num)

def suma_rango():
    n = int(input("Sumar desde el 1 hasta:   "))
    suma = 0

    for i in range(1, n + 1):
        suma = suma + i

    return suma

def promedio():
    cantidad = int(input("Cuantas calificaciones vas a meter?   "))
    suma = 0

    for i in range(cantidad):
        cal = float(input(f"Calificacion {i + 1}:   "))
        suma = suma + cal

    resultado = suma / cantidad
    print(f"El promedio es: {resultado:.2f}")

def contar_vocales():
    palabra = input("Escribe una palabra:   ").lower()
    vocales = 0

    for letra in palabra:
        if letra in "aeiou":
            vocales = vocales + 1

    print(f"{palabra} tiene {vocales} vocales")

def invertir_palabra():
    palabra = input("Escribe una palabra:   ")
    invertida = ""
    posicion = len(palabra) - 1

    while posicion >= 0:
        invertida = invertida + palabra[posicion]
        posicion = posicion - 1

    print(f"Al reves: {invertida}")

def mayor_de_lista():
    lista = [4, 7, 2, 9, 5]
    mayor = lista[0]

    for x in lista:
        if x > mayor:
            mayor = x

    print(f"La lista es {lista}")
    print(f"El mayor es {mayor}")

def contar_digitos():
    num = int(input("Ingresa un numero:   "))
    digitos = 0

    while num > 0:
        digitos = digitos + 1
        num = num // 10

    print(f"Tiene {digitos} digitos")

def rfc():
    nombre = input("Ingresa tu nombre (o nombres):   ").upper()
    apellido_paterno = input("Ingresa tu apellido paterno:   ").upper()
    apellido_materno = input("Ingresa tu apellido materno (si no tienes, solo Enter):   ").upper()
    dia = input("Dia de nacimiento (2 digitos, ej. 05):   ")
    mes = input("Mes de nacimiento (2 digitos, ej. 09):   ")
    año = input("Anio de nacimiento (4 digitos, ej. 2006):   ")
    año_corto = año[2:4]

    inicial_paterno = apellido_paterno[0]

    vocal_paterno = "X"
    posicion = 1
    while posicion < len(apellido_paterno):
        if apellido_paterno[posicion] in "AEIOU":
            vocal_paterno = apellido_paterno[posicion]
            break
        posicion = posicion + 1

    if apellido_materno == "":
        inicial_materno = "X"
    else:
        inicial_materno = apellido_materno[0]

    inicial_nombre = nombre[0]
    if nombre.startswith("JOSE "):
        inicial_nombre = nombre[5]
    elif nombre.startswith("MARIA "):
        inicial_nombre = nombre[6]

    letras = inicial_paterno + vocal_paterno + inicial_materno + inicial_nombre

    prohibidas = ["BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO",
                  "COGE", "COJA", "COJE", "COJI", "COJO", "CULO", "FETO", "GUEY",
                  "JOTO", "KACA", "KACO", "KAGA", "KAGO", "KOGE", "KOJO", "KAKA",
                  "KULO", "MAME", "MAMO", "MEAR", "MEAS", "MEON", "MION", "MOCO",
                  "MULA", "PEDA", "PEDO", "PENE", "PUTA", "PUTO", "QULO", "RATA",
                  "RUIN"]

    if letras in prohibidas:
        letras = inicial_paterno + vocal_paterno + inicial_materno + "X"

    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra1 = random.choice(abecedario)
    letra2 = random.choice(abecedario)
    numero_aleatorio = random.randint(0, 9)
    aleatorio = letra1 + letra2 + str(numero_aleatorio)

    rfc_final = letras + año_corto + mes + dia + aleatorio
    print(f"\nTu RFC es: {rfc_final}")

def salir():
    print("Vuelva Pronto!!")


opcion = 0

while (opcion != 12):
    print("\nMENU")
    print("1. Par o impar")
    print("2. Tabla de multiplicar")
    print("3. Verificar si es primo")
    print("4. Primos del 1 al 100")
    print("5. Suma del 1 al N")
    print("6. Promedio de calificaciones")
    print("7. Contar vocales")
    print("8. Invertir una palabra")
    print("9. El mayor de una lista")
    print("10. Contar digitos")
    print("11. Sacar RFC")
    print("12. Salir")

    opcion = int(input("Elige una opcion:   "))

    if (opcion == 1):
        par_impar()
    elif (opcion == 2):
        tabla_multiplicar()
    elif (opcion == 3):
        es_primo()
    elif (opcion == 4):
        primos_1_al_100()
    elif (opcion == 5):
        print(f"La suma es {suma_rango()}")
    elif (opcion == 6):
        promedio()
    elif (opcion == 7):
        contar_vocales()
    elif (opcion == 8):
        invertir_palabra()
    elif (opcion == 9):
        mayor_de_lista()
    elif (opcion == 10):
        contar_digitos()
    elif (opcion == 11):
        rfc()
    elif (opcion == 12):
        salir()
    else:
        print("Numero invalido, intenta de nuevo")
