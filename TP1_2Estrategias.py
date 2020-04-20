import matplotlib.pyplot as plt
import random as ran
import numpy as np  
from scipy import stats

min = 0
max = 37
cantidadTiradas =  1000
ruleta = [] 

def CrearRuleta():
    ruleta.extend(range(min,max))
    print("La ruleta es la siguiente:", ruleta)

def GirarRuleta():
    return ran.randint(min,max-1)

def RealizarTiradas(cantidadTiradas):
    tiradas = []
    for i in range(0,cantidadTiradas):
        tiradas.append(GirarRuleta())
    return tiradas
    
