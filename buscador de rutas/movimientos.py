def movimientos_posibles(nodo, tablero):
    fila, columna = nodo #(fila, columna) representa como nodo
    movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)] #abajo, derecha, arriba, izquierda
    vecinos = []
    
    for df, dc in movimientos: #por cada direccion en los movimientos posibles
        nueva_fila = fila + df 
        nueva_columna = columna +dc
        if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]): #si la nueva fila y nueva columna esta dentro del tablero
            celda = tablero[nueva_fila][nueva_columna] #crea una celda con eso 
            
            if celda == " . " or celda == " F ": #si mi celda es un punto o f
                vecinos.append(((nueva_fila, nueva_columna), 1)) #agrega esos nuevas posiciones en vecinos  con valor 1
            elif celda == " A ": #si es A
                vecinos.append(((nueva_fila, nueva_columna), 1.5)) #agrega con un costo mayor
    return vecinos #retorno mi vecino