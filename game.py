from sys import exit
from map import TileMap
from data import *
import pygame

S_WIDTH, S_HEIGHT = 1080, 720

class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.display.set_caption("Scribble Platform Game")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        # initialize the world
        self.tile_map = TileMap(self.screen, (S_WIDTH, S_HEIGHT), (64, 64), MAP_MATRIX)
        self.tile_map.render()
    
    def run(self):
        # event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # render map
            self.tile_map.render()
            # logistic
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()