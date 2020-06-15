#Programa que simula la consulta de los tipos de motores que se encuentran en un deposito
#By Fernando Romero

import numpy as np

def printStatement():
    print("""Bienvenid@!!\n
La siguiente matriz muestra la distribución de los motores que se encuentran en sus cuatro (4) diferentes depositos, de la ciudad de Pamplona:\n""")

def printMatrix(depositos):
    print("Motor/Depo", end="")
    
    for i in range(1, len(depositos)+1):
        print("\t{}".format(i), end="")

    print("\n")

    typeMotors = ["1100", "2200", "4300", "5000"]
    i=0
    for deposito in depositos:
        print("\t",typeMotors[i], end="\t") 
        for motores in deposito:
            print(motores, end = "\t")
        print()
        i+=1

def showOpt():
    print("\n¿Que desea conocer?:\n")
    print("1. ¿Cuantos depositos tienen mas de dos (2) MOTORES 1100?")
    print("2. ¿Cual es la cantidad de MOTORES 2200 en todos los depositos?")
    print("3. ¿La cantidad de motores en cada deposito?")
    print("4. ¿La cantidad total de cada tipo de motor?\n")
    print("A continuación digite el numero de la opción que desea conocer hoy.")
    print("Para salir digite cualquier otra tecla...: ", end="")
    tecla = input()
    return tecla

def validarTecla(tecla, depositos):
    status = True
    if(not tecla.isdigit() or int(tecla) > 4):
        status = False
    elif(tecla == '1'):
        status = execOptOne(depositos[0])
    elif(tecla == '2'):
        status = execOptTwo(depositos[1])
    elif(tecla == '3'): 
        status = execOptThree(depositos)
    else:
        status = execOptFour(depositos)
    
    return status
        
def execOptOne(mot1100):
    print()
    tam=len(mot1100)
    i=0
    cont=0
    while(i<tam):
        if(mot1100[i]>2):
            cont+=1
        i+=1
    print("Existen {} depositos con mas de dos (2) MOTORES 1100.\n".format(cont))
    return askContinue()

def execOptTwo(mot2200):
    print()
    totMot2200 = sum(mot2200)
    print("Existen {} MOTORES 2200 en los cuatro(4) depositos.\n".format(totMot2200))
    return askContinue()


def execOptThree(depositos):
    print()
    list_numpy = np.array(depositos)
    sumas = list_numpy.sum(0)
    tam = len(sumas)
    for i in range (tam):
        print("Existen {0} motores en el deposito {1}".format(sumas[i], i+1))
    print()
    return askContinue()
    
def execOptFour(depositos):
    print()
    typeMotors = ["1100", "2200", "4300", "5000"]
    tam = len(depositos)
    for i in range (tam):
        total = sum(depositos[i][:])
        print("Existen {0} MOTORES {1}".format(total, typeMotors[i]))
    print()
    return askContinue()

def askContinue():
    print("¿Desea realizar otra consulta? (s/n): ", end = "")
    tecla = input()
    return tecla == 's'

def exitApp():
    print("Ha finalizado la aplicación. Buen día...")


depositos=[
    [5,4,1,5],
    [7,5,6,2],
    [2,1,1,2],
    [2,1,2,1]
]

continuar = True
printStatement()
printMatrix(depositos)
while(continuar):
    tecla = showOpt()
    continuar = validarTecla(tecla, depositos)
exitApp()