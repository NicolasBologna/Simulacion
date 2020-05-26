import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.stats import chisquare
import math
import requests
import scipy.stats as st

#------Generador medio del cuadrado-------

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
    print(arrayNumerosAleatorios)
    return(arrayNumerosAleatorios)

def chi2():
    salto=1/k
    listaFA = np.array([0] * k)
    
    for i in numeros:
        intervalo = 0
        for j in np.arange(0,1,salto):
            if j < i < j+salto:
                listaFA[intervalo] += 1 
                break
            intervalo += 1

    listaFr = listaFA/n #lista de frecuencias relativas

    #---------------Grafica frecuencia relativa-----------------------
    plt.title('Frecuencia relativa de los números generados por cada intervalo')
    plt.bar(range(0,k),(listaFr))
    plt.xlabel("Intervalo")
    plt.ylabel("Frecuencia absoluta")
    plt.ylim(0,max(listaFr)*2)
    plt.xlim(-1,k)   
    plt.show()

    #---------------Calculo X²-----------------------
    sumatoriaFrecuencias = 0
    listaFrecuencias = []
    for frec in listaFA:
        sumatoriaFrecuencias += (frec-(n/k))**2
        listaFrecuencias.append((frec-(n/k))**2)
    chicuadrado = (k/n)*(sumatoriaFrecuencias)


    print("X^2 = ",chicuadrado)

    valorTabla = stats.chi2.ppf(1-alfa,k-1)
    print("valor tabla para alfa:", alfa ,"y grados de libertad:", k-1, " = ",valorTabla)

    if chicuadrado > valorTabla:
        print("No son uniformes")
    else:
        print("Son uniformes")

    #-------------Gráficos chi cuadrado--------------------

    x = np.arange(0, max(numeros), 10)
    plt.plot(x, stats.chi2.pdf(x, df=k-1), color='r', lw=2)
    plt.show()


#-----------Test de corridas-------------------------------------------

def corridas():
    media=np.mean(numeros) #calculo la media de los generados
    print("La media es: ",media)
    secuencia= []   
    alfaCorridas = 0.05  
    print("La confianza utilizada es: ", 1-alfaCorridas)
    cantidadHastaCambio = 0 
    listaCantidadHastaCambio = []
    cantidadCorridas=1
    
    for index, num in enumerate(numeros):
        if num<media:
            secuencia.append(0)
        else: 
            secuencia.append(1)
        if index >= 1:
            cantidadHastaCambio +=1
            if secuencia[-2] != secuencia[-1]:
                listaCantidadHastaCambio.append(cantidadHastaCambio)
                cantidadHastaCambio = 0
                cantidadCorridas=cantidadCorridas+1

    frecuenciaAbsolutaCanCambios = []            
    for cantHastaCambio in range(0,max(listaCantidadHastaCambio)):
        frecuenciaAbsolutaCanCambios.append(listaCantidadHastaCambio.count(cantHastaCambio))
    #print("la secuencia es: ",secuencia)
    frecuenciaRelativaCanCambios = np.array(frecuenciaAbsolutaCanCambios)/cantidadCorridas

    print(frecuenciaRelativaCanCambios[0:15])
    #---------------Grafica frecuencia cambio-----------------------
    plt.title('Frecuencia relativa de cambio a medida \n que aumenta el tamaño de la corrida')
    plt.bar(range(0,len(frecuenciaRelativaCanCambios)),(frecuenciaRelativaCanCambios))
    plt.xlabel("cantidad de números en la corrida")
    plt.ylabel("Frecuencia relativa de cambio")
    plt.ylim(0,1)
    plt.xlim(0,15)   
    plt.show()

    cantidadMenores=secuencia.count(0)
    cantidadMayores=secuencia.count(1)
    num=secuencia[0]
    
    print("Cantidad de numeros menores a la media: ",cantidadMenores)
    print("Cantidad de numeros mayores a la media: ",cantidadMayores)
    print("Cantidad de corridas: ",cantidadCorridas)


    #n cantidad de numeros

    muco=(2*cantidadMenores*cantidadMayores)/(cantidadMenores+cantidadMayores) + 1
    var2co=(2*cantidadMenores*cantidadMayores*(2*cantidadMenores*cantidadMayores-n))/(n**2*(n-1))
    z0=(cantidadCorridas-muco)/math.sqrt(var2co)

    print(z0)

    zalfa=1.96

    if (-zalfa<z0<zalfa):
        print("Los valores son independientes")
    else:
        print("Los valores no son independientes.")

#--------------------------------------Test de correlación-------------------------

