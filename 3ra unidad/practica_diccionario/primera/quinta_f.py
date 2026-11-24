def ejecutar_resumen_de_aproximaciones():
    asteroides_nasa = [
    {
        "id": "2099942",
        "name": "99942 Apophis",
        "estimated_diameter_km": 0.37,
        "is_potentially_hazardous": True,
        "close_approach_years": [2029, 2036, 2068]
    },
    {
        "id": "2001620",
        "name": "1620 Geographos",
        "estimated_diameter_km": 2.56,
        "is_potentially_hazardous": True,
        "close_approach_years": [2026, 2038]
    },
    {
        "id": "3102712",
        "name": "2002 MN",
        "estimated_diameter_km": 0.08,
        "is_potentially_hazardous": False,
        "close_approach_years": [2028]
    },
    {
        "id": "2004330",
        "name": "433 Eros",
        "estimated_diameter_km": 16.84,
        "is_potentially_hazardous": False,
        "close_approach_years": [2026, 2031, 2056]
    }
    ]

    print(f'\n***Resumen de aproximaciones***')
    resumen_asteroides={}
    for resum in asteroides_nasa:
        clave_id=resum["id"]
        resumen_asteroides[clave_id]={
        "nombre": resum["name"],
        "total_aproximaciones": len(resum["close_approach_years"])
    }

    for id_ast, datos in resumen_asteroides.items():
        print(f"ID: {id_ast} | Asteroide: {datos['nombre']} | Total aproximaciones: {datos['total_aproximaciones']}")

if __name__ == "__main__":
    ejecutar_resumen_de_aproximaciones()