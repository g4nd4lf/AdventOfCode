from os import F_OK
import pandas as pd
import numpy as np
#f = open("id6pru.txt", "r")
f = open("input_day6.txt", "r")
input=f.read()
ini=input.split(",")
pob=[int(x) for x in ini]
#pob2=list(range(0,9))
pob2=[0]*9
for i in range(0,len(pob)):
    pob2[pob[i]]+=1
for i in range(1,256+1): #18 dias 26peces
    print(i)
    crear=0
    if(pob2[0]>0):
        crear=pob2[0]
    for j in range(1,9):
        pob2[j-1]=pob2[j]
    pob2[6]=pob2[6]+crear
    pob2[8]=crear
        
    # #print(str(i)+";"+str(len(pob)))
    # #print(pob2)
    # res=""
    # for j in range(0,len(pob2)):
    #     for k in range(0,pob2[j]):
    #         res=res+","+str(j)
    # #print(res)
    # suma=0
    # for p in pob2:
    #     suma=suma+p
    #print("suma "+str(i))
    #print(suma)
suma=0
for p in pob2:
    suma=suma+p
print(suma)