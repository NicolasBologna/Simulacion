def MedioCuadrado(semilla, cantNumGenerar):
    cantDigitos = len(str(semilla))
    cantDigitosGenerados = cantDigitos * 2
    numeroGenerado = semilla
    arrayNumerosAleatorios = []
    for i in range(0,cantNumGenerar):
        numeroGenerado = int(numeroGenerado) ** 2
        if len(str(numeroGenerado)) != cantDigitosGenerados:        
            numeroGenerado = str(numeroGenerado).zfill(cantDigitos*2) 
        numeroGenerado = str(numeroGenerado)[cantDigitos-cantDigitos//2:cantDigitos+cantDigitos//2]
        arrayNumerosAleatorios.append(int(numeroGenerado))
    #print(arrayNumerosAleatorios)
    return(arrayNumerosAleatorios)

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
    return (listaAleatoria)

if __name__ == "__main__":
    GCL(10000,45,5000,15,4)
    MedioCuadrado(1009,50)


