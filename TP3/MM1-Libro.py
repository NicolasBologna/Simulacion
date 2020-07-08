import sys
import numpy as np
import statistics
import matplotlib.pyplot as plt

from MM1Utiles import funExpon

#README
#Criterio de estabilidad MM1: la tasa de servicio debe ser mayor que la tasa de llegada

NumEvents = 2 #Defimos número de tipos de eventos (usamos 2: arribos y llegadas)

#Constantes a usar para entender mejor el código
BUSY = 1 
IDLE = 0

QLIMIT = 10**5 #Hay que probar cambiando

def Report():
    global NumCustsDelayed
    AvgDelayInQ = TotalOfDelays/NumCustsDelayed
    AvgNumInQ = AreaNumInQ/Time
    ServerUtilization = AreaServerStatus/Time
    '''print("Promedio de espera en la cola: ",round(AvgDelayInQ,3)," minutos.")
    print("Promedio de largo de la cola: ",round(AvgNumInQ,3)," clientes.")
    print("Utilización del servidor: ",round(ServerUtilization,3))
    print("Tiempo de finalización: ",round(Time,3))'''
    return [AvgNumInQ,AvgDelayInQ, ServerUtilization]


def Initialize():
    global MeanInterarrival, Time, TimeNextEvent, ServerStatus, NumCustsDelayed, TotalOfDelays, AreaNumInQ, AreaServerStatus, NextEventType, NumDelaysRequired, NumInQ, MeanService, TimeLastEvent, TimeArrival
    Time = 0

    ServerStatus = IDLE

    #variables enteras
    NextEventType = 0
    NumCustsDelayed = 0
    NumInQ = 0 #número de clientes en cola
    ServerStatus = 0

    #variables reales
    AreaNumInQ = 0 #área debajo de la función número de clientes en cola
    AreaServerStatus = 0
    Time = 0
    TimeLastEvent = 0 #tiempo del último evento que cambió el número en cola
    TotalOfDelays = 0 #número de clientes que completaron sus demoras

    #arrays
    TimeArrival = np.zeros([QLIMIT+1])
    TimeNextEvent = np.zeros([NumEvents+1]) #arreglo que contiene el tiempo del próximo evento I en la posición TimeNextEvent[I]


    TimeNextEvent[1] = Time + funExpon(1/MeanInterarrival)
    TimeNextEvent[2] = 10**30

def Timing():
    global Time, NextEventType

    MinTimeNextEvent = 10**29
    NextEventType = 0

    for i in range(1,NumEvents+1):
        if TimeNextEvent[i] < MinTimeNextEvent:
            MinTimeNextEvent = TimeNextEvent[i]
            NextEventType = i

    if (NextEventType > 0):
        Time = TimeNextEvent[NextEventType]
    else:
        print("La lista de eventos está vacía en el momento: ", Time, " NextEventType == 0, error en timing")
        sys.exit()
        
def Arrive():
    global ServerStatus,TimeArrival, TotalOfDelays, NumCustsDelayed, TimeNextEvent, NumInQ, MeanService
    TimeNextEvent[1] = Time + funExpon(1/MeanInterarrival)
    #print("arribo")
    if ServerStatus == BUSY:    
        NumInQ += 1   
        if NumInQ > QLIMIT:
            print("se excedió la cantidad máxima de usuarios en cola en el momento: ", Time)
        TimeArrival[NumInQ] = Time
        
    else:
        Delay = 0
        TotalOfDelays = TotalOfDelays + Delay
    
        NumCustsDelayed = NumCustsDelayed + 1

        ServerStatus = BUSY

        TimeNextEvent[2] = Time + funExpon(1/MeanService)
    
def Depart():
    global NumInQ, TotalOfDelays,NumCustsDelayed, ServerStatus, TimeNextEvent, Time, TimeArrival
    if (NumInQ == 0):
        ServerStatus = IDLE
        TimeNextEvent[2] = 10**30
    else:
        NumInQ = NumInQ - 1

        Delay = Time - TimeArrival[1]
        TotalOfDelays = TotalOfDelays + Delay

        NumCustsDelayed += 1
        TimeNextEvent[2] = Time + funExpon(1/MeanService)

        for I in range(1,NumInQ+1):
            TimeArrival[I] = TimeArrival[I+1]

