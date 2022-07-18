import pygame
from data import *



class TileMap:
    def __init__(self, screen, size: tuple, tile_size: tuple, generator):
        # size of tilemap and sprites
        self.width, self.height = size
        self.t_size = tile_size
        # a list of all the tiles of the tile map
        self.matrix = generator
        # background and surface of the tilemap
        self.surface = screen
        
    def render(self):
        self.surface.fill(BG_COLOR)
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                pos = (col*self.t_size[0], row*self.t_size[1])
                tile_nbr = self.matrix[row][col]
                self.render_tile(tile_nbr, pos)
 
    def render_tile(self, tile_nbr, pos):
        """This function is called in a loop"""
        img = None
        match tile_nbr:
            case 0:
                return
            case 1:
                img = pygame.transform.scale(pygame.image.load('assets/environment/tiles/tiles/tile.png'), self.t_size)
            case 2:
                img = pygame.transform.scale(pygame.image.load('assets/environment/tiles/tiles/tile_top.png'), self.t_size)
        if img != None:
            self.surface.blit(img, pos)
