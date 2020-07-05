import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng

n = 100000
inicio = 0
ancho = 20
K = 3
numerosGamma = sp.gamma.rvs(size=n, a = K)

print("Media: ", round(np.mean(numerosGamma),3))
print("Desvio: ", round(np.sqrt(np.var(numerosGamma)),3))
print("Varianza: ", round(np.var(numerosGamma),3))

plt.hist(numerosGamma, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
plt.xlabel("valores")
plt.ylabel("Frecuencia Absoluta")
plt.show()

#----------Naylor----------
randomGCL = ng.generarNumeros(n)

def gamma(k, alfa):
    gammas= []
    for i in range (n):
        tr=1
        for j in range (k):
            r=rm.choice(randomGCL)
            tr= tr * r
        x= -math.log(tr)/alfa
        gammas.append(x)
    print("Media: ", round(np.mean(gammas),3))
    print("Desvio: ", round(np.sqrt(np.var(gammas)),3))
    print("Varianza: ", round(np.var(gammas),3))
    plt.title("Distribucion Gamma")
    plt.hist(numerosGamma, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
    plt.hist(gammas, bins=50, edgecolor="black", histtype="bar",alpha=0.6)
    plt.show()

gamma(K,1)