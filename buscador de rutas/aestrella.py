import heapq
from movimientos import movimientos_posibles

def heuristica(a, b):
    # distancia de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_star(tablero, inicio, destino):
    abiertos = []
    heapq.heappush(abiertos, (0, inicio, [inicio], 0))  
    # (f, nodo, camino, g)

    visitados = {}

    while abiertos: #mientras haya nodo en la frontera
        f, nodo, camino, g = heapq.heappop(abiertos)  #saca el de menor f

        if nodo == destino: #si llego al destino
            return camino #devuelve el camino

        if nodo in visitados and visitados[nodo] <= g: #si ya visite con menor costo 
            continue

        visitados[nodo] = g #guardo el mejor costo hasta ahora

        for vecino, costo in movimientos_posibles(nodo, tablero):
            g_nuevo = g + costo #costo acumulado
            f_nuevo = g_nuevo + heuristica(vecino, destino)
            heapq.heappush(abiertos, (f_nuevo, vecino, camino + [vecino], g_nuevo))

    return None

def marcar_camino(tablero, camino, inicio, destino):
    # No borra obstáculos, solo marca el camino
    for fila, col in camino:
        if (fila, col) == inicio:
            tablero[fila][col] = " P "#punto de inicio 
        elif (fila, col) == destino:
            tablero[fila][col] = " F " #destino
        elif tablero[fila][col] == " . ":
            tablero[fila][col] = " * " #marca el camino
        elif tablero[fila][col] == " A ":
            tablero[fila][col] = " A "  # mantener agua visible en el camino
