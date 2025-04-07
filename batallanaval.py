# Simple Battleship Game
import random

n: int = 10
cantidad_barcos: int = 15
intentos_max: int = 40

tablero_barcos: list[list[str]] = []
tablero_jugador: list[list[str]] = []

# Initialize both boards
for i in range(n):
    tablero_barcos.append([" "] * n)
    tablero_jugador.append([" "] * n)

def agregar_barcos(cantidad: int):
    for i in range(cantidad):
        x: int = random.randint(0, n-1)
        y: int = random.randint(0, n-1)
        tablero_barcos[x][y] = "X"

def imprimir_tablero_barcos():
    print("   " + " ".join(str(i+1) for i in range(n)))
    for i in range(n):
        print(f"{i+1:2d} {' '.join(tablero_barcos[i])}")

def imprimir_tablero_jugador():
    print("   " + " ".join(str(i+1) for i in range(n)))
    for i in range(n):
        print(f"{i+1:2d} {' '.join(tablero_jugador[i])}")

def disparar():
    try:
        x: int = int(input("Elegí la fila para disparar (1-10): "))
        y: int = int(input("Elegí la columna para disparar (1-10): "))
        
        # Convert 1-10 coordinates to 0-9 indices
        x = x - 1
        y = y - 1
        
        if x < 0 or x >= n or y < 0 or y >= n:
            print(f"Las coordenadas deben estar entre 1 y 10")
            return False
            
        if tablero_barcos[x][y] == "X":
            tablero_jugador[x][y] = "X"
            print("¡Hundido!")
        else:
            tablero_jugador[x][y] = "O"
            print("Agua")
        return True
    except ValueError:
        print("Por favor ingresa números válidos")
        return False

def main():
    agregar_barcos(cantidad_barcos)
    intentos = 0
    barcos_hundidos = 0
    
    while intentos < intentos_max and barcos_hundidos < cantidad_barcos:
        print(f"\nIntentos: {intentos}/{intentos_max} | Barcos hundidos: {barcos_hundidos}/{cantidad_barcos}")
        imprimir_tablero_jugador()
        
        if disparar():
            intentos += 1
            # Count sunk ships after each successful move
            barcos_hundidos = sum(row.count("X") for row in tablero_jugador)
    
    # Game over
    print("\nJuego terminado")
    if barcos_hundidos == cantidad_barcos:
        print("¡Ganaste! Hundiste todos los barcos.")
    else:
        print("Se acabaron los intentos. Perdiste.")
    
    print("\nTablero de barcos:")
    imprimir_tablero_barcos()

main()