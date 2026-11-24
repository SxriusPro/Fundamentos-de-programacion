def mult (numero=int(input('Coloque un numero:   '))):
    print(f"\nTabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    
    
    if resultado % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
        
    print(f"{numero} x {i} = {resultado} ({tipo})")