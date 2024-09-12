import pygame

class Triangulo:
    def __init__(self, x, y, color, velocidad):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = velocidad

    def movimiento(self):
        # Añade lógica de movimiento aquí
        pass

    def dibujar(self):
        triangulo = ((0, 0), (0, 0), (0, 0))
        pygame.draw.polygon(pantalla, "Rojo", triangulo)