import pygame
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Корабль по синусоиде')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

amplitude = 100  
frequency = 0.01  
speed = 2  
ship_width = 60
ship_height = 30
flag_height = 20
x = 0
y = height // 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    x += speed
    y = height // 2 + amplitude * math.sin(frequency * x)
    

    if x > width:
        x = -ship_width

    screen.fill(WHITE)
    for i in range(width):
        sine_y = height // 2 + amplitude * math.sin(frequency * i)
        pygame.draw.circle(screen, GREEN, (i, int(sine_y)), 1)
    pygame.draw.ellipse(screen, BLUE, (x, y, ship_width, ship_height))
    pygame.draw.rect(screen, RED, (x+ship_width // 2 - 2, y - flag_height, 4, flag_height))
    pygame.draw.polygon(screen, RED, [
        (x + ship_width // 2 - 2, y - flag_height),
        (x + ship_width // 2 - 2, y - flag_height + 10),
        (x + ship_width // 2 + 10, y - flag_height + 5)
        ])
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
