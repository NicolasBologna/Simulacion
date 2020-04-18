import matplotlib.pyplot as plt
import random as ran
import numpy as np  
from scipy import stats
from tabulate import tabulate

min = 0
max = 37
cantidadTiradas =  250
ruleta = [] 

def CrearRuleta():
    ruleta.extend(range(min,max))
    print("La ruleta es la siguiente:", ruleta)

def GirarRuleta():
    return ran.randint(min,max-1)

def RealizarTiradas(cantidadTiradas):
    tiradas = []
    for i in range(0,cantidadTiradas):
        tiradas.append(GirarRuleta())
    return tiradas

def calcularFrCadaElemento():
    unicos, cuenta = np.unique(tiradas, return_counts=True)
    fk= cuenta/cantidadTiradas
    fkn = np.asarray((ruleta, fk)).T # .T hace la transpuesta
    headers = ["Ni","Fr"]
    print(tabulate(fkn,headers = headers))

def CalcularFrecuenciasRelativasPorTirada(tiradas, numero):
    saleNumero = 0
    frecuenciaRelativaDelNumeroPorTirada = []
    for index, tirada in enumerate(tiradas):
        if tirada == numero:
            saleNumero += 1
        frecuenciaRelativaDelNumeroPorTirada.append(saleNumero/(index+1))
    return frecuenciaRelativaDelNumeroPorTirada

def graficarFrecuenciasRelativas():
    listaFrPorTirada = CalcularFrecuenciasRelativasPorTirada(tiradas,2)
    Px = int(cantidadTiradas/2)
    Py = listaFrPorTirada[Px]
    plt.annotate('Frecuencia relativa \n del número X con respecto a n',
         xy=(Px, Py),
         xycoords='data',
         xytext=(cantidadTiradas/6, 0.06),
         fontsize=9,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=.2"))
    plt.annotate(r'Frecuencia relativa esperada de X',
         xy=(Px, 1/(max-min)),
         xycoords='data',
         xytext=(cantidadTiradas/2, 0.01),
         fontsize=9,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=.2"))
    plt.title('Frecuencia relativa de un número X')
    plt.plot(range(0,cantidadTiradas),listaFrPorTirada)
    plt.xlabel("Tiradas")
    plt.ylabel("Frecuencia Relativa")
    plt.axhline(1/(max-min), color='k',ls="dotted", xmax=cantidadTiradas)
    plt.ylim(0,0.09)
    plt.xlim(0,cantidadTiradas)   
    plt.show()

def CalcularEsperanzaPorTirada(tiradas):
    esperanzaPorTirada = []
    tiradaTemp = []
    for tirada in tiradas:
        tiradaTemp.append(tirada)
        esperanzaPorTirada.append(np.mean(tiradaTemp))
    #print(esperanzaPorTirada)
    return esperanzaPorTirada

def graficarEsperanza(cantidadCorridas):
    #listaEsperanzaPorTirada = CalcularEsperanzaPorTirada(tiradas)
    tiradas = RealizarTiradas(cantidadTiradas)
    esperanzaTeorica = np.median(tiradas)
    for i in range(0,cantidadCorridas):
        tiradas = RealizarTiradas(cantidadTiradas)
        listaEsperanzaPorTirada = CalcularEsperanzaPorTirada(tiradas)
        plt.plot(listaEsperanzaPorTirada, label = "line "+ str(i))
    plt.title('Esperanza matemática')
    #plt.plot(listaEsperanzaPorTirada)
    plt.xlabel("Tiradas")
    plt.ylabel("Valor")
    plt.ylim(0,max)
    plt.xlim(0,cantidadTiradas)
    plt.axhline(esperanzaTeorica,color='k', ls="dotted", xmax=cantidadTiradas)
    plt.show()

def calculoVarianzaPorTirada(tiradas):                      #Calcula la varianza de los datos
    varianzaPorTirada = []
    tiradaTemp = []
    for tirada in tiradas:
        tiradaTemp.append(tirada)
        varianzaPorTirada.append(np.var(tiradaTemp))
    return varianzaPorTirada

def graficarVarianza(cantidadCorridas):
    tiradas = RealizarTiradas(cantidadTiradas)
    varianzaTeorica = np.var(tiradas)
    for i in range(0,cantidadCorridas):
        tiradas = RealizarTiradas(cantidadTiradas)
        listaVarianzaPorTirada = calculoVarianzaPorTirada(tiradas)
        plt.plot(listaVarianzaPorTirada, label = "line "+ str(i))
    
    plt.title('Varianza Matematica')
    plt.xlabel("Tiradas")
    plt.ylabel("Valor")
    plt.ylim(0,varianzaTeorica*2)
    plt.xlim(0, cantidadTiradas)
    plt.axhline(np.var(tiradas),color='k', ls="dotted", xmax=cantidadTiradas)  # ls es el tipo de linea
    plt.show()


def calculoDesvioPorTirada(tiradas):                      #Calcula la varianza de los datos
    desvioPorTirada = []
    tiradaTemp = []
    for tirada in tiradas:
        tiradaTemp.append(tirada)
        desvioPorTirada.append(np.std(tiradaTemp))
    return desvioPorTirada

def graficarDesvio(cantidadCorridas):
    tiradas = RealizarTiradas(cantidadTiradas)
    desvioTeorico = np.std(tiradas)
    for i in range(0,cantidadCorridas):
        tiradas = RealizarTiradas(cantidadTiradas)
        listaDesvioPorTirada = calculoDesvioPorTirada(tiradas)
        plt.plot(listaDesvioPorTirada, label = "line "+ str(i))
    
    plt.title('Varianza Matematica')
    plt.xlabel("Tiradas")
    plt.ylabel("Valor")
    plt.ylim(0,desvioTeorico*2)
    plt.xlim(0, cantidadTiradas)
    plt.axhline(np.std(tiradas),color='k', ls="dotted", xmax=cantidadTiradas)  # ls es el tipo de linea
    plt.show()
    
CrearRuleta()
tiradas = RealizarTiradas(cantidadTiradas)
#print(tiradas)
#print(CalcularFrecuenciasRelativasPorTirada(tiradas,2))


for i in range(1,6,4):
    #graficarFrecuenciasRelativas()
    #graficarEsperanza(i)
    #graficarVarianza(i)
    graficarDesvio(i)
