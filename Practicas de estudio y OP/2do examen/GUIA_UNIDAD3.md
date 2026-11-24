# GUIA DE ESTUDIO - 3ra Unidad
### Examen: miercoles 21 de octubre

Todo esto sale de TUS archivos de la 3ra unidad. Al final hay un "chuletario" para el dia del examen.

---

## 1. FUNCIONES (`def`)

Una **funcion** es un bloque de codigo con nombre que puedes usar (llamar) las veces que quieras.

### 1.1 Forma basica

```python
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("yo"))          # Hola yo
print(saludar("otra vez yo")) # Hola otra vez yo
```

- `def` empieza la funcion.
- `(nombre)` son los **parametros** (los datos que le pasas).
- `return` devuelve un resultado.
- Para usarla, la **llamas**: `saludar("yo")`.

### 1.2 Parametros y return (tu archivo `defprof2.py`)

```python
contador = 0
def saludo(nom, conta):
    conta = conta + 1
    return conta

contador = saludo('yo', contador)
contador = saludo('otra vez yo', contador)
print(contador)   # 2
```

Aqui NO se usa `global`. En lugar de eso, la funcion **recibe** el contador, le suma 1 y lo **devuelve** con `return`. Por eso hay que guardarlo: `contador = saludo(...)`.

### 1.3 La palabra `global` (tu archivo `defprof.py`)

```python
contador = 0
def saludo(nom):
    global contador        # permiso para modificar la variable de afuera
    contador = contador + 1
    return f'Hola {nom}'

print(saludo('yo'))          # Hola yo
print(saludo('Otra vez yo')) # Hola otra vez yo
print(contador)              # 2
```

**Regla de oro:**
- Si solo **lees** una variable de afuera, no necesitas nada.
- Si quieres **modificarla** dentro de la funcion, necesitas `global`.
- La forma "limpia" (como `defprof2.py`) es pasar el valor por parametro y devolverlo con `return`. Evita `global` cuando puedas.

### 1.4 Diferencia con las variables de adentro

Una variable creada dentro de una funcion **solo existe ahi dentro**:

```python
def suma(a, b):
    resultado = a + b     # 'resultado' es local
    return resultado

suma(2, 3)
# print(resultado)  <-- ERROR: resultado no existe afuera
```

---

## 2. MODULOS E `import`

Un **modulo** es simplemente **otro archivo .py**. Para usar una funcion de otro archivo, la importas.

### 2.1 `from ... import ...` (lo que pide el profe)

`main_menu.py`:
```python
from primera_f import ejecutar_lista_todos
from segunda_f import ejecutar_lista_peligrosos

ejecutar_lista_todos()       # ya puedes usarla
```

Sintaxis: `from nombre_del_archivo import nombre_de_la_funcion`
- `archivo.py` se escribe **sin** el `.py`.
- Los dos archivos deben estar en la **misma carpeta**.

### 2.2 Otras formas de importar

```python
import primera_f                 # luego usar: primera_f.ejecutar_lista_todos()
from primera_f import *          # importa TODO (no muy recomendado)
from primera_f import a, b       # varias funciones separadas por coma
```

### 2.3 `if __name__ == "__main__":` (aparece en tus archivos)

```python
def ejecutar_promedio():
    ...

if __name__ == "__main__":
    ejecutar_promedio()
```

Sirve para que la funcion **solo se ejecute sola cuando corres ESE archivo directo**, y **no** cuando lo importas desde el menu. Asi, al importar no salta la funcion sin querer.

- Corres el archivo directo -> `__name__` vale `"__main__"` -> se ejecuta.
- Lo importas desde otro -> `__name__` vale el nombre del archivo -> NO se ejecuta.

---

## 3. DICCIONARIOS

Un diccionario guarda datos en pares **clave : valor**. Se escribe con llaves `{ }`.

```python
frutas = {"manzanas": 10, "platanos": 5, "naranjas": 8}
```

- `"manzanas"` es la **clave** (key).
- `10` es el **valor** (value).
- Van separados por `:` y cada par por `,`.

### 3.1 Acceder a un valor

```python
print(frutas["manzanas"])   # 10
```

Si la clave no existe -> **KeyError**. Para evitarlo:

```python
print(frutas.get("peras"))          # None (no truena)
print("peras" in frutas)            # False
```

### 3.2 Agregar y modificar

```python
frutas["peras"] = 4          # agrega una clave nueva
frutas["manzanas"] = 20      # modifica una que ya existia
print(frutas["manzanas"])    # 20
```

### 3.3 Borrar

```python
del frutas["naranjas"]       # borra esa clave
print(len(frutas))           # cuantas claves hay
```

### 3.4 Recorrer un diccionario (tu archivo `drio.py`)

```python
frutas = {"manzanas": 10, "platanos": 5, "naranjas": 8}

# A) solo las CLAVES (comportamiento normal)
for fruta in frutas:
    print(fruta)                 # manzanas, platanos, naranjas

# B) solo los VALORES con .values()
for cantidad in frutas.values():
    print(cantidad)              # 10, 5, 8

# C) CLAVES y VALORES a la vez con .items()  <-- el mas usado
for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} unidades de {fruta}.")
```

**Truco para recordar:** `.items()` te da los dos (item = pareja). Por eso pones **dos** variables: `for clave, valor in d.items()`.

### 3.5 Sumar todos los valores

```python
total = 0
for cantidad in frutas.values():
    total = total + cantidad
print(f"Total: {total}")     # 23
```

---

## 4. LISTA DE DICCIONARIOS  (lo de los asteroides)

Es una **lista** `[ ]` donde cada elemento es un **diccionario** `{ }`. Asi se ven los datos de una API.

