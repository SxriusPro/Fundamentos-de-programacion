# 15 PRÁCTICAS TIPO EXAMEN + SOLUCIONES

**Todas las soluciones de este archivo fueron ejecutadas y verificadas con Python 3.13.**

Cómo usarlas: **tapa la solución con la mano** e inténtalo tú primero. Si te sale, lo
comparas. Si no, la lees, la copias a un archivo y la corres. El examen es "práctica",
así que lo que importa es que **sepas escribirlo de memoria**, no reconocerlo.

Nivel: 🟢 fácil · 🟡 medio · 🔴 difícil (estilo profe con práctica)

---

## 🟢 1 — Variables, `print` y f-string
Pide el **nombre** y la **edad** del usuario e imprime: `Me llamo X y tengo Y años`.

```python
nombre = input("Cual es tu nombre? ")
edad = int(input("Cual es tu edad? "))
print(f"Me llamo {nombre} y tengo {edad} años")
```
*Concepts: input, int, f-string.*

---

## 🟢 2 — Suma de dos números
Pide dos números enteros y muestra los tres resultados: suma, resta y multiplicación.

```python
n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
```
*Concepts: int, operaciones, f-string.*

---

## 🟢 3 — Par o impar
Pide un número y di si es par o impar. **Pista:** `num % 2 == 0`.

```python
num = int(input("Numero: "))
if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")
```

---

## 🟢 4 — El mayor de tres números
Declara tres variables con números y muestra el mayor, **sin usar `max()`**.

```python
a, b, c = 10, 45, 3
mayor = a                      # suponemos que a es el mayor
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(f"El mayor es {mayor}")
```
*Ojo: son dos `if` sueltos, NO un `if/elif/else` (pues el dato ya viene de variables).*

---

## 🟡 5 — Positivo, negativo o cero
Pide un número y clasifícalo con `if/elif/else`.

```python
n = int(input("Numero: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Cero")
```

---

## 🟡 6 — Suma del 1 al N con `while` (contador + acumulador)
Pide N y suma los números del 1 al N **usando `while`**.

```python
n = int(input("Hasta donde sumo: "))
suma = 0
contador = 0
while contador < n:
    contador = contador + 1
    suma = suma + contador
print(f"La suma de 1 a {n} es {suma}")
```
*Concepts: contador + acumulador. Prueba con N=5 → 15, N=10 → 55.*

**Variante con `for`** (más corta, misma cosa):
```python
for i in range(1, n + 1):
    suma = suma + i
```

---

## 🟡 7 — Los pares del 2 al 100 con `for`
Imprime los números pares del 2 al 100 usando `range` con paso.

```python
for i in range(2, 101, 2):
    print(i)
```
⚠️ `range` **nunca incluye** el final. Por eso es `101` y no `100`. (Esto es `pares-pract.py`
hecho con `for` en vez de `while`.)

---

## 🟡 8 — Suma y mayor de una lista (recorrer con `for`)
Dada la lista `[4, 7, 2, 9, 5]`, calcula la suma total y el número mayor.

```python
lista = [4, 7, 2, 9, 5]
suma = 0
mayor = lista[0]
for x in lista:
    suma = suma + x              # ACUMULADOR
    if x > mayor:
        mayor = x
print(f"Suma={suma}  Mayor={mayor}")
# Salida: Suma=27  Mayor=9
```

---

## 🟡 9 — ¿Cuántos dígitos tiene? (contador con `while`)
Pide un número y di cuántos dígitos tiene, **sin convertirlo a texto**.

```python
num = int(input("Numero: "))
digitos = 0
while num > 0:
    digitos = digitos + 1
    num = num // 10              # le quita el ultimo digito
print(f"Tiene {digitos} digitos")
```
*`//` (división entera) borra el último dígito: 123//10 = 12 → 12//10 = 1 → 1//10 = 0.*
Con 123 → `Tiene 3 digitos`.

---

## 🔴 10 — NÚMERO PRIMO (el clásico)
Pide un número y determina si es primo. **Un primo solo es divisible entre 1 y sí mismo,
o sea que tiene exactamente 1 divisor.** El 0 y el 1 **NO son primos**.

```python
num = int(input("Numero: "))
es_primo = True                        # BANDERA
if num <= 1:
    es_primo = False
else:
    for d in range(2, num):
        if num % d == 0:
            es_primo = False
            break                       # ya sabemos que no es primo
if es_primo:
    print("Es primo")
else:
    print("NO es primo")
```
Verificado: `0→NO · 1→NO · 2→SÍ · 7→SÍ · 9→NO · 97→SÍ`

**Las 3 cosas que el profe mira aquí:**
1. `num % d == 0` (no `numero / divisor == numero // divisor`)
2. El filtro `num <= 1` (esto es lo que le falta a tu `Practica.py`)
3. El `break` (dejar de buscar cuando ya sabes la respuesta)

