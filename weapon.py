import pygame
from data import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, model: str, attack: float, health: int, size: tuple):
        super().__init__()
        self.model = model
        self.size = size
        # create the sprite from the model
        self.get_sprite_from_model()


    def get_sprite_from_model(self):
        match self.model:
            case 'sword':
                _path = 'assets/environment/tiles/items/item_sword.png'
            case 'bow':
                _path = 'assets/environment/tiles/items/item_gun.png'
            case 'spear':
                _path = 'assets/environment/tiles/items/item_spear.png'
            case 'helmet':
                _path = 'assets/environment/tiles/items/item_helmet.png'
        if img != None:
            img = pygame.transform.scale(pygame.image.load(_path), self.size)
            self.image = img
            self.rect = self.image.get_rect()