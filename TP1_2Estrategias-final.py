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
cantidadJuegos = 1
ruleta = [] 
capital=0

def CrearRuleta():
    ruleta.extend(range(min,max))
    print("La ruleta es la siguiente:", ruleta)

def GirarRuleta():
    return ran.randint(min,max)

def RealizarTirada():
    result = GirarRuleta()
    return result

def AssignSpace(resulta):
    if (resulta>=1 and resulta<=18):
        return 1
    elif (resulta>=19 and resulta<=36):
        return 2
    elif(resulta==0):
        return 0


def VerifyNumber(a):
    result=RealizarTirada()
    rate=AssignSpace(result)
    if(rate==a):
        return True
    else:
        return False
        
def ChooseSide():
    choice = ran.randint(1,2)
    return choice
    

def MartingalaInfinito():
    historico = []
    frecuenciasRelativas = []
    historioCapital = []
    bet= int(input("Ingrese apuesta\n"))
    currentBet=bet
    ganancia=0
    currentMoney=0
    capital=0
    money=0
    perdi=0
    gane=0
    meQuedeSinPlata=True
    i=0
    while (i<=cantidadTiradas):
        i+=1 
        choice=ChooseSide()
        resultado=VerifyNumber(choice)
        if(resultado):
            gane+=1
            currentMoney+=currentBet
            currentBet=bet

        else:
            currentMoney-=currentBet
            currentBet=currentBet*2
            perdi+=1
        frecuenciasRelativas.append(gane/i)  
        historioCapital.append(currentMoney)
        if(currentMoney>money):
            money=currentMoney

    #Grafica frecuencia relativa
    plt.title('Frecuencia relativa de cada elemento con '+str(i)+' tiradas')
    plt.bar(range(0,i), frecuenciasRelativas,1, color="red",edgecolor="blue")
    plt.ylim(0,1)
    plt.xlim(-1,i)
    plt.axhline(18/37, color='k',ls="dotted", xmax=i)
    plt.grid(True)
    plt.show()
    plt.clf()

            #Grafica frecuencia relativa
    plt.title('Frecuencia relativa de apuesta favorable')
    plt.plot(range(0,i),frecuenciasRelativas)
    plt.xlabel("Tiradas")
    plt.ylabel("Frecuencia Relativa")
    plt.axhline(18/37, color='k',ls="dotted", xmax=i)
    plt.ylim(0,1)
    plt.xlim(0,i)   
    plt.show()

    for index,f in enumerate(frecuenciasRelativas):
        frecuenciasRelativas[index] = f+1000
    #Grafica fluctuacion de capital
    plt.title('Capital en cada tirada')
    plt.plot(range(0,i),frecuenciasRelativas)
    plt.plot(range(0,i),historioCapital)
    plt.xlabel("Tiradas")
    plt.ylabel("Cantidad de capital en pesos")
    plt.axhline(money, color='k',ls="dotted", xmax=i)
    plt.ylim(-money,money*2)
    plt.xlim(0,i)   
    plt.show()


     
def MartingalaFinito():
    historico = []
    frecuenciasRelativas = []
    historioCapital = []
    money= int(input("Ingrese capital inicial\n"))  
    perdi=0
    gane=0
    currentMoney=money

    bet= int(input("Ingrese apuesta\n"))
    currentBet=bet
    currentMoney-=bet
    meQuedeSinPlata=True
    i=0
    while (meQuedeSinPlata and i<=100) :
        print (currentMoney)
        choice=ChooseSide()
        resultado=VerifyNumber(choice)
        if(resultado):
            currentMoney+=currentBet*2
            currentBet=bet
            gane+=1

        else:
            currentBet=currentBet*2
            perdi+=1
        
        if(currentMoney>currentBet):
                currentMoney-=currentBet
        else:
            meQuedeSinPlata=False
        i+=1 
        frecuenciasRelativas.append(gane/i)  
        historioCapital.append(currentMoney)
        # if capital_inicial <= 0:
        #     historico.append(0)
        # elif capital_inicial >= capital:
        #     historico.append(1)


    #Grafica frecuencia relativa
    plt.title('Frecuencia relativa de cada elemento con '+str(i)+' tiradas')
    plt.bar(range(0,i), frecuenciasRelativas,1, color="red",edgecolor="blue")
    plt.ylim(0,1)
    plt.xlim(-1,i)
    plt.axhline(18/37, color='k',ls="dotted", xmax=i)
    plt.grid(True)
    plt.show()
    plt.clf()

            #Grafica frecuencia relativa
    plt.title('Frecuencia relativa de apuesta favorable')
    plt.plot(range(0,i),frecuenciasRelativas)
    plt.xlabel("Tiradas")
    plt.ylabel("Frecuencia Relativa")
    plt.axhline(18/37, color='k',ls="dotted", xmax=i)
    plt.ylim(0,1)
    plt.xlim(0,i)   
    plt.show()

    for index,f in enumerate(frecuenciasRelativas):
        frecuenciasRelativas[index] = f+1000
    #Grafica fluctuacion de capital
    plt.title('Capital en cada tirada')
    plt.plot(range(0,i),frecuenciasRelativas)
    plt.plot(range(0,i),historioCapital)
    plt.xlabel("Tiradas")
    plt.ylabel("Cantidad de capital en pesos")
    plt.axhline(money, color='k',ls="dotted", xmax=i)
    plt.ylim(0,money*2)
    plt.xlim(0,i)   
    plt.show()

