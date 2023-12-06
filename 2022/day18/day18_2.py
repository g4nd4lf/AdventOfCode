import os,sys
import math
import numpy as np
import pathlib
import re
import time
start_time = time.time()
inputFile='input.txt'
#inputFile='sample.txt'
print("hola")
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
if inputFile=='sample.txt':
    tope=6
    minmin=1
else:
    tope=19
    minmin=0
#maxx=tope
#maxy=tope
#maxz=tope
contorno=set()
libre=set()
def esContorno(c):
    for i in range(2):
        if c[i]<=1 or c[i]==maxx:
            return True
    return False
def zonaLibre():
    for i in range(minmin-1,maxx+1):
        for j in range(minmin-1,maxy+1):
            for k in range(minmin-1,maxz+1):
                if [i,j,k] not in cubes:
                    if esContorno([i,j,k]):
                        contorno.add(str([i,j,k]))
                    libre.add(str([i,j,k]))
# con={}
# def conexiones():
#     for c in libre-contorno:
#         vecs=vecinos(eval(c))
#         vecsLibres=[str(v) for v in vecs if v not in cubes]
#         con[c]=set(vecsLibres)
        # if len(vecsLibres)>0:
        #     con[str(c)]=vecsLibres
        # else:
        #     con[str(c)]=None
posibles=set()
def addPosibles():
    for c in libre:
        if c not in contorno:
            if any([v in cubes for v in vecinos(eval(c))]):
                posibles.add(c)

def bfs(graph, S, D):
    queue = [(S, [S])]
    while queue:
        (vertex, path) = queue.pop(0)
        if len(graph[vertex])==0:
            queue=False
        else:
            for next in graph[vertex] - set(path):
                if next == D:
                    yield path + [next]
                elif next in contorno:
                    yield None
                else:
                    queue.append((next, path + [next]))

def shortest(graph, S, D):
    try:
        if len(graph[S])==0:
            return None
        if S in contorno:
            return 1
        if S in con:
            return next(bfs(graph, S, D))
        else:
            return None
    except StopIteration:
        return None

def vecinos(coor2):
    coor=coor2.copy()
    # x=[max(0,coor[0]-1),min(maxx,coor[0]+1)]
    # y=[max(0,coor[1]-1),min(maxx,coor[1]+1)]
    # z=[max(0,coor[2]-1),min(maxx,coor[2]+1)]
    x=[coor[0]-1,coor[0]+1]
    y=[coor[1]-1,coor[1]+1]
    z=[coor[2]-1,coor[2]+1]
    
    vecs=[]
    vecs.append([x[0],coor[1],coor[2]])
    vecs.append([x[1],coor[1],coor[2]])
    vecs.append([coor[0],y[0],coor[2]])
    vecs.append([coor[0],y[1],coor[2]])
    vecs.append([coor[0],coor[1],z[0]])
    vecs.append([coor[0],coor[1],z[1]])
    wrongVecs=[]
    for v in vecs:
        wrongVec=False
        for c in v:
            if c<-1 or c>maxx+1:
                wrongVec=True
                break
        if wrongVec:
            wrongVecs.append(v)
    for v2 in wrongVecs:
        vecs.remove(v2)
    return vecs
nohuecos=[]
sihuecos=[]
#pru=vecinos([3,6,1])

def esHueco(coor,cubes):
    vecs=vecinos(coor)
    if coor in nohuecos:
        return 0
    elif coor in sihuecos:
        return 1
    elif coor not in cube and any([x==1 or x==maxx for x in coor]): #Si la coordenada esta en el borde y no es un cubo->no es un hueco
        nohuecos.append(coor)
        return 0
    elif coor in cubes:
        return -1
    elif all([v in cubes for v in vecs]): #Roedado de cubos->es hueco
        sihuecos.append(coor)
        return 1
    else:
        for v in vecs:
            if v not in cube and esHueco(v,cubes)==0:
                return 0
    #return 1

def vision(cube,cubes,i):
    directions=[[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
    direction=directions[i]
    #for direction in directions:
    x=sum([a*b for a,b in zip(cube,direction)])
    x+=sum(direction)
    while x>0 and x<=maxx:
        newcube=[a+b for a,b in zip(cube,direction)]
        if newcube not in cubes:
            return True
        else:
            x+=sum(direction)
    return False    
    
#Read input
with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.read().splitlines()
    valve={}
    cubes=[]
    for l in lines:
        cubes.append([int(x) for x in l.split(",")])
minmin=1000
for c in cubes:
    for cara in c:
        if cara<minmin:
            minmin=cara
print(minmin)
print("zona libre...")
zonaLibre()
print("conexiones...")
#conexiones()
visitados=[]
#externo=contorno.copy()
externo=set()
externo.add(str([-1,-1,-1]))
externosExplorados=set()
carasVistas=0
while externo:
    e=externo.pop()
    externosExplorados.add(e)
    vecs=[v for v in vecinos(eval(e)) if str(v) not in externosExplorados]
    for v in vecs:
        if v in cubes:
            carasVistas+=1
            visitados.append([v,eval(e)])
        else:
            if str(v) not in externosExplorados:
                externo.add(str(v))
print(carasVistas)
# fs
# for c in cubes:
#     for cara in c:
#         if cara==1 or cara==tope:
#             carasVistas+=1
# print(carasVistas)        

# addPosibles()
# # pru=shortest(con,str([2,13,2]),str([9,19,5]))
# # print(pru)
# # pru2=shortest(con,str([8,12,15]),str([19,7,1]))
# # print(pru2)

# #res=shortest(con,str([2,2,5]),str([1,1,2]))
# #print("res:",res)
# #caras=len(cubes)*6
# caras=0
# visitCubes=cubes.copy()
# carasComunes=[]
# # for cube in cubes:
# #     for i in range(5):
# #         if vision(cube,cubes,i):
# #             caras+=1
# huecos=set()
# print("buscando huecos...",len(libre-contorno))
# id=0
# nuevoL=False
# tiempos=[]
# for l in posibles:
#     print(len(libre-contorno)-id)
#     id+=1
#     sinCamino=True
#     id2=0
#     for c2 in contorno:
#         #print("c2",len(contorno)-id2)
#         id2+=1
#         print(l,c2)
#         sh=shortest(con,l,c2)
#         print("--- %s seconds ---" % (time.time() - start_time))
#         tiempos.append([l,c2,time.time() - start_time])
#         if sh!=None:
#             sinCamino=False
#             nuevoL=True
#             #print("no hueco",len(contorno)-id2)
#             break
#     if sinCamino:
#         huecos.add(l)
#         print("hueco: ",l)
    
# print(caras)
# for i in range(1,maxx+1):
#     for j in range(1,maxy+1):
#         for k in range(1,maxz+1):
#             c=[i,j,k]
#             if esHueco(c,cubes)==1:
#                 print("Hueco:",c)
#for c in cubes:
    
#1.Buscar huecos:
##1.1. para cada coordenada donde no hay cubo:
## La coordenada no es de un hueco si alguna cara es del borde del espacio 
# o si alguna coordenada adyacente no es un hueco
## La coordeanda es un hueco si todas sus caras adyacentes son de cubos o de un "hueco"

#2. Para cada cubo contamos las caras que no tienen cubo vecino y que no dan a un hueco

#ERRORES: 1992, 2061 (esta entre estos dos)
#Segun day198aj2.py la solucion es 2042