print("Números primos entre 1 y 100:")

# Recorrer todos los números del 1 al 100
for num in range(1, 101):
    
    # Variable para contar cuántos divisores exactos tiene el número
    divisores = 0
    
    # Probar todos los números desde el 1 hasta el número actual
    for i in range(1, num + 1):
        if num % i == 0:
            divisores = divisores + 1  # Encontró un divisor exacto
            
    # Un número es primo si tiene exactamente 2 divisores (el 1 y sí mismo)
    if divisores == 2:
        print(num)  # Imprime cada número en una línea nueva sin usar 'end'
