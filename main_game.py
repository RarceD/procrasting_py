import pygame
import time
pygame.init()

win_x = 700
win_y = 500
win = pygame.display.set_mode((win_x, win_y - 20))  # dimensions of it
pygame.display.set_caption("My fucking game")  # title of this shit of game
bg = pygame.image.load('Game/bg.jpg')
clock = pygame.time.Clock()  # Don't have any idea about it


class player(object):
    # Create a list of the pictures in Game Folder
    walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load(
        'Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
    walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load(
        'Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]

    def __init__(self, x, y, width, height):
        self.height = height
        self.width = width
        self.x = x  # variables for the caracter
        self.y = y
        self.velocity = 20
        self.isJump = False  # Variables for jumpping
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)  # this is a rectangle

    def draw(self, win):
        if (self.walkCount + 1 >= 27):
            self.walkCount = 0
        if not (self.standing):
            if (self.left):
                # The //3 is because if not is out of range
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif (self.right):
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if (self.right):
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        # Continously update the position
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (0, 0, 255), self.hitbox, 2)


class projector (object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.velocity = 15 * direction

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy (object):
    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load(
        'Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'), pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load(
        'Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'), pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 6
        # Continously update the position
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        self.move()
        if (self.walkCount + 1 >= 33):
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        # Continously update the position
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if (self.vel > 0):
            if (self.x + self.vel < self.path[1]):
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if (self.x - self.vel > self.path[0]):
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        print("hit an enemy")


# create a instance of the chracter and bullets
font = pygame.font.SysFont('bitstreamverasans',30,True, True)
p = player(100, win_y - 80, 64, 64)
e = enemy(100, 410, 64, 64, 450)
bullets = []  # a list of elements
slow_bullets = 0  # just for not letting doeuble shotting
run = True  # The game loop running
score = 0

def reddrawGameWindow():
    win.blit(bg, (0, 0)) #always print first the background
    text = font.render('Score:' + str(score), 1, (0,0,0))
    win.blit(text,(400,10))
    e.draw(win)
    p.draw(win)
    pygame.draw.rect(win, (0,0,0),(550,10,120,40)) #pygame.draw.rect(screen, color, (x,y,width,height), thickness) 
    pygame.draw.rect(win, (255,0,0),(555,15,110 - score*10,30)) #pygame.draw.rect(screen, color, (x,y,width,height), thickness) 
    
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()  # update the screen frames


while(run):
    pygame.time.delay(50)  # 64x64 images
    if (slow_bullets > 2):
        slow_bullets = 0
    else:
        slow_bullets += 1

    for event in pygame.event.get():  # Check for events of close
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:  # loop in the projectils created and check for colisions
        if (bullet.y - bullet.radius < e.hitbox[1] + e.hitbox[3]and bullet.y + bullet.radius > e.hitbox[1]):
            if (bullet.x + bullet.radius > e.hitbox[0] and bullet.x - bullet.radius < e.hitbox[0] + e.hitbox[2]):
                e.hit()
                if (score > 10):
                    score = 0
                else:
                    score+=1

                bullets.pop(bullets.index(bullet))  # Delete the objects
        if bullet.x < win_x and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))  # Delete the objects

    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_SPACE] and slow_bullets == 0):
        slow_bullets += 1
        if (p.left):
            facing = -1
        else:
            facing = 1
        if (len(bullets) < 10):
            bullets.append(projector(round(p.x + p.width//2),
                                     round(p.y + p.height//2), 6, (250, 2, 2), facing))

    if (keys[pygame.K_RIGHT] and p.x < win_x - p.width - p.velocity):
        p.x += p.velocity
        p.right = True
        p.left = False
        p.standing = False
    elif (keys[pygame.K_LEFT]and p.x > p.velocity):
        p.x -= p.velocity
        p.left = True
        p.right = False
        p.standing = False
    else:
        p.standing = True
        p.walkCount = 0
    if not (p.isJump):
        if (keys[pygame.K_UP]):
            p.isJump = True
            p.right = False
            p.left = False
            p.walkCount = 0
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
    reddrawGameWindow()  # For drawing all the canvas
pygame.quit()
