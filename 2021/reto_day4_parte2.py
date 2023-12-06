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
#print("1.len(cartones): ")
#print(len(cartones))
def echarPartida(bingo,premiados):
    cartonPremiado=False
    #cartonesPremiados=[]
    for i in range(0,len(draw)):
        #print(draw[i])
        #marcar numero en los cartones
        m=0
        for c in bingo:
            #print("premiados:")
            #print(premiados)
            if m not in premiados:
                #print(m)
                for j in range(0,nrows):
                    lineasMarcadas=0
                    for k in range(0,ncols):
                        if(draw[i]==c[j][k][0]):
                            c[j][k][1]=1
                        lineasMarcadas+=c[j][k][1]
                    if(lineasMarcadas==5):
                        # print("Cartón premiado: ")
                        # print(m)
                        # print(c)
                        # print("Linea premiada:")
                        # print(c[j])
                        cartonPremiado=True
                #Para encontrar columnas marcadas:
                for k in range(0,ncols):
                    columnasMarcadas=0
                    for j in range(0,nrows):
                        columnasMarcadas+=c[j][k][1]
                    if (columnasMarcadas==5):
                        # print("Cartón premiado: ")
                        # print(m)
                        # print(c)
                        # print("Columna premiada:")
                        # print(str(k))
                        cartonPremiado=True
                if (cartonPremiado):
                    #cartonesPremiados.append(m)
                    # print("Fin de la partida")
                    # print("Final score:")
                    suma=0
                    for j in range(0,nrows):
                        for k in range(0,ncols):
                            if(c[j][k][1]==0):
                                suma+=int(c[j][k][0])
                    # print(suma)
                    # print(draw[i])
                    # print(suma*int(draw[i]))
                    # print(c)
                    return(draw[i],m)
                    break
            m+=1
        if (cartonPremiado):
            break
cartonesPremiados=[]
for i in range(0,100):
    (num,premiado)=echarPartida(cartones,cartonesPremiados)
    # print("2.len(cartones): ")
    # print(len(cartones))

    # print("carton premiado: "+str(premiado))
    cartonesPremiados.append(premiado)
    #del cartones[premiado]
    # print("3.len(cartones): ")
    # print(len(cartones))

print(cartonesPremiados)
suma=0
cfinal=cartones[cartonesPremiados[-1]]
for j in range(0,nrows):
    for k in range(0,ncols):
        if(cfinal[j][k][1]==0):
            suma+=int(cfinal[j][k][0])
print(suma)
print(num)
print(suma*int(num))

#PARTE 2: encontrar el último carton en ganar: