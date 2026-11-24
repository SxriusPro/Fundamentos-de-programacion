# GUÍA DE ESTUDIO — Fundamentos de Programación (Python)

Todo lo que necesitas está en **tus propios 19 archivos**. Esta guía los explica uno por uno,
marca los errores reales que tienen, y te da la base que te van a preguntar el miércoles.

---

## 1. Lo más básico: `print` y variables

```python
print("Hola")          # muestra texto en pantalla
edad = 20              # crea una variable llamada 'edad' que guarda 20
print(edad)            # muestra 20
```

**Regla de oro:** una variable se crea con `nombre = valor` (el `=` es *asignar*, no "es igual").
No necesitas `int`, `float` ni `str` para declararlas (eso es Java, no Python).

**Ojo con esto** (está en `listas.py` línea 7-8 y `replace2.py`):
```python
peso=32
name="Jose x"
print(f"nombre>{name} y peso:{peso*2}")
```
Aunque `name` se creara sin comillas en Java, en Python **las comillas son obligatorias**
para texto. Y las dos comillas pueden ser `"` o `'`.

---

## 2. Pedir datos: `input()` y `int()`

`input()` **siempre devuelve texto (string)**, aunque el usuario escriba un número.

```python
# MAL: input da texto, y "5" + 3 no existe
numero = input("Dame un numero: ") + 3     # TypeError

# BIEN: convertir con int()
numero = int(input("Dame un numero: ")) + 3  # 8
```

Usado en casi todas tus prácticas: `Practica.py:1`, `practica_prof.py:1`, `anidados.py:1-2`,
`nvociclov2.py:3`, `practica_3.py:10`, `prof2.py:9`, `Piedra_P_T.py:1-2`.

- `int("42")` → `42` (entero)
- `float("4.5")` → `4.5` (decimal)

---

## 3. Texto (strings) — `replace.py`, `listas.py`, `replace2.py`

### 3.1 Concatenar (juntar textos) con `+`
```python
txt = "Hello, world!"
texto_sph = " Buen dia"
print(txt + texto_sph)     # Hello, world! Buen dia
```
Ojo: `+` entre dos textos pega. Entre número y texto **no**.

### 3.2 `replace()` — cambiar un pedazo del texto
```python
txt = "Hello, world!"
print(txt.replace("Hello", "Hola"))   # Hola, world!
```
`.` significa "de este texto, haz esto". En Python casi todo son **objetos con métodos**
y se llaman con `objeto.método(...)`.

### 3.3 f-strings — meter variables dentro de un texto (lo que más se usa)
```python
name = "Jose x"
peso = 32
print(f"nombre>{name} y peso:{peso*2}")     # nombre>Jose x y peso:64
print(f"nombre>{name} y peso:{peso*2}")
```
Dentro de `{ }` puedes meter **cualquier expresión**, no solo variables: `peso*2` da 64.
Se usa en `practica_prof.py:10` y `prof2.py:21`.

### 3.4 Recorrer un texto carácter por carácter — `ciclos.py`
```python
txt = "The best things in life are free!"
for x in txt:
    print(x)
```
Imprime `T`, `h`, `e`, un espacio, `b`, `e`, `s`, `t`... uno por línea. **Un string es una
secuencia de caracteres**, igual que una lista es una secuencia de cosas.

### 3.5 `in` — ¿está esto dentro del texto?
```python
if ("free" in txt):
    print("Si aparece")
```
También sirve en listas: `if 5 in lista:`. Y lo contrario es `not in`.

---

## 4. Listas — `listas.py`, `listas2.py`, `listas3.py`, `pract_2.py`

Una lista guarda **varios valores en una sola variable, en orden**.

### 4.1 Crear, tamaño y acceder por índice
```python
lista = [5, -3, 5, "Jose x", True]
print(len(lista))    # 5  -> cantidad de elementos
print(lista[-3])     # 5
```

**Los índices empiezan en 0:**
| Posición | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Valor | 5 | -3 | 5 | "Jose x" | True |

**Índices negativos cuentan desde el final:** `lista[0]`=5, `lista[-1]`=True, `lista[-2]`="Jose x",
`lista[-3]`=5 ← por eso `lista[-3]` imprime 5.

