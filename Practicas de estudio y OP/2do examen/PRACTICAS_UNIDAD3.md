# PRACTICAS - 3ra Unidad
### Ejercicios tipo examen con soluciones

**Como usarlo:** intenta resolver cada uno en tu cabeza o en un archivo `.py` ANTES de ver la solucion. Las soluciones estan al final de cada bloque.

---

## BLOQUE A - FUNCIONES

### Ejercicio A1
Crea una funcion `saludar(nombre)` que devuelva `"Hola"` mas el nombre. Llamala dos veces e imprime los resultados.

### Ejercicio A2
Crea una funcion `area_rectangulo(base, altura)` que devuelva el area (base por altura). Pruebala con base 5 y altura 3.

### Ejercicio A3
Que imprime este codigo? (ojo con `global`)
```python
veces = 0
def contar():
    global veces
    veces = veces + 1
    return veces

contar()
contar()
print(veces)
```

### Ejercicio A4
Sin usar `global`, haz una funcion `sumar_uno(numero)` que reciba un numero y devuelva ese numero mas 1. Guarda el resultado en una variable.

---

### SOLUCIONES BLOQUE A

**A1**
```python
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Luis"))
print(saludar("Ana"))
```

**A2**
```python
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5, 3))   # 15
```

**A3**
```python
# Imprime: 2
# Porque 'global veces' permite modificar la variable de afuera
# y se llamo la funcion 2 veces.
```

**A4**
```python
def sumar_uno(numero):
    return numero + 1

resultado = sumar_uno(7)
print(resultado)   # 8
```

---

## BLOQUE B - DICCIONARIOS

### Ejercicio B1
Crea un diccionario `precios = {"manzana": 15, "platano": 8, "naranja": 12}` e imprime el precio del platano.

### Ejercicio B2
Al diccionario anterior, agregale `"pera": 20` y cambia el precio de la manzana a 18.

### Ejercicio B3
Recorre `precios` e imprime cada fruta con su precio en el formato: `La manzana cuesta 15`.

### Ejercicio B4
Suma todos los precios del diccionario e imprime el total.

### Ejercicio B5
Pide una fruta al usuario y dile si existe en el diccionario (usa `in`).

### Ejercicio B6
Que imprime este codigo?
```python
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10
print(len(d))
print(d["a"])
```

---

### SOLUCIONES BLOQUE B

**B1**
```python
precios = {"manzana": 15, "platano": 8, "naranja": 12}
print(precios["platano"])   # 8
```

**B2**
```python
precios["pera"] = 20        # agregar
precios["manzana"] = 18     # modificar
print(precios)
```

**B3**
```python
for fruta, precio in precios.items():
    print(f"La {fruta} cuesta {precio}")
```

**B4**
```python
total = 0
for precio in precios.values():
    total = total + precio
print(f"El total es {total}")
```

**B5**
```python
fruta = input("Que fruta buscas?   ").lower()
if fruta in precios:
    print(f"Si existe, cuesta {precios[fruta]}")
else:
    print("Esa fruta no esta en la lista")
```

**B6**
```python
# Imprime:
# 3    (hay 3 claves: a, b, c)
# 10   (el valor de 'a' se cambio a 10)
```

---

## BLOQUE C - LISTA DE DICCIONARIOS

### Ejercicio C1
Dada esta lista, recorre TODOS los alumnos e imprime `nombre - calificacion`:
```python
alumnos = [
    {"nombre": "Luis",  "calificacion": 7},
    {"nombre": "Ana",   "calificacion": 5},
    {"nombre": "Pedro", "calificacion": 9},
]
```

### Ejercicio C2
De la misma lista, imprime SOLO los alumnos aprobados (calificacion mayor o igual a 6).

### Ejercicio C3
Saca el promedio de las calificaciones de la lista.

### Ejercicio C4
Usando este estilo (como los asteroides), imprime los partidos donde gano el equipo local:
```python
partidos = [
    {"rival": "Tigres",  "gano_local": True},
    {"rival": "America", "gano_local": False},
    {"rival": "Chivas",  "gano_local": True},
]
```

---

### SOLUCIONES BLOQUE C

**C1**
```python
for alumno in alumnos:
    print(f"{alumno['nombre']} - {alumno['calificacion']}")
```

**C2**
```python
for alumno in alumnos:
    if alumno["calificacion"] >= 6:
        print(alumno["nombre"])
```

**C3**
```python
suma = 0
for alumno in alumnos:
    suma = suma + alumno["calificacion"]
promedio = suma / len(alumnos)
print(f"El promedio es {promedio}")   # 7.0
```

