# Modulo: muestra la tabla de multiplicar de un numero
def ejecutar_tabla_multiplicar():
    numero = int(input("Ingresa el numero de la tabla:   "))
    print(f"\nTabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i

        # Se muestra si el resultado es par o impar
        if resultado % 2 == 0:
            tipo = "par"
        else:
            tipo = "impar"

        print(f"{numero} x {i} = {resultado} ({tipo})")
