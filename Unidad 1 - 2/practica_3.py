respuesta=0
while(respuesta !=5):
    print("MENU")
    print("1.Cafe")
    print("2.Nieve")
    print("3.Frappe")
    print("4.Agua")
    print("5.Salir")

    respuesta=int(input("¿Que alimento del menu desea comprar?  "))

    if (respuesta==1):
        print("Gracias por comprar Cafe")
    elif(respuesta==2):
        print("Gracias por comprar Nieve")
    elif(respuesta==3):
        print("Gracias por comprar Frappe")
    elif(respuesta==4):
        print("Gracias por comprar Agua")
    elif(respuesta==5):
        print("Vuelva Pronto!!")
    else:
        print("Numero invalido, vuelva a intentar")