### 4.2 Listas dentro de listas — `listas2.py`
```python
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])      # p   -> primer nivel: x[3] = ['p','q',[5,6,7]]
print(x[3][2][0])   # 5   -> x[3][2] = [5,6,7], y de ahí el primero
print(x[3][2][2])   # 7
```
Se avanza **nivel por nivel**, como una caja dentro de una caja.

### 4.3 Los 8 métodos de listas — `listas3.py` (y 3 errores importantes)
```python
lista = ["melon","sandia","kiwi","melon"]
frutas = ["mango","cherry"]

lista.insert(1, "orange")   # mete en la posición 1
lista.append("piña")        # agrega AL FINAL
lista.extend(frutas)        # une otra lista al final
lista.remove("piña")        # borra por VALOR (el primero que encuentra)
lista.pop(3)                # borra por ÍNDICE (y devuelve lo borrado)
lista.pop()                 # borra el ÚLTIMO
del lista[2]                # borra por índice (sin paréntesis)
del lista                   # borra la variable entera
lista.clear()               # vacía la lista (con paréntesis)
```
La diferencia clave: `remove("piña")` es por **valor**, `pop(2)` / `del lista[2]` es por
**posición**.

### 4.4 Recorrer una lista con `while` — `pract_2.py`
```python
itera = 0
lista = [1,3,5,7,2,4,6]
while(itera < len(lista)):
    print(lista[itera])
    itera = itera + 1
```
Sirve paraít. Un **contador** que va de 0 a `len(lista)-1`; en cada vuelta imprime
`lista[itera]` y **suma 1**. Si olvidas `itera = itera + 1` → ciclo infinito.

### 4.5 OJO: `list` es un nombre prohibido
En `listas3.py` usaste `list` como nombre de variable. `list` es una función que ya existe
en Python. No da error, pero te puede dar problemas. Usa `lista`, `frutas`, `numeros`...

---

## 5. Condicionales — `if / elif / else`

Se ejecuta **solo la primera condición que sea verdadera**.

```python
if condicion:
    # se ejecuta si la condicion es True
elif otra_condicion:
    # si la primera fue False y esta es True
else:
    # si todas fueron False
```

### 5.1 Operadores de comparación
| Operador | Significado | Ejemplo |
|---|---|---|
| `==` | es igual a | `num == 5` |
| `!=` | es diferente a | `opc != 5` |
| `>` | mayor que | `peso > 1000` |
| `<` | menor que | `peso < 1000` |
| `>=` | mayor o igual | `anio >= 2020` |
| `<=` | menor o igual | `peso <= 1500` |

**El error #1 de todos los principiantes:** `=` es *asignar*, `==` es *comparar*.
En `if` siempre va `==`.

### 5.2 Tu ejemplo de `if/elif/else` — `anidados.py`
```python
if A_auto >= 2020:          # 2020 o más nuevo
    print("reciente")
elif A_auto > 2009:         # 2010 a 2019
    print("intermedio")
else:                        # 2009 o anterior
    print("antiguo")
```
Fíjate en el rango: si fuera `elif A_auto >= 2010` también funcionaría. Lo que importa es
el orden: **de más restrictivo a menos**.

### 5.3 `and`, `or`, `not` — `Piedra_P_T.py`
```python
elif jugador1 == "piedra" and jugador2 == "tijera":
    print("Gana el Jugador 1")
```
- `and` → **las dos** condiciones deben ser verdaderas
- `or` → **al menos una** debe ser verdadera
- `not` → niega: `if not es_primo:`

### 5.4 La cadena completa de `if/elif` — `prof2.py`, `practica_3.py`
Ambos archivos usan el mismo patrón (menú con opciones). Fíjate en la estructura:

```python
opc = 0
while(opc != 5):                # mientras opc NO sea 5
    print("1.- ..."); print("5.- Salir")
    opc = int(input("opc: "))
    if (opc == 1):  print("hola")
    elif(opc == 2): print("hi")
    elif(opc == 5): print("Hasta luego...")   # la salida también es un caso del if
    else:           print("invalido")          # opción no válida
```
**Fíjate:** el `while` es `!= 5` y el `elif(opc==5)` es la salida. Es un patrón clásico.

