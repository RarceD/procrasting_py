import pygame
import time
pygame.init()

win = pygame.display.set_mode((700, 480))
win_x = 700
win_y = 500

pygame.display.set_caption("My fucking game")

# Create a list of the pictures in Game Folder
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock() # Don't have any idea about it
height = 64
width = 64
x = 50 # variables for the caracter
y = win_y - height - 30 
velocity = 30

isJump = False # Variables for jumpping
jumpCount = 10

left = False
right = False

def reddrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))
    if (walkCount + 1 >= 27):
        walkCount = 0
    if (left):
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif (right):
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))


    pygame.display.update()  # update the screen frames

run = True
while(run):
    pygame.time.delay(50) ##64x64 images
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_RIGHT] and x < win_x - width - velocity):
        x += velocity
        right = True
        left = False
    elif (keys[pygame.K_LEFT]and x > velocity):
        x -= velocity
        left = True
        right = False
    else:
        left = False #This variables are for the movement animations
        right = False
        walkCount = 0
    if not (isJump):
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
    reddrawGameWindow() #For drawing

pygame.quit()