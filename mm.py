import os

isActive = True
saldo = 100000

while isActive:
    os.system("clear")
    print("Bienvenido a su cajero")
    print(f"Saldo actual: {saldo}")
    

    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("0. Salir")

    try:
        opcion=int(input("Elija una opcion:"))
    except ValueError:
        print("Ingrese una opcion correcta")
        input("Presiona enter")
            
    match opcion:
    
        case 1:
            print(f"Tu saldo es : {saldo}")
            input("Presiona enter")
        case 2:
            depositar = float(input("Ingresa saldo a depositar:"))
            if depositar > 0:
                nuevo = saldo + depositar
                print(f"Su nuevo saldo es : {nuevo}")
            input("Presiona enter")
        case 3:
            retirar = float(input("Ingresa el saldo a retirar:"))
            if retirar < saldo :
                retira = saldo - retirar
                print(f"El saldo que quedo en su cuenta es: {retira}")
            input("Presiona enter")
        case 0:
            print("Gracias por visitar nuestro cajero")
            isActive = False
        case _:
            print("Elija una opcion disponible")
            input("Presiona enter")
        

