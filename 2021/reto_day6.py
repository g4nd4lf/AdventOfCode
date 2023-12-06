import pandas as pd
import numpy as np
f = open("id6pru.txt", "r")
#f = open("input_day6.txt", "r")
input=f.read()
ini=input.split(",")
pob=[int(x) for x in ini]
for i in range(1,18+1):
    #print(i)
    newPob=[]
    for j in range(0,len(pob)):
        if (pob[j]==0):
            pob[j]=6
            newPob.append(8)
        else:
            pob[j]=pob[j]-1
    if(len(newPob)):
        pob=pob+newPob
    #print(str(i)+";"+str(len(pob)))
    print(pob)

