# Modulo: saca el promedio de varias calificaciones
def ejecutar_promedio():
    cantidad = int(input("Cuantas calificaciones vas a meter?   "))
    suma = 0

    # Se piden las calificaciones y se van acumulando
    for i in range(cantidad):
        cal = float(input(f"Calificacion {i + 1}:   "))
        suma = suma + cal

    resultado = suma / cantidad
    print(f"El promedio es: {resultado:.2f}")
