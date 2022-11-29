from player import Player
from data import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, img_name=None) -> None:
        super().__init__()
        if img_name != None:
            #TRICK: Setting the tile size to 60 (img=64x64) so they're aligned
            # so collider is at 60, but img is at 64
            self.image = pygame.image.load(f'assets/environment/tiles/tiles/{img_name}')
        else:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill('purple') # no texture
        #self.rect = pygame.Rect(pos[0], pos[1], TILE_SIZE, TILE_SIZE)
        self.rect = self.image.get_rect(center=pos)
        self.rect.x += 32
        self.rect.y += 32
    
    def update(self, shift=(0,0)):
        self.rect.x += shift[0]
        self.rect.y += shift[1]

class Level:
    def __init__(self, level_data) -> None:
        # setup attributes
        self.level_data = level_data
        self.world_shift = (0,0)
        # setup the tiles
        self.tiles = pygame.sprite.Group()
        # create the player
        self.player = pygame.sprite.GroupSingle()

        # adding all the tiles to the group at good pos
        tile = None
        for row_index, row in enumerate(self.level_data):
            for col_index, cell in enumerate(row):
                #DEBUG print(f"{row_index};{col_index} : {cell}")
                x, y = col_index*TILE_SIZE, row_index*TILE_SIZE
                match cell:
                    case 'X':
                        self.player.add(Player((x, y), 'assets/players/characters/player/character_squareGreen1.png'))
                    case 1:
                        tile = Tile((x,y), 'tile.png')
                    case 2:
                        tile = Tile((x,y), 'tile_brick.png')
                if tile != None:
                    self.tiles.add(tile)

    def horizontal_collisions(self):
        player = self.player.sprite
        # move the player
        player.rect.x += player.direction.x * player.speed * DeltaTime.dt
        # collisions between the player and the tile map
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left       

    def vertical_collisions(self):
        player = self.player.sprite
        # apply gravity to the player
        player.apply_gravity()
        # collisions between the player and the tile map
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # ground
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_grounded = True
                # ceiling
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        # ground check
        for tile in self.tiles:
            if tile.rect.collidepoint(self.player.sprite.rect.bottomleft) \
                or tile.rect.collidepoint(self.player.sprite.rect.bottomright):
                self.player.sprite.is_grounded = True
                break
            self.player.sprite.is_grounded = False
    
    def draw(self, surface):
        self.tiles.draw(surface)
        self.player.sprite.draw(surface)

    def update(self):
        # update the tiles
        self.tiles.update(self.world_shift)
        # //*DEBUG: Show the tilemap collider
        #for tile in self.tiles:
        #    pygame.draw.rect(self.render, (0, 255, 0), tile.rect, 2)
        

        # update the player
        self.player.update()
        self.horizontal_collisions()
        self.vertical_collisions()
        # //* DEBUG: Show the player collider
        #pygame.draw.rect(self.render, (255, 0, 0), self.player.sprite.rect, 2)

        # //? it that in the player class ?
        # //? ive got a huge fucking cock
        # //? okay so I just had a question : rotate the sword with the cursor or just animate it and when
        # //? mouse click it play that animation (add hit point, range, attack, etc.)
        # draw and update the weapons
        #self.player.sprite.weapon.draw(self.render)
        #self.player.sprite.weapon.update()
        