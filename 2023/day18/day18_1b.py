import heapq
import os
os.chdir("./day18")
input1='sample.txt'
#input1='input.txt'

import heapq
def area(map):
    area=0
    xmax=max([p[0] for p in map])
    ymax=max([p[1] for p in map])
    for j in range(ymax):
        for i in range(xmax):
            
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
        newpos=pos.copy()
        dir,num,col=l.split(" ")
        if dir=='R':
            newpos[0]+=int(num)
        elif dir=='L':
            newpos[0]-=int(num)
        elif dir=='D':
            newpos[1]+=int(num)
        elif dir=='U':
            newpos[1]-=int(num)
        map.append(newpos)
        pos=newpos

xmax=max([p[0] for p in map])
ymax=max([p[1] for p in map])

dibujo=""
for j in range(ymax+1):
    for i in range(xmax+1):
        if [i,j] in map:
            dibujo+="#"
        else:
            dibujo+="."
    dibujo+="\n"
print(dibujo)
#for y in range(ymax):
area= calcular_area(map)

print("area: ",area)