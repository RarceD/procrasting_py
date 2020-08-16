from separasilabas import *
import sys
import pygame

# print ('Argument List:', str(sys.argv))
# palabra = str(sys.argv[1])
palabra='elefante'
silabas = silabizer()
syllables = silabas(palabra)
print(syllables)


pygame.init()

win_x = 500
win_y = 700
win = pygame.display.set_mode((win_x, win_y - 20))  # dimensions of it
# bg = pygame.image.load('example.jpeg')
pygame.display.set_caption("Syllable Game")  # title of this shit of game
clock = pygame.time.Clock()  # Don't have any idea about it

# create a instance of the chracter and bullets
font = pygame.font.SysFont('bitstreamverasans',30,True, True)
run = True  # The game loop running
score =0
def renderGameWindow():
    win.fill((157, 209, 237))
    text = font.render(palabra, 1, (0,0,0))
    index = 12

    for syl in syllables:
        t = font.render(str(syl), 1, (0,0,0))
        win.blit(t,(100 + index,10))
        index+=50
        temp = 0
        if (len(str(syl))>1):   
            for letter in str(syl):
                t = font.render(str(letter), 1, (0,0,0))
                win.blit(t,(100+ temp ,50+ index))
                temp+=50
    win.blit(text,(400,10))

    pygame.draw.rect(win, (0,0,0),(10,10,120,40)) #pygame.draw.rect(screen, color, (x,y,width,height), thickness) 
    pygame.draw.rect(win, (255,0,0),(10, 400,110 - score*10,30)) #pygame.draw.rect(screen, color, (x,y,width,height), thickness) 
    
    pygame.display.update()  # update the screen frames


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
