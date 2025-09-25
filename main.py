# main.py
import copy
from mapa import crear_tablero, imprimir_tablero
from obstaculos import agregar_obstaculos_usuario, modificar_celda
from input_usuario import pedir_coordenadas
from Aestrella import A_star, marcar_camino

def generar_mapa_camino_limpio(mapa, camino):
    """Genera un mapa solo con el camino y el agua visible."""
    filas = len(mapa)
    columnas = len(mapa[0])
    mapa_limpio = [[" . " for _ in range(columnas)] for _ in range(filas)]
    if camino:
        for fila, col in camino:
            if mapa[fila][col] == " A ":
                mapa_limpio[fila][col] = " A "
            else:
                mapa_limpio[fila][col] = " * "
        # Marcar inicio y destino
        mapa_limpio[camino[0][0]][camino[0][1]] = " P "
        mapa_limpio[camino[-1][0]][camino[-1][1]] = " F "
    return mapa_limpio

def iniciar_tablero():
    filas = int(input("Ingrese cantidad de filas: "))
    columnas = int(input("Ingrese cantidad de columnas: "))
    mapa = crear_tablero(filas, columnas)
    agregar_obstaculos_usuario(mapa)
    print("\nTablero con obstáculos:")
    imprimir_tablero(mapa)
    return mapa, filas, columnas

def pedir_inicio_destino(mapa):
    while True:
        inicio = pedir_coordenadas("Inicio", mapa)
        destino = pedir_coordenadas("Destino", mapa)
        if inicio != destino:
            return inicio, destino
        else:
            print("Inicio y destino no pueden ser iguales, intenta de nuevo.")

def main():
    print("BIENVENIDOS AL BUSCADOR DE RUTAS")
    print(".: Camino libre\nA: Agua\nX: Obstáculo")
    
    mapa, filas, columnas = iniciar_tablero()
    mapa_original = copy.deepcopy(mapa) #guardo copia intacta
    inicio, destino = pedir_inicio_destino(mapa)
    
    camino = A_star(mapa, inicio, destino) #calculo el camino
    mapa_completo = copy.deepcopy(mapa_original)
    if camino:
        marcar_camino(mapa_completo, camino, inicio, destino)
    mapa_limpio = generar_mapa_camino_limpio(mapa_completo, camino)
    
    while True:
        print("\nOpciones:")
        print("1: Mostrar tablero completo con obstáculos y camino")
        print("2: Mostrar solo el camino más corto limpio")
        print("3: Agregar o cambiar obstáculos y recalcular camino")
        print("4: Crear un nuevo tablero")
        print("5: Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if camino:
                imprimir_tablero(mapa_completo)
            else:
                print("No hay camino calculado aún.")
                
        elif opcion == "2":
            if camino:
                imprimir_tablero(mapa_limpio)
            else:
                print("No hay camino calculado aún.")
                
        elif opcion == "3":
            print("Ingrese la celda que desea modificar:")
            fila = int(input(f"Fila (1-{filas}): ")) - 1
            columna = int(input(f"Columna (1-{columnas}): ")) - 1
            print("Tipos de celda disponibles:\n . -> Camino libre\n A -> Agua\n X -> Obstáculo")
            tipo = input("Ingrese el tipo de celda: ").strip().upper()
            tipo = f" {tipo} "  # Ajusta el formato con espacios para que coincida con el tablero
            
            if modificar_celda(mapa_original, fila, columna, tipo):
                camino = A_star(mapa_original, inicio, destino)
                mapa_completo = copy.deepcopy(mapa_original)
                if camino:
                    marcar_camino(mapa_completo, camino, inicio, destino)
                mapa_limpio = generar_mapa_camino_limpio(mapa_completo, camino)
                print("Camino recalculado con los nuevos obstáculos.")
            else:
                print("Tipo de celda inválido.")
                
        elif opcion == "4":
            mapa, filas, columnas = iniciar_tablero()
            mapa_original = copy.deepcopy(mapa)
            inicio, destino = pedir_inicio_destino(mapa)
            camino = A_star(mapa_original, inicio, destino)
            mapa_completo = copy.deepcopy(mapa_original)
            if camino:
                marcar_camino(mapa_completo, camino, inicio, destino)
            mapa_limpio = generar_mapa_camino_limpio(mapa_completo, camino)
            print("Nuevo tablero creado y camino calculado.")
            
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
