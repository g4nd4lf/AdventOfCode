import os,sys
import math
import numpy as np
import pathlib
import re

inputFile='input.txt'
#inputFile='sample.txt'
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
def retorno(camino,valve):
    retorno=0
    for c in camino[1:]:
        retorno +=(30-c[1])*valve[c[0]]['flow']
    return retorno
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
#print(retorno([['AA', 0], ['DD', 1], ['CC', 2], ['BB', 3], ['JJ', 6], ['EE', 10], ['HH', 13]],valve))

vecinos={}
for v1 in valve:
    vecinos[v1]=[]
    for v2 in valve:
        if v2!=v1 and valve[v2]["flow"]!=0:
            sp=shortest(valve,v1,v2)
            valve[v1][v2]=len(sp[1:])+1
            vecinos[v1].append(v2)

nodosFlow=[x for x in valve if valve[x]["flow"]!=0]
nodosNoFlow=[x for x in valve if valve[x]["flow"]==0]
valvulasUtiles=len(nodosFlow)
nodos=[x for x in valve]
#coste, retorno = evalua(camino,valve)
#coste2, retorno2 = evalua2(camino2)
nodo="AA"
paths=[]
finalistas=[]
#startPath={"nodos":[("AA",0)],"time":0,"totFlow":0}
paths=[]
startPath=[["AA",0]] #el primer elemento es el nodo actual, y el segundo el coste hasta ese punto
paths.append(startPath)
#previousPath=startPath
#ops=valve[nodo]["neig"]
#paths=set()
fin=False

estados={}
for v in valve:
    estados[v]=0

while(len(paths)>0):
    for previousPath in paths:
        #nodo de partida:
        nodo=previousPath[-1][0]
        coste=previousPath[-1][1]
        #actualizamos estados:
        #nodosPreviousPath=[x[0] for x in previousPath]
        visited=[x[0] for x in previousPath]
        visitables=[vec for vec in vecinos[nodo] if vec not in visited]
        for vec in visitables:
            #estados[vec]=1            
            newPath=previousPath.copy()        
            newCost=valve[nodo][vec]+coste
            newPath.append([vec,newCost])
            if newCost<30 and len(newPath)<valvulasUtiles+1:
                paths.append(newPath)
            if len(newPath)==valvulasUtiles+1 or newCost==30:
                finalistas.append(newPath)
            if newCost>30:
                finalistas.append(previousPath)
            print(len(paths),len(finalistas))
        paths.remove(previousPath)
maxRet=0
maxP=[]
for f in finalistas:
    ret=retorno(f,valve)
    if ret>maxRet:
        maxRet=ret
        maxP=f
print(maxRet,maxP)

    
    