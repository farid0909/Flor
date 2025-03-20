import pygame
import random
import math
# Inicializar Pygame
pygame.init()
# Configurar pantalla
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flor Interactiva")
# Colores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
# Generar color aleatorio
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
# Clase de la flor
class Flor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.petalo_color = random_color()
        self.centro_color = YELLOW
    def draw(self):
        # Dimensiones de los pétalos
        petalo_ancho = 50
        petalo_alto = 30
        radio_petalo = 40  # Distancia entre pétalos y centro
        # Dibujar pétalos en círculo usando coordenadas polares
        num_petalos = 6  # Cantidad de pétalos
        for i in range(num_petalos):
            angle = (math.pi * 2 / num_petalos) * i  # Ángulo en radianes
            px = self.x + math.cos(angle) * radio_petalo - petalo_ancho // 2
            py = self.y + math.sin(angle) * radio_petalo - petalo_alto // 2
            pygame.draw.ellipse(screen, self.petalo_color, (px, py, petalo_ancho, petalo_alto))
        
        # Dibujar centro
        pygame.draw.circle(screen, self.centro_color, (self.x, self.y), 25)
        # Dibujar tallo
        pygame.draw.rect(screen, GREEN, (self.x - 5, self.y + 25, 10, 100))
    def check_click(self, pos):
        px, py = pos
        if (self.x - 25 < px < self.x + 25) and (self.y - 25 < py < self.y + 25):
            self.petalo_color = random_color()
# Crear flor centrada
flor = Flor(WIDTH//2, HEIGHT//2)
# Loop principal
running = True
while running:
    screen.fill(WHITE)
    flor.draw()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flor.check_click(event.pos)
pygame.quit()