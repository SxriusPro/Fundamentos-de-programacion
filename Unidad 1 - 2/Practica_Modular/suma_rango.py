# Modulo: suma los numeros del 1 hasta N
def ejecutar_suma_rango():
    n = int(input("Sumar desde el 1 hasta:   "))
    suma = 0

    for i in range(1, n + 1):
        suma = suma + i

    print(f"La suma es {suma}")
