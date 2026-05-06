# Hundir_la_Flota

### `Descripción:`
Este proyecto permite jugar a *Hundir la Flota* en terminal, versión de una persona contra el ordenador. Desarrollado con el objetivo principal de practicar con el lenguaje Python.

### Características:
- Tablero de 10x10 casillas, en filas del 0 al 9.
- Seis barcos por jugador (de 4, 3 o 2 casillas) colocados aleatoriamente en el tablero. Los barcos se representan como "B"
- Turno de un disparo, el jugador selecciona las coordenadas (fila, disparo), (0,9).
- Leyenda: "~" agua (vista normal), "X" tocado, "o" agua en las casillas ya disparadas
 
### Estructura:
hundir_la_flota  

  ├── utils.py  
  
  ├── main.py  
  
  └── README.md

#### `utils.py`
Incluye las funciones principales del juego:
- crear_tablero
  -   imprimir_tablero
- colocar_barco
  -   colocar_barcos_jugador
  -  colocar_barcos_ordenador
- disparar
   -  disparo_ordenador
- juego_terminado

#### `main.py`
Archivo principal que ejecuta el juego:
- Presentación e instrucciones
- Controla el sistema de turnos
- Detecta victoria o derrota

### Para jugar:
Ejecutar el archivo principal en terminal mediante python main.py.
Los barcos se colocan automáticante y se abre el turno de disparo, el jugador dispara primero-
Introduce coordenadas para disparar (0,9), un número del 0 al 9 por fila y columna, respectivamente.
El juego finaliza cuando todos los barcos de un oponente han sido hundidos.

### Dependencias:
- **Python 3.10**
- **NumPy**
