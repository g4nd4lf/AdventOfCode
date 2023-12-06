import os,sys
import math
import numpy as np
import pathlib

inputFile='input.txt'
#inputFile='sample.txt'

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
def createMap(map,paths,minx,maxx,miny,maxy):
    for path in paths:
        for i in range(len(path)-1):
            if path[i][0]==path[i+1][0]:
                for j in range(min(path[i][1],path[i+1][1]),max(path[i][1],path[i+1][1])+1):
                    map[path[i][0],j]=1
            elif path[i][1]==path[i+1][1]:
                for k in range(min(path[i][0],path[i+1][0]),max(path[i][0],path[i+1][0])+1):
                    map[k,path[i][1]]=1
    return map
def printMap(map,maxx,miny,maxy):
    for i in range(0,maxx+1):
        for j in range(miny,maxy+1):
            if map[i,j]==1:
                print("#",end='')
            elif map[i,j]==-1:
                print("o",end='')
            else:
                print(".",end='')
        print()
def move(pos,map,floor):
    pos1=(pos[0]+1,pos[1]-1)
    pos2=(pos[0]+1,pos[1])
    pos3=(pos[0]+1,pos[1]+1)
    if pos3[1]==len(map[1]):
        base=[abs(map[x]) for x in [pos1,pos2]]+[0]
    else:
        try:
            base=[abs(map[x]) for x in [pos1,pos2,pos3]]
        except:
            print("error")
    if base==[1,1,1] or pos[0]+1==floor:
        return pos
    elif base[1]==0:
        return pos2
    elif base[0]==0:
        return pos1
    else:
        return pos3

def addSand(map,newpos):
    if newpos[1]==len(map[0]):
        newcol=np.zeros((len(map),1))
        map=np.concatenate((map,newcol),axis=1)
    map[newpos]=-1
    return map
  
#Read input
with open(inputFile) as f:
    lines=f.readlines()
    paths=[]
    maxx=0
    maxy=0
    minx=sys.maxsize
    miny=sys.maxsize
    for l in lines:
        points=l.split(" -> ")
        newpath=[]
        for p in points:
            y,x=[int(x) for x in p.split(",")]
            if x>maxx:
                maxx=x
            if y>maxy:
                maxy=y
            if x<minx:
                minx=x
            if y<miny:
                miny=y
            newpath.append((x,y))
        #path=[(p.split(",")[0],p.split(",")[1]) for p in points]
        #path.append(newpath)
        paths.append(newpath)
    floor=maxx+2
    print("maxx",maxx-minx,"maxy",maxy-miny)
    map=np.zeros((maxx+3,maxy+1),dtype=int)
    map=createMap(map,paths,minx,maxx,miny,maxy)
    printMap(map,maxx,miny,maxy)
    fin=False
    sandsResting=0
    while not fin:
        start=(0,500)
        oldpos=start
        stop=False
        while not stop:
            newpos=move(oldpos,map,floor)
            if newpos[1]==len(map[0]):
                newcol=np.zeros((len(map),1))
                map=np.concatenate((map,newcol),axis=1)
            #print(newpos)
            if newpos==oldpos:
                stop=True
                map=addSand(map,newpos)
                sandsResting+=1
            oldpos=newpos
            if newpos==(0,500):
                stop=True
                fin=True
        #printMap(map,maxx,miny,maxy)
    print("part1:",sandsResting)

    # for m in map:
    #     if 
    # for path in paths:
    #     for i in range(len(path)-1):
    #         if path[i][0]==path[i+1][0]:
    #             #print("")
    #             pass