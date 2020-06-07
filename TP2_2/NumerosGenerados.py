import numpy as np
def GCL(mod,semilla,cantidadGenerada,a,c):
    '''Generador gcl
    Parametros: mod,semilla,cantidadGenerada
    '''
    listaAleatoria = []
    N = semilla
    for i in range (cantidadGenerada):
        N = (((a)* N + c) % mod)
        listaAleatoria.append(N)
    #print(listaAleatoria)  
    listaAleatoria = np.asarray(listaAleatoria)/2**32    
    return (listaAleatoria)

if __name__ == "__main__":
    GCL(10000,45,5000,15,4)

def generarNumeros(n):
    return GCL(2**32,3298876,n,134775813,1)