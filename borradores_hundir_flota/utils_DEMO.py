#PASO 0,  
import numpy as np
import random

def crear_tablero(): 
        return np.full((10, 10), "~", dtype=str) 
'''
    PASO 1
    Crea un tablero de 10x10, todas las casillas son str.
'''

def imprimir_tablero(tablero, ocultar_barcos=True):
    print("   " + " ".join(str(i) for i in range(10)))  # Numeros de columnas
    for i in range(10):
        if ocultar_barcos:# xa el tablero de disparos
            fila_mostrar = ['~' if tablero[i][j] == 'B' else tablero[i][j] for j in range(10)]
        else:
            fila_mostrar = [tablero[i][j] for j in range(10)]
        print(f"{i}  " + " ".join(fila_mostrar))  # Numero de fila y contenido

'''
   PASO 2
   Imprime un tablero con los elementos básicos agua '~' y barcos 'B'.
   Ocultar barcos es booleano: False es la posición real, True el jugador ve agua.
'''

def colocar_barco(tablero, tamano):
    while True:
        orientacion = random.choice(['H', 'V'])  # H: Horizontal, V: Vertical
        if orientacion == 'H': # H, la fila fija y la columna variable
            fila = random.randint(0, 9)
            col = random.randint(0, 9 - tamano)  # xa que quepa
            if all(tablero[fila][col + i] == '~' for i in range(tamano)):#sólo en casilla vacía
                for i in range(tamano):
                    tablero[fila][col + i] = 'B'  
                return
        else:  # V, columna fija y fila variable
            fila = random.randint(0, 9 - tamano)
            col = random.randint(0, 9)
            if all(tablero[fila + i][col] == '~' for i in range(tamano)):
                for i in range(tamano):
                    tablero[fila + i][col] = 'B'
                return
'''
    PASO 3
    Coloca un barco de forma aleatoria.
    No superpone en casillas pero puede aparecer en casilla contígua.
    Define tamaño y tablero.
'''

def colocar_barcos_jugador():
    tablero = crear_tablero()
    barcos = [4, 3]  
    for tamano in barcos:
        colocar_barco(tablero, tamano)
    return tablero
'''
    PASO 4
    Coloca los 2 barcos en tablero del jugador aleatoriamente.
    Define el tamaño de los barcos: 1 de 4 casillas, 1 de 3 casillas.
'''

def colocar_barcos_ordenador():
    tablero = crear_tablero()
    barcos = [4, 3]
    for tamano in barcos:
        colocar_barco(tablero, tamano)
    return tablero
'''
   PASO 5
    Coloca los barcos en tablero del ordenador.
    Es igual que colocar_barcos_jugador.
'''

def disparar(tablero_barcos, tablero_disparos, fila, col):
    if tablero_disparos[fila][col] != '~': # xa no disparar dos veces en el mismo sitio
        return "ya disparado"
    if tablero_barcos[fila][col] == 'B': # # si hay barco en el tablero oculto
        tablero_disparos[fila][col] = 'X'  # tocado, marca X en tablero disparos
        tablero_barcos[fila][col] = 'H'    # xa que el jugador no se confunda 
        return "tocado"
    else:
        tablero_disparos[fila][col] = 'o'  # diferencia agua en casillas ya disparadas
        return "agua"

'''
    PASO 6
    Turno de disparo del jugador.
    Coordenadas del disparo [fila] [columna], las introduce el jugador.
    No permite disparar dos veces en el mismo sitio.
    Refleja el resultado del disparo en tablero del jugador:
    'X' indica barco tocado, 'H' barco hundido, 'o' agua (cambia por '~').
'''

def disparo_ordenador(tablero_barcos_jugador, tablero_disparos_ordenador):
    while True:
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        if tablero_disparos_ordenador[fila][col] == '~': # ~ = nunca disparó aquí
            resultado = disparar(tablero_barcos_jugador, tablero_disparos_ordenador, fila, col)
            return fila, col, resultado
'''
    PASO 7
    Turno de disparo del ordenador.
    El ordenador elige coordenadas aleatorias, también usa la función disparar.
'''

def juego_terminado(tablero_barcos):
    for i in range(10):
        for j in range(10):
            if tablero_barcos[i][j] == 'B':
                return False  # Todavia quedan barcos
    return True  # Todos los barcos hundidos
'''
    PASO 8
    La batalla termina cuando todos los barcos han sido hundidos, 
    no quedan 'B's en el tablero.
'''