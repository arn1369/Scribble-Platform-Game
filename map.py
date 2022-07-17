import pygame
from tile import Tile

class TileMap:
    def __init__(self, size: tuple, tile_size: tuple):
        # size of tilemap and sprites
        self.width, self.height = size
        self.tile_w, self.tile_h = tile_size
        #self.bridge_tile = self.create_tile('assets/bridge.png', (50, 50))

    def create_tile(self, _path, _pos):
        tile = pygame.sprite.Sprite()
        tile.image = pygame.image.load(_path)
        tile.rect = tile.image.get_rect(center=_pos)
