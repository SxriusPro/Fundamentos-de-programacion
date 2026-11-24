precios = {"manzana": 15, "platano": 8, "naranja": 12}
t=0
for precio in precios.values():
    t = t + precio
print(f"La suma de todos los precios es de {t}")