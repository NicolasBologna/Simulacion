import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import TP2_1NumerosAleatorios as generadores

#k > 100!! cantidad de subintervalos
#n/k > 5 n = cantidad de numeros

mod = 512 #poner el valor maximo + 1
n = 450
k = 100
salto = 1/k

generadosGCL = np.array(generadores.GCL(mod,347887,n,557,33453))/(mod-1)

enter = 0
'''for elem in generadosGCL:
	if enter == 9:
		print(round(elem,5), " \\\ ")
		enter = 0
	else:
		print(round(elem,5), " & ")
		enter += 1'''
confianza = 0.99

listaFrAbs = np.array([0] * k)
   
for i in generadosGCL:
	posLista = 0
	for j in np.arange(0,1,salto):
		if j < i < j+salto:
			listaFrAbs[posLista] += 1 
			break
		posLista += 1


print(listaFrAbs)
listaFr = listaFrAbs/n
#Grafica frecuencia relativa
plt.title('Frecuencia relativa de números generados por intervalo')
plt.bar(range(0,k),(listaFr))
plt.xlabel("Intervalo")
plt.ylabel("Frecuencia absoluta")
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

