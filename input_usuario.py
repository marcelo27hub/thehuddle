# input_usuario.py
def pedir_coordenadas(mensaje, tablero):
    while True:
        try:
            fila = int(input(f"Ingrese fila de {mensaje} (1-{len(tablero)}): ")) - 1
            columna = int(input(f"Ingrese columna de {mensaje} (1-{len(tablero[0])}): ")) - 1
        except ValueError:
            print("Ingresaste algo que no es un número entero, intenta de nuevo!")
            continue
        if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
            if tablero[fila][columna] == " . ":
                return (fila, columna)
            else:
                print("Celda ocupada por un obstáculo")
        else:
            print("Coordenadas fuera del tablero, intenta de nuevo!")
