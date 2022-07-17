from sys import exit
from map import TileMap
import pygame

S_WIDTH, S_HEIGHT = 800, 600

class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.display.set_caption("Scribble Platform Game")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.clock = pygame.time.Clock()

        # initialize the world
        self.tile_map = TileMap((S_WIDTH, S_HEIGHT), (64, 64))

    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.clock.tick(60)
            # update the whole screen
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()