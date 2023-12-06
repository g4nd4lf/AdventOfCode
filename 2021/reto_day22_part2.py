import time
import numpy as np
import math
from collections import defaultdict

def intersec(rg1,rg2):
    if rg2[0][1]<rg1[0][0] or rg2[0][0]>rg1[0][1] or \
        rg2[0][1]<rg1[0][0] or rg2[0][0]>rg1[0][1]:
            print(False)
    else
        print(True)

def inserta(rg,cube,val):
    for c in cube:
        if intersec(rg,c):
            new=resuelveIntersec(rg,c)
        else


start = time.time()
f = open("id22pru3.txt", "r")
#f = open("input_day22.txt", "r")
input=f.read()
lines=input.splitlines()
minis=[]
maxis=[]
reactor=dict()
for line in lines:
    mode=line.split(" ")[0]
    changesS=line.split(" ")[1].split(",")
    minis=[1e6]*3
    maxis=[-1e6]*3
    changes=[]
    for i in range(len(changesS)):
        c=changesS[i]
        ini=int(c.split("..")[0][2:])+50
        fin=int(c.split("..")[1])+50
        # if ini<minis[i]:
        #     minis[i]=ini
        # if fin>maxis[i]:
        #     maxis[i]=fin
        changes.append((ini,fin))
    if mode=="on":
        inserta(tuple(changes),reactor,1)
        
    else:
        inserta(tuple(changes),reactor,0)
totals=[]
total=0
for r,v in reactor.items():
    if v==1:
        total+=(r[0][1]-r[0][0]+1)*(r[1][1]-r[1][0]+1)*(r[2][1]-r[2][0]+1)
    #totals.append()
print(total)
    
#         #changes.append(ini)
#         #changes.append(fin)
#         
#         changesi=[]
#         for r in rango:
#             if minis[i]<=r<=maxis[i]:
#                 changesi.append(r)
#         changes.append(changesi)

#     #print(changes)
#     for i in changes[0]:
#         for j in changes[1]:
#             for k in changes[2]:
#                 if mode=="on":
#                     reactor[i][j][k]=1
#                 else:
#                     reactor[i][j][k]=0
# t2 = time.time()
# print("Reactor modificado"+str(t2-start))
# #unos = filter(lambda x: x==1, reactor)
# print(np.sum(reactor))
# t3 = time.time()
# print("Suma realizada"+str(t3-start))



                
    