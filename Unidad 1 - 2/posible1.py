# Solicitar la calificación al usuario
calificacion = float(input("Ingresa la calificación del examen (0 a 100): "))

# Evaluar el rango correspondiente
if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")