### 5.5 `.lower()` — `Piedra_P_T.py`
```python
jugador1 = input("piedra, papel o tijera: ").lower()
```
`.lower()` pasa todo a minúsculas. Así "Piedra", "PIEDRA" y "piedra" funcionan igual.
Sin esto, `jugador1 == "piedra"` sería `False` si el escribió "Piedra".

---

## 6. Ciclo `for` y `range`

### 6.1 `for` sobre una lista — `for.py`
```python
lista = [5, 9, 10]
for l in lista:
    print(l)
```
Imprime 5, 9, 10. `l` toma **el valor de cada elemento** en cada vuelta.
(Fíjate: el archivo escribe los resultados como comentarios `#5 #9 #10`.)

### 6.2 `range()` — `for2.py`
```python
for valor in range(1, 1001, 2):
    print(valor)
```
`range(inicio, fin, salto)`:
- `inicio` = desde dónde (**sí se incluye**)
- `fin` = hasta dónde (**NO se incluye**) ← regla importantísima
- `salto` = de cuánto en cuánto

Entonces imprime `1, 3, 5, ..., 999`. Son 500 números. El 1001 nunca se imprime.

Ejemplos que te van a caer:
```python
range(5)              # 0,1,2,3,4            -> 5 elementos, empieza en 0
range(2, 6)           # 2,3,4,5              -> 4 elementos
range(0, 10, 2)       # 0,2,4,6,8
range(10, 1, -1)      # 10,9,8,...,2         -> para ir hacia atrás, salto negativo
```

### 6.3 Ciclos anidados (for dentro de for) — `pruebas.py`
```python
for valor in range(2, 101):          # loop EXTERNO
    contador = 0                     # se reinicia en cada vuelta externa
    for itera in range(2, valor+1):  # loop INTERNO
        residuo = valor % itera
        if (residuo == 0):
            contador = contador + 1
    if (contador == 1):
        print(f'El numero {valor} es primo')
```
El externo recorre 2..100. Por cada número, el interno prueba TODOS los divisores
2..valor. Imprime solo los primos.

**Y `anidados.py` NO tiene ciclos anidados** (a pesar del nombre): son dos `if`
independientes. A propósito para que vieras la diferencia.

---

## 7. Ciclo `while`

Repite **mientras la condición sea verdadera**. Tú decides cuándo parar.

```python
while(condicion):
    # lo que se repite
    # DEBE cambiar algo o nunca termina
```

### 7.1 while que se queda infinito — `nvociclov1.py` ⚠️
```python
num = int(input("Ingresa valor: "))
while(num > 0):
    print("Es positivo")
```
**Este archivo tiene un bug real:** `num` NUNCA cambia dentro del while, así que si
escribes 5 te imprime "Es positivo" **para siempre**. Te va a colgarse el examen.
La forma correcta:
```python
num = int(input("Ingresa valor: "))
while(num > 0):
    print("Es positivo")
    num = num - 1        # <--esto es lo que faltaba
```

### 7.2 while controlado por el usuario — `nvociclov2.py` ✅
```python
num = 1
while(num > 0):
    num = int(input("Ingresa valor: "))
    if(num > 0):
        print("Es positivo")
```
El while repite **mientras el número siga siendo positivo**. Si el usuario mete 0 o
negativo, se acaba. Esta es la versión "correcta" del archivo anterior.

### 7.3 while con contador — `pares-pract.py`
```python
num = 2
while(num < 101):
    print(num)
    num = num + 2
```
Imprime 2, 4, 6, ..., 100. Acá sí se modifica `num` (de 2 en 2).

### 7.4 `for` vs `while` — cuándo usar cada uno
| Situación | Usa |
|---|---|
| Recorrer una lista o texto | `for` |
| Contar del 1 al 100 / los pares / los primos | `for` con `range` |
| Menú que se repite hasta que el usuario salga | `while` |
| No sabes cuántas veces hay que repetir | `while` |

---

## 8. TAREA de tu profe: contadores, acumuladores y banderas

Esto estaba en `nvociclov2.py` líneas 6-8 como tarea. **Es tema de examen seguro.**