def autocorrelacion():

	for w in range (0, len(numeros)):
	    numeros[w] = round(numeros[w],5)
	i=2
	l=5
	N=n
	rs=0
	M= math.trunc((N - i)/l -1)
	if ((i+(M+1)*l)<N):
		print (M, "sirve")
	else:
		print (M, " No sirve")

	print(M)


	while i+l <= N :
		rs = rs + numeros[i-1]*numeros[i-1+l]
		i=i+l
		
	R = 1/(N+1) * rs
	print (R)

	D = round((math.sqrt(13*M + 7))/(12*(M+1)),3)

	Z = (R - 0.25)/D
	Z=abs(Z)
	print(D)
	print(Z)
	if (Z<1.28):
		print("Son aleatorios")
	else:
		print("No son aleatorios")

def smirnov():
    salto=1/k
    listaFA = np.array([0] * k)
    
    for i in numeros:
        intervalo = 0
        for j in np.arange(0,1,salto):
            if j < i < j+salto:
                listaFA[intervalo] += 1 
                break
            intervalo += 1
    listaFAA = []
    listaPA = []
    listaPAA = []
    FAA=0
    PA = 0
    PAA=0
    PEA=0
    PE=1/k
    listaPEA = []
    listaDMcalculado = []
    DM = 0
    for v in range(len(listaFA)):
        FAA= FAA + listaFA[v]
        listaFAA.append(FAA)
        PA = listaFA[v]/n
        listaPA.append(PA)
        PAA=PAA + PA
        listaPAA.append(PAA)
        PEA = PEA + PE
        listaPEA.append(PEA)
        listaDMcalculado.append(abs(PEA-PAA))

    print(listaPEA)
    print(listaPAA)
    DM=max(listaDMcalculado)
    DMcritico = 1.22/math.sqrt(n)
    print(DM)
    print(DMcritico)
    if (DM<DMcritico):
        print("Son uniformes")
    else: 
        print("No son uniformes")
    print(stats.kstest(numeros, 'uniform'))

def compararGeneradores():

    plt.title('Números generados')
    plt.plot(range(0,len(numeros)),numeros, linewidth=0.1)
    plt.xlabel("Número")
    plt.ylabel("Valor")
    plt.ylim(0,max(numeros))
    plt.xlim(0,len(numeros))   
    plt.show()


def poker():

    todos = []
    for t in (numeros):
        c1=''
        lista = [0] * 10
        for numero in range (0,10):
            lista[numero]=str(t)[2:7].count(str(numero))
        for l in range (len(lista)):
            if (lista[l] == 1):
                for ka in range(l+1, len(lista)):
                    if (lista[ka] == 1):
                        for j in range(ka + 1, len(lista)):
                            if (lista[j] ==1):
                                for m in range(j + 1, len(lista)):
                                    if (lista[j] ==1):
                                        c1 ='Distintos'
                                    elif(lista [j]== 2):
                                        c1 ='Un Par'
                            elif(lista[j]==2):
                                c1='Un Par'
                            elif(lista[j]==3):
                                c1= 'Pierna'
                    elif(lista[ka]==2):
                        for na in range (ka+1, len(lista)):
                            if (lista[na]== 1):
                                c1 ='Un Par'
                            elif(lista[na]==2):
                                c1='Doble Par'
                    elif(lista[ka]== 3):
                        c1='Pierna'
                    elif(lista[ka]== 4):
                        c1='Poker'
            elif(lista[l] == 2):
                for o in range(l+1, len(lista)):
                    if(lista[o]==1):
                        for p in range (o+1, len(lista)):
                            if(lista[p]==1):
                                c1='Un Par'
                            elif(lista[p]==2):
                                c1='Doble Par'
                    elif(lista[o]==2):
                        c1='Doble Par'
                    elif(lista[o]==3):
                        c1='Par y Pierna'
            elif (lista[l] == 3):
                for kb in range(l+1, len(lista)):
                    if (lista[kb] == 1):
                        c1='Pierna'
                    elif(lista[kb] == 2):
                        c1 = 'Par y Pierna'
            elif (lista[l] == 4):
                c1='Poker'
            elif (lista[l] == 5):
                c1= 'Quintilla'
        todos.append(c1)

    #Frecuencia esperada de cada jugada
    feDis=0.3024 * n
    fePar=0.5040 * n
    fePierna=0.072 * n
    feFull= 0.0090 * n
    feDoble=0.1080 * n
    fePoker= 0.0045 * n
    feQuntilla= 0.0001 * n

    listaFrecuenciasEsperadas = [feDis,fePar,fePierna,feFull,feDoble,fePoker,feQuntilla]
    nombresListaFrecuenciasEsperadas = ['Distintos','Un Par','Pierna','Par y\n Pierna','Doble \n Par','Poker','Quintilla']
    #Frecuencia Observada de cada jugada
    foDis= (todos.count('Distintos'))
    foPar= (todos.count('Un Par'))
    foPierna= (todos.count('Pierna'))
    foFull= (todos.count('Par y Pierna'))
    foDoble= (todos.count('Doble Par'))
    foPoker= (todos.count('Poker'))
    foQuntilla= (todos.count('Quintilla'))

    listaFrecuenciasObservadas = [foDis,foPar,foPierna,foFull,foDoble,foPoker,foQuntilla]
    print(listaFrecuenciasEsperadas)
    print(listaFrecuenciasObservadas)

    #---------------Grafica frecuencia cambio-----------------------
    plt.title('Frecuencia absoluta de cada jugada \n observada con respecto a la teórica')
    plt.bar(nombresListaFrecuenciasEsperadas,(listaFrecuenciasEsperadas), width=0.8)
    plt.bar(nombresListaFrecuenciasEsperadas,(listaFrecuenciasObservadas), width=0.4, color = "red")
    plt.xlabel("Mano")
    plt.ylabel("Frecuencia Absoluta")
    plt.ylim(0,max(listaFrecuenciasEsperadas)*1.5)
    plt.xlim(-1,len(listaFrecuenciasEsperadas))   
    plt.show()

    #Calculo Poker
    cDis= (((feDis -foDis)**2)/feDis)
    cPar=(((fePar -foPar)**2)/fePar)
    cPierna=(((fePierna -foPierna)**2)/fePierna)
    cFull=(((feFull -foFull)**2)/feFull)
    cDoble=(((feDoble -foDoble)**2)/feDoble)
    cPoker=(((fePoker -foPoker)**2)/fePoker)
    cQuintilla=(((feQuntilla -foQuntilla)**2)/feQuntilla)

    print(cDis,cPar,cPierna,cFull,cDoble,cPoker,cQuintilla)
    ct = cDis+cPar+cPierna+cFull+cDoble+cPoker+cQuintilla

    print("X^2 = ",ct)
    alfa = 0.05

    valorTabla = st.chi2.ppf(1-alfa,6)
    print("valor tabla para alfa:", alfa ,"y grados de libertad:", 6, " = ",valorTabla)
    if (ct <= valorTabla): #Nivel de confianza y grados de libertad
        print('Se acepta la hipotesis, son numeros aleatorios')
    else:
        print('No se acepta la hipotesis')

