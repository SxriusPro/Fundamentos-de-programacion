from datos_asteroides import asteroides_nasa

def ejecutar_lista_todos():
    print(f'\n***Lista de asteroides***')
    for asteroide in asteroides_nasa:
        print(f'Asteroide {asteroide["name"]} --- diametro {asteroide["estimated_diameter_km"]}')


def ejecutar_lista_peligrosos():
    print(f'\n***Lista de asteroides peligrosos***')
    for peligro in asteroides_nasa:
        if peligro["is_potentially_hazardous"] == True:
            print("Este asteroide es peligroso:", peligro["name"])


def ejecutar_lista_esteaño():
    print(f'\n***Lista de asteoides de este año***')
    for año in asteroides_nasa:
        if 2026 in año["close_approach_years"]:
            print(año["name"])


def ejecutar_promedio():
    print(f'\n***Promedio de diametros***')
    sumprom = 0
    for promedio in asteroides_nasa:
        sumprom = sumprom + promedio["estimated_diameter_km"]
    prome = sumprom / len(asteroides_nasa)
    print(f'El promedio de los asteroides es de: {prome}km')


def ejecutar_resumen_de_aproximaciones():
    print(f'\n***Resumen de aproximaciones***')
    resumen_asteroides = {}
    for resum in asteroides_nasa:
        clave_id = resum["id"]
        resumen_asteroides[clave_id] = {
            "nombre": resum["name"],
            "total_aproximaciones": len(resum["close_approach_years"])
        }

    for id_ast, datos in resumen_asteroides.items():
        print(f"ID: {id_ast} | Asteroide: {datos['nombre']} | Total aproximaciones: {datos['total_aproximaciones']}")
