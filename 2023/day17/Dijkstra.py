import heapq

def dijkstra(matriz):
    rows, cols = len(matriz), len(matriz[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    # Inicializar las distancias con infinito para todos los nodos
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distances[start] = matriz[start[0]][start[1]]

    # Conjunto de nodos no visitados
    nodos_no_visitados = [(matriz[start[0]][start[1]], start)]

    # Direcciones de movimiento: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while nodos_no_visitados:
        distancia_actual, nodo_actual = heapq.heappop(nodos_no_visitados)

        if nodo_actual == end:
            return distancia_actual

        for direccion in direcciones:
            vecino = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])

            if 0 <= vecino[0] < rows and 0 <= vecino[1] < cols:
                nuevo_costo = distancia_actual + matriz[vecino[0]][vecino[1]]

                if nuevo_costo < distances[vecino]:
                    distances[vecino] = nuevo_costo
                    heapq.heappush(nodos_no_visitados, (nuevo_costo, vecino))

    # Si no se puede llegar al destino
    return -1

# Ejemplo de uso
matriz_costos = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = dijkstra(matriz_costos)

if resultado != -1:
    print(f"El costo mínimo para llegar de (0,0) a ({len(matriz_costos)-1},{len(matriz_costos[0])-1}) es: {resultado}")
else:
    print("No hay camino válido.")
