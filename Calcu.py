
def Suma(x, y):
    return x + y

def Resta(x, y):
    return x - y


def Multiplicar(x, y):
    return x * y


def Dividir(x, y):
    return x / y



salir = False

while not salir:
    print("Que desea hacer:")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")


    opcion = input("elige una opcion")
    num1 = int(input("ingrese primer numero"))
    num2 = int(input("ingrese segundo numero"))
    if opcion == "1":
        print(Suma(num1,num2))
    elif opcion == "2":
        print(Resta(num1,num2))
    elif opcion == "3":
        print( Multiplicar(num1,num2))
    elif opcion == "4":
        print(Dividir(num1,num2))
    elif opcion == "5":
        salir = True
        
    else:
        print ("Introduce un numero entre 1 y 5")
print ("Fin")

        