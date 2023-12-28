import os
from operator import itemgetter
#from colorama import Fore, Style, init
space_len=100
def calculate_distances(map):
    recorridos=set()
    total_distance=0
    for i,m1 in enumerate(map):
        for j,m2 in enumerate(map):
            if j!=i and (j,i) not in recorridos:
                distance=manhattan_distance(m1,m2)
                recorridos.add((i,j))
                total_distance+=manhattan_distance(m1,m2)
                #distances.append(distance)
                print([m1,m2,distance])
    return(total_distance)
def expand(map,xmax,ymax,row):
    col=[]
    for i in range(xmax):
        emptycol=True
        for j in range(ymax):
            if [i,j] in map:
                emptycol=False
                break
        if emptycol:
            col.append(i)
            #break
    #print("rows: ",row," cols: ",col)
    for m in map:
        m[0]+=(space_len-1)*sum([x<m[0] for x in col])
        m[1]+=(space_len-1)*sum([x<m[1] for x in row])
    xmax=xmax+len(col)
    ymax=ymax+len(row)
    return map, xmax, ymax
def print_map(map,xmax,ymax):
    cadena=""
    for j in range(ymax):
        for i in range(xmax):
            if [i,j] in map:
                c="#"
            else:
                c='.'
            cadena+=c
        cadena+='\n'
    print(cadena)
def manhattan_distance(coor1,coor2):
    x1,y1 = coor1
    x2,y2 = coor2
    return abs(x1 - x2) + abs(y1 - y2)

os.chdir("./day11")
#print(os.getcwd())
input1='sample.txt'
#input1='input.txt'
print("Reading and parsing data:")
with open(input1) as f:
    lines=f.readlines()
    universe=[]
    row=[]
    for j,l in enumerate(lines):
        l=l.replace("\n","")
        if all([x=='.' for x in l]):
            row.append(j)
        for i,c in enumerate(l):
            if c=="#":
                universe.append([i,j])
    xmax=len(lines[0])-1
    ymax=len(lines)
    print("Expanding universe...")
    universe,xmax,ymax=expand(universe,xmax,ymax,row)
    #print_map(universe,xmax,ymax)
    print("Calculating distances...")
    distance=calculate_distances(universe)
    print("Result:")
    #print(distances)
    print(distance)
