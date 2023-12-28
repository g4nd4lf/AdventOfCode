import os
from operator import itemgetter
#from colorama import Fore, Style, init
space_len=1000000
def rows_and_cols_between(coor1,coor2,row,col):
    x1,y1=coor1
    x2,y2=coor2
    ncols=sum([x1<x<x2 for x in col])+sum([x2<x<x1 for x in col])
    nrows=sum([y1<y<y2 for y in row])+sum([y2<y<y1 for y in row])
    return nrows,ncols
def calculate_distances(map,row,col):
    recorridos=set()
    total_distance=0
    for i,m1 in enumerate(map):
        for j,m2 in enumerate(map):
            if j!=i and (j,i) not in recorridos:
                recorridos.add((i,j))
                rows,cols=rows_and_cols_between(m1,m2,row,col)
                #distance=manhattan_distance(m1,m2)+(rows+cols)*(space_len-1)
                total_distance+=manhattan_distance(m1,m2)+(rows+cols)*(space_len-1)
                #distances.append(distance)
                #print([m1,m2,distance])
    return(total_distance)
def find_cols(map,xmax,ymax):
    col=[]
    for i in range(xmax):
        emptycol=True
        for j in range(ymax):
            if [i,j] in map:
                emptycol=False
                break
        if emptycol:
            col.append(i)
    return col

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
#input1='sample.txt'
input1='input.txt'
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
    col=find_cols(universe,xmax,ymax)
    #universe,xmax,ymax=expand(universe,xmax,ymax,row)
    print_map(universe,xmax,ymax)
    print("Calculating distances...")
    distance=calculate_distances(universe,row,col)
    print("Result:")
    #print(distances)
    print(distance)
