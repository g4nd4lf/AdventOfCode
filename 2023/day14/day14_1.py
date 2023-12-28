import os
os.chdir("./day14")
input1='sample.txt'
#input1='input.txt'

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
with open(input1) as f:
    lines=f.readlines()
    xmax=len(lines)
    ymax=len(lines[0])
    for i,l in enumerate(lines):
        #print(l)        
        l=l.replace("\n","")
        stones+=([[i,j] for j,char in enumerate(l) if char =="#"])
        rocks+=([[i,j] for j,char in enumerate(l) if char =="O"])
        #rocks.append([ymax-i+1 for i, char in enumerate(l) if char == "O"])
        #stones.append([ymax-i+1 for i, char in enumerate(l) if char == "#"])
lines2=flip(transpose(lines))
for l in lines2:
    rocks.append([i for i,char in enumerate(l) if char =="O"])
    newStones=[i for i,char in enumerate(l) if char =="#"]
    if len(newStones)>0:
        stones.append(newStones)
    else:
        stones.append([0])
#rocks2=flip(transpose(rocks))
#stones2=flip(transpose(stones))
#a=['OO.', '.O.', 'O.#']
#print(transpose(a))
tot=0
#North
orig_rocks=[]
for i,rl in enumerate(rocks):
    for j in reversed(range(len(rl))):
        stones_above=[s for s in stones[i] if s>rl[j]] # '#'
        stone_blocking=float('inf')
        if len(stones_above)>0:
            stone_blocking=min(stones_above)
        rocks_above=[r for r in rl if r>rl[j]]  # 'O'
        rock_blocking=float('inf')
        if len(rocks_above)>0:
            rock_blocking=min(rocks_above)
            
        rl[j]=min(stone_blocking-1,rock_blocking-1,xmax-1)
        orig_rocks.append([xmax-rl[j]-1,i])
        tot+=rl[j]+1
        pass
for r in orig_rocks:
    linea=r[0]
    rocks_left=[x[1] for x in orig_rocks if x[0]==linea and x[1]<r[1]]

    if len(rocks_left)>0:
        rock_blocking=max(rocks_left)
    stones_left=[x[1] for x in orig_stones if x[0]==linea and x[1]<r[1]]  
    if len(stones_left)>0:
        stone_blocking=max(stones_left)  
    r[1]=max()
    pass

for i,l in enumerate(lines):
    l=l.replace("\n","")
    l=l.replace("O",".")
    for r in [x for x in orig_rocks if x[0]==i]:
        l=l[:r[1]]+"O"+l[r[1]+1:]
    print(l)

#West

        #obstacle=min(rl[j+1],)
        #value=max()    
print(tot)
#         l=l.replace(".","0")
#         l=l.replace("#","1")
#         if l=="":
#             patterns.append(pattern)
#             result+=count_score(pattern)
#             pattern=[]
            
#         else:
#             pattern.append(l)
    
#         #print(number_of_valid_combination)
#     patterns.append(pattern)
#     #pattern=[]
#     result+=count_score(pattern)
    
#     print("result:",result)
