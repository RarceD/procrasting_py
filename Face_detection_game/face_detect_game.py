import pygame
import b_game_class
from b_game_class import Platform
from b_game_class import Cat
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# To capture video from webcam. 
cap = cv2.VideoCapture(0)
   
pygame.init()
screen_x = 950
screen_y = 620
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
cat = Cat(320, 120, 120, 120)
gravity = 9
def check_limits():
    cat.y += gravity
    if (cat.y > 800):
        if (cat.max_score < cat.score):
            cat.max_score = cat.score
        cat.score = 0
        cat.x = 320
        cat.y = 120
    else:
        cat.y += gravity
    for p in platforms:
        if (p.x < cat.x + 60 and p.x + 140 > cat.x + 60 and cat.y + cat.l - 20 > p.y):
            cat.y -= 100
            cat.jump = True
            cat.score += 1
def render():
    win.blit(bg, (0, 0))  # always print first the background
    text = font.render('Try to jump Bea', 2, (255, 182, 8))
    text2 = font.render('Counter: ' + str(cat.score), 2, (255, 182, 8))
    text3 = font.render('Max Score: ' + str(cat.max_score), 2, (255, 0, 8))

    win.blit(text, (50, 30))
    win.blit(text2, (700, 30))
    win.blit(text3, (700, 80))

    for p in platforms:  # draw all the moving platforms
        p.draw(win)
        p.x += p.vel
        if (p.x > 700):
            p.vel *= -1
        if (p.x < 50):
            p.vel *= -1
    cat.draw(win)
    pygame.display.update()  # update the screen frames

game_run = True
while(game_run):
    pygame.time.delay(10)  # 64x64 images
    for event in pygame.event.get():  # Check for events of close
        if event.type == pygame.QUIT:
            game_run = False

    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    check_limits()
    if (keys[pygame.K_SPACE] and not cat.jump):
        print("Jump")
        cat.jump = True
    if cat.jump:
        if (cat.jump_count >= -5):
            neg = 1
            if cat.jump_count < 0:
                neg = -1
            cat.y -= (cat.jump_count ** 2) * 0.5 * neg
            cat.jump_count -= 1
        else:
            cat.jump_count = 12
            cat.jump = False
    if (keys[pygame.K_RIGHT]):
        cat.x += cat.vel
    if (keys[pygame.K_LEFT]):
        cat.x -= cat.vel
     # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        if (x<100):
            cat.x -= cat.vel*2
        elif (x>300):
            cat.x += cat.vel*2


    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    render()
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
pygame.quit()
