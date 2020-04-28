import matplotlib.pyplot as plt
import random as ran
import numpy as np  
import os

from scipy import stats
result=0
choice=0
rate=0
resultado=False
exit=False
min = 0
max = 37
cantidadTiradas =  100
ruleta = [] 

def CrearRuleta():
    ruleta.extend(range(min,max))
    print("La ruleta es la siguiente:", ruleta)

def GirarRuleta():
    return ran.randint(min,max)

def RealizarTirada():
    result = GirarRuleta()

def AssignSpace():
    if (result>=1 and result<=18):
        rate=1
    elif (result>=19 and result<=36):
        rate=2
    elif(result==0):
        rate=0


def VerifyNumber(a):
    RealizarTirada()
    AssignSpace()
    if(rate==a):
        return True
    else:
        return False
        
def ChooseSide():
    choice = ran.randint(1,2)

def Martingala():
    menu2()
    case = int(input("Seleccione una opcion: "))
    switch2(case)
def Dalembert():
    menu2()
    case = int(input("Seleccione una opcion: "))
    switch2(case)

def DalembertInfinito():

def MartingalaInfinito():

def MartingalaFinito():

    money= int(input("Sngrese capital inicial"))  

    currentMoney=money

    bet= int(input("Ingrese apuesta"))
    currentBet=bet

    currentMoney=currentMoney-bet


    for i in range(0,cantidadTiradas):
        while currentMoney>0:
            ChooseSide()
            resultado=VerifyNumber(choice)
            if(resultado):
                currentMoney=currentMoney+currentBet*2
                currentBet=bet
            else:
                currentBet=currentBet*2
                if(resultado==0):
                    print ("Tremendo 0 te toco") 
        """continuar"""       
                
            



def menu():
    try:
        os.system('cls')
        print ("Seleccionar una opción")
        print ("\t1 - Estrategia Martingala")
        print ("\t2 - Estrategia D'alembert")
        print ("\t3 - Salir")
    

def menu2():
	print ("Seleccionar una opción")
	print ("\t1 - Capital infinito")
	print ("\t2 - Capital finito")
	print ("\t3 - Volver")
    
def default():
       return "Opcion Invalida"

def exit():
    exit=True

def switch(case):
    sw = {
      1: Martingala(),
      2: Dalembert(),
      3: exit(),
    }
    return sw.get(case, default())

def switch2(case):
    sw = {
      1: suma(a, b),
      2: resta(a, b),
      3: multiplicacion(a, b)
    }
    return sw.get(case, default())


while not exit:
    menu()
    case = int(input("Seleccione una opcion: "))
    print(switch(case))