**Otra versión válida** (la de tu `practica_prof.py`, contando divisores):
```python
valor = int(input("Numero: "))
if valor > 1:
    contador = 0
    for itera in range(2, valor + 1):
        if valor % itera == 0:
            contador = contador + 1
    if contador == 1:
        print(f"El numero {valor} es primo")
    else:
        print(f"El numero {valor} NO es primo")
else:
    print(f"El numero {valor} NO es primo")
```

---

## 🔴 11 — Menú interactivo con `while`
Repite un menú hasta que el usuario elija "3. Salir". Opciones: 1. Saludar, 2. Despedir,
3. Salir. Si escribe otra cosa, avisa.

```python
opc = 0
while opc != 3:
    print("1.- Saludar  2.- Despedir  3.- Salir")
    opc = int(input("Opcion: "))
    if opc == 1:
        print("Hola")
    elif opc == 2:
        print("Adios")
    elif opc == 3:
        print("Hasta luego")
    else:
        print("Opcion invalida")
```
*Es EXACTAMENTE el patrón de `prof2.py` y `practica_3.py`. Memoriza la estructura:*
*`while` fuera + `if/elif/else` dentro + `else` para lo inválido.*

---

## 🟡 12 — Contar vocales (recorrer un texto)
Pide una palabra y cuenta cuántas vocales tiene.

```python
palabra = input("Palabra: ").lower()
vocales = 0
for letra in palabra:
    if letra in "aeiou":
       vocales = vocales + 1
print(f"{palabra} tiene {vocales} vocales")
```
*Con "Programacion" → 5 vocales. Fíjate en `letra in "aeiou"`: `in` funciona con textos
y con listas.*

---

## 🔴 13 — Invertir una palabra con `while` (índice que baja)
Pide una palabra y muéstrala al revés, **sin usar `palabra[::-1]`**.

```python
palabra = input("Palabra: ")
invertida = ""
indice = len(palabra) - 1
while indice >= 0:
    invertida = invertida + palabra[indice]
    indice = indice - 1
print(invertida)
```
*"Hola" → "aloH". Clave: empiezas en `len(palabra) - 1` (el último) y **restas** 1.*

---

## 🟡 14 — Solo los pares de una lista
Dada `[1, 2, 3, 4, 5]`, suma **solo los números pares**.

```python
lista = [1, 2, 3, 4, 5]
total = 0
for x in lista:
    if x % 2 == 0:
        total = total + x       # el acumulador SOLO suma si es par
print(f"Los pares suman {total}")   # 6
```

---

## 🟢 15 — Índices negativos y `len`
Dada `lista = [5, -3, 5, 8, True, "Jose"]`, imprime el tamaño, el primero, el último y
el que está en la posición **-3**.

```python
lista = [5, -3, 5, 8, True, "Jose"]
print(f"len={len(lista)} primero={lista[0]} ultimo={lista[-1]} neg3={lista[-3]}")
# len=6  primero=5  ultimo=Jose  neg3=8
```

---

## 🎯 RETO FINAL — contador + acumulador + bandera a la vez
Pide 5 números y muestra: cuántos son pares, la suma de los impares, y el mayor de todos.
(Usa un contador, un acumulador y una bandera.)

```python
pares = 0                 # CONTADOR
suma_impares = 0          # ACUMULADOR
mayor = -999999           # BANDERA (guarda el mayor; necesita un valor inicial muy bajo)
for i in range(5):
    n = int(input(f"Numero {i+1}: "))
    if n % 2 == 0:
        pares = pares + 1
    else:
        suma_impares = suma_impares + n
    if n > mayor:
        mayor = n
print(f"Pares: {pares}")
print(f"Suma de impares: {suma_impares}")
print(f"El mayor: {mayor}")
```

---

## 📋 CHECKLIST: ¿estoy listo para el miércoles?

Marca lo que puedas hacer **sin mirar nada**:

- [ ] Pedir un dato y convertirlo con `int()` / `float()`
- [ ] Escribir un `if / elif / else` con `==`, `>`, `>=`, `<=`, `!=`
- [ ] Combinar condiciones con `and` / `or` / `not`
- [ ] Recorrer una lista con `for` y con `while` + `len()`
- [ ] Usar `range(inicio, fin, paso)` sabiendo que el final no se incluye
- [ ] Menú con `while` + `if/elif/else` + opción de salir
- [ ] Saber si un número es primo con `%` y bandera
- [ ] Declarar y usar un **contador**, un **acumulador** y una **bandera**
- [ ] Saber la diferencia entre `=` y `==`
- [ ] Usar f-strings para imprimir variables
- [ ] Los métodos de lista: `append`, `insert`, `remove`, `pop`, `len`
- [ ] Métodos de texto: `replace`, `lower`, `upper`

### Los 3 errores que más te van a costar puntos
1. **Olvidar `contador = contador + 1`** en el `while` → ciclo infinito (como `nvociclov1.py`).
2. **=` en vez de `==`** en el `if` → siempre es True.
3. **Olvidar el filtro `<= 1`** en el programa de primos → decir que 1 es primo.
