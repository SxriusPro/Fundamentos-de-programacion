import json
import urllib.request
from urllib.parse import quote




def obtener_datos_pokemon(identificador):
   identificador = quote(identificador.strip().lower(), safe="")
   url = f"https://pokeapi.co/api/v2/pokemon/{identificador}"


   req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
   with urllib.request.urlopen(req) as response:
       return json.loads(response.read().decode())
