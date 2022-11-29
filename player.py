from data import *
from weapon import Weapon


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, img_path: str): 
        super().__init__()
        # setup health
        self.health = 100
        # setup GFX
        self.image = pygame.image.load(img_path).convert_alpha()
        # //? modify that to change the player collider 
        self.rect = pygame.rect.Rect(pos[0], pos[1], 40, TILE_SIZE-4)
        # setup move
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 700
        self.gravity = 50
        self.jump_speed = -16
        self.is_grounded = True
        # weapon
        self.weapon = Weapon('sword')
        
    
    def apply_gravity(self):
        self.direction.y += self.gravity * DeltaTime.dt
        self.rect.y += self.direction.y
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        # move left
        if keys[pygame.K_a] and self.rect.left > 0:
            self.direction.x = -1            
        # move right
        elif keys[pygame.K_d] and self.rect.right < S_WIDTH:
            self.direction.x = 1
        # jump
        elif keys[pygame.K_SPACE] and self.is_grounded:
            self.jump()
        else:
            self.direction.x = 0
    
    def jump(self):
        self.direction.y = self.jump_speed
        self.is_grounded = False

    def draw(self, render):
        render.blit(self.image, self.rect)
        if self.weapon:
            self.weapon.draw(render)
        
        # //* DEBUG : show the center of the sprite
        pygame.draw.rect(render, pygame.Color('red'), self.weapon.rect, 2)

    
    def update(self):
        # get the input for the player
        self.get_input()
        
        if self.weapon:
            # place the weapon for the player
            self.weapon.rect.center = self.rect.center
            self.weapon.update()