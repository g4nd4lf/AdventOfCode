import os,sys
import math
import numpy as np
import pathlib
import re

#inputFile='input.txt'
inputFile='sample.txt'
def maxi(paths,maxi):
        maxp=[]
        for p in paths:
            coste, retorno = evalua2(p)
            if coste == maxi:
                print(p)
                maxp.append(p)
                break
        return maxp

def maxr(paths):
        maxret=0
        maxp=[]
        for p in paths:
            coste, retorno = evalua2(p)
            if retorno > maxret:
                print(p)
                maxp.append(p)
                maxret = retorno
        return maxp, retorno
def evalua2(camino):
    #['AADD', '00']
    coste=0
    retorno=0
    primero=True
    for i in range(len(camino[1])):
        if not primero:
            coste+=1
        else:
            primero=False
        if int(camino[1][i]):
            coste+=int(camino[1][i])
            nodo=camino2[0][i*2:i*2+2]
            retorno+=(30-coste)*valve[nodo]['flow']
    return coste, retorno
def isallopen(path):
    nodos=[x for x in valve if valve[x]["flow"]!=0]
    isopen=[False]*len(nodos)
    for j in range(len(nodos)):
        for i in range(len(camino2[1])):
            if path[0][i*2:i*2+2]==nodos[j] and int(path[1][i]):
                isopen[j]=True
    return all(isopen)


def evalua(camino):
    coste=0
    retorno=0
    primero=True
    for step in camino:
        if not primero:
            coste+=1
        else:
            primero=False
        if step[1]:
            coste+=step[1]
            valve[step[0]]['estado']=1
            retorno+=(30-coste)*valve[step[0]]['flow']
        
    return (coste,retorno)
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#Read input
with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.readlines()
    valve={}
    for l in lines:
        #Valve OJ has flow rate=0; tunnels lead to valves EW, IG
        name=l[6:8]
        flow = re.search('has flow rate=(.*); tunnel', l).group(1)
        neigS=re.search('lead[s]? to valve[s]? (.*)',l).group(1)
        neig=neigS.split(", ")
        #valve["name"]=name
        valve[name]={"estado":0,"flow":int(flow),"neig":neig}
        #print(valve,result.group(1),neig.group(1))
    #allopen=''.join([str(int(valve[x]["flow"]!=0)) for x in valve])
    camino=[("AA",0),("DD",1),("CC",0),("BB",1),("AA",0),("II",0),("JJ",1),("II",0),("AA",0),("DD",0),("EE",0),("FF",0),("GG",0),("HH",1),("GG",0),("FF",0),("EE",1),("DD",0),("CC",1)]
    camino2=["AADDCCBBAAIIJJIIAADDEEFFGGHHGGFFEEDDCC","0101001000000100101"]
    nodosFlow=[x for x in valve if valve[x]["flow"]!=0]
    nodosNoFlow=[x for x in valve if valve[x]["flow"]==0]
    nodos=[x for x in valve]
    coste, retorno = evalua(camino)
    coste2, retorno2 = evalua2(camino2)
    nodo="AA"
    paths=[]
    #startPath={"nodos":[("AA",0)],"time":0,"totFlow":0}
    startPath=["AA","0"]
    paths.append(startPath)
    previousPath=startPath
    ops=valve[nodo]["neig"]
    #paths=set()
    fin=False
    while(not fin):
        fin=True
        oldPaths=paths.copy()
        print(len(paths))
        for previousPath in paths:
            #nodo de partida:
            nodo=previousPath[0][-2:]
            #actualizamos estados:
            nodosi=[previousPath[0][i:i+2] for i in range(0, len(previousPath[0]), 2)]
            
            li=nodosi
            estados={}
            for x in nodos:
                estados[x]="0"
            for nod in nodosi:    
                estados[nod]=previousPath[1][len(li) - 1 - li[::-1].index(nod)]
            
            ops=valve[nodo]["neig"]
            for n in ops:
                #si flow=0 no abro valvula
                #si valvula abierta no la cierro
                #si valvula cerrada y flow!=0 puedo abrirla o no

                #newPath+=n
                if estados[n]=="0" and n not in nodosNoFlow:
                    for s in ["0","1"]:
                        newPath=previousPath.copy()
                        coste, retorno = evalua2(newPath)
                        if coste <30 and not isallopen(newPath):
                            newPath[0]+=n
                            newPath[1]+=s
                            estados[n]==s
                            fin=False
                            if newPath not in paths:
                                paths.append(newPath)
                else:
                    newPath=previousPath.copy()
                    coste, retorno = evalua2(newPath)
                    if coste <30 and not isallopen(newPath):
                        newPath[0]+=n
                        newPath[1]+="0"
                        fin=False
                        if newPath not in paths:
                            paths.append(newPath)
            paths.remove(previousPath)
        print(len(paths))
        if oldPaths==paths:
            fin=True
    print(newPath)
    print(coste,retorno)
    print(coste2,retorno2)

    
    