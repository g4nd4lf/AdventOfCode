import os,sys
import math
import numpy as np
import pathlib
import re
import time
from itertools import chain, combinations, permutations

#inputFile='input.txt'
inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#----------------------------------------------------------------
def mayor(r1,r2):
    return r1[0]>=r2[0] and r1[1]>=r2[1] and r1[2]>=r2[2] and r1[3]>=r2[3]
def reduceEstados(estadosAnt,b):
    #Cuanto mineral maximo necesito de cada uno para la proxima iteraccion:
    estados=estadosAnt.copy()
    # for e in estadosAnt:
    #     if e[1][0]>2*maxOre or e[1][1]>2*maxClay or e[1][2]>2*maxObs:
    #         if len(estados)>1:
    #             estados.remove(e)
    prevReducido=estados.copy()
    reducido=prevReducido.copy()
    hayIguales=True
    while hayIguales:
        reducido=prevReducido.copy()
        hayIguales=False
        for e1 in prevReducido:
            for e2 in prevReducido:
                if e1!=e2:
                    if e1[0]==e2[0]:
                        if mayor(e1[1],e2[1]):
                            hayIguales=True
                            if e2 in reducido:
                                reducido.remove(e2)
                        elif mayor(e2[1],e1[1]):
                            hayIguales=True
                            if e1 in reducido:
                                reducido.remove(e1)
                        #break
        prevReducido=reducido.copy()
    newReducido0=reducido.copy()
    # if any([x[1][1]>0 for x in reducido]):
    #     maxi=max([x[1][1] for x in reducido])
    #     for r in reducido:
    #         #if r[1][1]==0:
    #         if maxi//2>0:
    #             if r[1][1]<maxi//2:
    #                 newReducido0.remove(r)
    newReducido=newReducido0.copy()
    if any([x[1][2]>0 for x in newReducido0]):
        maxi=max([x[1][2] for x in newReducido0])
        for r in newReducido0:
            #if maxi//2>0:
                #if r[1][2]<maxi//2:
            if r[1][2]==0:
                newReducido.remove(r)
    newReducido2=newReducido.copy()
    if any([x[1][3]>0 for x in newReducido]):
        maxi=max([x[1][3] for x in newReducido])
        for r in newReducido:
            #if r[1][3]==0:
            #    newReducido2.remove(r)
            if r[1][3]<maxi:
                newReducido2.remove(r)
    return newReducido2
def creaRobots(id,num,estado,blueprint):
    #id: identificador del robot a crear
    #num: numero de robots de tipo id que vamos a crear
    #estado: [[robots],[recursos]]
    recursos=estado[1].copy()
    bpRobot=blueprint[id]
    recursosRestantes=[]
    for i in range(len(recursos)):
        resto=recursos[i]-num*bpRobot[i]
        if resto < 0:
            return estado
        else:
            recursosRestantes.append(resto)
    nuevoEstado=[estado[0].copy(),recursosRestantes]
    nuevoEstado[0][id]+=num
    return nuevoEstado

def enoughtResources(id,newe):
    print("a")
#------MAIN----------------------------------------------------------

with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.read().splitlines()
blueprints=[]
for l in lines:
    ore=[int(l.split("ore robot costs ")[1].split(" ore. Each clay")[0]),0,0,0]
    clay=[int(l.split("clay robot costs ")[1].split(" ore. Each obsidian")[0]),0,0,0]
    obsidian=[int(x) for x in [l.split("obsidian robot costs ")[1].split(" ore and ")[0],l.split("ore and ")[1].split(" clay")[0]]]+[0,0]
    geode=[int(x) for x in [l.split("geode robot costs ")[1].split(" ore and ")[0],"0",l.split("ore and ")[2].split(" obsidian")[0]]]+[0]
    blueprints.append([ore,clay,obsidian,geode])
