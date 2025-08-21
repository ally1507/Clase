numero = int(input("introduce un numero:"))

for i in range ( 1, numero+1) :
    print (i)

palabra = (input("introduce una palabra:"))

for i in palabra :
    print (i)

import os

os.system ("clear")


while True:
    numero=int(input("ingrese un numero: "))
    if numero == 0 :
        print ("el numero es correcto")
        break
    else:
        print("ingrese el numero cero")

isActive=True

while isActive:
    numero=int(input("ingrese un numero: "))
    if numero == 0 :
        print ("el numero es correcto")
        isActive=False
    else:
        print("ingrese el numero cero")

