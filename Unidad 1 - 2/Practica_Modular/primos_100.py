# Modulo: muestra los numeros primos del 1 al 100
def ejecutar_primos_100():
    print("Numeros primos del 1 al 100:")

    for num in range(1, 101):
        divisores = 0

        # Se revisan todos los divisores del numero actual
        for i in range(1, num + 1):
            if num % i == 0:
                divisores = divisores + 1

        if divisores == 2:
            print(num)
