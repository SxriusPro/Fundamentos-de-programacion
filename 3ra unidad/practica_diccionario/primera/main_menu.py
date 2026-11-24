from primera_f import ejecutar_lista_todos
from segunda_f import ejecutar_lista_peligrosos
from tercera_f import ejecutar_lista_esteaño
from cuarta_f import ejecutar_promedio
from quinta_f import ejecutar_resumen_de_aproximaciones

eleccion=0

while eleccion != 6:
    print("\n===== MENU PRINCIPAL =====")
    print(' ')
    print('1. Lista Asteroides')
    print('2. Lista de asteroides peligrosos')
    print('3. Lista de asteroides 2026')
    print('4. Sacar promedio de todos los asteroides')
    print('5. Sacar resumen de aproximaciones')
    print('6. Salir')

    dato=input(f'\nElige una opcion:   ')
    if dato.isdigit():
        eleccion = int(dato)
    else:
        eleccion = 0

    if eleccion == 1:
        ejecutar_lista_todos()
    elif eleccion == 2:
        ejecutar_lista_peligrosos()
    elif eleccion == 3:
            ejecutar_lista_esteaño()
    elif eleccion == 4:
            ejecutar_promedio()
    elif eleccion == 5:
            ejecutar_resumen_de_aproximaciones()
    elif eleccion == 6:
        print(f'\nVuelve pronto!')
    else:
        print(f'\nOpcion invalida! Vuelva a elegir')


