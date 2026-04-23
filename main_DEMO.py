import random
import numpy as np
from utils_DEMO import (
    crear_tablero,
    imprimir_tablero,
    colocar_barco,
    colocar_barcos_jugador,
    colocar_barcos_ordenador,
    disparar,
    juego_terminado,
    disparo_ordenador)

def main():
    print(":" * 60)
    print("     BIENVENIDO A HUNDIR LA FLOTA - JUGADOR/ORDENADOR")
    print(":" * 60)
    print("\nINSTRUCCIONES:")
    print("- Tablero de 10x10 (coordenadas del 0 al 9), primera coordenada fila, segunda columna")
    print("- Tienes dos barcos: un portaviones (4 casillas) y un submarino (3 casillas)")
    print("- El ordenador tiene los mismos barcos que tú")
    print("- Turnos alternos de un disparo: empiezas disparando tú")
    print("- La batalla termina cuando un jugador hunde todos los barcos enemigos")
    input("\nPresiona ENTER para comenzar...")
    '''
    Funcion principal que controla el flujo del juego.
    Da la bienvenida y las instrucciones de juego
    Alterna turnos entre jugador y ordenador hasta que alguien gana.
    '''
    # Imprime los tableros
    print("\n" + "=" * 60)
    print("POR FAVOR ESPERE, COLOCANDO BARCOS...")
    print("=" * 60)

    # Tableros jugador, registra disparos jugador-ordenador
    tablero_barcos_jugador = colocar_barcos_jugador()
    tablero_disparos_jugador = crear_tablero()  
    
    # Tableros del ordenador, registra disparos ordenador-jugador
    tablero_barcos_ordenador = colocar_barcos_ordenador()
    tablero_disparos_ordenador = crear_tablero()  
    
    print("Barcos colocados aleatoriamente")

    # Estadistica
    disparos_jugador = 0
    disparos_ordenador = 0
    
    # Bucle principal del juego
    turno_jugador = True  # Empieza el jugador 
    
    while True:
        if turno_jugador:
            print("\n" + ":" * 60)
            print("TU TURNO - TABLERO DE DISPAROS (al contrincante):")
            print(":" * 60)
            imprimir_tablero(tablero_disparos_jugador, ocultar_barcos=True)
            
            print("\n" + "-" * 60)
            print("TUS BARCOS")
            print("-" * 60)
            imprimir_tablero(tablero_barcos_jugador, ocultar_barcos=False)
            
            # Solicita coordenadas al jugador para disparar
            while True:
                try:
                    print("\n" + "-" * 60)
                    fila = int(input("Ingresa la coordenada fila (0-9): "))
                    col = int(input("Ingresa la coordenada columna (0-9): "))
                    
                    if fila < 0 or fila > 9 or col < 0 or col > 9:
                        print("Coordenadas invalidas. Deben estar entre 0 y 9.")
                        continue
                    
                    # Dispara
                    resultado = disparar(tablero_barcos_ordenador, tablero_disparos_jugador, fila, col)
                    
                    if resultado == "ya_disparado":
                        print("¿Otra vez aquí?, ¡madre mía, ponte gafas!")
                        continue
                    elif resultado == "tocado":
                        print("\n¡Toma petardo, Ricardo!")
                    else:
                        print("\nAguita para baldear la cubierta")
                    
                    disparos_jugador += 1
                    break
                    
                except ValueError:
                    print("Por favor, ingresa números validos.")
            
            # Para terminar el juego
            if juego_terminado(tablero_barcos_ordenador):
                print("\n" + "=" * 60)
                print("¡BRAVO PACIFISTA! HAS DEJADO AL ORDENADOR SIN FLOTA!")
                print(f"Has disparado {disparos_jugador} pepinos.")
                print(f"El ordenador ha disparado {disparos_ordenador} pepinos.")
                print("=" * 60)
                
                # Tableros finales
                print("\nTABLERO FINAL DEL ORDENADOR (tus disparos):")
                imprimir_tablero(tablero_disparos_jugador, ocultar_barcos=False)
                print("\nTABLERO FINAL DEL JUGADOR (disparos del ordenador):")
                imprimir_tablero(tablero_disparos_ordenador, ocultar_barcos=False)
                break
            
            # Cambio de turno
            turno_jugador = False
            input("\nFin de tu turno. Presiona ENTER para el turno del ordenador...")
            
        else:
            # ===== TURNO DEL ORDENADOR =====
            print("\n" + "=" * 60)
            print("TURNO DEL ORDENADOR")
            print("=" * 60)
            
            # tablero del jugador con disparos recibidos
            print("\nDisparos recibidos")
            print("X = Tocado | o = Agua | B = Barco intacto | ~ = Sin disparar")
            print("-" * 60)
            imprimir_tablero(tablero_disparos_ordenador, ocultar_barcos=False)
            
            # Ordenador dispara
            fila, col, resultado = disparo_ordenador(tablero_barcos_jugador, tablero_disparos_ordenador)
            disparos_ordenador += 1
            
            print(f"\nEnemigo dispara en ({fila}, {col})...")
            if resultado == "tocado":
                print("!Tocado¡")
            else:
                print("Ha fallado")
            
            # Para terminar el juego
            if juego_terminado(tablero_barcos_jugador):
                print("\n" + "=" * 60)
                print("¡SE ACABÓ LO QUE SE DABA! te has quedado sin flota.")
                print(f"Disparos del ordenador: {disparos_ordenador}")
                print(f"Tus disparos: {disparos_jugador}")
                print("=" * 60)
                
                # Tableros finales
                print("\nTABLERO FINAL DEL JUGADOR (tus barcos y disparos recibidos):")
                imprimir_tablero(tablero_disparos_ordenador, ocultar_barcos=False)
                break
            
            # Cambio turno
            turno_jugador = True
            input("\nFin del turno del ordenador. Presiona ENTER para tu turno...")

if __name__ == "__main__":
    main()