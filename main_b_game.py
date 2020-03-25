import pygame
import b_game_class
from b_game_class import Platform
pygame.init()
screen =[600,400]
win = pygame.display.set_mode((950, 650))  # dimensions of it
pygame.display.set_caption("Bea's Game")  # title of this shit of game
bg = pygame.image.load('b_land.jpg')

game_run = True
while(game_run):
    pygame.time.delay(50)  # 64x64 images
    win.blit(bg, (0, 0)) #always print first the background
    pygame.display.update()  # update the screen frames
    for event in pygame.event.get():  # Check for events of close
        if event.type == pygame.QUIT:
            game_run = False
    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_SPACE]):
        print("Gilipollas")
        p = Platform(300,50,20,150)
        p.draw(win)