import pygame
import time
import math

WIN_HEIGHT = 600
WIN_WIDTH = 400
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Try to Balance")


class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lenght = 80
        self.width = 30

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0),
                         (self.x, self.y, self.lenght, self.width))
        pygame.draw.rect(win, (24, 111, 217),
                         (self.x+5, self.y+5, self.lenght-10, self.width-10))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y  # current position
        self.vel = 8
        self.jump_counter = 20
        self.num = 1
        self.direction = 1

    def move(self, platforms):
        self.y += self.vel * self.direction
        self.jump_counter -= 1
        # If is in the bottom of the screen it jumps and reestart
        if (self.y > WIN_HEIGHT-20 or self.colision(platforms)):
            self.direction = -1
            self.jump_counter = 20
        if (self.jump_counter < 0):  # If is on the
            self.direction = 1
            self.jump_counter = 20
        if (self.y < 0):
            self.y = WIN_HEIGHT


    def colision(self, platforms):
        for platform in platforms:
            if (self.x > platform.x and self.x < platform.x+platform.lenght):
                if (self.y > platform.y-platform.width and self.y < platform.y+50):
                    return True
        return False

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (int(self.x), int(self.y)), 20)
        pygame.draw.circle(win, (150, 17, 133), (int(self.x), int(self.y)), 15)

    def move_right(self):
        if (self.x < WIN_WIDTH-20):
            self.x += self.vel

    def move_left(self):
        if (self.x > 20):
            self.x += -self.vel


def draw_all(win,  balls, platforms, time, max_height):
    win.fill([105, 167, 209])
    text = FONT.render("Pole Play - RarceD", 1, (11, 0, 107))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    text_time = FONT.render("Time: " + str(time) + "s", 1, (221, 0, 107))
    win.blit(text_time, (10, 6))
    text_height = FONT.render(
        str(WIN_HEIGHT-max_height) + " m", 1, (11, 0, 107))
    win.blit(text_height, (10, 25))

    for ball in balls:
        ball.draw(win)
    for platform in platforms:
        platform.draw(win)
    pygame.display.update()


def manual_movement(keys, ball):
    if (keys[pygame.K_RIGHT]):
        ball.move_right()
    if (keys[pygame.K_LEFT]):
        ball.move_left()


def main():
    max_height = WIN_HEIGHT
    run = True
    plat_pos_y = WIN_HEIGHT/3
    platforms = []
    platforms.append(Platform(50, plat_pos_y))
    platforms.append(Platform(WIN_WIDTH/2+50, plat_pos_y * 2-100))
    platforms.append(Platform(50, plat_pos_y * 3 - 100))

    # I start the game to train the generations:
    clock = pygame.time.Clock()
    # If they spend to much time I kill them
    start_time = time.time()
    balls = []
    balls.append(Ball(WIN_WIDTH-50, WIN_HEIGHT - 50))
    ball = balls[0]
    while (run):
        clock.tick(30)  # Every second it run 30 times
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        ball.move(platforms)
        if (max_height > ball.y):
            max_height = ball.y

        keys = pygame.key.get_pressed()
        manual_movement(keys, ball)

        draw_all(WIN, balls, platforms, ' %.2f' %
                 (time.time() - start_time), max_height)


main()
