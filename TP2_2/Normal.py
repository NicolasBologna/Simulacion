import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng

n = 100000
inicio = 0
ancho = 20
alfa = 200
numerosNormal = sp.norm.rvs(size=n, loc = inicio, scale=ancho)

plt.hist(numerosNormal, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
plt.xlabel("valores")
plt.ylabel("Frecuencia Absoluta")
plt.show()

#----------Naylor----------
randomGCL = ng.generarNumeros(n)

def normal(esperanza, desvio):
    normales = []
    for i in range (n):
        sumatoria = 0
        for j in range (1,12):
            r=rm.choice(randomGCL)
            sumatoria = sumatoria + r
        normales.append((desvio * (sumatoria-6)) + esperanza )
    print("Media: ", round(np.mean(normales),3))
    print("Desvio: ", round(np.sqrt(np.var(normales)),3))
    print("Varianza: ", round(np.var(normales),3))
    plt.title("Distribuciones Normales")
    plt.hist(numerosNormal, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
    plt.hist(normales, bins=50,color = 'skyblue', histtype="bar",alpha=0.8,ec="black")
    plt.show()

normal(10,20)