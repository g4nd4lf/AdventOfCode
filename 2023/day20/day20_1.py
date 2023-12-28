import heapq
import os
os.chdir("./day17")
input1='sample.txt'
#input1='input.txt'


import heapq

def reconstruir_camino(padres, start, end):
    camino = [end]
    actual = end

    while actual != start:
        actual = padres[actual]
        camino.insert(0, actual)

    return camino

def consecutive_nodes(prox,actual,padres):
    n4=prox
    n3=actual
    if n3 in padres:
        if padres[n3]==None:
            return 0
        else:
            n2=padres[n3]
    else:
        return 0
    if n2 in padres:
        if padres[n2]==None:
            return 0
        else:
            n1=padres[n2]
    else:
        return 0
    if n1 in padres:
        if padres[n1]==None:
            return 0
        else:
            n0=padres[n1]
    else:
        return 0
    
    xs=[x[0] for x in [n0,n1,n2,n3,n4]]
    ys=[x[1] for x in [n0,n1,n2,n3,n4]]
    x_counts=[xs.count(x) for x in xs]
    y_counts=[ys.count(x) for x in ys]
    return max(max(x_counts),max(y_counts))

# Diccionario para rastrear los padres de cada nodo
#padres = {}

def dijkstra(matriz):
    rows, cols = len(matriz), len(matriz[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    padres = {start: None}
    # Inicializar las distancias con infinito para todos los nodos
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distances[start] = 0 #matriz[start[0]][start[1]]

    # Conjunto de nodos no visitados
    #nodos_no_visitados = [(matriz[start[0]][start[1]], start, 0, (0, 0))]
    nodos_no_visitados = [(matriz[start[0]][start[1]], start,(0,0))]
    
    

    # Direcciones de movimiento: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #direccion_actual = (0, 0)
    #nodos_consecutivos = 0

    while nodos_no_visitados:
        #distancia_actual, nodo_actual, nodos_consecutivos, direccion_actual = heapq.heappop(nodos_no_visitados)
        distancia_actual, nodo_actual, direccion_actual = heapq.heappop(nodos_no_visitados)
        pass
        if nodo_actual == end:
            # Reconstruir el camino desde el nodo de inicio hasta el objetivo
            camino = reconstruir_camino(padres, start, end)
            return distancia_actual, camino

        for direccion in direcciones:
            #if not (direccion == direccion_actual and nodos_consecutivos>3):
            vecino = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if 0 <= vecino[0] < rows and 0 <= vecino[1] < cols and direccion!=[-x for x in direccion_actual]:
                nodos_consecutivos=consecutive_nodes(vecino,nodo_actual,padres)
                pass
                if direccion!=direccion_actual or nodos_consecutivos<5:
                    nuevo_costo = distancia_actual + matriz[vecino[0]][vecino[1]]
                    pass
                    if nuevo_costo < distances[vecino]:
                        distances[vecino] = nuevo_costo
                        heapq.heappush(nodos_no_visitados, (nuevo_costo, vecino, direccion))
                        
                        # Registrar el padre del nodo actual
                        padres[vecino] = nodo_actual
                else:
                    pass
        pass

    # Si no se puede llegar al destino
    return -1, []


print("Reading and parsing data:")
result=0
map=[]
with open(input1) as f:
    lines=f.readlines()
    for i,l in enumerate(lines):
        l=l.replace("\n","")
        map.append(list([int(x) for x in l]))

xmax=len(lines[0])
ymax=len(lines)
#print(map)

resultado,camino = dijkstra(map)

print("Result: ",resultado)
print("Camino recorrido:", camino)