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
        cubeIntersec.append((max(rg1[i][0],rg2[i][0]),min(rg1[i][1],rg2[i][1])))
    return(tuple(cubeIntersec))
          
def enciende(n): #n: new element
    global reactor
    nuevo=True
    newReactor=reactor.copy()
    newReactor.append((n,+1))
    for r in reactor: #para cada cuboide r en reactor
        if intersec(n,r[0]):
            negat=calculaIntersec(n,r[0])
            if r[1]==1:
                newReactor.append((negat,-1))
            else:
                newReactor.append((negat,+1))
    reactor=newReactor.copy()
def apaga(n): #n: new element
    global reactor
    newReactor=reactor.copy()
    for r in reactor: #para cada cuboide r en reactor
        if intersec(n,r[0]):
            negat=calculaIntersec(n,r[0])
            if r[1]==1: 
                newReactor.append((negat,-1))
            else:
                newReactor.append((negat,+1))
    reactor=newReactor.copy()
start = time.time()
#f = open("id22pru2.txt", "r")
f = open("input_day22.txt", "r")
input=f.read()
lines=input.splitlines()
total=0
reactor=[]
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
        enciende(tuple(changes)) 
        #reactor=une(tuple(changes),reactor)
    else:
        apaga(tuple(changes)) 
for re in reactor:
    r=re[0]
    val=re[1]
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
    total+=val*(r[0][1]-r[0][0]+1)*(r[1][1]-r[1][0]+1)*(r[2][1]-r[2][0]+1)
print(total)
#aj 1233304599156793
#yo 1234240644613908

# for r in reactor:
#     for i in range(r[0][0],r[0][1]+1):
#         for j in range(r[1][0],r[1][1]+1):
#             for k in range(r[2][0],r[2][1]+1):
#                 print(str(i)+","+str(j)+","+str(k))