geodas=[]
for b1 in blueprints:
    maxOre=max([x[0] for x in b1])
    maxClay=max([x[1] for x in b1])
    maxObs=max([x[2] for x in b1])
    maxis=[maxOre,maxClay,maxObs,10000]
    plans=[]
    resources=[0,0,0,0]
    robots=[1,0,0,0]
    print(blueprints)
    #recolectamos con los robots existentes:
    t=0
    nuevosEstados=[[robots,resources]]
    estados=[]
    robotsVistos=set()
    estadosVistos=set()
    while t<25:
        #robotsVistosSet=set()
        print("t",t)
        #para cada estado previo, calculamos posibles estados futuros
        #estados=nuevosEstados.copy()
        tp=tuple([(tuple(x[0]),tuple(x[1])) for x in nuevosEstados])
        estados={}
        for x in tp:
            if x[0] in estados:
                val1=[a*b for a,b in zip((x[1]),(1,10,100,10000))]
                val2=[a*b for a,b in zip(estados[x[0]],(1,10,100,10000))]
                if val1>val2:
                    estados[x[0]]=x[1]
            else:
                estados[x[0]]=x[1]
        if any([v[2]>0 for (k,v) in estados.items()]):
            estados = {k:v for (k,v) in estados.items() if v[2] > 0}
        if any([v[3]>0 for (k,v) in estados.items()]):
            maxi=max(v[3] for (k,v) in estados.items())
            estados = {k:v for (k,v) in estados.items() if v[3] >= maxi}

        for e in estados:
            print("estadosset",e)

        # if any([x[1][2]>0 for x in estados]):
        #     estados = [item for item in estados if item[1][2] > 0]
        # if any([x[1][3]>0 for x in estados]):
        #     maxi=max([x[1][3] for x in estados])
        #     estados = [item for item in estados if item[1][3] >= maxi]

        #estados=reduceEstados(nuevosEstados.copy(),b1)
        print("estados",len(estados))
        nuevosEstados=[]
        for e in estados:
            print(e)
            #robotsCreables=[int(x) for x in ]
            #calcular posibles estados a partir de e
            oldRobots=e[0].copy()
            resources=estados[e]
            #maximo numero de robots que se pueden fabricar de cada uno

            r0=int(resources[0]>=b1[0][0])
            r1=int(resources[0]>=b1[1][0])
            r2=int((resources[0]>=b1[2][0])*(resources[1]>=b1[2][1]))
            r3=int((resources[0]>=b1[3][0])*(resources[2]>=b1[3][3]))
            if t>18:
                r2=0
            robotsCreables=(r0,r1,r2,r3)
            ordenes=list(permutations([0,1,2,3]))
            for orden in ordenes:
                res=list(resources)
                rob=[]
                for o in orden:
                    if e[o]>maxis[o]:
                            continue
                    if op[o]: #and enoughtResources(o,op[o],newe,b1)
                        for i in range(len(res)):
                            resto=res[i]-b1[o][i]
                            if resto:
                                res[i]=b1[o][i]
                                rob.append(1)
                            else:
                                rob.append(0)
                                

                        



                        newe=creaRobots(o,numrobots[o],newe,b1)
            numrobots=[r0,r1,r2,r3]            
            #Si no fuera conveniente fabricar el maximo de robots, para ahorrar recursos...
            opciones=[]
            for i in range(r0+1):
                for j in range(r1+1):
                    for k in range(r2+1):
                        for l in range(r3+1):
                            # if t>18:
                            #     j=0
                            opciones.append([i,j,k,l])
            numrobots=[int(x>0) for x in numrobots]
            
            for op in opciones:
                
            
                ordenes=list(permutations([0,1,2,3]))
                for orden in ordenes:                    
                    newe=e.copy()
                    for o in orden:
                        if e[0][o]>maxis[o]:
                            continue
                        #Creamos los maximos robots o posibles y calculamos cuantos recuros nos sobran
                        #if numrobots[o]>0:
                        #    newe=creaRobots(o,numrobots[o],newe,b1)
                        if op[o]>0: #and enoughtResources(o,op[o],newe,b1)
                                newe=creaRobots(o,numrobots[o],newe,b1)
                        
                    #actuaizamos recursos:
                    newrobots=newe[0]
                    newresources=[]
                    for i in range(len(newe[1])):
                        newresources.append(newe[1][i]+oldRobots[i])
                    if [newrobots,newresources] not in nuevosEstados:
                        if str(newrobots) not in robotsVistos:
                            nuevosEstados.append([newrobots,newresources])
                            estadosVistos.add(str([newrobots,newresources]))
                            robotsVistos.add(str(newrobots))
                        else:
                            old=[eval(x) for x in estadosVistos if (x.split("], ")[0].split("]]")[0]+"]")[1:]==str(newrobots)][0]
                            if mayor(old[1],newresources):
                                continue
                            elif mayor(newresources,old[1]):
                                estadosVistos.remove(str(old))
                                estadosVistos.add(str([newrobots,newresources]))
                                nuevosEstados.append([newrobots,newresources])
        t+=1
    geodas.append(max([x[1][3] for x in estados]))            
    print(max([x[1][3] for x in estados]))
print(geodas)

#En cada turno:
#Calculo las combinaciones posibles de robots que puedo crear con los recursos disponibles
#Otra opcion es ver las formas posibles de repartir los recursos actuales entre los robots:
#Con [a, b, c] recursos
#Puedo crear r0 robots1, o r2 robots 2, o r3 robots 3 o r4 robots 4
# o una combinación de ellos
#El recurso a es comun a todos, el b y el c no
# Como mucho puedo crear b//r3 robots 3 y c//r4 robots 4
#-> 