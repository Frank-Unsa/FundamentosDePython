import random
comenzar=True
while comenzar:
    opciones=("piedra","papel","tijera")
    while True:
        human=input("ingrese su eleccion:").lower()
        if not human in opciones :
            print("Debe de ingresar un valor valido")
        else:
            break
    print("Usted Escogio =>", human )
    comp=random.choice(opciones)
    print("La computadora escogio =>", comp)
    if human == comp:
        print("Se produjo un empáte")
    elif human=='piedra':
        if comp=="tijera":
            print("Ganaste!")
        elif comp== 'papel':
            print("Perdiste..")
    elif human=='papel':
        if comp=="tijera":
            print("Perdiste..")
        elif comp=="piedra":
            print("ganaste")
    else:
        if comp=="piedra":
            print("Perdiste..")
        elif comp=='papel':
            print("ganaste")
    continuar=input("Desea jugar nuevamente? Si o no => ")
    continuar=continuar.lower()
    if continuar=="si":
       
        comenzar=True
    else:
        comenzar=False
