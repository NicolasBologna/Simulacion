

def NumerosIgualesPornumero(listaaleatoria, todos):
    for t in (listaaleatoria):
        c1=''
        lista = [0] * 10
        for numero in range (0,10):
            lista[numero]=t.count(str(numero))
        for l in range (len(lista)):
            if (lista[l] == 1):
                for k in range(l+1, len(lista)):
                    if (lista[k] == 1):
                        for j in range(k + 1, len(lista)):
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
                    elif(lista[k]==2):
                        for n in range (k+1, len(lista)):
                            if (lista[n]== 1):
                                c1 ='Un Par'
                            elif(lista[n]==2):
                                c1='Doble Par'
                    elif(lista[k]== 3):
                        c1='Pierna'
                    elif(lista[k]== 4):
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
                for k in range(l+1, len(lista)):
                    if (lista[k] == 1):
                        c1='Pierna'
                    elif(lista[k] == 2):
                        c1 = 'Par y Pierna'
            elif (lista[l] == 4):
                c1='Poker'
            elif (lista[l] == 5):
                c1= 'Quintilla'
        todos.append(c1)
    return todos

def Poker(todos,m):
    #Frecuencia esperada de cada jugada
    feDis=0.3024 * m
    fePar=0.5040 * m
    fePierna=0.072 * m
    feFull= 0.0090 * m
    feDoble=0.1080 * m
    fePoker= 0.0045 * m
    feQuntilla= 0.0001 *m

    #Frecuencia Observada de cada jugada
    foDis= (todos.count('Distintos'))
    foPar= (todos.count('Un Par'))
    foPierna= (todos.count('Pierna'))
    foFull= (todos.count('Par y Pierna'))
    foDoble= (todos.count('Doble Par'))
    foPoker= (todos.count('Poker'))
    foQuntilla= (todos.count('Quintilla'))

    #Calculo Poker
    cDis= (((feDis -foDis)**2)/feDis)
    cPar=(((fePar -foPar)**2)/fePar)
    cPierna=(((fePierna -foPierna)**2)/fePierna)
    cFull=(((feFull -foFull)**2)/feFull)
    cDoble=(((feDoble -foDoble)**2)/feDoble)
    cPoker=(((fePoker -foPoker)**2)/fePoker)
    cQuintilla=(((feQuntilla -foQuntilla)**2)/feQuntilla)

    ct = cDis+cPar+cPierna+cFull+cDoble+cPoker+cQuintilla
    if (ct <= st.chi2.ppf(0.95,6)): #Nivel de confianza y grados de libertad
        print('Se acepta la hipotesis, son numeros aleatorios')
    else:
        print('No se acepta la hipotesis')