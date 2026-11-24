# Diccionario de inventario de una tienda
frutas = {"manzanas": 10, "plátanos": 5, "naranjas": 8}

# A. Recorrer solo las CLAVES (comportamiento por defecto)
for fruta in frutas:
    print(fruta)  # Imprime: manzanas, plátanos, naranjas

# B. Recorrer solo los VALORES usando .values()
for cantidad in frutas.values():
    print(cantidad)  # Imprime: 10, 5, 8

# C. Recorrer CLAVES y VALORES a la vez usando .items()
for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} unidades de {fruta}.")
