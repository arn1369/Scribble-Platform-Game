from data import *
from sys import exit
from map import Level


class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.clock = pygame.time.Clock()

        # background
        self.bg = pygame.Surface((S_WIDTH, S_HEIGHT))
        self.bg.fill('lightgray')

        # cursor
        self.cursor_img = pygame.image.load('assets/players/crosshair.png')
        self.cursor_rect = self.cursor_img.get_rect(center=pygame.mouse.get_pos())

        # initialize the world
        self.level = Level(MAP_MATRIX)

    def cursor(self):
        self.cursor_rect.center = pygame.mouse.get_pos()
        self.screen.blit(self.cursor_img, self.cursor_rect)
    
    def run(self):
        # event loop
        while True:
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            # background
            self.screen.blit(self.bg, (0, 0))
            # render map
            self.level.draw(self.screen)
            self.level.update()


            # pointer 
            self.cursor()
            # logistic
            pygame.display.update()
            # FPS handling
            pygame.display.set_caption(f"FPS : {str(round(self.clock.get_fps()))}")
            DeltaTime.dt = self.clock.tick(FPS)/1000

game = Game()
game.run() 