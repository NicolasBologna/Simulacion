import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng


# Graficando Binomial
n, p = 30, 0.4
x = np.arange(sp.binom.ppf(0.01, n, p),
              sp.binom.ppf(0.99, n, p))
fmp = sp.binom.pmf(x, n, p) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

#----------Naylor----------
randomGCL = ng.generarNumeros(n)

def funBinomial(n, p):
    binomiales= []
    for i in range (n):
        x= 0
        for j in range (n):
            r=rm.choice(randomGCL)
            if ((r-p)<=0):
                x = x + 1
        binomiales.append(x)
    print("Media: ", np.mean(binomiales))
    print("Desvio: ", np.sqrt(np.var(binomiales)))
    print("Varianza: ", np.var(binomiales))
    plt.title("Distribucion Binomial")
    plt.hist(binomiales, density=True , bins=15, edgecolor="black")
    plt.show()

funBinomial(n,p)