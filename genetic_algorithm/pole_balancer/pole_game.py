import pygame
import time
import math

WIN_HEIGHT = 400
WIN_WIDTH = 600
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 40)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Try to Balance")


class Pole:
    def __init__(self, x, h):
        self.x = x
        self.y = WIN_HEIGHT - 50
        self.pole_height = h
        self.lenght = 80
        self.width = 50
        self.vel = 5
        self.eq = Equilibrium(self.x + self.lenght / 2,self.y, self.pole_height)

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0),
                         (self.x, self.y, self.lenght, self.width))
        pygame.draw.rect(win, (24, 111, 217),
                         (self.x+5, self.y+5, self.lenght-10, self.width-10))
        self.eq.draw(win, self.x + self.lenght / 2)


class Equilibrium():
    def __init__(self, x, y ,h):
        self.x = x
        self.y = y
        self.pole_height = h
        self.width = 20

    def draw(self, win, x):
        off = 5
        pygame.draw.rect(win, (19, 8, 51),
                         (x-10,WIN_HEIGHT- self.pole_height -25, self.width, self.pole_height ))
        pygame.draw.rect(win, (174, 235, 52),
                         (x-10 + off,WIN_HEIGHT- self.pole_height -25 + off, self.width - 2*off, self.pole_height - 2*off))

def draw_all(win, pole, time):
    win.fill([105, 167, 209])
    text = FONT.render("Pole Play - RarceD", 1, (11, 0, 107))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 6))
    text_gen = FONT.render("Time: " + str(time) + "s", 1, (221, 0, 107))
    win.blit(text_gen, (10, 6))
    pole.draw(win)
    pygame.display.update()


def manual_movement(keys, pole):
    if (keys[pygame.K_UP]):
        pass
    if (keys[pygame.K_RIGHT] and pole.x < WIN_WIDTH):
        pole.x += pole.vel
    if (keys[pygame.K_LEFT]and pole.x > 0):
        pole.x -= pole.vel


run = True
pole = Pole(200, 100)
# I start the game to train the generations:
clock = pygame.time.Clock()
# If they spend to much time I kill them
start_time = time.time()
while (run):
    clock.tick(30)  # Every second it run 30 times
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break
    keys = pygame.key.get_pressed()
    manual_movement(keys, pole)
    draw_all(WIN, pole, ' %.2f' % (time.time()-start_time))
