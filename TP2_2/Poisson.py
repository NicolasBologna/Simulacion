import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng
import scipy.interpolate as si

mu =  3.6 
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

#----------Naylor----------
cant = 10000
randomGCL = ng.generarNumeros(cant)

def poisson(lamda):
    poissons = []
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
    print("Media: ", np.mean(poissons))
    print("Desvio: ", np.sqrt(np.var(poissons)))
    print("Varianza: ", np.var(poissons))
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

poisson(mu)