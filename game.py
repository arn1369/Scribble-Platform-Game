from sys import exit
from map import Level
from player import Player
from data import *
import pygame


class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.display.set_caption("Scribble Platform Game")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.clock = pygame.time.Clock()

        # background
        self.bg = pygame.Surface((S_WIDTH, S_HEIGHT))
        self.bg.fill('lightgray')

        # initialize the world
        self.level = Level(MAP_MATRIX, self.screen)
    
    def run(self):
        # event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # background
            self.screen.blit(self.bg, (0, 0))
            # render map
            self.level.render()
            # logistic
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()