import os

print("Bienvenido al programa de tablas de multiplicar")

numero = int (input("Ingrese el numero de tabla que desea consultar:"))
print("Tabla consultada:")

if 1<= numero <=10:
    print(f"\n Tabla de multiplicar de {numero} \n" )
    for i in range (1,10 + 1) :
        tabla = numero * i
        print(f"{numero} * {i} = {tabla} ")
        
else:
    print("El numero debe de estar entre 1 y 10")


    

