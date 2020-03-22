import pygame
import time
pygame.init()

win = pygame.display.set_mode((700, 480))
win_x = 700
win_y = 500

pygame.display.set_caption("My fucking game")

# Create a list of the pictures in Game Folder
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load(
    'Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load(
    'Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()  # Don't have any idea about it


class player(object):
    def __init__(self, x, y, width, height):
        self.height = height
        self.width = width
        self.x = x  # variables for the caracter
        self.y = y
        self.velocity = 30
        self.isJump = False  # Variables for jumpping
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    def draw(self,win):
        if (self.walkCount + 1 >= 27):
            self.walkCount = 0
        if (self.left):
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))# The //3 is because if not is out of range
            self.walkCount += 1
        elif (self.right):
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
           win.blit(char, (self.x, self.y))

p = player(100, win_y - 80, 64, 64)  # create a instance of the chracter

def reddrawGameWindow():
    win.blit(bg, (0, 0))
    p.draw(win)
    pygame.display.update()  # update the screen frames


run = True
while(run):
    pygame.time.delay(50)  # 64x64 images
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            p.run = False
    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_RIGHT] and p.x < win_x - p.width - p.velocity):
        p.x += p.velocity
        p.right = True
        p.left = False
    elif (keys[pygame.K_LEFT]and p.x > p.velocity):
        p.x -= p.velocity
        p.left = True
        p.right = False
    else:
        p.left = False  # This variables are for the movement animations
        p.right = False
        p.walkCount = 0
    if not (p.isJump):
        if (keys[pygame.K_SPACE]):
            p.isJump = True
    else:
        if (p.jumpCount >= -10):
            neg = 1
            if p.jumpCount < 0:
                neg = -1
            p.y -= (p.jumpCount ** 2) * 0.5 * neg
            p.jumpCount -= 1
        else:
            p.jumpCount = 10
            p.isJump = False
    reddrawGameWindow()  # For drawing

pygame.quit()
