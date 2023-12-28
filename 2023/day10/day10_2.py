import os
from operator import itemgetter
from colorama import Fore, Style, init

os.chdir("./day10")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
def imprime_resultado(map,posarr,xmax,ymax):
    init()
    cadena=""
    for j in range(ymax):
        for i in range(xmax):
            if [i,j] in posarr:
                cadena+=f"{Fore.GREEN}{Style.BRIGHT}{map[i,j]}{Style.RESET_ALL}"
            else:
                cadena+=map[i,j]
        cadena+="\n"
    print(cadena)
def next_pos(prev,pos,map,xmax,ymax):
    pos=tuple(pos[:2])
    if map[pos]=='|':
        if prev[0]!=pos[0]:
            return -1
        elif prev[1]>pos[1]:
            if pos[1]-1<0:
                return -1
            else:
                return [pos[0],pos[1]-1,-1]
        else:
            if pos[1]+1==ymax:
                return -1
            else:
                return [pos[0],pos[1]+1,-1]
    if map[pos]=='-':
        if prev[1]!=pos[1]:
            return -1
        elif prev[0]>pos[0]:
            if pos[0]-1<0:
                return -1
            else:
                return [pos[0]-1,pos[1],-1]
        else:
            if pos[0]+1==xmax:
                return -1
            else:
                return [pos[0]+1,pos[1],-1]
    if map[pos]=='L':
        if (prev[1]==pos[1] and prev[0]>pos[0]):
            if pos[1]-1<0:
                return -1
            else:
                return [pos[0],pos[1]-1,-1]
        elif (prev[0]==pos[0] and prev[1]<pos[1]):
            if pos[0]+1==xmax:
                return -1
            else:
                return [pos[0]+1,pos[1],-1]
        else:
            return -1
    if map[pos]=='J':
        if (prev[1]==pos[1] and prev[0]<pos[0]):
            if pos[1]-1<0:
                return -1
            else:
                return [pos[0],pos[1]-1,-1]
        elif (prev[0]==pos[0] and prev[1]<pos[1]):
            if pos[0]-1<0:
                return -1
            else:
                return [pos[0]-1,pos[1],-1]    
        else:
            return -1
    if map[pos]=='7':
        if (prev[1]==pos[1] and prev[0]<pos[0]):
            if pos[1]+1==ymax:
                return -1
            else:
                return [pos[0],pos[1]+1,-1]
        elif (prev[0]==pos[0] and prev[1]>pos[1]):
            if pos[0]-1<0:
                return -1
            else:
                return [pos[0]-1,pos[1],-1]    
        else:
            return -1
    if map[pos]=='F':
        if (prev[1]==pos[1] and prev[0]>pos[0]):
            if pos[1]+1==ymax:
                return -1
            else:
                return [pos[0],pos[1]+1,-1]
        elif (prev[0]==pos[0] and prev[1]>pos[1]):
            if pos[0]+1==xmax:
                return -1
            else:
                return [pos[0]+1,pos[1],-1]   
        else:
            return -1
    else:
        return -1
def pieza(pos1,pos2):
    if pos1[0]==pos2[0]:
        return "|"
    elif pos1[1]==pos2[1]:
        return "-"
    elif (pos1[0]<pos2[0] and pos1[1]>pos2[1]) or (pos2[0]<pos1[0] and pos2[1]>pos1[1]):
        return "J"
    elif (pos1[0]<pos2[0] and pos1[1]<pos2[1]) or (pos2[0]<pos1[0] and pos2[1]<pos1[1]) :
        return "7"
    elif (pos1[0]>pos2[0] and pos1[1]>pos2[1]) or (pos2[0]>pos1[0] and pos2[1]>pos1[1]):
        return "L"
    elif (pos1[0]>pos2[0] and pos1[1]<pos2[1]) or (pos2[0]>pos1[0] and pos2[1]<pos1[1]):
        return "F"
    pass
    
def findNeighbour(x,y,xmax,ymax):
    neig=[]
    if (x-1)>=0:
        neig.append([x-1,y,-1])
    if (x+1)<xmax:
        neig.append([x+1,y,-1])
    if (y-1)>=0:
        neig.append([x,y-1,-1])
    if (y+1)<ymax:
        neig.append([x,y+1,-1])
    return neig
map={}
with open(input1) as f:
    lines=f.readlines()
    data=[]
    start=[]
    for j,l in enumerate(lines):
      l.replace("\n","")
      for i,c in enumerate(l):
        map[i,j]=c
      if "S" in l:
          start=[l.index('S'),j,0]
    xmax=len(lines[-1])
    ymax=len(lines)
    neig=findNeighbour(start[0],start[1],xmax,ymax)
    l=l.replace("\n","")
    for n in neig:
        posarr=[]   
        pos=n
        prev=start
        endPath=False
        steps=0
        while map[tuple(pos[:2])]!='S' and not endPath:
            newpos=next_pos(prev,pos,map,xmax,ymax)
            posarr.append(pos[:2])
            if newpos==-1:
                endPath=True
                break
            steps+=1
            prev=pos
            pos=newpos
        imprime_resultado(map,posarr,xmax,ymax)
        if not endPath:
            map[tuple(pos[:2])]=pieza(prev,posarr[0])
            result=(steps+1)/2
            break
    tiles=0
    loop=[tuple(x) for x in posarr]
    for m in map:
        if m not in loop:
            cortes=0
            cortesL=0
            cortesJ=0
            cortesF=0
            cortes7=0
            for i in range(m[0]+1,xmax):
                if (i,m[1]) in loop or (i,m[1])==tuple(start[:2]):
                    c=map[i,m[1]]
                    if c=="|":
                        cortes+=1
                    elif c=='L':
                        cortesL+=1
                    elif c=='J':
                        cortesJ+=1
                    elif c=='F':
                        cortesF+=1
                    elif c=='7':
                        cortes7+=1
                    pass
            cortes+=(abs(cortesL-cortesJ)+abs(cortesF-cortes7))/2
            if cortes%2!=0:
                tiles+=1
                print(m)
                print(map[m[:2]])
    print(tiles)