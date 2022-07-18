import pygame
from player import Player
from data import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('purple') # no texture for now
        self.rect = self.image.get_rect(topleft=pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift

class Level:
    def __init__(self, level_data, surface) -> None:
        # setup attributes
        self.display_s = surface
        self.level_data = level_data
        self.world_shift = 0
        # setup the tiles
        self.tiles = pygame.sprite.Group()
        # create the player
        self.player = pygame.sprite.GroupSingle()

        # adding all the tiles to the group at good pos
        tile = None
        for row_index, row in enumerate(self.level_data):
            for col_index, cell in enumerate(row):
                print(f"{row_index};{col_index} : {cell}")
                x, y = col_index*TILE_SIZE, row_index*TILE_SIZE
                match cell:
                    case 'X':
                        self.player.add(Player((x, y), 'assets/players/characters/player/character_squareGreen.png'))
                    case 1:
                        tile = Tile((x,y), TILE_SIZE)
                if tile != None:
                    self.tiles.add(tile)

    def horizontal_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        # collisions between the player and the tile map
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collisions(self):
        player = self.player.sprite
        player.apply_gravity()
        # collisions between the player and the tile map
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def render(self):
        # draw and update the tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_s)

        # draw and update the player
        self.player.update()
        self.horizontal_collisions()
        self.vertical_collisions()
        self.player.draw(self.display_s)
