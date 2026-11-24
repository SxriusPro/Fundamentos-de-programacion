opc=0
while(opc !=5):
    print("1.- Saludo en español")
    print("2.- Saludo en ingles")
    print("3.- Saludo en portuges")
    print("4.- Saludo en italiano")
    print("5.- Salir")

    opc= int(input("selecciona una opcion: "))
    if (opc == 1 ):
        print("hola")
    elif(opc==2):
        print("hi")
    elif(opc==3):
        print ("olá")
    elif(opc==4):
        print("ciao")
    elif(opc==5):
        print("Hasta luego...")
    else:
        print(f"Numero {opc} invalido, intenta de nuevo")