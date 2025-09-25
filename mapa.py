#lista de listas
def crear_tablero(filas, columnas):
    
    tablero = []
    for f in range(filas): #recorro cada fila
        fila = []
        for j in range(columnas): #recorro cada columna
            fila.append(" . ") #agrego celdas vacias como " . "
        tablero.append(fila) #agrego cada fila en tablero
        
    return tablero #retorno mi tablero
            


 #poner esto en el main
def imprimir_tablero(tablero):
    for fila in tablero: #por cada fila en tablero
        print(" ".join(fila)) # uno los elementos como uno 