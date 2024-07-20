import pygame
import math
import random
import numpy as np

def relation(x, y, points, s):
    sum = 0
    for point in points:
        numer = (point[0] - x) ** 2 + (point[1] - y) ** 2
        denom = 2 * (s ** 2)
        sum += math.exp(-numer / denom)
    return sum

def getGradx(x, y, points, s):
    sum = 0
    for point in points:
        numer = (point[0] - x) ** 2 + (point[1] - y) ** 2
        denom = 2 * (s ** 2)
        sum += math.exp(-numer / denom) * (point[0] - x)
    return (-1 / (s ** 2)) * sum

def getGrady(x, y, points, s):
    sum = 0
    for point in points:
        numer = (point[0] - x) ** 2 + (point[1] - y) ** 2
        denom = 2 * (s ** 2)
        sum += math.exp(-numer / denom) * (point[1] - y)
    return (-1 / (s ** 2)) * sum

def march_points(step, points, weights, s, t):
    ascend = 0
    for i, point in enumerate(points):
        x = getGradx(point[0], point[1], weights, s)
        y = getGrady(point[0], point[1], weights, s)
        
        if relation(point[0], point[1], weights, s) > t:
            ascend = 1
        else:
            ascend = -1
        
        points[i] = (point[0] + ascend * step * x, point[1] + ascend * step * y)


pygame.init()

width, height = 500, 500

window = pygame.display.set_mode((width, height))

running = True

points = []

for i in np.arange(0.0, 360.0, 0.5):
    x = math.cos(math.radians(i)) * 80 + width  / 2 + random.randint(0, 20)
    y = math.sin(math.radians(i)) * 80 + height / 2 + random.randint(0, 20)
    points.append((x, y))
    
point2 = (width / 2 + 50, height / 2)
leap = 10

while running:
    
    window.fill((255, 255, 255))
    
    for point in points:
        pygame.draw.circle(window, (0, 0, 0), point, 2.5, 1)
    
    march_points(100, points, [(width / 2 - 50, height / 2), point2],  30, 0.1)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP or event.key == ord('w'):
                point2 = (point2[0], point2[1] - leap)
                print("up")
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                point2 = (point2[0] - leap, point2[1])
                print("left")
            if event.type == pygame.K_DOWN or event.key == ord('s'):
                point2 = (point2[0], point2[1] + leap)
                print("down")
            if event.type == pygame.K_RIGHT or event.key == ord('d'):
                point2 = (point2[0] + leap, point2[1])
                print("right")