def UpdateTimeAvgStats():
    global TimeLastEvent, AreaNumInQ, AreaServerStatus, Time
    TimeSinceLastEvent = Time - TimeLastEvent
    TimeLastEvent = Time

    AreaNumInQ = AreaNumInQ + NumInQ * TimeSinceLastEvent

    AreaServerStatus = AreaServerStatus + ServerStatus * TimeSinceLastEvent

def ExecuteSimulation():
    global NumCustsDelayed, NumDelaysRequired
    Initialize()
    while(NumCustsDelayed < NumDelaysRequired):
        Timing()
        UpdateTimeAvgStats()
        #print(NumCustsDelayed)
        if (NextEventType == 1):
            Arrive()
        elif (NextEventType == 2):
            Depart()
        else:
            print ("Error in NextEventType, Value =  ",NextEventType)

    return Report()

if __name__ == '__main__':
    global MeanInterarrival, MeanService, NumDelaysRequired
    MeanInterarrival = 5.9 #tiempo medio de llegada **lambda
    MeanService = 6 #tiempo medio de servicio **MU
    NumDelaysRequired = 10000 #número total de clientes cuyas demoras serán observadas

    '''print("Mean Interarrival")
    MeanInterarrival = float(input())
    print("Mean Service")
    MeanService = float(input())
    print("Number delays Required")
    NumDelaysRequired = float(input())'''

    print("Mean Interarrival: ",MeanInterarrival,"Mean Service: ",MeanService,"Number delays Required (cuantas personas  ): ", NumDelaysRequired)

    #Valores teóricos
    promedio_clientes_en_cola = (MeanInterarrival**2)/(MeanService*(MeanService-MeanInterarrival))
    promedio_demora_en_cola = MeanInterarrival/(MeanService*(MeanService-MeanInterarrival))
    promedio_utilizacion_servidor = MeanInterarrival/MeanService

    print(promedio_clientes_en_cola, "  ",promedio_demora_en_cola, "  ", promedio_utilizacion_servidor)

    clientes_en_cola = []
    demora_en_cola = []
    utilizacion_servidor = []

    n = 250
    for i in range(n):
        rta = ExecuteSimulation()
        clientes_en_cola.append(rta[0])
        demora_en_cola.append(rta[1])
        utilizacion_servidor.append(rta[2])

    lista_clientes_en_cola = []
    lista_demora_en_cola = []
    lista_utilizacion_servidor = []

    for i in range(n):
        clientes_en_cola_i = statistics.mean(clientes_en_cola[:i+1])
        lista_clientes_en_cola.append([i,clientes_en_cola_i])
        demora_promedio_i = statistics.mean(demora_en_cola[:i+1])
        lista_demora_en_cola.append([i,demora_promedio_i])
        utilizacion_servidor_i = statistics.mean(utilizacion_servidor[:i+1])
        lista_utilizacion_servidor.append([i,utilizacion_servidor_i])

    plt.title('Número promedio de clientes en cola') 
    x1, y1 = zip(*[m for m in lista_clientes_en_cola])
    p1 = plt.plot(x1, y1, markersize=1, lw=1,color='r')
    plt.plot([promedio_clientes_en_cola for i in range(n)], linestyle='dashed', color='blue')
    plt.grid(True)
    plt.show()

    x, y = zip(*[m for m in lista_demora_en_cola])
    plt.title('Número promedio de demora en cola') 
    plt.plot(x, y, markersize=1, lw=1,color='b')
    plt.plot([promedio_demora_en_cola for i in range(n)], linestyle='dashed', color='blue')
    plt.grid(True)
    plt.show()

    x, y = zip(*[m for m in lista_utilizacion_servidor])
    plt.title('Utilización promedio del servidor') 
    plt.plot(x, y, markersize=1, lw=1,color='g')
    plt.plot([promedio_utilizacion_servidor for i in range(n)], linestyle='dashed', color='blue')
    plt.grid(True)
    plt.show()