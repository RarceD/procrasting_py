import pygame
import time
pygame.init()

win = pygame.display.set_mode((700, 500))
win_x = 700
win_y = 500

pygame.display.set_caption("My fucking game")

x = 50
y = 50
width = 40
height = 60
velocity = 30

isJump = False
jumpCount = 10
run = True
while(run):
    pygame.time.delay(50)
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_RIGHT] and x < win_x - width - velocity):
        x += velocity
    if (keys[pygame.K_LEFT]and x > velocity):
        x -= velocity
    if not (isJump):
        if (keys[pygame.K_UP] and y > velocity):
            y -= velocity
        if (keys[pygame.K_DOWN] and y < win_y - height - velocity):
            y += velocity
        if (keys[pygame.K_SPACE]):
            isJump = True
    else:
        if (jumpCount >= -10):
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (250, 123, 11), (x, y, width, height)
                     )  # draw a rectangule
    pygame.display.update()  # update the screen frames
