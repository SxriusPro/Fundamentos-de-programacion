A_auto = int(input("De que año es tu vehiculo?   "))
peso_auto = int(input("Cual es el peso en KG de tu vehiculo?   "))

if A_auto >= 2020:
    print("Como es de", A_auto, ". Tu vehiculo es reciente.")
elif A_auto > 2009:
    print("Como es de", A_auto, ". Tu vehiculo es intermedio.")
else:  
    print("Como es de", A_auto, ". Tu vehiculo es antiguo.")

if peso_auto < 1000:
    print("Y ya que pesa", peso_auto, "KG, tu vehiculo es liviano.")
elif peso_auto <= 1500:
    print("Y ya que pesa", peso_auto, "KG, tu vehiculo es mediano.")
else:  
    print("Y ya que pesa", peso_auto, "KG, tu vehiculo es pesado.")
