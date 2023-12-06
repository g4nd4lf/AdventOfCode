import os
import math
import numpy as np
import pathlib

def mr(x):
    return int(math.copysign(math.ceil(abs(x)), x))

def next(h,t):
    if math.dist(h,t) >= 2:
        t[0]=t[0]+mr((h[0]-t[0])/2)
        t[1]=t[1]+mr((h[1]-t[1])/2)
    return(t)
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
#def dist(h,t):
#print(currentDir)
#inputFile='./day9/sample.txt'
inputFile='input.txt'
#inputFile='sample.txt'
with open(inputFile) as f:
    lines = f.read().splitlines()
    s=[4,0]
    points=set()
    points.add(tuple(s))
    h=[4,0]
    t=[4,0]
    #m=np.zeros((5,6),dtype=str)
    #m[0,4]='s'
    for l in lines:
        dir,st=l.split(" ")
        steps=int(st)
        if dir == 'R':
            for i in range(steps):
                h[1]+=1
                t=next(h,t)
                points.add(tuple(t))
        if dir == 'L':
            for i in range(steps):
                h[1]-=1
                t=next(h,t)
                points.add(tuple(t))
        if dir == 'U':
            for i in range(steps):
                h[0]-=1
                t=next(h,t)
                points.add(tuple(t))
        if dir == 'D':
            for i in range(steps):
                h[0]+=1
                t=next(h,t)
                points.add(tuple(t))
        #m=np.zeros((5,6),dtype=str)
        #m[(4,0)]='s'
        #t2=tuple(t)
        #h2=tuple(h)
        #m[t2]='T'
        #m[h2]='H'
#        print(m)
#        print()
    print(len(points))    
