for valor in range(2, 100 + 1):
    contador = 0
    for itera in range (2, valor+1):
        residuo = valor % itera
        if (residuo == 0):
            contador= contador + 1

    if (contador==1):
        print(f'El numero {valor} es primo')
    #else:
       # print(f'El numero {valor} NO es primo')
#else:
    #print(f'El numero {valor} NO es primo')