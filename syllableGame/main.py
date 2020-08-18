from separasilabas import *
import sys
import pygame 

# print ('Argument List:', str(sys.argv))
# palabra = str(sys.argv[1])
palabra = 'gato'
silabas = silabizer()
syllables = silabas(palabra)
print(syllables)
BACK_COLOR = (157, 209, 237)

pygame.init()

win_x = 500
win_y = 700
win = pygame.display.set_mode((win_x, win_y))  # dimensions of it
# bg = pygame.image.load('example.jpeg')
pygame.display.set_caption("Syllable Game")  # title of this shit of game
clock = pygame.time.Clock()  # Don't have any idea about it

# create a instance of the chracter and bullets
font = pygame.font.SysFont('bitstreamverasans', 50, True, False)
image = pygame.image.load('img.png') 
image = pygame.transform.scale(image, (360, 210))

run = True  # The game loop running
score = 0

def renderGameWindow():
    win.fill(BACK_COLOR)
    # Add the visual part:
    pygame.draw.rect(win, (0, 0, 0), (20, 20, win_x-40, 300))
    pygame.draw.rect(win, BACK_COLOR, (23, 23, win_x-40-6 ,300-6))
    win.blit(image, (75, 65)) 

    pygame.draw.rect(win, (0, 0, 0), (20, 350, win_x-40, 100))
    pygame.draw.rect(win, BACK_COLOR, (20+3,350+3, win_x-40-6, 100-6))
    index = 12

    text = font.render(palabra, 1, (0, 0, 0))
    win.blit(text, (win_x/2 - 80, 370))
  

    for syl in syllables:
        t = font.render(str(syl), 1, (255, 255, 255))
        win.blit(t, (100 + index, 450))
        index += 60
        temp = 0

    for letter in str(palabra):
        t = font.render(str(letter), 1, (255, 255, 255))
        win.blit(t, (100 + temp, 410 + index))
        temp += 50

    pygame.display.update()  # update the win frames

while(run):
    pygame.time.delay(50)  # 64x64 images

    for event in pygame.event.get():  # Check for events of close
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_SPACE] and slow_bullets == 0):
        pass
    if (keys[pygame.K_RIGHT] and p.x < win_x - p.width - p.velocity):
        pass
    elif (keys[pygame.K_LEFT]and p.x > p.velocity):
        pass

    renderGameWindow()  # For drawing all the canvas
pygame.quit()

