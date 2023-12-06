import os,sys
import math
import numpy as np
import pathlib
import re

inputFile='input.txt'
#inputFile='sample.txt'

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#Read input
with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.read().splitlines()
    valve={}
    cubes=[]
    for l in lines:
        cubes.append([int(x) for x in l.split(",")])
caras=len(cubes)*6
comunes=0
visitCubes=cubes.copy()
while len(visitCubes)>0:
    c1=visitCubes[0]
    for c2 in visitCubes:
        if c1!=c2:
            suma=0
            for i in range(3):
                if c1[i]==c2[i]:
                    suma+=1
            if suma==2:
                resta=sum([a-b for a,b in zip(c1,c2)])
                if abs(resta)==1:
                    comunes+=1
    visitCubes.remove(c1)
print(caras-comunes*2)
ex=[0,0]
ey=[0,0]
ez=[0,0]
for c in cubes:
    if c[0]<ex[0]:
        ex[0]=c[0]
    elif c[0]>ex[1]:
        ex[1]=c[0]
    if c[1]<ey[0]:
        ey[0]=c[1]
    elif c[1]>ey[1]:
        ey[1]=c[1]
    if c[2]<ez[0]:
        ez[0]=c[2]
    elif c[2]>ez[1]:
        ez[1]=c[2]

