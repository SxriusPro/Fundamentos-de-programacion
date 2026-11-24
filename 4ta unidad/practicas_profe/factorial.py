def calculadora_factorial():
    print("=== Calculadora Factorial ===")
    numero = int(input("Coloca un número: "))

    if numero < 1 or numero > 25:
        print(f"El número {numero} no es válido.")
        
        rango_permitido = list(range(1, 26))
        print("El rango permitido es:")
        print(rango_permitido)
    else:

        factorial = 1
        for i in range(1, numero + 1):
            factorial = factorial * i

        print(f"El factorial de {numero} ({numero}!) es: {factorial}")


if __name__ == "__main__":
    calculadora_factorial()
