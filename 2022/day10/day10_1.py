import os
import math
import numpy as np
import pathlib

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

inputFile='input.txt'
#inputFile='sample.txt'
x=[1]
cycles=0
with open(inputFile) as f:
    lines = f.read().splitlines()
    for l in lines:
        newCommand=l.split(" ")
        if cycles==218:
            print(cycles)
        if len(newCommand)>1:
            valStr=newCommand[1]
            val=int(valStr)
            cycles+=1
            x.append(x[cycles-1])
            cycles+=1
            x.append(x[cycles-1]+val)
        else:
            cycles+=1
            x.append(x[cycles-1])
            
sum=0
for i in range(19,220,40):
    sum+=(i+1)*x[i]
    print(i+1,x[i],(i+1)*x[i])
   # print(len(points))    
print(sum)