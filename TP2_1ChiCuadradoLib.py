#test de chicuadrado a un conjunto generado por librería

import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import stats

mod = 64 #poner el valor maximo + 1

n = 450
k = 10
salto = 1/k

confianza = 0.95

generadosLib = []
for i in range(0,n):
    generadosLib.append(random.uniform(0,1))

enter = 0
for elem in generadosLib:
	if enter == 9:
		print(round(elem,5), " \\\ ")
		enter = 0
	else:
		print(round(elem,5), " & ")
		enter += 1
confianza = 0.95

listaFrAbs = np.array([0] * k)

for i in generadosLib:
	posLista = 0
	for j in np.arange(0,1,salto):
		if j < i < j+salto:
			listaFrAbs[posLista] += 1 
			break
		posLista += 1
print(listaFrAbs)
listaFr = listaFrAbs/n
#Grafica frecuencia absoluta
plt.title('Frecuencia relativa de números generados por intervalo')
plt.bar(range(0,k),(listaFr))
plt.xlabel("Intervalo")
plt.ylabel("Frecuencia relativa")
plt.ylim(0,max(listaFr)*2)
plt.xlim(-1,k)   
plt.show()

sumatoriaFrecuencias = 0
for frec in listaFrAbs:
	print(frec, " ", n, " ", k)
	sumatoriaFrecuencias += (frec-(n/k))**2

chicuadrado = (k/n)*(sumatoriaFrecuencias)

print("X^2 = ",chicuadrado)

valorTabla = stats.chi2.ppf(1-confianza,k-1)
print(valorTabla)

if chicuadrado > valorTabla:
	print("No son uniformes")
else:
	print("Son uniformes")