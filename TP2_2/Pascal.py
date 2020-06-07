import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng


# Graficando Binomial negativa
n, p = 20 , 0.2 # parametros de forma 
nbinomial = sp.nbinom(n=n, p=p) # Distribución
x = np.arange(nbinomial.ppf(0.01),
              nbinomial.ppf(0.99))
fmp = nbinomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial Negativa')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

#Naylor

#----------Naylor----------
randomGCL = ng.generarNumeros(n)

def nBinomial(n, p):
    pascales= []
    for r in randomGCL:
        tr=1
        qr = math.log(p)
        for i in np.arange(n):
            tr = tr * r
        nx = math.log(tr)/qr
        pascales.append(nx)
    print("Media: ", np.mean(pascales))
    print("Desvio: ", np.sqrt(np.var(pascales)))
    print("Varianza: ", np.var(pascales))
    plt.title("Distribucion Binomial Negativa (Pascal)")
    plt.hist(pascales, bins=15, edgecolor="black")
    plt.show()

nBinomial(n,p)