### 8.1 BANDERA (flag) — `True` o `False` que cambia según un caso
Una variable booleana que empieza valiendo "todavía no sé" y se apaga cuando encuentras
la respuesta. `Practica.py:3-7`:
```python
es_primo = True                       # la bandera arranca "sí es primo"
for divisor in range(2, numero):
    if numero / divisor == numero // divisor:   # si es divisible
        es_primo = False              # la APAGO: ya no es primo
if es_primo == True:                  # si nunca se apagó...
    print("El número es primo")
```
Lógica: "asumo que SÍ es primo; si encuentro un divisor, cambio de opinión."

### 8.2 CONTADOR — cuenta cuántas veces pasó algo
Empieza en 0 y **suma 1** cada vez. `practica_prof.py:2,7`:
```python
contador = 0                    # arranca en cero
for itera in range(2, valor+1):
    residuo = valor % itera
    if (residuo == 0):
        contador = contador + 1 # cuenta un divisor
if (contador == 1):
    print('es primo')            # si solo tiene UN divisor (él mismo) = primo
```
Y `pract_2.py:1-5` también es un contador (`itera`), pero usado para **recorrer** una lista.

### 8.3 ACUMULADOR — suma valores que vas leyendo
Igual que el contador, pero en vez de sumar 1, **suma el dato**:
```python
suma = 0                        # acumulador arranca en cero
for numero in lista:
    suma = suma + numero        # acumula cada valor
print(suma)                     # suma total
```

| | Contador | Acumulador | Bandera |
|---|---|---|---|
| Empieza en | `0` | `0` | `True` / `False` |
| Qué hace | `x = x + 1` | `x = x + dato` | `x = False` |
| Pregunta que responde | **¿cuántas veces?** | **¿cuánto suma?** | **¿sí o no?** |

Los tres aparecen en el mismo ejercicio: `practica_prof.py` cuenta divisores
(contador) y usa un `if valor>1` como filtro (bandera).

---

## 9. Aritmética y operadores que necesitas

```python
10 + 3   # 13    suma
10 - 3   # 7     resta
10 * 3   # 30    multiplicación
10 / 3   # 3.33  división REAL (siempre decimal, nunca da error si es /0... sí da)
10 // 3  # 3     división ENTERA (descarta decimales)
10 % 3   # 1     RESTO o módulo (¡el más usado en tus ejercicios!)
10 ** 2  # 100   potencia
```

### 9.1 El módulo `%` — el motor de "primo" y "par"
```python
10 % 2    # 0  -> es PAR
10 % 3    # 1  -> NO es múltiplo de 3
7  % 2    # 1
```
Regla: **`n % 2 == 0` significa que n es par.** Y `n % d == 0` significa que
d es un divisor de n. De ahí sale todo lo de primos.

### 9.2 `//` vs `/` para ver si es divisible — `Practica.py:6`
```python
if numero / divisor == numero // divisor:
```
`/` da decimales, `//` los quita. Si **son iguales**, entonces no hubo decimales
= es divisible exacto. (Funciona, pero con `%` es más fácil: `numero % divisor == 0`.)

### 9.3 Los 3 bugs de `Practica.py` ⚠️
1. Si `numero` es **0 o 1** (o negativo), `range(2, numero)` está vacío, el for no
   corre nunca y `es_primo` se queda en `True` → **dice "es primo" y es mentira**.
   Un 1 NO es primo.
2. Cuando encuentra un divisor **no se detiene** (`break`). Sigue hasta el final.
3. El `if es_primo == True:` se puede escribir simplemente `if es_primo:`

Versión corregida y más simple:
```python
numero = int(input("Numero: "))
es_primo = True
for divisor in range(2, numero):
    if numero % divisor == 0:
        es_primo = False
        break                      # ya sabemos que NO es primo
if numero <= 1:
    es_primo = False
if es_primo:
    print("El numero es primo")
else:
    print("El numero NO es primo")
```

### 9.4 Cómo `practica_prof.py` resuelve el 1
```python
if(valor > 1):          # <-- este filtro salva el problema del 0 y el 1
    for itera in range (2, valor+1):
        ...
else:
    print(f'El numero {valor} NO es primo')
```
Además usa `range(2, valor+1)` (con `+1`) y cuenta divisores: si hay **exactamente 1**
divisor (el mismo número) → primo. Funciona bien. Este **es el patrón que te va a pedir el profe.**

