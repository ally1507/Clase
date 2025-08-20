import os
os.system

print("Tus frutas y precio")

opcion=(input("escribe la fruta que quieras: "))

match opcion:
    case "manzana":
        print ("haz elegido manzana, su valor es 2.000")
    case "mango" :
        print ("haz elegido mango, su valor es 5.000")
    case "peras":
        print ("haz elegido peras, su valor es 3.000")
    case _:
        print("haz elegido un valor no existente")
        

