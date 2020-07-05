import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng
import scipy.interpolate as si


# Graficando Binomial negativa
n, p = 4 , 0.2 # parametros de forma 
nbinomial = sp.nbinom(n=n, p=p) # Distribución
xLine = np.arange(nbinomial.ppf(0.01),
              nbinomial.ppf(0.99))
fmp = nbinomial.pmf(xLine) # Función de Masa de Probabilidad
plt.plot(xLine, fmp, '--')
plt.vlines(xLine, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial Negativa')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
print("Media: ", np.mean(xLine))
print("Desvio: ", np.sqrt(np.var(xLine)))
print("Varianza: ", np.var(xLine))

#Naylor

#----------Naylor----------
cant=100000
randomGCL = ng.generarNumeros(cant)

#q = probabilidad de fracaso.

def nBinomial(k, q):
    pascales= []
    qr = math.log(q)
    for j in range (cant):
        tr=1.0
        for i in range(k):
            r = rm.choice(randomGCL)
            tr = tr * r
        nx = math.log(tr)//qr
        pascales.append(nx)
    unicos, cuenta = np.unique(pascales, return_counts=True)
    frec = np.array(cuenta/cant)
    print("Media: ", np.mean(pascales))
    print("Desvio: ", np.sqrt(np.var(pascales)))
    print("Varianza: ", np.var(pascales))
    plt.title("Distribucion Binomial Negativa (Pascal)")
    xnew=np.linspace(unicos.min(),unicos.max(),300)
    spl = si.make_interp_spline(unicos,frec, k=3)
    frec_suavizada=spl(xnew)
    plt.xlim(0,50)
    plt.plot(xLine, fmp, '--',color = "violet")
    plt.vlines(xLine, 0, fmp, colors='black', lw=5, alpha=0.5,linestyles='dashed')

    plt.plot(xnew,frec_suavizada,'--',color="brown")
    plt.bar(unicos, frec, width=0.2, alpha = 0.7)
    plt.show()

#int(n-(n*(1-p)))

nBinomial(n,1-p)

