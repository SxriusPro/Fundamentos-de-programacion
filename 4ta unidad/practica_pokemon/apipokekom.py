from urllib.error import HTTPError, URLError


from datos_pokemon import obtener_datos_pokemon


identificador = input("Escribe el nombre o numero de Pokedex del Pokemon: ").strip()
if not identificador:
   print("Debes escribir un nombre o numero de Pokedex.")
   raise SystemExit(1)


try:
   datos_pokemon = obtener_datos_pokemon(identificador)
except HTTPError as error:
   if error.code == 404:
       print(f"No se encontro un Pokemon con el identificador '{identificador}'.")
   else:
       print(f"PokéAPI respondio con un error HTTP: {error.code}.")
   raise SystemExit(1) from error
except URLError as error:
   print(f"No se pudo conectar con PokéAPI: {error.reason}.")
   raise SystemExit(1) from error
print(f"\n--- Datos del Pokémon '{identificador}' ---\n")
print(datos_pokemon)
print (" @@@@@ @@@@ @@@  @@@  @@@  @@@  @@@@@  @@@@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@")
# 1. Acceso a datos directos
print(f"Pokémon: {datos_pokemon['name'].capitalize()}")
print(f"ID Pokedex: #{datos_pokemon['id']}")
print(f"Peso: {datos_pokemon['weight']}")


# 2. Recorrido de tipos
mis_tipos = []
for elemento in datos_pokemon["types"]:
   nombre_tipo = elemento["type"]["name"]
   mis_tipos.append(nombre_tipo)


print(f"\nTipos del Pokémon: {mis_tipos}")

# Reto: Sacar primeros 5 movimientos
print("\n--- Primeros 5 movimientos ---")
cantidad = 0
for elemento in datos_pokemon["moves"]:
   if cantidad < 5:
      nombre_movimiento = elemento["move"]["name"]
      print(f"{cantidad + 1}. {nombre_movimiento}")
      cantidad = cantidad + 1

# Otros datos interesantes

# Habilidades (dice si es una habilidad oculta)
print("\n--- Habilidades ---")
for elemento in datos_pokemon["abilities"]:
   nombre_habilidad = elemento["ability"]["name"]
   if elemento["is_hidden"] == True:
      print(f"{nombre_habilidad} (habilidad oculta)")
   else:
      print(nombre_habilidad)

# Estadisticas base y su suma total
print("\n--- Estadisticas base ---")
suma_stats = 0
for elemento in datos_pokemon["stats"]:
   nombre_stat = elemento["stat"]["name"]
   valor = elemento["base_stat"]
   suma_stats = suma_stats + valor
   print(f"{nombre_stat}: {valor}")
print(f"Total de estadisticas: {suma_stats}")

# Altura y peso convertidos (la API los da en decimetros y hectogramos)
altura = datos_pokemon["height"] / 10
peso = datos_pokemon["weight"] / 10
print(f"\nAltura: {altura} m")
print(f"Peso: {peso} kg")

# Experiencia base que da al ser derrotado
print(f"Experiencia base: {datos_pokemon['base_experience']}")

# Cuantos movimientos puede aprender en total
print(f"Total de movimientos que puede aprender: {len(datos_pokemon['moves'])}")

# Imagen oficial del Pokemon
print(f"Imagen: {datos_pokemon['sprites']['front_default']}")