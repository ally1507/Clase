import os
os.system

print("Bienvenido al programa de eleccion de numeros ")

numero1=int (input("ingrese el primer numero:"))
numero2=int (input("ingrese el segundo numero:"))
numero3= int (input("ingrese el tercer numero:"))

if numero1 >= numero2 >= numero3 :
  print (f"numero mayor es : {numero1}")
elif numero2 >= numero1 >= numero3:
  print (f"numero mayor es : {numero2} ")
else :
  print (f"numero mayor es: {numero3}")



if numero1<= numero2 <= numero3 :
  print (f"numero menor es : {numero1}")
elif numero2 <= numero1 <= numero3:
  print (f"numero menor es: {numero2}")
else :
  print (f"numero menor es : {numero3}")

