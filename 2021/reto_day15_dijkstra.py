import pandas as pd
import time
from queue import PriorityQueue
import heapq

#f = open("id15pru.txt", "r")
#f = open("input_day15.txt", "r")
f = open("input15_2.txt", "r")
input=f.read()
lines=input.splitlines()
visitados=[]
vertices=[]
lastCol=len(lines[0])-1
lastRow=len(lines)-1
values=[]
dict={(0,0):0}
for i in range(lastRow+1):
    values.append([int(c) for c in list(lines[i])])
    for j in range(lastCol+1):
        vertices.append((i,j))
        dict[(i,j)]=values[i][j]
dict[(0,0)]=0
print("Datos leidos, buscando solución...")
def neighbors2(v,dim):
    i=v[0]
    j=v[1]
    vecinos=[]
    if i<dim[0]:
        vecinos.append((i+1,j))
    if j<dim[1]:
        vecinos.append((i,j+1))
    return vecinos

def myDijkstra2(start_vertex,dic):
    dim=list(dic.keys())[-1]
    visitados=[]
    D = {v:float('inf') for v in list(dic.keys())}
    D[start_vertex] = 0
    pq = PriorityQueue()
    pq.put((0, start_vertex))
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visitados.append(current_vertex)
        #dim=(dim[0]+1,dim[1]+1)
        for neighbor in neighbors2(current_vertex,dim):
            distance = dic[neighbor]
            if neighbor not in visitados:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D
def neighbors(v):
    vecinos=[]
    if v[0]<dimFi:
        vecinos.append((v[0]+1,v[1]))
    if v[1]<dimFj:
        vecinos.append((v[0],v[1]+1))
    if v[0]>0:
        vecinos.append((v[0]-1,v[1]))
    if v[1]>0:
        vecinos.append((v[0],v[1]-1))
    return vecinos

def myDijkstra(start_vertex,dic):
    dim=list(dic.keys())[-1]
    visitados=set()
    D = {v:float('inf') for v in list(dic.keys())}
    D[start_vertex] = 0
    pq = []
    heapq.heappush(pq, (0, start_vertex))
    #pq.put((0, start_vertex))
    while pq:
        (dist, current_vertex) = heapq.heappop(pq)
        visitados.add(current_vertex)
        #dim=(dim[0]+1,dim[1]+1)
        vecinos=neighbors(current_vertex)
        for neighbor in vecinos:
            distance = dic[neighbor]
            if neighbor not in visitados:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    heapq.heappush(pq,(new_cost, neighbor))
                    D[neighbor] = new_cost
    return D

# dimFi=len(values)-1
# dimFj=len(values[0])-1

# D = myDijkstra((0,0),dict)

# print(D[(lastRow,lastCol)])

#PARTE2:

#values5=pd.DataFrame(values)
values5=[]
for i in range(0,lastRow+1):
    newLine=[]
    for i2 in range(5):
        col5=[x+i2 for x in values[i]]
        newLine+=col5
    values5.append(newLine)

for i in range(0,len(values5)):
    for j in range(0,len(values5[0])):
        if values5[i][j]>9:      
            values5[i][j]-=9

values55=[]
for i2 in range(5):
    for i in range(0,len(values5)):
        nLine=[x+i2 for x in values5[i]]
        values55.append(nLine)

dict2={}
dict2[(0,0)]=0
for i in range(0,len(values55)):
    for j in range(0,len(values55[0])):
        if values55[i][j]>9:      
            values55[i][j]-=9
        #print(values55[i][j],end="")
    #print("")
for i in range(0,len(values55)):
    for j in range(0,len(values55[0])):
        dict2[(i,j)]=values55[j][i]
dict2[(0,0)]=0
dimFi=len(values55)-1
dimFj=len(values55[0])-1

print("Calculo de distancia...")

D2 = myDijkstra2((0,0),dict2)
dim=list(dict2.keys())[-1]
print("solucion:")
print(D2[dim])

#print(values55)

f2 = open("matr1.txt", "r")
input2=f2.read()
lines2=input2.splitlines()