import time
import numpy as np
import math
from collections import defaultdict

def intersec(rg1,rg2):
    if rg2[0][1]<rg1[0][0] or rg2[0][0]>rg1[0][1] or \
       rg2[1][1]<rg1[1][0] or rg2[1][0]>rg1[1][1] or \
       rg2[2][1]<rg1[2][0] or rg2[2][0]>rg1[2][1]:
        return False
    else:
        return True
def calculaIntersec(rg1,rg2):
    cubeIntersec=[]
    for i in range(3):
        cubeIntersec.append(max(rg1[i][0],rg2[i][0]),min(rg1[i][1],rg1[2][1]))
    return(tuple(cubeIntersec))
def une(n,react):
    if type(react)!=set:
        newReact=set()
        newReact.add(n)
    else:
        nuevo=True
        newCubes=set()
        newReact=react
        for r in react:
            if intersec(n,r): 
                n1xl=r[0][0]-n[0][0]
                n2xl=n[0][1]-r[0][1]
                n1yl=r[1][0]-n[1][0]
                n2yl=n[1][1]-r[1][1]
                n1zl=r[2][0]-n[2][0]
                n2zl=n[2][1]-r[2][1]
                rx=r[0]
                ry=r[1]
                if n1xl>0:
                    newCubes.add(((n[0][0],r[0][0]-1),n[1],n[2]))
                else:
                    rx=(n[0][0],min(n[0][1],r[0][1]))
                if n2xl>0:
                    newCubes.add(((r[0][1]+1,n[0][1]),n[1],n[2]))
                else:
                    rx=(max(n[0][0],r[0][0]),n[0][1])
                if n1yl>0:
                    newCubes.add((rx,(n[1][0],r[1][0]-1),n[2]))
                else:
                    ry=(n[1][0],min(n[1][1],r[1][1]))
                if n2yl>0:
                    newCubes.add((rx,(r[1][1]+1,n[1][1]),n[2]))
                else:
                    ry=(max(n[1][0],r[1][0]),n[1][1])
                if n1zl>0:
                    newCubes.add((rx,ry,(n[2][0],r[2][0]-1)))
                if n2zl>0:
                    newCubes.add((rx,ry,(r[2][1]+1,n[2][1])))
                nuevo=False
        for c in newCubes:
            newReact=react
            newReact=une(c,react)
        if nuevo:
            react.add(n)
            newReact=react
    return newReact   
        
def enciende(n): #n: new element
    global reactor
    nuevo=True
    newReactor=reactor.copy()
    newReactor.add(n)
    for r in reactor: #para cada cuboide r en reactor
        if intersec(n,r[0]):
            if r[1]==1:
                negat=calculaIntersec(n,r)
                newReactor.add((negat,-1))
def apaga(n): #n: new element
    global reactor
    newReactor=reactor.copy()
    for r in reactor: #para cada cuboide r en reactor
        if intersec(n,r[0]): 
            negat=calculaIntersec(n,r)
            newReactor.add((negat,-1))
    reactor=newReactor.copy()
start = time.time()
f = open("id22pru3.txt", "r")
#f = open("input_day22.txt", "r")
input=f.read()
lines=input.splitlines()
total=0
reactor=set()
for line in lines:
    mode=line.split(" ")[0]
    changesS=line.split(" ")[1].split(",")
    minis=[1e6]*3
    maxis=[-1e6]*3
    changes=[]
    for i in range(len(changesS)):
        c=changesS[i]
        ini=int(c.split("..")[0][2:])
        fin=int(c.split("..")[1])
        changes.append((ini,fin))
    if mode=="on":
        #enciende(tuple(changes)) 
        reactor=une(tuple(changes),reactor)
    else:
        apaga(tuple(changes)) 
for r in reactor:
    # contar=True
    # c2=[]
    # for c in r:
    #     c2i=[]
    #     if c[0]<-50:
    #         c2i.append(-50)
    #     else:
    #         c2i.append(c[0])
    #     if c[1]>50:
    #         c2i.append(50)
    #     else:
    #         c2i.append(c[0])
    #     if c[0]>50 or c[1]<-50:
    #         contar=False
    #     c2.append(tuple(c2i))
    # c2t=tuple(c2)
    # if contar:
    #     total+=(c2t[0][1]-c2t[0][0]+1)*(c2t[1][1]-c2t[1][0]+1)*(c2t[2][1]-c2t[2][0]+1)
    total+=(r[0][1]-r[0][0]+1)*(r[1][1]-r[1][0]+1)*(r[2][1]-r[2][0]+1)
print(total)

# for r in reactor:
#     for i in range(r[0][0],r[0][1]+1):
#         for j in range(r[1][0],r[1][1]+1):
#             for k in range(r[2][0],r[2][1]+1):
#                 print(str(i)+","+str(j)+","+str(k))