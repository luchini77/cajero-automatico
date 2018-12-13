global saldo
saldo = 1000

def cupo():
    global saldo
    saldo = saldo
    print(f"Tiene actualmente en la cuenta ${saldo}")
    print()

def depositar():
    global saldo
    deposito = int(input("Cuanto va a depositar: "))
    saldo += deposito
    print(f"Ahora posee ${saldo}")
    print()

def giro():
    global saldo
    retiro = int(input("Cuanto va a retirar: "))

    if retiro > saldo:
        print("***************************************************")
        print("No se puede realizar la operacion,falta de saldo!!")
        print("***************************************************")
    else:
        saldo -= retiro
        print(f"Ahora posee ${saldo}")
        print()

def salir():
    print()
    print("Gracias por utilizar el cajero de Mt.")


def menu():
    while True:
        print(".:MENU:.")
        print("1.- Cupo")
        print("2.- Depositar")
        print("3.- Giro")
        print("4.- Salir")
        print()
        opcion = int(input("Ingrese la opcion a ejecutar: "))
        print()
        if opcion == 1:
            cupo()
        elif opcion == 2:
            depositar()
        elif opcion == 3:
            giro()
        elif opcion == 4:
            salir()
            break

def principal():
    print("Bienvenido al Cajero de MT bank.")
    print()
    menu()

principal()
