import os,sys
import math
import numpy as np
import pathlib
import re

#inputFile='input.txt'
inputFile='sample.txt'
def bfs(graph, S, D):
    queue = [(S, [S])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex]["neig"] - set(path):
            if next == D:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest(graph, S, D):
    try:
        return next(bfs(graph, S, D))
    except StopIteration:
        return None

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
            coste, retorno = evalua(p)
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
    #newvalve={}
    isopen=[False]*len(nodos)
    for j in range(len(nodos)):
        #newValve[nodos[j]]=0
        for i in range(len(path)):
            if path[i][0]==nodos[j] and int(path[i][1]):
                isopen[j]=True
    return all(isopen)

def evalua(camino,valve):
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
            #valve[step[0]]['estado']=1
            retorno+=(30-coste)*valve[step[0]]['flow']
    return (coste,retorno)

#print(evalua([['AA', 0], ['BB', 0], ['CC', 1], ['DD', 1], ['AA', 0], ['BB', 0], ['AA', 0], ['BB', 0], ['AA', 0], ['BB', 0], ['AA', 0], ['DD', 0], ['EE', 0], ['DD', 0], ['AA', 0], ['BB', 0], ['AA', 0], ['DD', 0], ['EE', 0], ['FF', 0], ['EE', 0], ['DD', 0], ['EE', 0]]),valve)
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
        valve[name]={"estado":0,"flow":int(flow),"neig":set(neig)}
        #print(valve,result.group(1),neig.group(1))
    #allopen=''.join([str(int(valve[x]["flow"]!=0)) for x in valve])
    camino=[("AA",0),("DD",1),("CC",0),("BB",1),("AA",0),("II",0),("JJ",1),("II",0),("AA",0),("DD",0),("EE",0),("FF",0),("GG",0),("HH",1),("GG",0),("FF",0),("EE",1),("DD",0),("CC",1)]
    isallopen(camino)

    camino2=["AADDCCBBAAIIJJIIAADDEEFFGGHHGGFFEEDDCC","0101001000000100101"]
    nodosFlow=[x for x in valve if valve[x]["flow"]!=0]
    nodosNoFlow=[x for x in valve if valve[x]["flow"]==0]
    nodos=[x for x in valve]
    coste, retorno = evalua(camino,valve)
    coste2, retorno2 = evalua2(camino2)
    nodo="AA"
    paths=[]
    finalistas=[]
    #startPath={"nodos":[("AA",0)],"time":0,"totFlow":0}
    paths=[]
    startPath=[["AA",0]] #el primer elemento es el nodo actual y el segundo indica si accionamos  la valvula(1) o la dejamos como está (0)
    paths.append(startPath)
    #previousPath=startPath
    #ops=valve[nodo]["neig"]
    #paths=set()
    fin=False
    maxRet=0
    while(len(paths)>0):
        #fin=True
        #oldPaths=paths.copy()
        #print(len(paths))
        for previousPath in paths:
            if isallopen(previousPath):
                finalistas.append(previousPath)
                coste,retorno=evalua(previousPath,valve)
                if retorno>maxRet:
                        maxRet=retorno
                paths.remove(previousPath)
                continue
            #nodo de partida:
            nodo=previousPath[-1][0]
            #actualizamos estados:
            #nodosPreviousPath=[x[0] for x in previousPath]
            for v in valve:
                valve[v]["estado"]=0
            for p in previousPath:
                if p[1]==1:
                    #print(p)
                    valve[p[0]]["estado"]=1
                
            #buscamos vecinos:
            neigs=valve[nodo]["neig"]
            #buscamos caminos más cortos a valvulas sin abrir:
            destinos=[]
            for v in valve:
                if not valve["estado"] and valve["flow"]!=0:
                    destinos.append(v)
            newPaths=[]
            for d in destinos:
                sp=shortest(valve,n,d)
                newPathAdd=[[x,0] for x in sp]
                newPathAdd[-1][1]=1
                newPaths.append(newPathAdd)
            for p in newPaths:
                newPath=previousPath+p
                if isallopen(newPath):
                    finalistas.append(previousPath)
                    coste,retorno=evalua(previousPath,valve)
                    if retorno>maxRet:
                        maxRet=retorno
                else:
                    paths.add(newPath)
            paths.remove(previousPath)

            #creamos las posibles nuevas formas de aumentar el path previo:
            for n in neigs:
                #si flow=0 no abro valvula
                #si valvula abierta no la cierro
                #si valvula cerrada y flow!=0 puedo abrirla o no
                actions=[0,1]
                if valve[n]["flow"]==0 or valve[n]["estado"]==1:
                    actions=[0]
                if len(previousPath)>1:
                    if previousPath[-1][1]==0 and previousPath[-2][0]==n:
                        continue
                for a in actions:
                    newPath=previousPath.copy()
                    if a==1:
                        valve[n]["estado"]=1
                    coste, retorno = evalua(newPath,valve)
                    
                    if coste <30 and not isallopen(newPath): #si no se cumple esto no tiene sentido seguir aumentando el camino
                        newPath.append([n,a])
                        if newPath not in paths and newPath not in finalistas:
                            paths.append(newPath)
                            print(coste,retorno,len(paths),len(finalistas),maxRet)
                            fin=False #Como acabamos de agrandar un camino, significa qeu no hemos acabado aún
            if previousPath not in finalistas:
                paths.remove(previousPath)
        #print(len(paths))
        if oldPaths==paths:
            fin=True
    #print(newPath)
    #print(coste,retorno)
    #print(coste2,retorno2)
    print(maxRet)

    
    