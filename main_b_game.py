import pygame
import b_game_class
from b_game_class import Platform
from b_game_class import Cat
pygame.init()
screen_x = 950
screen_y = 650
win = pygame.display.set_mode((screen_x, screen_y))  # dimensions of it
pygame.display.set_caption("Bea's Game")  # title of this shit of game
bg = pygame.image.load('b_land.jpg')
font = pygame.font.SysFont('bitstreamverasans', 30, True, True)

down_space = 100
right_space = 300
platforms = []
platforms.append(Platform(100, 500, 140, 20))                   # fix platforms
platforms.append(Platform(100 + right_space, 550, 140, 20))     # fix platforms
platforms.append(Platform(100 + right_space * 2,
                          600, 140, 20))  # fix platforms
cat = Cat(320,120,120,120)


def render():
    win.blit(bg, (0, 0))  # always print first the background
    text = font.render('Try to jump Bea', 2, (255, 182, 8))
    win.blit(text, (50, 30))
    for p in platforms: #draw all the moving platforms
        p.draw(win)
        p.x += p.vel
        if (p.x > 700):
            p.vel *= -1
        if (p.x < 50):
            p.vel *= -1
    cat.draw(win)
    pygame.display.update()  # update the screen frames
def check_limits(value):
    if ()

    return True

game_run = True
while(game_run):
    pygame.time.delay(50)  # 64x64 images
    for event in pygame.event.get():  # Check for events of close
        if event.type == pygame.QUIT:
            game_run = False

    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    check_limits()
    if (keys[pygame.K_SPACE]):
        print("Jump")
    if (keys[pygame.K_RIGHT]):
        cat.x+=cat.vel
    if (keys[pygame.K_LEFT]):
        print("Jump")
        cat.x-=cat.vel

    if (keys[pygame.K_SPACE]):
        print("Jump")

    render()
pygame.quit()