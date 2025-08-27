import os
os.system("clear")

print("Bienvenido al sistema donde conviertes tu moneda")

valor=float(input("Ingrese la cantidad que desea cambiar:"))
opcion=float(input("Ingresa la opcion de moneda a convertir: \n1.cop_usd \n2.usd_jpy \n3.jpy_cop \n"))
cops = valor/4000
usd = valor * 144
jpy = valor * 28





match opcion :
    case 1:
        print(f"La conversion a dolares es es {cops}")
    case 2:
        print(f"La conversion a Yenes es: {usd}")
    case 3:
        print(f"La conversion a pesos colombianos es {jpy}")


