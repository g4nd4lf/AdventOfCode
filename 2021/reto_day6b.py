import pandas as pd
import numpy as np
f = open("id6pru.txt", "r")
#f = open("input_day5.txt", "r")
input=f.read()
ini=input.split(",")
pob=[int(x) for x in ini]
for i in range(1,18+1):
    newPob=[]
    for i in pob:
        if (p==0):
            p=6
            newPob.append([8])
        else:
            p=p-1
    if(len(newPob)):
        pob.append(newPob)
    print(pob)
