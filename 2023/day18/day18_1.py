import heapq
import os
os.chdir("./day18")
#input1='sample.txt'
input1='input.txt'

import heapq
def inside(point,lines,map,xmax,ymax):
    if point in map:
        return True
    elif point[1]==0 or point[1]==ymax-1:
        return False
    else:
        right=lines[point[1]][point[0]:]
        starts= [point[0]+i+1 for i, c in enumerate(right[:-1]) if (c == "." and right[i+1] == "#") or (i==0 and right[0] =="#")]
        ends=[point[0]+i for i, c in enumerate(right[:-1]) if (c == "#" and right[i+1] == ".")]
        if len(right)>0:
            if right[len(right)-1] == "#":
                ends.append(len(lines[0])-1)
        rightwalls=0
        for i in range(len(starts)):
            if ([starts[i],point[1]-1] in map) and ([ends[i],point[1]+1] in map) or \
               ([starts[i],point[1]+1] in map) and ([ends[i],point[1]-1] in map):
                rightwalls+=1
        if (rightwalls)%2:
            return True
        else:
            return False
    
def calc_area(lines,map):
    area=0
    xmin=min([p[0] for p in map])
    ymin=min([p[1] for p in map])
    xmax=max([p[0] for p in map])+1
    ymax=max([p[1] for p in map])+1
    for j in range(ymin,ymax):
        for i in range(xmin,xmax):
            if inside([i,j],lines,map,xmax,ymax):
                area+=1
    return area
            
def calcular_area(vertices):
    # Encontrar las coordenadas extremas del polígono
    min_x = min(x for x, y in vertices)
    max_x = max(x for x, y in vertices)
    min_y = min(y for x, y in vertices)
    max_y = max(y for x, y in vertices)

    # Inicializar el contador de puntos dentro del polígono
    puntos_dentro = 0

    # Contar los puntos dentro del polígono
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if punto_dentro_del_poligono(x, y, vertices):
                puntos_dentro += 1

    return puntos_dentro

def punto_dentro_del_poligono(x, y, vertices):
    # Verificar si el punto (x, y) está dentro del polígono utilizando el método de ray-casting
    # Este método asume que el polígono está definido en sentido horario o antihorario

    n = len(vertices)
    dentro = False

    for i in range(n):
        xi, yi = vertices[i]
        xj, yj = vertices[(i + 1) % n]

        # Verificar si el punto cruza la línea del segmento del polígono
        if ((yi <= y and y < yj) or (yj <= y and y < yi)) and \
           (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            dentro = not dentro

    return dentro

print("Reading and parsing data:")
result=0
pos=[0,0]
map=[pos]
with open(input1) as f:
    lines=f.readlines()
    for i,l in enumerate(lines):
        dir,num,col=l.split(" ")
        num=int(num)
        if dir=='R':
            map+=[[x,pos[1]] for x in list(range(pos[0],pos[0]+num+1))]
            pos[0]+=num
        elif dir=='L':
            map+=[[x,pos[1]] for x in list(range(pos[0]-num,pos[0]))]
            pos[0]-=num
        elif dir=='D':
            map+=[[pos[0],y] for y in list(range(pos[1],pos[1]+num+1))]
            pos[1]+=num
        elif dir=='U':
            map+=[[pos[0],y] for y in list(range(pos[1]-num,pos[1]))]
            pos[1]-=num
        pass
        #map.append(newpos)
        #pos=newpos

xmax=max([p[0] for p in map])
ymax=max([p[1] for p in map])
xmin=min([p[0] for p in map])
ymin=min([p[1] for p in map])

dibujo=""
for j in range(ymin,ymax+1):
    for i in range(xmin,xmax+1):
        if [i,j] in map:
            dibujo+="#"
        else:
            dibujo+="."
    dibujo+="\n"
#print(dibujo)
with open("output.txt", "w") as archivo:
    # Escribir el string en el archivo
    archivo.write(dibujo)
#for y in range(ymax):
lineas=dibujo.split("\n")
area= calc_area(lineas,map)

print("area: ",area)