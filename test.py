import pygame, math
pygame.init()

screen = pygame.display.set_mode((500,600))
clock = pygame.time.Clock()

rect = pygame.Rect(100, 100, 50, 50)

def update():
    global rect
    first_img = pygame.image.load('assets/environment/tiles/items/item_sword.png')
    # rotate the weapon to mouse
    pos = rect.center
    mouse_pos = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_pos[0]-pos[0], mouse_pos[1]-pos[1]
    angle = (180/math.pi) * -math.atan2(rel_y, rel_x)
    image = pygame.transform.rotate(first_img, int(angle))
    rect = image.get_rect(center=pos)
    return rect, image

while True:
    screen.fill((100,100,100))
    [pygame.quit() for event in pygame.event.get() if event.type == pygame.QUIT]
    pygame.draw.rect(screen, pygame.Color('red'), rect, 2)
    rect, img = update()
    screen.blit(img, rect.topleft)

    clock.tick(60)
    pygame.display.update()