import pygame
import math

def relation():
    pass

def march_points():
    pass


pygame.init()

width, height = 500, 500

window = pygame.display.set_mode((width, height))

running = True

points = []

for i in range(0, 359, 16):
    x = math.cos(math.radians(i)) * 80 + width  / 2
    y = math.sin(math.radians(i)) * 80 + height / 2 
    points.append((x, y))

while running:
    
    window.fill((255, 255, 255))
    
    for point in points:
        pygame.draw.circle(window, (0, 0, 0), point, 5, 1)
        
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
