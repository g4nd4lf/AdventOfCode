import os,sys
import math
import numpy as np
import pathlib
import re
inputFile='input2.txt'
#inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
newfloors=[]
allmaxis=[]
puzzle=open(inputFile).read()
#goal=2022
goal=5*len(puzzle)
def soluSample(x,sol):
    x-=1
    coc=(x-50)//35
    res=(x-50)%35
    base=50+res
    return sol[base]+53*coc

def solu(x,sol):
    x-=1
    coc=(x-558)//1720
    res=(x-558)%1720
    base=558+res
    return sol[base]+2738*coc

def ver2(a):
    minx=min([x[0] for x in a])
    maxx=max([x[0] for x in a])
    miny=min([x[1] for x in a])
    maxy=max([x[1] for x in a])
    for y in range(maxy,miny-1,-1):
        for x in range(minx,maxx+1):
            if [x,y] in a:
                print("#",end="")
            else:
                print(".",end="")
        print()
def ver(a):
    minx=min([x[0] for x in a])
    maxx=max([x[0] for x in a])
    miny=min([x[1] for x in a])
    maxy=max([x[1] for x in a])
    for y in range(maxy,0,-1):
        print("|",end="")
        for x in range(1,maxx+1):
            if [x,y] in a:
                print("#",end="")
            else:
                print(".",end="")
        print("|")
    print("+-------+")
#ver([[5, 7], [6, 7], [7, 7], [8, 7]])
def newx(i):
    return 1 if puzzle[i%len(puzzle)]=='>'else -1
    # c=puzzle(i%len(puzzle))
    # if c=='<':
    #     return(-1)
    # else:
    #     return(1)

# def colx():
#     for r in rock
rocks=[]
#rock1 - :
rocks.append([[x,0] for x in range(4)])
#rock2 + :
rocks.append([[0,1],[1,0],[1,1],[1,2],[2,1]])
#rock3 L :
rocks.append([[0,0],[1,0],[2,0],[2,1],[2,2]])
#rock4 | :
rocks.append([[0,x] for x in range(4)])
#rock5 o:
rocks.append([[0,0],[0,1],[1,0],[1,1]])

# rock1=np.ones((1,4),dtype=[])
# rock2=np.zeros((3,3),dtype=[])
# rock2[0,1]=1
# rock2[1,:]=1
# rock2[2,1]=1
# rock3=np.zeros((3,3),dtype=[])
# rock3[0,2]=1
# rock3[1,2]=1
# rock3[2,:]=1
# rock4=np.ones((4,1),dtype=[])
# rock5=np.ones((2,2),dtype=[])
# rocks=[rock1,rock2,rock3,rock4,rock5]
# for r in rocks:
#     ver(r)
#     print("------")
def actualizaRoca(rock,newpos):
    newrock=[]
    #newpos=pos
    #pos[0]+=nx    
    for r in rock:
        nr=[r[0]+newpos[0],r[1]+newpos[1]]
        newrock.append(nr)
    return newrock
def reduce(cave,newfloor):
    for c in cave:
        if c[1]<newfloor:
            cave.remove(c)

def colx(rock,cave):
    for r in rock:
        if r[0]<=0 or r[0]>=wide+1 or r in cave:
            return True
    return False
def coly(rock,cave):
    newrock=[]
    for r in rock:
        if r[1]<=0 or r in cave:
            return True
    return False
def findTop(cave):
    top=0
    for c in cave:
        if c[1]>top:
            top=c[1]
    return top
def findTops(cave):
    maxis=(wide+1)*[0]
    for x in range(1,wide+2):
        for c in cave:
            if c[0]==x and c[1]>maxis[x]:
                maxis[x]=c[1]
    return maxis
cave=[]
sol=[]
wide=7
highest=0
origin=(highest+4,3)
ri=0 #indice para recorrer las rocas
pos=origin
nuevaRoca=True
units=0
newrocks=rocks.copy()
ji=0 #jet index
while nuevaRoca:
    rock=rocks[ri%5]
    sigueBajando=True
    nx0=3
    ny0=highest+4
    pos0=[nx0,ny0]
    pos=pos0
    rock=actualizaRoca(rock,pos)
    while sigueBajando:
        #pos=pos0
        nx=pos[0]+newx(ji)
        ji+=1
        posibleRoca=actualizaRoca(rocks[ri%5],[nx,pos[1]])
        if colx(posibleRoca,cave): #colision en eje x
            nx=pos[0]
        ny=pos[1]-1
        posibleRoca=actualizaRoca(rocks[ri%5],[nx,ny])
        if coly(posibleRoca,cave): #colision en eje y
            newfloors.append(ny)
            allmaxis.append(findTops(cave))
            ny=pos[1]
            rock=actualizaRoca(rocks[ri%5],[nx,ny])
            sigueBajando=False
            units+=1
            cave+=rock
            highest=findTop(cave)
            sol.append(highest)
            maxis=findTops(cave)
            newFloor=min(maxis[1:])
            #reduce(cave,newFloor)
            #highest=findTop(cave)
            #sol.append(highest)
            #print(units)
            if units>100:
                reduce(cave,newFloor-100)
                #print(units)
                #nuevaRoca=False
                #break
            if units==2300:
                nuevaRoca=False
                break
            if units==goal:
                nuevaRoca=False
                break
            
        pos=[nx,ny]
        rock=actualizaRoca(rocks[ri%5],pos)
        
    highest=findTop(cave)
    ri+=1 #siguiente roca
print("part1: ",soluSample(2022,sol))
print("part1:",highest)
#ver(cave)
