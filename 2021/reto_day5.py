import pandas as pd
import numpy as np
#f = open("id5pru.txt", "r")
f = open("input_day5.txt", "r")
input=f.read()
ilines=input.splitlines()
field = [[0 for i in range(1000)] for j in range(1000)]
#field = [[0 for i in range(10)] for j in range(10)]
linesStr=[]
for i in ilines:
    ori=i.split()[0].split(",")
    end=i.split()[2].split(",")
    linesStr.append(ori+end)
print(linesStr[0])
lines=[list( map(int,i) ) for i in linesStr]
print(lines[0])

for i in lines:
    #lineas horizontales:
    if (i[0]==i[2]):
        if (i[1]<=i[3]):
            for j in range(i[1],i[3]+1):
                field[i[0]][j]+=1
        else:
            for j in range(i[3],i[1]+1):
                field[i[0]][j]+=1
    #lineas verticales:
    elif (i[1]==i[3]):
        if (i[0]<=i[2]):
            for j in range(i[0],i[2]+1):
                field[j][i[1]]+=1
        else:
            for j in range(i[2],i[0]+1):
                field[j][i[1]]+=1
    #diagonales:
    else:
        print("diagonales...")

count=0    
for i in range(0,len(field)):
    for j in range(0,len(field)):
        if(field[i][j]>=2):
            count+=1
print("contador: ")
print(count)
