import os,sys
import math
import numpy as np
import re
import time
from itertools import chain, combinations, permutations
import os,pathlib
from itertools import cycle

#inputFile='sample.txt'
inputFile='input.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
roadmap={}
def gira(estado,rot):
    if rot=="R":
        newOr=estado[2]+1
    elif rot=="L":
        newOr=estado[2]-1
    if newOr>3:
        newOr=0
    elif newOr<0:
        newOr=3
    return (estado[0],estado[1],newOr)

def avanza(estado,m):
    if estado[2]==0: # >
        fila=[x for x in roadmap if x[0]==estado[0]]
        recta=[x for x in fila if x[1]>=estado[1]]
        obstaculos=[x for x in recta if roadmap[x]==1]
        if len(obstaculos)>0:
            obstaculo=min(obstaculos)
        else:
            obstaculo=(0,10000)
        maxrecta=max(recta)[1]
        tope=min(estado[1]+m,maxrecta,obstaculo[1]-1)
        if tope==maxrecta and tope!=estado[1]+m:
            oldx=estado[1]
            newy=min(fila)[1]
            if roadmap[(estado[0],newy)]:
                return (estado[0],max(fila)[1],estado[2])
            estado=(estado[0],newy,estado[2])
            return avanza(estado,m-(tope-oldx)-1)
        else:
            return (estado[0],tope,estado[2])
    elif estado[2]==1: # v
        columna=[x for x in roadmap if x[1]==estado[1]]
        recta=[x for x in columna if x[0]>=estado[0]]
        obstaculos=[x for x in recta if roadmap[x]==1]
        if len(obstaculos)>0:
            obstaculo=min(obstaculos)
        else:
            obstaculo=(10000,0)
        if len(recta)>0:
            maxrecta=max(recta)[0]
        else:
            maxrecta=estado[0]
        tope=min(estado[0]+m,maxrecta,obstaculo[0]-1)
        if tope==maxrecta and tope!=estado[0]+m:
            oldy=estado[0]
            newx=min(columna)[0]
            if roadmap[(newx,estado[1])]:
                return (max(columna)[0],estado[1],estado[2])
            estado=(newx,estado[1],estado[2])
            return avanza(estado,m-(tope-oldy)-1)
        else:
            return (tope,estado[1],estado[2])
    elif estado[2]==2: # <
        fila=[x for x in roadmap if x[0]==estado[0]]
        recta=[x for x in fila if x[1]<=estado[1]]
        obstaculos=[x for x in recta if roadmap[x]==1]
        if len(obstaculos)>0:
            obstaculo=max(obstaculos)
        else:
            obstaculo=(0,-10)
        minrecta=min(recta)[1]
        tope=max(estado[1]-m,minrecta,obstaculo[1]+1)
        if tope==minrecta and tope!=estado[1]-m:
            oldx=estado[1]
            newy=max(fila)[1]
            if roadmap[(estado[0],newy)]:
                return (estado[0],min(fila)[1],estado[2])
            estado=(estado[0],newy,estado[2])
            
            return avanza(estado,m-(oldx-tope)-1)
        else:
            return (estado[0],tope,estado[2])
    elif estado[2]==3: # ^
        columna=[x for x in roadmap if x[1]==estado[1]]
        recta=[x for x in columna if x[0]<=estado[0]]
        obstaculos=[x for x in recta if roadmap[x]==1]
        if len(obstaculos)>0:
            obstaculo=max(obstaculos)
        else:
            obstaculo=(-10,0)
        minrecta=min(recta)[0]
        tope=max(estado[0]-m,minrecta,obstaculo[0]+1)
        if tope==minrecta and tope!=estado[0]-m:
            oldy=estado[0]
            newx=max(columna)[0]
            if roadmap[(newx,estado[1])]:
                return (min(columna)[0],estado[1],estado[2])
            estado=(newx,estado[1],estado[2])
            return avanza(estado,m-(oldy-tope)-1)
        else:
            return (tope,estado[1],estado[2])
with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.read().splitlines()
cubo={
    ()

}
leePath=False
for i,l in enumerate(lines[:lines.index("")]):
    for j,c in enumerate(l):
        if c==".":
            roadmap[(i,j)]=0
        elif c=="#":
            roadmap[(i,j)]=1
    print(l)
print("-------------PATH-------------------")
#Leer path:
path=lines[lines.index("")+1]
print(path)
#punto de origen: (i para las filas y j para las columnas)
oi=0
oj=min([x[1] for x in roadmap if x[0]==oi])
movs=re.split(r"[RL]",path)
rot=re.findall(r"[RL]",path)
estado=(oi,oj,0)
print("origen:",oi,oj)

for i,m in enumerate(movs):
    estado=avanza(estado,int(m))
    if i<len(rot):
        estado=gira(estado,rot[i])
    print(i,estado)
print("Final:",estado)
resultado=(estado[0]+1)*1000+(estado[1]+1)*4+estado[2]
print("result:",resultado)
    # name=l.split(":")[0]
    # yell=l.split(":")[1].strip()
    # if yell.isdigit():
    #     monkeys[name]=int(yell)
    # else:
    #     monkeys[name]=tuple(yell.split(" "))
#pru=avanza(estado,10)
#print(pru)
print("fin") 