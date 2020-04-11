import matplotlib as mp
import random as ran
import numpy as np  
from scipy import stats

min = 0
max = 37
cantidadTiradas = 100
ruleta = [] 

def CrearRuleta():
    ruleta.extend(range(min,max))
    print("La ruleta es la siguiente:", ruleta)

def GirarRuleta():
    return ran.randint(min,max)

def RealizarTiradas(cantidadTiradas):
    tiradas = []
    for i in range(0,cantidadTiradas):
        tiradas.append(GirarRuleta())
    print("Las tiradas fueron: ", tiradas)
    return tiradas

CrearRuleta()


unicos, cuenta = np.unique(RealizarTiradas(cantidadTiradas), return_counts=True)

# frecuencia relativa
fk= cuenta/cantidadTiradas
fkn = np.asarray((ruleta, fk)).T # T transpuesta
print(fk)
print(fkn)