# Programa principal: menu que manda a llamar a los modulos
# Cada modulo esta en su propio archivo .py y aporta una funcion

from par_impar import ejecutar_par_impar
from tabla_multiplicar import ejecutar_tabla_multiplicar
from primo import ejecutar_primo
from primos_100 import ejecutar_primos_100
from suma_rango import ejecutar_suma_rango
from promedio import ejecutar_promedio
from vocales import ejecutar_vocales
from invertir import ejecutar_invertir
from mayor_lista import ejecutar_mayor_lista
from digitos import ejecutar_digitos
from rfc import ejecutar_rfc
from juego import ejecutar_juego

opcion = 0

while opcion != 13:
    print("\n===== MENU PRINCIPAL =====")
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
    print("12. Juego: Piedra, papel o tijera")
    print("13. Salir")

    # Se revisa que la opcion sea un numero para no marcar error
    dato = input("Elige una opcion:   ")
    if dato.isdigit():
        opcion = int(dato)
    else:
        opcion = 0

    if opcion == 1:
        ejecutar_par_impar()
    elif opcion == 2:
        ejecutar_tabla_multiplicar()
    elif opcion == 3:
        ejecutar_primo()
    elif opcion == 4:
        ejecutar_primos_100()
    elif opcion == 5:
        ejecutar_suma_rango()
    elif opcion == 6:
        ejecutar_promedio()
    elif opcion == 7:
        ejecutar_vocales()
    elif opcion == 8:
        ejecutar_invertir()
    elif opcion == 9:
        ejecutar_mayor_lista()
    elif opcion == 10:
        ejecutar_digitos()
    elif opcion == 11:
        ejecutar_rfc()
    elif opcion == 12:
        ejecutar_juego()
    elif opcion == 13:
        print("Vuelva Pronto!!")
    else:
        print("Opcion invalida, intenta de nuevo")
