contador=0
def saludo(nom:str):
    global contador
    contador=contador + 1
    return f'Hola {nom}'
print(saludo('yo'))
print(saludo('Otra vez yo'))
print(contador)