---

## 10. Errores reales en tu carpeta (repásalos, el profe puede preguntarlos)

| Archivo | Problema | Cómo se arregla |
|---|---|---|
| `listas3.py` | `del list` **borra la variable**, luego `list.clear` y `print(list)` dan `NameError`. El archivo **está roto** | Quita `del list`, y escribe `lista.clear()` con paréntesis |
| `nvociclov1.py` | `while(num>0)` nunca cambia `num` → **ciclo infinito** | Agrega `num = num - 1` dentro del while |
| `Practica.py` | El 0 y el 1 los marca como primos | Agrega el filtro `if numero <= 1` |
| `Practica.py` | No usa `break`, sigue buscando divisores sin necesidad | Agrega `break` |
| `listas3.py` | `list` como nombre de variable (ocupa un nombre de Python) | Renómbrala a `lista` |
| `anidados.py` | Se llama "anidados" pero son dos `if` separados, no anidados | Nada, solo el nombre confunde |
| `for2.py` | Imprime hasta 999, no hasta 1001 (el final nunca se incluye) | `range(1, 1000, 2)` es igual; para 1000: `range(1, 1001, 2)` + cambiar paridad |

---

## 11. Cheat sheet (imprímelo para el miércoles)

```python
# SALIDA
print("texto")                     # texto fijo
print(f"hola {nombre} {edad+1}")   # f-string con variables
print("a", 5, "b")                 # print con coma separa por espacio
print("a" + "b")                   # concatenar

# ENTRADA
n = int(input("numero: "))        # entero
x = float(input("decimal: "))     # decimal
t = input("texto: ")              # texto

# CONDICIONALES
if a == b: ...        elif a != b: ...        else: ...
if a > b and c < d: ...      # las dos
if a > b or  c < d: ...      # al menos una
if not (a == b): ...         # negación
if "t" in texto: ...         # está dentro
if d in lista: ...

# CICLO FOR
for x in lista: ...                 # cada elemento
for i in range(10): ...             # 0..9
for i in range(2, 11): ...          # 2..10
for i in range(0, 100, 2): ...      # pares 0..98
for i in range(10, 0, -1): ...      # 10..1

# CICLO WHILE
i = 0
while i < 10: i = i + 1             # siempre:i = i + 1 o break

# LISTAS
lista = [1, 2, 3]
len(lista)      # 3
lista[0]  lista[-1]
lista.append(4)  lista.insert(0, 9)  lista.extend(otra)  lista.clear()
lista.remove(5)  lista.pop()  lista.pop(1)  del lista[0]
lista.sort()     lista.reverse()
lista[0] = 99

# TEXTO
texto.replace("a", "b")
texto.lower()  texto.upper()  texto.strip()
f"valor: {variable}"
"x" in texto

# MATEMÁTICAS
a + b   a - b   a * b   a / b   a // b   a % b   a ** b
a > b   a < b   a >= b  a <= b  a == b  a != b

# UTILES
break        # sale del ciclo
continue    # salta a la siguiente vuelta
```

---

## 12. Cómo_areparar la noche del martes (plan de estudio)

| Tiempo | Qué haces |
|---|---|
| 20 min | Relee los puntos 1-5 (print, input, texto, listas, if) |
| 20 min | Relee los puntos 6-7 (for, while, range) y corre `for.py`, `for2.py`, `pares-pract.py` |
| 20 min | **Escribe de memoria** los 3 patrones: contador, acumulador, bandera (punto 8) |
| 20 min | Relee el punto 9 (módulo `%`, primos) y los 2 programas de primos |
| 20 min | Haz las 15 prácticas de `PRACTICAS.md` SIN ver la solución |
| 15 min | Relee el cheat sheet del punto 11 y los bugs del punto 10 |

**Los 4 patrones que con seguridad te van a pedir:**
1. Recorrer una lista → `for` o `while` con `len()`
2. Menú que se repite → `while` + `if/elif/else`
3. Número primo → `%` + bandera + `break`
4. Contador / Acumulador / Bandera → los del punto 8