```python
asteroides = [
    {"name": "99942 Apophis",   "estimated_diameter_km": 0.37,  "is_potentially_hazardous": True},
    {"name": "1620 Geographos", "estimated_diameter_km": 2.56,  "is_potentially_hazardous": True},
    {"name": "2002 MN",         "estimated_diameter_km": 0.08,  "is_potentially_hazardous": False},
]
```

### 4.1 Recorrer y sacar datos

```python
for asteroide in asteroides:                 # asteroide es UN diccionario
    print(asteroide["name"])                 # acceso con corchetes
```

### 4.2 Filtrar con `if` (como en `segunda_f.py`)

```python
for asteroide in asteroides:
    if asteroide["is_potentially_hazardous"] == True:
        print("Peligroso:", asteroide["name"])
```

### 4.3 Buscar un dato dentro de una lista (como en `tercera_f.py`)

```python
for asteroide in asteroides:
    if 2026 in asteroide["close_approach_years"]:
        print(asteroide["name"])
```

`in` sirve para preguntar si algo esta dentro de una lista o texto (ya lo usabas con vocales).

### 4.4 Promedio (como en `cuarta_f.py`)

```python
suma = 0
for asteroide in asteroides:
    suma = suma + asteroide["estimated_diameter_km"]
promedio = suma / len(asteroides)            # len = cuantos hay
print(f"El promedio es: {promedio}km")
```

---

## 5. COMPRENSION DE DICCIONARIOS (tu archivo `drioav.py`)

Forma corta de crear un diccionario en una sola linea.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = {x: x**2 for x in numeros}
print(cuadrados)     # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Se lee: "para cada `x` en `numeros`, guarda `x` como clave y `x**2` como valor".

- `**` significa "elevado a". `x**2` = x al cuadrado.
- Se puede agregar condicion al final:

```python
pares = {x: x**2 for x in numeros if x % 2 == 0}
print(pares)         # {2: 4, 4: 16}
```

---

## 6. MENU CON `while` Y VALIDACION (tu archivo `main_menu.py`)

```python
from primera_f import ejecutar_lista_todos
from segunda_f import ejecutar_lista_peligrosos

eleccion = 0

while eleccion != 6:
    print("\n===== MENU PRINCIPAL =====")
    print('1. Lista Asteroides')
    print('2. Lista de asteroides peligrosos')
    print('6. Salir')

    dato = input('Elige una opcion:   ')
    if dato.isdigit():          # comprueba que sea un numero
        eleccion = int(dato)
    else:
        eleccion = 0            # si no es numero, se trata como invalida

    if eleccion == 1:
        ejecutar_lista_todos()
    elif eleccion == 2:
        ejecutar_lista_peligrosos()
    elif eleccion == 6:
        print('Vuelve pronto!')
    else:
        print('Opcion invalida! Vuelva a elegir')
```

Partes clave:
- La variable se inicializa **antes** del `while` (`eleccion = 0`).
- `while eleccion != 6` -> se repite hasta que el usuario elija salir.
- `.isdigit()` evita que `int()` truene si escriben letras.
- El `else` final avisa de opcion invalida.

---

## 7. ERRORES COMUNES (trampas del examen)

| Error | Que pasa | Solucion |
|---|---|---|
| Poner `=` al crear diccionario | `{"a": 1}` esta bien, `{"a"= 1}` es ERROR | Usar `:` |
| Usar `( )` en vez de `{ }` | lista/tupla en vez de diccionario | Diccionario = llaves `{ }` |
| Olvidar `global` para modificar | se modifica una variable local | Poner `global nombre` |
| `d["clave"]` que no existe | **KeyError** | Usar `.get("clave")` o `in` |
| Olvidar `,` entre pares | SyntaxError | `{"a": 1, "b": 2}` |
| Recorrer con `for k, v in d` | ERROR | Es `for k, v in d.items()` |
| f-string con comillas iguales anidadas | SyntaxError en Python viejo | Ver nota abajo |
| Olvidar el `.py`? No... | Se pone SIN `.py` en el import | `from archivo import func` |

**Nota del bug real en tus archivos** (`primera_f.py`, `prepractica.py`):
```python
print(f'Asteroide {asteroide['name']} --- diametro ...')   # <-- comillas simples dentro de simples
```
Esto **solo funciona en Python 3.12 o mas nuevo**. En versiones viejas hay que cambiar las de afuera a dobles:
```python
print(f"Asteroide {asteroide['name']} --- diametro ...")
```

---

## 8. CHULETARIO (para el dia del examen)

```python
# FUNCION
def nombre(param1, param2):
    return algo

# FUNCION con contador global
contador = 0
def contar():
    global contador
    contador = contador + 1

# IMPORTAR
from archivo import funcion

# PROTEGER la ejecucion
if __name__ == "__main__":
    funcion()

# DICCIONARIO
d = {"clave": valor}
d["nueva"] = 1          # agregar / modificar
del d["clave"]          # borrar
d.get("x")              # sin truenar
"clave" in d            # existe?
len(d)                  # cuantas claves

# RECORRER
for k in d:                    # claves
for v in d.values():           # valores
for k, v in d.items():         # ambos

# LISTA DE DICCIONARIOS
for elem in lista:
    if elem["campo"] == True:
        print(elem["otro_campo"])

# COMPRENSION
{x: x**2 for x in numeros}

# MENU
opcion = 0
while opcion != 6:
    print("...menu...")
    dato = input("Opcion: ")
    if dato.isdigit():
        opcion = int(dato)
    else:
        opcion = 0
    if opcion == 1:
        ...
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion invalida")
```