**C4**
```python
for partido in partidos:
    if partido["gano_local"] == True:
        print(f"Gano contra {partido['rival']}")
```

---

## BLOQUE D - COMPRENSION DE DICCIONARIOS

### Ejercicio D1
Crea con comprension un diccionario donde la clave sea el numero (del 1 al 5) y el valor sea ese numero multiplicado por 10.

### Ejercicio D2
Dada `numeros = [1, 2, 3, 4, 5, 6]`, crea un diccionario solo con los numeros pares (clave = numero, valor = su cuadrado).

### Ejercicio D3
Que imprime?
```python
palabras = ["sol", "luna", "mar"]
largos = {p: len(p) for p in palabras}
print(largos)
```

---

### SOLUCIONES BLOQUE D

**D1**
```python
d = {x: x * 10 for x in range(1, 6)}
print(d)   # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
```

**D2**
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = {x: x**2 for x in numeros if x % 2 == 0}
print(pares)   # {2: 4, 4: 16, 6: 36}
```

**D3**
```python
# {'sol': 3, 'luna': 4, 'mar': 3}
```

---

## BLOQUE E - MODULOS Y MENU

### Ejercicio E1
Tienes un archivo `matematicas.py` con:
```python
def sumar(a, b):
    return a + b
```
Escribe las lineas para importar `sumar` y usarla con 4 y 6 desde `main.py`.

### Ejercicio E2
Para que sirve `if __name__ == "__main__":`? En tus palabras.

### Ejercicio E3
Escribe un menu con `while` que muestre 3 opciones:
1. Saludar
2. Despedirse
3. Salir
Usa funciones y valida con `.isdigit()` que la opcion sea un numero.

---

### SOLUCIONES BLOQUE E

**E1**
```python
from matematicas import sumar

print(sumar(4, 6))   # 10
```

**E2**
```python
# Sirve para que la funcion solo se ejecute sola cuando corres ESE archivo.
# Cuando lo importas desde otro archivo, NO se ejecuta automaticamente.
```

**E3**
```python
from acciones import saludar, despedirse   # si estuvieran en otro archivo

opcion = 0

while opcion != 3:
    print("\n===== MENU =====")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    dato = input("Elige una opcion:   ")
    if dato.isdigit():
        opcion = int(dato)
    else:
        opcion = 0

    if opcion == 1:
        print("Hola!")
    elif opcion == 2:
        print("Adios!")
    elif opcion == 3:
        print("Vuelve pronto!")
    else:
        print("Opcion invalida")
```

---

## BLOQUE F - MEZCLADOS (nivel examen final)

### Ejercicio F1 (el mas probable)
Completa el menu principal para que use las funciones de otro archivo:
```python
from inventario import ejecutar_mostrar, ejecutar_total, ejecutar_agregar

opcion = 0

while opcion != 4:
    print("1. Mostrar inventario")
    print("2. Total de piezas")
    print("3. Agregar producto")
    print("4. Salir")
    dato = input("Opcion: ")
    if __________________:
        opcion = int(dato)
    else:
        opcion = ______

    if opcion == 1:
        ______________________
    elif opcion == 2:
        ______________________
    elif opcion == 3:
        ______________________
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion invalida")
```

### Solucion F1
```python
from inventario import ejecutar_mostrar, ejecutar_total, ejecutar_agregar

opcion = 0

while opcion != 4:
    print("1. Mostrar inventario")
    print("2. Total de piezas")
    print("3. Agregar producto")
    print("4. Salir")
    dato = input("Opcion: ")
    if dato.isdigit():
        opcion = int(dato)
    else:
        opcion = 0

    if opcion == 1:
        ejecutar_mostrar()
    elif opcion == 2:
        ejecutar_total()
    elif opcion == 3:
        ejecutar_agregar()
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion invalida")
```

---

## AUTOEXAMEN (responde sin ver nada)

1. Que palabra se pone antes del nombre de una funcion? _____
2. Como se agrega la clave `"x"` con valor `5` al diccionario `d`? _____
3. Como recorres claves Y valores al mismo tiempo? _____
4. Que hace `.isdigit()`? _____
5. Para que sirve `return`? _____
6. Escribe el import para usar `ejecutar_total` del archivo `inventario.py`: _____

**Respuestas:** 1) `def`   2) `d["x"] = 5`   3) `for k, v in d.items():`   4) Dice si el texto es solo numeros (True/False)   5) Devuelve un resultado de la funcion   6) `from inventario import ejecutar_total`
