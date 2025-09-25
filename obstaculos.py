import random #importo ramdon
#creo mi funcion para agregar mis obstaculos 
def agregar_obstaculo(tablero, fila, columna, tipo):
    
    filas = len(tablero)
    columnas = len(tablero[0])
    #si en la posicion donde quiere agregar esta dentro de los limites los agrega
    if 0 <= fila < filas and 0<= columna < columnas:
        tablero[fila][columna]= f"{tipo}" #elige poner el tipo que elija
    else:
        print("coordenadas fuera del rango") #si no esta en el rango
    #defino mi funcion para que el usuario agregue    
def agregar_obstaculos_usuario(tablero):
    tipos = {
        " A " : "Agua",
        " X " : "zona bloqueada"
    }        
    
    for tipo, nombre in tipos.items(): #por cada tipo y nombre en items
        cantidad = int(input(f"ingrese la cantidad de {nombre}: ")) #pregunta al usuario la cantidad de obstaculos que pondra el usuario
        filas = len(tablero)
        columnas = len(tablero[0])
        #aca inicializamos para que ponga los obstaculos de manera ramdon
        puestos = 0
        while puestos < cantidad: 
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            if tablero[fila][columna] == " . ":
                agregar_obstaculo(tablero, fila, columna, tipo) 
                
                puestos +=1    
#creo mi funcion para modificar celda
def modificar_celda(tablero, fila, columna, tipo):
    if tipo in [" . ", " A ", " X "]: #aca si el tipo esta en esta  lista 
        tablero[fila][columna] = tipo #reemplaza por el tipo que pidio el usuario cambiar
        return True #retorna true si se puede hacer el cambio
    return False #aca si no puede hacer el cambio

            