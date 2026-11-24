#Sacar el promedio de 10 estudiantes y luego sacar el promedio de todo el grupo
tot_promedios = 0
for estudiantes in range (10):
    nombre=input("ingrese su nombre:   ")
    totcal = 0 
    for calis in range (3):
        cals = float(input(f"Ingrese la calificación {calis + 1} del 1 al 10: "))
        totcal += cals
    prom= totcal / 3
    print(f"El promedio de {nombre} es de: {prom:.2f}")
    tot_promedios = tot_promedios + prom
promedio_general = tot_promedios / 10
print(f"El promedio general de la clase es: {promedio_general:.2f}")



