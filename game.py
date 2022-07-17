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

        # background
        self.bg_img = pygame.transform.scale(pygame.image.load('assets/background.jpeg'), (S_WIDTH, S_HEIGHT))

        # initialize the world
        self.tile_map = TileMap((S_WIDTH, S_HEIGHT), (64, 64))

    
    def run(self):
        # event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # background
            self.screen.blit(self.bg_img, (0,0))
            # logistic
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()