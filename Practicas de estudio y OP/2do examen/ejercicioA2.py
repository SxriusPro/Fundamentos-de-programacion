arre=0
def area_rectangulo (base, altura):
    area = base * altura
    return area
arre= area_rectangulo(int(input('Define la base:   ')), int(input('Define la altura:   ')))
print(f'\nEl area del rectangulo es: {arre}')