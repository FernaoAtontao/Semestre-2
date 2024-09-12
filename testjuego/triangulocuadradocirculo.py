import pygame
pygame.init()
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("varias figuritas mover test")
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
TAMANO_TRIANGULO = 50
TAMANO_CUADRADO = 100
RADIO_CIRCULO = 50
pos_triangulo = [ANCHO // 4, ALTO // 2]
pos_cuadrado = [ANCHO // 2, ALTO // 2]
pos_circulo = [3 * ANCHO // 4, ALTO // 2]
velocidad = 5
def dibujar_triangulo(superficie, color, posicion):
    pygame.draw.polygon(superficie, color, [
        (posicion[0], posicion[1] - TAMANO_TRIANGULO),
        (posicion[0] - TAMANO_TRIANGULO, posicion[1] + TAMANO_TRIANGULO),
        (posicion[0] + TAMANO_TRIANGULO, posicion[1] + TAMANO_TRIANGULO)
    ])
def dibujar_cuadrado(superficie, color, posicion):
    pygame.draw.rect(superficie, color, pygame.Rect(posicion[0] - TAMANO_CUADRADO // 2, posicion[1] - TAMANO_CUADRADO // 2, TAMANO_CUADRADO, TAMANO_CUADRADO))
def dibujar_circulo(superficie, color, posicion):
    pygame.draw.circle(superficie, color, posicion, RADIO_CIRCULO)
correr = True
while correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
    teclas = pygame.key.get_pressed()
#triángulo WASD
    if teclas[pygame.K_w]:
        pos_triangulo[1] -= velocidad
    if teclas[pygame.K_s]:
        pos_triangulo[1] += velocidad
    if teclas[pygame.K_a]:
        pos_triangulo[0] -= velocidad
    if teclas[pygame.K_d]:
        pos_triangulo[0] += velocidad
#cuadrado IJKL
    if teclas[pygame.K_i]:
        pos_cuadrado[1] -= velocidad
    if teclas[pygame.K_k]:
        pos_cuadrado[1] += velocidad
    if teclas[pygame.K_j]:
        pos_cuadrado[0] -= velocidad
    if teclas[pygame.K_l]:
        pos_cuadrado[0] += velocidad
#círculo flechas arriba abajo izquierda derecha
    if teclas[pygame.K_UP]:
        pos_circulo[1] -= velocidad
    if teclas[pygame.K_DOWN]:
        pos_circulo[1] += velocidad
    if teclas[pygame.K_LEFT]:
        pos_circulo[0] -= velocidad
    if teclas[pygame.K_RIGHT]:
        pos_circulo[0] += velocidad
    PANTALLA.fill(NEGRO)
    dibujar_triangulo(PANTALLA, ROJO, pos_triangulo)
    dibujar_cuadrado(PANTALLA, VERDE, pos_cuadrado)
    dibujar_circulo(PANTALLA, AZUL, pos_circulo)
    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()