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
maximo = 36
cantidadTiradas =  80
cantidadJuegos = 5
ruleta = [] 
capital = 1000

def CrearRuleta():
    ruleta.extend(range(min,maximo))
    print("La ruleta es la siguiente:", ruleta)

def GirarRuleta():
    return ran.randint(min,maximo)

def RealizarTiradas(cantidadTiradas):
    tiradas = []
    for i in range(0,cantidadTiradas):
        tiradas.append(AssignSpace(GirarRuleta()))
    return tiradas

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
    capital_inicial = capital
    historico = []
    cincoFRs = []
    cincoHCs = []
    for i in range(0,cantidadJuegos):
        frecuenciasRelativas = []
        historioCapital = []
        apuesta = 1
        capital_inicial = capital
        indice = 0
        vecesGanadas = 0
        for i in range(0,cantidadTiradas):          
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
        cincoFRs.append(frecuenciasRelativas)
        cincoHCs.append(historioCapital)
        if capital_inicial <= 0:
            historico.append(0)
        elif capital_inicial >= capital:
            historico.append(1)


    #Grafica frecuencia relativa
    plt.title('Frecuencia relativa apuesta favorable con '+str(indice)+' tiradas')
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

    #Grafica fluctuacion de capital
    plt.title('Capital en cada tirada')
    plt.plot(range(0,indice),historioCapital)
    plt.xlabel("Tiradas")
    plt.ylabel("Cantidad de capital en pesos")
    plt.axhline(capital, color='k',ls="dotted", xmax=indice)
    plt.ylim(600,(capital*2)-600)
    plt.xlim(0,indice)   
    plt.show()

    #Grafica frecuencia relativa de 5
    plt.title('Frecuencia relativa de apuesta favorable')
    for fr in cincoFRs:
        plt.plot(range(0,indice),fr)
    plt.xlabel("Tiradas")
    plt.ylabel("Frecuencia Relativa")
    plt.axhline(18/37, color='k',ls="dotted", xmax=indice)
    plt.ylim(0,1)
    plt.xlim(0,indice)   
    plt.show()

    #Grafica fluctuacion de capital de 5
    plt.title('Capital en cada tirada')
    for hc in cincoHCs:
        plt.plot(range(0,indice),hc)
    plt.plot(range(0,indice),historioCapital)
    plt.xlabel("Tiradas")
    plt.ylabel("Cantidad de capital en pesos")
    plt.axhline(capital, color='k',ls="dotted", xmax=indice)
    plt.ylim(600,(capital*2)-600)
    plt.xlim(0,indice)   
    plt.show()

    #Grafica fluctuacion de capital vs fr
    plt.title('Porcentaje de capital con \n respecto a la freceuncia \n en cada tirada')
    plt.plot(range(0,indice),frecuenciasRelativas)
    historioCapital = np.asarray(historioCapital)/max(historioCapital)

    plt.plot(range(0,indice),historioCapital)
    plt.xlabel("Tiradas")
    plt.ylabel("Cantidad de capital en pesos")
    plt.axhline(capital, color='k',ls="dotted", xmax=indice)
    plt.ylim(-0.5,1.5)
    plt.xlim(0,indice)   
    plt.show()

    '''print(historico)
    unicos, cuenta = np.unique(historico, return_counts=True)
    print(unicos,cuenta)
    if cuenta[0] and cuenta[1]:
        print("perdida: ", cuenta[0]*capital)
        print("ganancia: ", cuenta[1]*10)
        print("neto: ", cuenta[1]*10 - cuenta[0]*capital)'''




if __name__ == "__main__":
    CrearRuleta()
    tiradas = RealizarTiradas(cantidadTiradas) #tiradas en 0,1,2
    lado = ChooseSide()     #elijo un "lado" random
    print(lado)
    Dalembert(capital)
    

