# Modulo: dice si un numero es par o impar
def ejecutar_par_impar():
    num = int(input("Ingresa un numero entero:   "))
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")
