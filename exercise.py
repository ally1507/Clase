import os
import random

x = random.randint(1 ,10)
print(x)

isActive=True
while isActive:
    os.system("clear")
    print("Bienvenido al minijuego para adivinar un numero entre 1 y 10")

    numero = int(input("Ingrese el numero que cree que es:"))
    if numero == x :
        print("\nFelicidades, adivinaste el numero")
        isActive= False
        input("Presiona ENTER para continuar")

    else:
        print("\nLo siento, intenta de nuevo")
        input("Presiona ENTER para continuar")
    











