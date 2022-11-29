import pygame


class DeltaTime:
    dt = 0

# max fps
FPS = 60

# tile
TILE_SIZE = 60

BG_COLOR = (150, 150, 150)
S_WIDTH, S_HEIGHT = TILE_SIZE*15+4, TILE_SIZE*7+4 # tile_size multiple

# player
ACC = 0.3
FRICTION = -0.1

MAP_MATRIX = [
    [1, 0, 0, 0, 'X', 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]