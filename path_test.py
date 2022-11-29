from scipy import interpolate
import numpy as np
import pygame

pygame.init()
screen = pygame.display.set_mode((720, 800))
clock = pygame.time.Clock()
screen.fill(pygame.Color('White'))

smooth = []
waypoints = []

def B_spline(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    tck, v = interpolate.splprep([x, y])
    u = np.linspace(0, 1, num=500)
    smooth = interpolate.splev(u, tck)
    return smooth

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), pos, 7, 0)
            waypoints.append(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                smooth_X, smooth_Y = B_spline(waypoints)
                screen.fill((255,255,255))
                for x,y in zip(smooth_X, smooth_Y):
                    pygame.draw.circle(screen, (255,0,0), (x,y), 2, 0)
                for point in waypoints:
                    pygame.draw.circle(screen, (0,0,0), point, 7, 0)
    pygame.display.update()
