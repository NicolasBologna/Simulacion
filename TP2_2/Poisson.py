import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng
import scipy.interpolate as si
from Testsdiscretos import testPoisson

mu =  6.3 
poisson = sp.poisson(mu) 
xLine = np.arange(poisson.ppf(0.01),
              poisson.ppf(0.99))
fmp = poisson.pmf(xLine)
plt.plot(xLine, fmp, '--',color = "red")
plt.vlines(xLine, 0, fmp, colors='b', lw=5, alpha=0.5,ec='black')
plt.title('Distribución Poisson')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
print("Media: ", round(np.mean(xLine),3))
print("Desvio: ", round(np.sqrt(np.var(xLine)),3))
print("Varianza: ", round(np.var(xLine),3))

#----------Naylor----------
cant = 10000
randomGCL = ng.generarNumeros(cant)
poissons = []

def funPoisson(lamda):
    for i in range (cant):
        x = 0
        b = np.exp(-lamda)
        tr = 1
        r = rm.uniform(1,0)
        tr = tr * r
        while((tr-b)>=0):
            x = x + 1
            r = rm.uniform(1,0)
            tr = tr * r
        poissons.append(x)
    unicos, cuenta = np.unique(poissons, return_counts=True)
    frec = np.array(cuenta/cant)
    print("Media: ", round(np.mean(poissons),3))
    print("Desvio: ", round(np.sqrt(np.var(poissons)),3))
    print("Varianza: ", round(np.var(poissons),3))
    plt.title("Distribucion de Poisson")
    print(unicos,cuenta)
    xnew = np.linspace(unicos.min(), unicos.max(), 300)  
    spl = si.make_interp_spline(unicos, frec, k=3)
    frec_suavizada = spl(xnew)

    plt.plot(xLine, fmp, '--',color = "violet")
    plt.vlines(xLine, 0, fmp, colors='black', lw=5, alpha=0.5)

    plt.plot(xnew, frec_suavizada, '--', color = "brown")
    plt.bar(unicos, frec, width=0.2, alpha = 0.7)
    plt.show()

funPoisson(mu)

poissonTeorica = np.random.poisson(mu,cant)

testPoisson(poissons,poissonTeorica)
