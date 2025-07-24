#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Juego de Tres en Raya (Tic-Tac-Toe)
Creado con Claude MCP para GitHub
"""

class TresEnRaya:
    def __init__(self):
        # Tablero vacío representado como lista de 9 elementos
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'
    
    def mostrar_tablero(self):
        """Muestra el tablero de juego en formato visual"""
        print("\n   |   |   ")
        print(f" {self.tablero[0]} | {self.tablero[1]} | {self.tablero[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.tablero[3]} | {self.tablero[4]} | {self.tablero[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.tablero[6]} | {self.tablero[7]} | {self.tablero[8]} ")
        print("   |   |   ")
        print()
    
    def mostrar_posiciones(self):
        """Muestra las posiciones numeradas para guiar al jugador"""
        print("\nPosiciones del tablero:")
        print("   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   ")
        print()
    
    def hacer_movimiento(self, posicion):
        """
        Realiza un movimiento en la posición especificada
        posicion: número del 1 al 9
        """
        if posicion < 1 or posicion > 9:
            return False
        
        indice = posicion - 1  # Convertir a índice 0-8
        
        if self.tablero[indice] == ' ':
            self.tablero[indice] = self.jugador_actual
            return True
        return False
    
    def verificar_ganador(self):
        """Verifica si hay un ganador"""
        # Todas las combinaciones ganadoras posibles
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combo in combinaciones_ganadoras:
            if (self.tablero[combo[0]] == self.tablero[combo[1]] == 
                self.tablero[combo[2]] != ' '):
                return self.tablero[combo[0]]
        return None
    
    def tablero_lleno(self):
        """Verifica si el tablero está lleno (empate)"""
        return ' ' not in self.tablero
    
    def cambiar_jugador(self):
        """Cambia entre jugadores X y O"""
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
    
    def jugar(self):
        """Función principal del juego"""
        print("🎮 ¡Bienvenido al Tres en Raya!")
        print("=" * 40)
        print("Jugador 1: X")
        print("Jugador 2: O")
        print("=" * 40)
        
        self.mostrar_posiciones()
        
        while True:
            self.mostrar_tablero()
            print(f"Turno del jugador {self.jugador_actual}")
            
            try:
                posicion = int(input("Elige una posición (1-9): "))
            except ValueError:
                print("❌ Por favor, ingresa un número válido del 1 al 9")
                continue
            
            if self.hacer_movimiento(posicion):
                # Verificar si hay ganador
                ganador = self.verificar_ganador()
                if ganador:
                    self.mostrar_tablero()
                    print(f"🎉 ¡El jugador {ganador} ha ganado!")
                    break
                
                # Verificar empate
                if self.tablero_lleno():
                    self.mostrar_tablero()
                    print("🤝 ¡Es un empate!")
                    break
                
                # Cambiar de jugador
                self.cambiar_jugador()
            else:
                print("❌ Movimiento inválido. Esa posición ya está ocupada o no existe.")

def main():
    """Función principal para ejecutar el juego"""
    while True:
        juego = TresEnRaya()
        juego.jugar()
        
        print("\n" + "=" * 40)
        jugar_otra = input("¿Quieres jugar otra partida? (s/n): ").lower()
        if jugar_otra != 's' and jugar_otra != 'si':
            print("👋 ¡Gracias por jugar! ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
