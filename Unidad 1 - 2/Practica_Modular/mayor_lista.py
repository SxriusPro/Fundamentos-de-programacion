# Modulo: encuentra el numero mayor de una lista
def ejecutar_mayor_lista():
    lista = [4, 7, 2, 9, 5]
    mayor = lista[0]

    # Se compara cada elemento con el mayor encontrado
    for x in lista:
        if x > mayor:
            mayor = x

    print(f"La lista es {lista}")
    print(f"El mayor es {mayor}")
