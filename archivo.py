import os

os.system ("clear")

print("Calcular tu imc")

peso=float(input("ingrese su peso: "))
altura=float(input("ingrese su altura: "))
imc=peso/(altura**2)

if imc < 18.5 :
    print(f"Usted tiene bajo peso y su imc es: {imc:.2f} ")
elif imc >= 18.5 and imc < 24.9 :
    print (f"usted tiene un peso normal y su imc es : {imc:.2f}")
elif imc >= 25 and imc < 29.9 :
    print (f"usted tiene un peso ideal y su imc es : {imc:.2f}")
else:
    print (f"Usted tiene obesidad y su imc es {imc:.2f}")


