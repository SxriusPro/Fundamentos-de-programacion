numero = int(input("Introduce un número random que se te ocurra: "))

es_primo = True

for divisor in range(2, numero):
    if numero / divisor == numero // divisor:
        es_primo = False

if es_primo == True:
    print("El número es primo")
else:
    print("El número NO es primo")