#--------MENU-------

def menu():

    print ("Selecciona una opción")
    print ("\t1 - Medio del Cuadrado")
    print ("\t2 - Test Chi Cuadrado GCL")
    print ("\t3 - Test de Corridas Arriba-Abajo de la Media")
    print ("\t4 - Test Autocorrelación")
    print ("\t5 - Poker")
    print ("\t6 - Comparar Generadores")



    print ("\t9 - salir")


#-----------------------GCL-----------------------
#Siempre inicio con la generacíon de los números para todos los test

def GCL(mod,semilla,cantidadGenerada,a,c):
    '''Generador gcl
    Parametros: mod,semilla,cantidadGenerada
    '''
    listaAleatoria = []
    N = semilla
    for i in range (cantidadGenerada):
        N = (((a)* N + c) % mod)
        listaAleatoria.append(N)      
    return (listaAleatoria)

#-------------Pedir número a random.org---------
def randomorg_test(cant, min, max):                                   # Test with Random.org numbers
    '''cantidad, min, max'''
    data = {                                                        # Objeto JSON enviado a random.org para solicitar los numeros aleatorios
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "5c256795-b0b4-44bb-a418-7323d45a388b",       # API Key generada para un usuario de random.org. Es gratis.
            "n": cant,                                              # Cantidad de numeros solicitados
            "min": min,                                               # Numero minimo
            "max": max,                                              # Numero maximo
            "replacement": True
        },
        "id": 42
    }
    r = requests.post('https://api.random.org/json-rpc/2/invoke2', json=data)
    # print("Codigo de respuesta solicitud HTTP: " + str(r.status_code))
    my_JSON = r.json()
    my_data = my_JSON["result"]["random"]["data"]
    my_data_array = np.asarray(my_data)

    data = my_data_array/max 
    return data


#k > 100!! cantidad de subintervalos
#n/k > 5 n = cantidad de numeros
#alfa es el margen de error

mod = 2**32 #poner el valor maximo + 1
n = 5000
k = 101
salto = 1/k
alfa = 0.05
semilla = 3298876

numeros = np.array(GCL(mod,semilla,n,134775813,1))/(mod-1)
#numeros = randomorg_test(n,0,99999)


 
while True:

    menu()

    opcionMenu = input("Inserta un numero valor >> ")

    if opcionMenu=="1":
        MedioCuadrado(semilla,n)
        input("Pulsa una tecla para continuar")
    elif opcionMenu=="2":
        chi2()
        input("Pulsa una tecla para continuar")
    elif opcionMenu=="3":
        corridas()
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu=="4":
        autocorrelacion()
        input("Pulsa una tecla para continuar")
    elif opcionMenu=="5":
        compararGeneradores()
        input("Pulsa una tecla para continuar")
    elif opcionMenu=="6":
        poker()
        input("Pulsa una tecla para continuar")    
    elif opcionMenu=="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")