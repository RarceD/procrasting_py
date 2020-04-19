import pygame
import neat
import time
import os
import random

WIN_WIDTH = 550
WIN_HEIGHT = 800

BACKGROUND_IMD = pygame.transform.scale2x(
    pygame.image.load('game_images/bg.png'))
PIPE_IMG = pygame.transform.scale2x(pygame.image.load('game_images/pipe.png'))
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 50)


class Bird():
    BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load("game_images/bird1.png")), pygame.transform.scale2x(
        pygame.image.load("game_images/bird2.png")), pygame.transform.scale2x(pygame.image.load("game_images/bird3.png"))]
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5  # how fast is going topm be in the air

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0  # for rotate the images
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.BIRD_IMAGES[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # seconds up and down for fallinfg
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if (d > 16):
            d = 16
        if d < 0:
            d -= 2
        self.y += d
        if (d < 0 or self.y < self.height + 50):
            if (self.tilt < self.MAX_ROTATION):
                self.tilt = self.MAX_ROTATION
        else:
            if (self.tilt > -90):
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1
        if (self.img_count < self.ANIMATION_TIME):
            self.img = self.BIRD_IMAGES[0]
        elif (self.img_count < self.ANIMATION_TIME*2):
            self.img = self.BIRD_IMAGES[1]
        elif (self.img_count < self.ANIMATION_TIME*3):
            self.img = self.BIRD_IMAGES[2]
        elif (self.img_count < self.ANIMATION_TIME*4):
            self.img = self.BIRD_IMAGES[1]
        elif (self.img_count < self.ANIMATION_TIME*4 + 1):
            self.img = self.BIRD_IMAGES[0]
            self.img_count = 0
        if (self.tilt <= -80):
            self.img = self.BIRD_IMAGES[1]
            self.img_count = self.ANIMATION_TIME*2
        # I just rotate the image related with the center of the screen and not from the corner
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe():
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(
            PIPE_IMG, False, True)  # I flip one image
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False  # For knowing if there is a colision with the bird
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collision_detection(self, bird):
        # I obtein the mask, arrays of what is or not the background of a chracter
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x-bird.x, self.top - round(bird.y))
        bottom_offset = (self.x-bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)
        if (b_point or t_point):
            return True
        return False


class Base():
    VEL = 5
    BASE_IMG = pygame.transform.scale2x(
        pygame.image.load('game_images/base.png'))
    WIDTH = BASE_IMG.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        # I have two images and move them to show that they are moving
        if (self.x1+self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH
        if (self.x2+self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.BASE_IMG, (self.x1, self.y))
        win.blit(self.BASE_IMG, (self.x2, self.y))


def draw_window(win, bird, pipes, base, score):
    win.blit(BACKGROUND_IMD, (0, 0))  # The corner of the image
    for pipe in pipes:
        pipe.draw(win)
    text = FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(),10))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()


def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird(230, 350)
    base = Base(700)
    pipes = [Pipe(600)]
    score = 0
    run = True
    while (run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # bird.move()
        rem = []
        add_pipe = False
        for pipe in pipes:
            # If colision kill the game
            if pipe.collision_detection(bird):
                run = False
            # If the x of the pipe is out the screen I crearte another
            if pipe.x + pipe.PIPE_TOP.get_width() < -10:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
        for r in rem:
            pipes.remove(r)
        if (bird.y + bird.img.get_height() > 730):
            pass

        base.move()
        draw_window(win, bird, pipes, base, score)


main()
