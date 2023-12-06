import os
import math
import numpy as np
import pathlib

def mr(x):
    return int(math.copysign(math.ceil(abs(x)), x))

def next(t,h):
    if math.dist(t,h) >= 2:
        t[0]=t[0]+mr((h[0]-t[0])/2)
        t[1]=t[1]+mr((h[1]-t[1])/2)
    return(t)
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
#def dist(h,t):
#print(currentDir)
#inputFile='./day9/sample.txt'
inputFile='input.txt'
#inputFile='sample2.txt'
with open(inputFile) as f:
    lines = f.read().splitlines()
    s=[4,0]
    points=set()
    points.add(tuple(s))
    h=[4,0]
    t=[4,0]
    tarr=[]
    for i in range(9):
        tarr.append([4,0])
    #m=np.zeros((5,6),dtype=str)
    #m[0,4]='s'
    for l in lines:
        dir,st=l.split(" ")
        steps=int(st)
        if dir == 'R':
            for i in range(steps):
                h[1]+=1
                tarr[0]=next(tarr[0],h)
                for i in range(1,9):
                    tarr[i]=next(tarr[i],tarr[i-1])
                points.add(tuple(tarr[8]))
        if dir == 'L':
            for i in range(steps):
                h[1]-=1
                tarr[0]=next(tarr[0],h)
                for i in range(1,9):
                    tarr[i]=next(tarr[i],tarr[i-1])
                points.add(tuple(tarr[8]))
        if dir == 'U':
            for i in range(steps):
                h[0]-=1
                tarr[0]=next(tarr[0],h)
                for i in range(1,9):
                    tarr[i]=next(tarr[i],tarr[i-1])
                points.add(tuple(tarr[8]))
        if dir == 'D':
            for i in range(steps):
                h[0]+=1
                tarr[0]=next(tarr[0],h)
                for i in range(1,9):
                    tarr[i]=next(tarr[i],tarr[i-1])
                points.add(tuple(tarr[8]))
        #m=np.zeros((5,6),dtype=str)
        #m[(4,0)]='s'
        #t2=tuple(t)
        #h2=tuple(h)
        #m[t2]='T'
        #m[h2]='H'
#        print(m)
#        print()
    print(len(points))    
