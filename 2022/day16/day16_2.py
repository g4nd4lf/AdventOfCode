import os,sys
import math
import numpy as np
import pathlib
import re
minutes =26
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
        retorno +=(minutes-c[1])*valve[c[0]]['flow']
    return retorno
def retorno2(camino,valve):
    retorno=0
    for c in camino:
        retorno +=(minutes-c[1])*valve[c[0]]['flow']
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
longi=len(nodosFlow)//2+1
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
            if newCost<minutes and len(newPath)<valvulasUtiles+1:
                paths.append(newPath)
            #if len(newPath)==valvulasUtiles+1 or newCost==minutes:
            #if len(newPath)>=longi and newPath[-1][1]<=26:
            if newPath[-1][1]<=26:
                finalistas.append(newPath)
            #if newCost>minutes:
             #   finalistas.append(previousPath)
            print(len(paths),len(finalistas))
        paths.remove(previousPath)
maxRet=0
maxP=[]
newFin=[]
for f in finalistas:
    ret=retorno(f,valve)
    newFin.append([f[1:],ret])
    if ret>maxRet:
        maxRet=ret
        maxP=f
print(maxRet,maxP)

def Sort(sub_li):
    return(sorted(sub_li, key = lambda x: x[1]))  

newFin2=Sort(newFin)

maxP={}
for n in nodosFlow:
    maxP[n]=0
for f1 in newFin:
    for n in f1:
        ret=(minutes-n[1])*valve[n[0]]["flow"]
        if ret>maxP[n[0]]:
            maxP[n[0]]=ret
maxRetTot=0
candidatos=[]
mejor=[]
l=longi
i=0
for f1 in newFin:
    c1=[x[0] for x in f1]

    print(len(newFin)-i)
    i+=1
    for f2 in newFin:
        
        c2=[x[0] for x in f2]
        # if c1==["DD","HH","EE"] and c2==["JJ","BB","CC"]:
        #     r1=retorno2(f1[:l],valve)
        #     r2=retorno2(f2[:3],valve)
        #     print(r1+r2)
        #     print("encontrado")

        if len(set(c1).intersection(set(c2)))==0:

        #max1=set([n[0] for n in f1 if (minutes-n[1])*valve[n[0]]["flow"]==maxP[n[0]]])
        #max2=set([n[0] for n in f2 if (minutes-n[1])*valve[n[0]]["flow"]==maxP[n[0]]])
        #if len(max1.intersection(max2))==0:
            r1=retorno2(f1[:l],valve)
            r2=retorno2(f2[:l],valve)
            #r2=sum(maxP[x] for x in max2)
            candidatos.append([f1,f2,r1,r2])
            if r1+r2>maxRetTot:
                maxRetTot=r1+r2
                mejor=[f1,f2,maxRetTot]

print(maxRetTot)        
print(mejor)

f1=mejor[0]
f2=mejor[1]
c1=[x[0] for x in f1[:l]]
c2=[x[0] for x in f2[:l]]
if len(set(c1).intersection(set(c2)))==0:

#max1=set([n[0] for n in f1 if (minutes-n[1])*valve[n[0]]["flow"]==maxP[n[0]]])
#max2=set([n[0] for n in f2 if (minutes-n[1])*valve[n[0]]["flow"]==maxP[n[0]]])
#if len(max1.intersection(max2))==0:
    r1=retorno2(f1[:l],valve)
    r2=retorno2(f2[:l],valve)
    #r2=sum(maxP[x] for x in max2)
    candidatos.append([f1,f2,r1,r2])
    if r1+r2>maxRetTot:
        maxRetTot=r1+r2
        mejor=[f1,f2,maxRetTot]

#Solucion sample _2
#Elephant:DD,HH,EE
#Me:JJ,BB,CC

#part 1 (['FC', 'SJ', 'IG', 'EW', 'WC', 'JF'], 1871)
#part 2 ((['ZD', 'RL'], 719), (['FC', 'SJ', 'IG', 'EW', 'WC', 'JF'], 1447), 2166)

solpath1=[['AA',0],['ZD', 3], ['RL', 6]]
solpath2=[['AA',0],['FC', 3], ['SJ', 6], ['IG', 10], ['EW', 13], ['WC', 16], ['JF', 19]]
solpath1b=[['ZD', 3], ['RL', 6]]
solpath2b=[['FC', 3], ['SJ', 6], ['IG', 10], ['EW', 13], ['WC', 16], ['JF', 19]]
print(retorno2(solpath1b,valve),retorno2(solpath2b,valve))

sol1=['ZD', 'RL']
sol2=['FC', 'SJ', 'IG', 'EW', 'WC', 'JF']
maxpru=0
maxf=[]
for f in newFin:
    nods=[x[0] for x in f]
    if nods[:2]==sol1 and len(set(sol2).intersection(set(nods)))==0:
        ret=retorno2(f,valve)
        if ret>maxpru:
            maxpru=ret
            maxf=f
    if nods==sol2:
        print(f)

print(maxf)
print(maxpru)

nodsFin=[]
for f in newFin:
    nodsFin.append([x[0] for x in f])


def complement(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)==0

parejas=[]
comps=0
for f1 in nodsFin:
    for f2 in nodsFin:
        if complement(f1,f2):
            comps+=1
            #parejas.append([f1,f2])
print(comps)