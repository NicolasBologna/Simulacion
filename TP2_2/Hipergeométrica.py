import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import NumerosGenerados as ng
import scipy.interpolate as si



# Graficando Hipergeométrica
M, n, N = 30, 10, 12 # parametros de forma 
hipergeometrica = sp.hypergeom(M, n, N) # Distribución
xLine = np.arange(0, n+1)
fmp = hipergeometrica.pmf(xLine) # Función de Masa de Probabilidad
plt.plot(xLine, fmp, '--')
plt.vlines(xLine, 0, fmp, colors='red', lw=5, alpha=0.5,ec="black")
plt.title('Distribución Hipergeométrica')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

#----------Naylor----------
cant = 10000
randomGCL = ng.generarNumeros(cant)

def hiper(N, n, p):
    hipers = []
    for i in range (cant):
        x = 0
        Nn= N
        Pp = p
        for j in range (n):
            r = rm.choice(randomGCL)
            if ((r-Pp)<=0):
                s = 1
                x = x +1
            else:
                s = 0
            Pp = (Nn * Pp - s)/(Nn - 1)
            Nn = Nn - 1
        hipers.append(x)
    unicos, cuenta = np.unique(hipers, return_counts=True)
    frec = np.array(cuenta/cant)
    print("Media: ", np.mean(hipers))
    print("Desvio: ", np.sqrt(np.var(hipers)))
    print("Varianza: ", np.var(hipers))
    plt.title("Distribucion Hipergeométrica")
    print(unicos,cuenta)
    xnew = np.linspace(unicos.min(), unicos.max(), 300)  
    spl = si.make_interp_spline(unicos, frec, k=3)
    frec_suavizada = spl(xnew)

    plt.plot(xLine, fmp, '--')
    plt.vlines(xLine, 0, fmp, colors='black', lw=5, alpha=0.5)

    plt.plot(xnew, frec_suavizada, '--')
    plt.bar(unicos, frec, width=0.2, alpha = 0.7)
    plt.show()

hiper(n, M , N)