import pygame
import math

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Квадрат движется по полукругу и вращается")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

sz = 50
c_x, c_y = w // 2, h // 2
rad = 200
ang_sp = 0.02
rot_sp = 5

angle = 0
rotation_angle = 0
direction = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    x = c_x + rad * math.cos(angle) - sz // 2
    y = c_y + rad * math.sin(angle) - sz // 2
    square = pygame.Surface((sz, sz), pygame.SRCALPHA)
    square.fill(WHITE)
    rotated_square = pygame.transform.rotate(square, rotation_angle)
    rect = rotated_square.get_rect(center=(x + sz // 2, y + sz // 2))
    screen.blit(rotated_square, rect.topleft)
    angle += ang_sp * direction
    rotation_angle += rot_sp

    if angle > math.pi or angle < 0:
        direction *= -1
        angle += ang_sp * direction  
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
