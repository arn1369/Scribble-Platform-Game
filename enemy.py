from dataclasses import dataclass

import numpy as np
from scipy import interpolate

from data import *


@dataclass
class Waypoint:
    pos: tuple = (0, 0)
    x, y = pos

@dataclass
class Enemy:
    # Setup attributes
    pos: tuple=(0,0)
    category: str='red'
    health: int = 100

    # Setup values
    velocity = pygame.math.Vector2(0, 0)
    waypoints = []
    current_wp_index = 0


    # Setup image and rect from category
    match(category):
        case 'red':
            img = pygame.image.load('assets/players/characters/player/character_roundRed.png')
        case 'green':
            img = pygame.image.load('assets/players/characters/player/character_roundGreen.png')
        case _:
            img = None
            print("Debug >>> Error while finding the image of enemy")
    rect = img.get_rect(center=pos)

    def add_waypoint(self, x, y):
        self.waypoints.append(Waypoint((x, y)))

    def get_next_waypoint(self):
        return self.waypoints[self.current_wp_index + 1]
    
    def moveXY(self, pos):
        
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def update(self):
        if self.waypoints != [] and self.current_wp_index != None:
            # //! Not FINISHED
            if None:
                self.current_wp_index += 1
                self.current_wp = self.get_next_waypoint()
        self.moveXY(self.current_wp_index)


e = Enemy(pos=(150, 200), category='red')
e.update()
e.add_waypoint(100, 100)
e.add_waypoint(200, 200)
print("Position of current waypoint : ", e.waypoints[e.current_wp_index])
e.update()
print(e.rect.x, e.rect.y)
e.update()
print(e.rect.x, e.rect.y)
e.update()
print(e.rect.x, e.rect.y)
e.update()
print(e.rect.x, e.rect.y)
e.update()
print("Position of current waypoint : ", e.waypoints[e.current_wp_index])