def menu():
    
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

def Exit():
    exit=True

def switch(case):
    sw = {
      1: Martingala(),
      2: Dalembert(),
      3: exit(),
    }
    return sw.get(case, default())

def switchMartingala(case):
    sw = {
      1: MartingalaInfinito(),
      2: MartingalaFinito(),
    }
    return sw.get(case, default())

def switchDalembert(case):
    pass
  
while not exit:
    
    menu()
    case = int(input("Seleccione una opcion: "))
    print(switch(case))

def AssignSpace(result):
    if (result>=1 and result<=18):
        return 1
    elif (result>=19 and result<=36):
        return 2
    elif(result==0):
        return 0

        
def ChooseSide():
    return ran.randint(1,2)

def calcularFrCadaElemento():
    unicos, cuenta = np.unique(tiradas, return_counts=True)
    fk= cuenta/cantidadTiradas
    fkn = np.asarray((ruleta, fk)).T
    return fk

def Dalembert(capital):
    capital_retiro = 0
    capital_inicial = capital
    historico = []
    for i in range(0,cantidadJuegos):
        frecuenciasRelativas = []
        historioCapital = []
        apuesta = 1
        capital_inicial = capital
        indice = 0
        vecesGanadas = 0
        while(capital_inicial >= 0 and capital_inicial <= 1200):          
            indice += 1
            tirada = AssignSpace(GirarRuleta())
            if lado == tirada:
                capital_inicial += apuesta
                vecesGanadas += 1              
                print(tirada,apuesta, capital_inicial)
                if apuesta > 1:
                    apuesta = apuesta - 1
            else:
                capital_inicial -= apuesta
                print(tirada,apuesta, capital_inicial)
                apuesta = apuesta + 1
            frecuenciasRelativas.append(vecesGanadas/indice)  
            historioCapital.append(capital_inicial)
        if capital_inicial <= 0:
            historico.append(0)
        elif capital_inicial >= capital:
            historico.append(1)


        #Grafica frecuencia relativa
        plt.title('Frecuencia relativa de cada elemento con '+str(indice)+' tiradas')
        plt.bar(range(0,indice), frecuenciasRelativas,1, color="red",edgecolor="blue")
        plt.ylim(0,1)
        plt.xlim(-1,indice)
        plt.axhline(18/37, color='k',ls="dotted", xmax=indice)
        plt.grid(True)
        plt.show()
        plt.clf()

        #Grafica frecuencia relativa
        plt.title('Frecuencia relativa de apuesta favorable')
        plt.plot(range(0,indice),frecuenciasRelativas)
        plt.xlabel("Tiradas")
        plt.ylabel("Frecuencia Relativa")
        plt.axhline(18/37, color='k',ls="dotted", xmax=indice)
        plt.ylim(0,1)
        plt.xlim(0,indice)   
        plt.show()

        for index,f in enumerate(frecuenciasRelativas):
            frecuenciasRelativas[index] = f+1000
        #Grafica fluctuacion de capital
        plt.title('Capital en cada tirada')
        plt.plot(range(0,indice),frecuenciasRelativas)
        plt.plot(range(0,indice),historioCapital)
        plt.xlabel("Tiradas")
        plt.ylabel("Cantidad de capital en pesos")
        plt.axhline(capital, color='k',ls="dotted", xmax=indice)
        plt.ylim(0,capital*2)
        plt.xlim(0,indice)   
        plt.show()


if __name__ == "__main__":
    
    CrearRuleta()
    tiradas = RealizarTiradas(cantidadTiradas) #tiradas en 0,1,2
    lado = ChooseSide()     #elijo un "lado" random
    print(lado)
    Dalembert(capital)
    MartingalaFinito()
    MartingalaInfinito()
    Dalembert()
    
