import numpy
import random
import matplotlib.pyplot as plt
from scipy import stats

def crearRuleta(ruleta,cantNum):
 for i in range(0, cantNum):
     ruleta[i] = i
 return ruleta

def girarRuleta(ruleta):
     num=random.choice(ruleta)                      #Elije algun valor en la lista Ruleta
     return num

def calculoEsperanza(lista):
 esperanza= numpy.mean(lista)                       #Calcula la esperanza matematica de los datos
 return esperanza

def calculoDesvioEstandar(lista):
    desviacionEstandar=numpy.std(lista)             #Calcula el desvio estandar de los datos
    return desviacionEstandar

def calculoVarianza(lista):
    varianza=numpy.var(lista)                       #Calcula la varianza de los datos
    return varianza

def calculoFrecuenciaRelativaDeCadaElemento(lista,ruleta,cantTiradas):
   frecNumeros=[]
   vecesNumeros=[]
   for i in range(0, len(ruleta)):
        vecesNumeros.append(lista.count(ruleta[i]))    #Cuenta la cantidad de veces que aparecio cada numero
        frecNumeros.append(vecesNumeros[i]/cantTiradas)         #Lo divido por la cantidad de tiradas y se tiene la frecuencia relativa de cada elemento
   print("\nLas veces que aparecio cada numero es = ",vecesNumeros)
   print("La frecuencia relativa de los numeros es= ",frecNumeros)

def calculoFrecuanciaRel(lista,nroTirada):
    frecRelativa=[]
    frecRelativa.append(lista.count(5)/(nroTirada+1)) #Misma idea que Gianluca para ver con que frecuencia sale un valor
    return frecRelativa

def creoGraficosFrecRelativa(lista,cantTiradas):
    plt.title('Frecuencia relativa')
    plt.plot(lista)
    plt.xlabel("Tiradas")
    plt.ylabel("Probabilidad ")
    plt.axhline(1/37, color='k',ls="dotted", xmax=cantTiradas)      #Comando para linea horizontal constante
    plt.ylim(0,0.5)                                                 #Limites para el eje Y
    plt.xlim(0,cantTiradas)                                         #Limites para el eje X
    plt.show()

def creoGraficoEsperanza(lista,cantTiradas):
    plt.title('Esperanza matematica')
    plt.plot(lista)
    plt.xlabel("Tiradas")
    plt.ylabel("Valor")
    plt.ylim(0,37)
    plt.xlim(0,cantTiradas)
    plt.axhline(18,color='k', ls="dotted", xmax=cantTiradas)        #ls es el tipo de linea
    plt.show()

def creoGraficoHistograma(lista):
   plt.figure("Grafico de Frecuencia absoluta")
   plt.title('Numeros ganadores')
   plt.hist(lista,bins=37,range=(0,36),color='#0504aa',histtype='bar', alpha=0.7, rwidth=0.85,linewidth=1)
   plt.grid(True)                      #Se crea las rendijas del histograma
   plt.xlabel("Numeros")               #Nombro al eje X
   plt.ylabel("Cantidad de veces")            #Nombro al eje Y
   plt.show()
   plt.clf()

def creoGraficoDesvioEstandar(lista,cantTiradas):
    plt.title('Desvio Estandar Matematico')
    plt.plot(lista)
    plt.xlabel("Tiradas")
    plt.ylabel("Valor")
    plt.ylim(0,37)
    plt.xlim(0,cantTiradas)
    plt.axhline(10.631,color='k', ls="dotted", xmax=cantTiradas)        #ls es el tipo de linea
    plt.show()

def creoGraficoVarianzaEsperanza(lista):
    plt.title('Varianza Matematica de la Esperanza Matematica')
    plt.plot(lista)
    plt.xlabel("Tiradas")
    plt.ylabel("Valor")
    plt.ylim(0,36)
    plt.xlim(0, cantTiradas)
    plt.axhline(color='k', ls="dotted", xmax=cantTiradas)  # ls es el tipo de linea
    plt.show()

listaGanadores=[]                       #Lista donde se van a meter el resultado de las tiradas
listaFrecuencia=[]                      #Lista de frecuencias de un numero x
listaEsperanzas=[]                      #Lista con las esperanzas
listaDesviosEstandar=[]                 #Lista de los desvios estandar
listaVarianzaDeEsperanza=[]             #Lista de Varianzas de las Esperanzas
listaEsperanzaDeEsperanza=[]            #Lista de Esperanzas de Esperanzas
cantTiradas=1000
cantNum=37
ruleta = [0] * cantNum
crearRuleta(ruleta,cantNum)             #Se crea la ruleta con los numeros ingresados

for i in range(cantTiradas):
    numGanador=girarRuleta(ruleta)        #Se devuelve el numero ganador y la cantidad de veces que se giro la ruleta
    listaGanadores.append(numGanador)       #Aca se va meteiendo el resultado de la tirada
    listaFrecuencia.append(calculoFrecuanciaRel(listaGanadores, i)) #Se calcula la frecuencia de un valor especifico tiro a tiro y se lo agrega en una lista
    listaEsperanzas.append(calculoEsperanza(listaGanadores))
    listaDesviosEstandar.append(calculoDesvioEstandar(listaGanadores))
    listaVarianzaDeEsperanza.append(calculoVarianza(listaEsperanzas))
    listaEsperanzaDeEsperanza.append(calculoEsperanza(listaEsperanzas))


creoGraficoEsperanza(listaEsperanzas,cantTiradas)
creoGraficosFrecRelativa(listaFrecuencia,cantTiradas)
creoGraficoDesvioEstandar(listaDesviosEstandar,cantTiradas)
creoGraficoVarianzaEsperanza(listaVarianzaDeEsperanza)
creoGraficoEsperanza(listaEsperanzaDeEsperanza,cantTiradas)
creoGraficoHistograma(listaGanadores)
#calculoFrecuenciaRelativaDeCadaElemento(listaGanadores,ruleta,cantTiradas)