numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    
    
    if resultado % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
        
    print(f"{numero} x {i} = {resultado} ({tipo})")
