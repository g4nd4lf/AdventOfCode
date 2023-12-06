import os,sys
import math
import numpy as np
import pathlib
import re
import time
from itertools import chain, combinations, permutations

inputFile='input.txt'
#inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#----------------------------------------------------------------
def mayor(r1,r2):
    return r1[0]>=r2[0] and r1[1]>=r2[1] and r1[2]>=r2[2] and r1[3]>=r2[3]

def creaRobot(id,res,rob,blueprint):
    #id: identificador del robot a crear
    #num: numero de robots de tipo id que vamos a crear
    #estado: [[robots],[recursos]]
    
    bpi=blueprint[id]
    recursosRestantes=[]
    for i in range(len(res)):
        resto=res[i]-bpi[i]
        if resto < 0:
            return [res,rob]
        else:
            recursosRestantes.append(resto)
    rob[id]+=1
    return recursosRestantes,rob

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
allEstados=[]
bnumber=0
#for b1 in [blueprints[11]]:
for b1 in blueprints:
    prohibidos=4*[False]
    bnumber+=1
    maxOre=max([x[0] for x in b1])
    maxClay=max([x[1] for x in b1])
    maxObs=max([x[2] for x in b1])
    maxis=[maxOre,maxClay,maxObs,10000]
    plans=[]
    resources=(0,0,0,0)
    robots=(1,0,0,0)
    #print(blueprints)
    #recolectamos con los robots existentes:
    t=0
    nuevosEstados=[[robots,resources]]
    estados={(robots,resources[:-1]):0}
    while t<24:
        #print("t",t)
        #tp=tuple([(tuple(x[0]),tuple(x[1])) for x in nuevosEstados])

        #print("estados",len(estados))
        nuevosEstados=[]
        oldEstados=estados.copy()
        for est,g in oldEstados.items():
            #print(e)
            #robotsCreables=[int(x) for x in ]
            #calcular posibles estados a partir de e
            robots=est[0]
            resources=est[1]
            #maximo numero de robots que se pueden fabricar de cada uno

            r0=int(resources[0]>=b1[0][0])
            r1=int(resources[0]>=b1[1][0])
            r2=int((resources[0]>=b1[2][0])*(resources[1]>=b1[2][1]))
            r3=int((resources[0]>=b1[3][0])*(resources[2]>=b1[3][2]))
            #if t>18:
            #    r2=0
            robotsCreables=[r0,r1,r2,r3]
            for i in range(len(robotsCreables)):
                if prohibidos[i]:
                    robotsCreables[i]=0
            ordenes=list(permutations([0,1,2,3]))
            for orden in ordenes:
                res=list(resources).copy()
                rob=list(robots).copy()
                for o in orden:
                    #if resources[o]>maxis[o]:
                     #   continue
                    #el
                    if robotsCreables[o]: #and enoughtResources(o,op[o],newe,b1)
                        res,rob=creaRobot(o,res,rob,b1)
                        #print(t,res,rob)
                        alo=0
                        break
                for i in range(len(res)):
                    res[i]+=robots[i]
                nuevoEstado=(tuple(rob),tuple(res))
                robotsVistos=[x[0] for x in oldEstados]
                #if nuevoEstado not in estados:
                if nuevoEstado[0] not in robotsVistos:
                    estados[nuevoEstado]=g+robots[-1]
                else:
                    if nuevoEstado not in estados or (nuevoEstado in estados and estados[nuevoEstado]<=g+robots[-1]):
                        val1=sum([a*b for a,b in zip((nuevoEstado[1]),(1,1,100))])
                        rec2=[x for x in estados if x[0]==nuevoEstado[0]][0]
                        val2=sum([a*b for a,b in zip(rec2[1],(1,1,100))])
                        if (val1>val2):                        
                            if(estados[rec2])==0:
                                del(estados[rec2])
                            estados[nuevoEstado]=g+robots[-1]
                        elif (val1==val2):
                            if(estados[rec2])<g+robots[-1]:
                                estados[nuevoEstado]=g+robots[-1]
                #Si decido no construir robores:
                #if nuevoEstado[0][-1]>
                res=list(resources)
                rob=list(robots)
                for i in range(len(res)):
                    res[i]+=robots[i]
                nuevoEstado=(tuple(rob),tuple(res))
                robotsVistos=[x[0] for x in oldEstados]
                if nuevoEstado[0] not in robotsVistos:
                    estados[nuevoEstado]=g+robots[-1]
                else:
                    if nuevoEstado not in estados or (nuevoEstado in estados and estados[nuevoEstado]<=g+robots[-1]):
                        val1=sum([a*b for a,b in zip((nuevoEstado[1]),(1,1,100))])
                        rec2=[x for x in estados if x[0]==nuevoEstado[0]][0]
                        val2=sum([a*b for a,b in zip(rec2[1],(1,1,100))])    
                        if (val1>val2):                        
                            if(estados[rec2])==0:
                                del(estados[rec2])
                            estados[nuevoEstado]=g+robots[-1]
                        elif (val1==val2):
                            estados[nuevoEstado]=g+robots[-1]
                        elif (rec2[0][-1]>0):
                            estados[nuevoEstado]=g+robots[-1]
                    

                #if nuevoEstado not in estados:
                #    estados[nuevoEstado]=g
                # else:
                #     val1=sum([a*b for a,b in zip((nuevoEstado[1]),(1,1,100,10000))])
                #     val2=sum([a*b for a,b in zip(estados[nuevoEstado[0]],(1,1,100,10000))])
                #     if (val1>=val2):
                # #      #print(val1,val2,val1>val2)
                #         estados[nuevoEstado[0]]=nuevoEstado[1]
                
                    #else:
                    #    print(val1,val2,val1>val2)
            #print("-")
        estadosBrutos=estados.copy()
        for e in estadosBrutos:
            for i in range(3):
                deficit = maxis[i] - e[0][i]
                max_useful_quantity = maxis[i] + deficit * (25-t)
                if e[1][i]>max_useful_quantity:
                    prohibidos[i]=True
#                    if e in estados and e[0][-1]==0 and e[0][-2]==0:
#                        del estados[e]
            
        #print(t,len(estados))
        t+=1
        allEstados.append([(k,v) for (k,v) in estados.items()])

    geodas.append(max([v for (_,v) in estados.items()]))            
    #m1=max([v[3] for (k,v) in estados.items()])
    #m2=max([x[1][3] for x in allEstados[-1]])
    #print(m1,m2)

print(geodas,sum([geodas[i]*(i+1) for i in range(len(geodas))]))
