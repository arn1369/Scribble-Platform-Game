import pygame
from data import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, img_path: str):
        """I should create parameters if I want to add 
        multiplayer but for now, just putting values for attributes"""
        super().__init__()
        # setup health
        self.health = 100
        # setup GFX
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect(center=pos)
        # setup move
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.is_grounded = True
    
    def apply_gravity(self):
        self.direction.y += self.gravity
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
    
    def update(self):
        self.get_input()