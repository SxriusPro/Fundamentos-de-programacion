# Modulo: cuenta cuantos digitos tiene un numero
def ejecutar_digitos():
    num = int(input("Ingresa un numero:   "))
    digitos = 0

    # La division entera entre 10 va quitando el ultimo digito
    while num > 0:
        digitos = digitos + 1
        num = num // 10

    print(f"Tiene {digitos} digitos")
