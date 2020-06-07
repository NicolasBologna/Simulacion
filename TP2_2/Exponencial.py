import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import random as rm
import math
import NumerosGenerados as ng

n = 100000
inicio = 0
alfa = 2
numeros_uniformes = sp.expon.rvs(size=n, loc = inicio, scale=1/alfa)

plt.hist(numeros_uniformes, bins=50, color='skyblue', histtype="bar",alpha=0.8,ec="black")
plt.xlabel("valores")
plt.ylabel("Frecuencia Absoluta")
plt.show()


#----------Naylor----------
randomGCL = ng.generarNumeros(n)

def exponencial(alfa):
    EX= 1/alfa
    exponenciales=[]
    for r in randomGCL:
        x= -EX*math.log(r)
        exponenciales.append(x)
    print("Media: ", round(np.mean(exponenciales),3))
    print("Desvio: ", round(np.sqrt(np.var(exponenciales)),3))
    print("Varianza: ", round(np.var(exponenciales),3))
    plt.title("Distribuciones Exponenciales")
    plt.hist(numeros_uniformes, bins=50, color='skyblue', histtype="bar",alpha=0.8,ec="black")
    plt.hist(exponenciales, bins=50, edgecolor="black", histtype="bar",color='darkgrey',alpha=0.8,ec="red")
    plt.show()

exponencial(alfa)
