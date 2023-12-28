import os
from colorama import Fore, Style, init

os.chdir("./day16")
input1='sample.txt'
#input1='input.txt'

def find_crossings(beams,mirrors,transited,visited,xmax,ymax):
    previous_beams=beams.copy()
    for b in previous_beams:
        if b in visited:
            beams.remove(b)
        else:
            visited.add(b)
            if b[1][0]==1:
                mirrors_right=[m for m in mirrors if m[1]==b[0][1] and m[0]>b[0][0] and mirrors[m]!='-']
                next_mirror_x=float('inf')
                if len(mirrors_right)>0:
                    next_mirror_x=min([x[0] for x in mirrors_right])
                    #mirror=mirrors([])
                    mirror_coor=next_mirror_x,b[0][1]
                    beams_y=b[0][1]
                    if mirrors[mirror_coor]=='\\':
                        beams.add(((next_mirror_x,beams_y),(0,1)))
                    elif mirrors[mirror_coor]=='/':
                        beams.add(((next_mirror_x,beams_y),(0,-1)))
                    elif mirrors[mirror_coor]=='|':
                        beams.add(((next_mirror_x,beams_y),(0,-1)))
                        beams.add(((next_mirror_x,beams_y),(0,1)))
                transited_x=min(next_mirror_x,xmax-1)
                transited.update((i,b[0][1]) for i in range(b[0][0],transited_x+1))
                beams.remove(b)
            if b[1][0]==-1:
                mirrors_left=[m for m in mirrors if m[1]==b[0][1] and m[0]<b[0][0] and mirrors[m]!='-']
                next_mirror_x=-1
                if len(mirrors_left)>0:
                    next_mirror_x=max([x[0] for x in mirrors_left])
                    #mirror=mirrors([])
                    mirror_coor=next_mirror_x,b[0][1]
                    beams_y=b[0][1]
                    if mirrors[mirror_coor]=='\\':
                        beams.add(((next_mirror_x,beams_y),(0,-1)))                   
                    elif mirrors[mirror_coor]=='/':
                        beams.add(((next_mirror_x,beams_y),(0,1)))
                    elif mirrors[mirror_coor]=='|':
                        beams.add(((next_mirror_x,beams_y),(0,-1)))
                        beams.add(((next_mirror_x,beams_y),(0,1)))
                transited_x=max(next_mirror_x,0)
                transited.update((i,b[0][1]) for i in range(transited_x,b[0][0]+1))
                beams.remove(b)
            if b[1][1]==-1:
                mirrors_up=[m for m in mirrors if m[0]==b[0][0] and m[1]<b[0][1] and mirrors[m]!='|']
                next_mirror_y=-1
                if len(mirrors_up)>0:
                    next_mirror_y=max([x[1] for x in mirrors_up])
                    mirror_coor=b[0][0],next_mirror_y
                    beams_x=b[0][0]
                    if mirrors[mirror_coor]=='\\':
                        beams.add(((beams_x,next_mirror_y),(-1,0)))
                    elif mirrors[mirror_coor]=='/':
                        beams.add(((beams_x,next_mirror_y),(1,0)))
                    elif mirrors[mirror_coor]=='-':
                        beams.add(((beams_x,next_mirror_y),(-1,0)))
                        beams.add(((beams_x,next_mirror_y),(1,0)))
                transited_y=max(next_mirror_y,0)
                transited.update((b[0][0],j) for j in range(transited_y+1,b[0][1]))
                beams.remove(b)
            if b[1][1]==1:
                mirrors_down=[m for m in mirrors if m[0]==b[0][0] and m[1]>b[0][1] and mirrors[m]!='|']
                next_mirror_y=ymax
                if len(mirrors_down)>0:
                    next_mirror_y=min([x[1] for x in mirrors_down])
                    mirror_coor=b[0][0],next_mirror_y
                    beams_x=b[0][0]
                    if mirrors[mirror_coor]=='\\':
                        beams.add(((beams_x,next_mirror_y),(1,0)))
                    elif mirrors[mirror_coor]=='/':
                        beams.add(((beams_x,next_mirror_y),(-1,0)))                    
                    elif mirrors[mirror_coor]=='-':
                        beams.add(((beams_x,next_mirror_y),(-1,0)))
                        beams.add(((beams_x,next_mirror_y),(1,0)))
                transited_y=min(next_mirror_y,ymax-1)
                transited.update((b[0][0],j) for j in range(b[0][1],transited_y+1))
                beams.remove(b)
    return beams, transited, visited
print("Reading and parsing data:")
result=0
#orig_stones=[]
mirrors={}
beams=set()
crossings=set()
transited=set()
beams.add(((-1,0),(1,0))) #(pos(x,y), direction(i,j)
with open(input1) as f:
    lines=f.readlines()
    for i,l in enumerate(lines):
        for j,c in enumerate(l):
            pass
            if c!='.':
                mirrors[j,i]=c
xmax=len(lines[0])-1
ymax=len(lines)
visited=set()
beams,transited,visited =find_crossings(beams,mirrors,transited,visited,xmax,ymax)
pass
#transited.add(newtransitions)
while len(beams)>0:
    beams,transited,visited =find_crossings(beams,mirrors,transited,visited,xmax,ymax)

import json
with open('bool_map_sample.json', 'r') as f:
    bool_map = json.load(f)
#with open('mirror_hit_sample.json', 'r') as f:
#    mirror_hit = json.load(f)

#cadena+=f"{Fore.GREEN}{Style.BRIGHT}{map[i,j]}{Style.RESET_ALL}"
printgraph=""
for j,l in enumerate(lines):
    pass
    for i,c in enumerate(l[:-1]):
        if False:#(i,j) in transited:
            printgraph+="#"
        else:
            if bool_map[j][i]:
                ch="#"
                printgraph+=f"{Fore.GREEN}{Style.BRIGHT}{ch}{Style.RESET_ALL}"
            else:
                printgraph+=c
    printgraph+="\n"
print(printgraph)
    
print("Result: ",len(transited))
    