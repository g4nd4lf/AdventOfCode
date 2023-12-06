import pandas as pd
import numpy as np
#f = open("id4pru.txt", "r")
f = open("input_day4.txt", "r")
input=f.read()
ilines=input.splitlines()
draw=ilines[0].split(",")
ilines.pop(0)
#ilines.pop(0)
print(draw)
cartones=[]
#k=0 #indice representativo del cartón
for i in range(0,len(ilines),6):
    carton=[]
    for j in range(i+1,i+6):
        linValue=ilines[j].split()
        linea=[]
        for k in range(0,len(linValue)):
            linea.append([linValue[k],0])
        carton.append(linea)
    cartones.append(carton)
ncols=len(cartones[2][0])
nrows=len(cartones[2])
cartonPremiado=False
cartonesPremiados=[]
for i in range(0,len(draw)):
    print(draw[i])
    #marcar numero en los cartones
    m=0
    for c in cartones:
        m+=1
        for j in range(0,nrows):
            lineasMarcadas=0
            for k in range(0,ncols):
                if(draw[i]==c[j][k][0]):
                    c[j][k][1]=1
                lineasMarcadas+=c[j][k][1]
            if(lineasMarcadas==5):
                print("Cartón premiado: ")
                print(c)
                print("Linea premiada:")
                print(c[j])
                cartonPremiado=True
        #Para encontrar columnas marcadas:
        for k in range(0,ncols):
            columnasMarcadas=0
            for j in range(0,nrows):
                columnasMarcadas+=c[j][k][1]
            if (columnasMarcadas==5):
                print("Cartón premiado: ")
                print(m)
                print(c)
                print("Columna premiada:")
                print(str(k))
                cartonPremiado=True
        if (cartonPremiado):
            cartonesPremiados.append(m)
            print("Fin de la partida")
            print("Final score:")
            suma=0
            for j in range(0,nrows):
                for k in range(0,ncols):
                    if(c[j][k][1]==0):
                        suma+=int(c[j][k][0])
            print(suma)
            print(draw[i])
            print(suma*int(draw[i]))
            print(c)
            break
    if (cartonPremiado):
        break

#PARTE 2: encontrar el último carton en ganar: