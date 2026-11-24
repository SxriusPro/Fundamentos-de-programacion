# Modulo: verifica si un numero es primo
def ejecutar_primo():
    numero = int(input("Ingresa un numero para verificar:   "))
    divisores = 0

    # Se cuentan cuantos divisores exactos tiene el numero
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1

    # Es primo si tiene exactamente 2 divisores (el 1 y el mismo)
    if divisores == 2:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} NO es primo")
