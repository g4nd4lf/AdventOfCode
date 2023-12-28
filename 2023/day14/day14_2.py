import os, copy

#os.chdir("./day14")
#input1='sample.txt'
input1='input.txt'
cycles=300

def ordena(points,order):
    def order_fun(coord,order):
        if order=='north':
            return (coord[0], coord[1])
        if order=='west':
            return (coord[1], coord[0])
        if order=='south':
            return (coord[0], -coord[1])
        if order=='east':
            return (coord[1], -coord[0])
    coordenadas_ordenadas = sorted(enumerate(points), key=lambda x: order_fun(x[1],order))
    indices_ordenados = [i for i, _ in coordenadas_ordenadas]
    return(indices_ordenados)
def rotate90(matriz):
    # Transponer la matriz (intercambiar filas por columnas)
    transpuesta = list(zip(*matriz))
    # Invertir el orden de las columnas (opcional)
    matriz_rotada = [fila[::-1] for fila in transpuesta]
    return matriz_rotada

def rotate90ccw(matriz): #ccw:counter clock wise
    # Transponer la matriz (intercambiar filas por columnas)
    transpuesta = list(zip(*matriz))

    # Invertir el orden de las filas
    matriz_rotada = transpuesta[::-1]

    return matriz_rotada
def transpose(matrix):
    transponse = list(zip(*matrix))
    newmatrix=[]
    for row in transponse:
        newmatrix.append(''.join(row))
    return newmatrix

def flip(matrix):
    flipped=[]
    for m in matrix:
        flipped.append(m[::-1])
    return flipped

rocks=[]
stones=[]
print("Reading and parsing data:")
result=0
#orig_stones=[]

with open('all_stones.json', 'r') as f:
    all_rocks = json.load(f)
with open('repeticiones.json', 'r') as f:
    repeticiones = json.load(f)

rocks=all_rocks[200]

with open(input1) as f:
    lines=f.readlines()
    xmax=len(lines)
    ymax=len(lines[0])-1
    for i,l in enumerate(lines):
        #print(l)        
        l=l.replace("\n","")
        stones+=([[j,i] for j,char in enumerate(l) if char =="#"])
        #rocks+=([[j,i] for j,char in enumerate(l) if char =="O"])
        #rocks.append([ymax-i+1 for i, char in enumerate(l) if char == "O"])
        #stones.append([ymax-i+1 for i, char in enumerate(l) if char == "#"])
all_stonesN=[]
all_stonesW=[]
all_stonesS=[]
all_stonesE=[]

for k in range(cycles):
    print("CYCLE ",k+1)
    #NORTH:
    #hay que obtener los indices tras reordenar rocks, por columnas y dentro de cada columnas de menor a mayor fila
    idrocks=ordena(rocks,'north')
    rocks2=copy.deepcopy(rocks)
    all_stonesN.append(rocks2)
    for id in idrocks:
        r=rocks[id]
        col=r[0]
        rocks_above=[x[1] for x in rocks if x[0]==col and x[1]<r[1]]
        rock_blocking=-1
        if len(rocks_above)>0:
            rock_blocking=max(rocks_above)
        stones_above=[x[1] for x in stones if x[0]==col and x[1]<r[1]]  
        stone_blocking=-1
        if len(stones_above)>0:
            stone_blocking=max(stones_above)  
        r[1]=max(rock_blocking+1,stone_blocking+1,0)
        pass
    #firstRocks=copy.deepcopy(rocks)
    #print("Rocks: ")
    #print(rocks)
    #print("firstRocks: ")
    #print(firstRocks)
    
    # print("SOUTH")
    # for i,l in enumerate(lines):
    #     l=l.replace("\n","")
    #     l=l.replace("O",".")
    #     for r in [x[0] for x in rocks if x[1]==i]:
    #         l=l[:r]+"O"+l[r+1:]
    #     print(l)
    #WEST
    idrocks=ordena(rocks,'west')
    
    for id in idrocks:
        r=rocks[id]
        row=r[1]
        rocks_left=[x[0] for x in rocks if x[1]==row and x[0]<r[0]]
        rock_blocking=-1
        if len(rocks_left)>0:
            rock_blocking=max(rocks_left)
        stones_left=[x[0] for x in stones if x[1]==row and x[0]<r[0]]  
        stone_blocking=-1
        if len(stones_left)>0:
            stone_blocking=max(stones_left)  
        r[0]=max(rock_blocking+1,stone_blocking+1,0)
    # print("WEST")
    # for i,l in enumerate(lines):
    #     l=l.replace("\n","")
    #     l=l.replace("O",".")
    #     for r in [x[0] for x in rocks if x[1]==i]:
    #         l=l[:r]+"O"+l[r+1:]
    #     print(l)
    #SOUTH
    idrocks=ordena(rocks,'south')
    for id in idrocks:
        r=rocks[id]
        col=r[0]
        rocks_below=[x[1] for x in rocks if x[0]==col and x[1]>r[1]]
        rock_blocking=float('inf')
        if len(rocks_below)>0:
            rock_blocking=min(rocks_below)
        stones_below=[x[1] for x in stones if x[0]==col and x[1]>r[1]]  
        stone_blocking=float('inf')
        if len(stones_below)>0:
            stone_blocking=min(stones_below)  
        r[1]=min(rock_blocking-1,stone_blocking-1,xmax-1)
    # print("SOUTH")
    # for i,l in enumerate(lines):
    #     l=l.replace("\n","")
    #     l=l.replace("O",".")
    #     for r in [x[0] for x in rocks if x[1]==i]:
    #         l=l[:r]+"O"+l[r+1:]
    #     print(l)

    #EAST
    idrocks=ordena(rocks,'east')
    for id in idrocks:
        r=rocks[id]
        row=r[1]
        rocks_right=[x[0] for x in rocks if x[1]==row and x[0]>r[0]]
        rock_blocking=float('inf')
        if len(rocks_right)>0:
            rock_blocking=min(rocks_right)
        stones_right=[x[0] for x in stones if x[1]==row and x[0]>r[0]]  
        stone_blocking=float('inf')
        if len(stones_right)>0:
            stone_blocking=min(stones_right)  
        r[0]=min(rock_blocking-1,stone_blocking-1,ymax-1)
        pass
    rocks2=copy.deepcopy(rocks)
    all_stonesE.append(rocks2)
x7=[x[7] for x in all_stones]
repeticiones=[]
repeticiones=[]
for r in range(len(all_stones[0])):
    xr=[x[r] for x in all_stones]
    coincidencias=[i for i,x in enumerate(xr) if xr[i+200:i+210]==xr[200:210]]
    if len(coincidencias)>1:
        print(r,": ",coincidencias[1])
        repeticiones.append(coincidencias[1])
    else:
        print(r,": sin repeticiones")
        repeticiones.append(-1)
pass
final_rocks=[]
for i,r in enumerate(repeticiones):
    idx=1000000000%r
    final_rocks.append(all_stones[idx][i])
#print("final_rocks: ",final_rocks)
#print("real 753: ",all_stones[753])
#print(final_rocks==all_stones[753])
result=0
#final_rocks=all_stones[753]
#final_rocks=firstRocks
for f in final_rocks:
    result+=xmax-f[1]
print(result)
pass

import json
with open('all_stones2.json', 'w') as f:
    json.dump(all_stones, f)
with open('repeticiones2.json', 'w') as f:
    json.dump(repeticiones, f)
