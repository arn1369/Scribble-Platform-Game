import math
from data import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, model: str, attack: float=0, size: tuple=(0,0)):
        super().__init__()
        self.model = model
        self.attack = attack
        self.size = size
        # create the sprite from the model
        self.get_sprite_from_model()


    def get_sprite_from_model(self):
        match self.model:
            case 'sword':
                _path = 'assets/environment/tiles/items/item_sword.png'
                self.attack = 10
            case 'bow':
                _path = 'assets/environment/tiles/items/item_gun.png'
                self.attack = 7
            case 'spear':
                _path = 'assets/environment/tiles/items/item_spear.png'
                self.attack = 13
            case 'helmet':
                _path = 'assets/environment/tiles/items/item_helmet.png'
                self.attack = 0
            case _:
                _path = None
                self.attack =0
        if _path is not None:
            self.image = pygame.image.load(_path)
            if self.size > (0,0):
                self.image = pygame.transform.scale(pygame.image.load(_path), self.size)
            tmp_rect = self.image.get_rect()
            self.rect = pygame.Rect(tmp_rect.topleft[0]+20, tmp_rect.topleft[1]+2, 24, 60)
        # setup the origin image (and rotate so it face the cursor then)
        self.image = pygame.transform.rotate(self.image, -90)
        self.origin_img = self.image
    
    def draw(self, surface):
        surface.blit(self.image, self.rect.center)
    
    def update(self):
        # rotate the weapon to mouse
        pos = self.rect.center
        mouse_pos = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_pos[0]-pos[0], mouse_pos[1]-pos[1]
        angle = (180/math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.origin_img, int(angle))
        self.rect = self.image.get_rect(center=pos)
        
