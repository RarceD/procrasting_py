import pygame
import random

WIN_WIDTH = 600
WIN_HEIGHT = 700
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 50)


class Dot():
    def __init__(self, x, y, end):
        self.x = x
        self.y = y
        self.vel = 10
        self.end = end

    def draw(self, win):
        if not self.end:
            pygame.draw.circle(win, (255, 200, 250), (self.x, self.y), 5)
        else:
            pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 10)

    def colision(self, obstacle):
        pass


class Obstacle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lenght = WIN_WIDTH-100
        self.width = 30

    def draw(self, win):
        pygame.draw.rect(win, (17, 18, 92),
                         (self.x, self.y, self.lenght, self.width))


def draw_all(win, dots, dot_end, obstacle):
    win.fill([105, 167, 209])
    text = FONT.render("Shitty dot game ", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 6))
    for dot in dots:
        dot.draw(win)
    dot_end.draw(win)
    obstacle.draw(win)
    pygame.display.update()


def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    dots = []
    for i in range(500):
        dots.append(Dot(120, 120, False))
    dot_end = Dot(300, 600, True)
    obstacle = Obstacle(0,  WIN_HEIGHT/2)
    run = True
    while (run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys = pygame.key.get_pressed()  # check the diferent letters of the key board
        """
        if (keys[pygame.K_DOWN] and dot.y < WIN_HEIGHT):
            if not (dot.y > obstacle.y -15 and dot.y<obstacle.y + obstacle.width and dot.x < obstacle.x+obstacle.lenght):
                dot.y += dot.vel
        if (keys[pygame.K_UP] and dot.y > 0):
            if not (dot.y < obstacle.y + obstacle.width +15 and dot.y > obstacle.y and dot.x < obstacle.x+obstacle.lenght):
                dot.y -= dot.vel
        if (keys[pygame.K_RIGHT] and dot.x < WIN_WIDTH):
            dot.x += dot.vel
        if (keys[pygame.K_LEFT]and dot.x > 0):
            dot.x -= dot.vel
        """
        for dot in dots:
            if (dot.y < WIN_HEIGHT):
                if not (dot.y > obstacle.y - 15 and dot.y < obstacle.y + obstacle.width and dot.x < obstacle.x+obstacle.lenght):
                    dot.y += random.randint(0, 15)
            if (dot.y > 0):
                if not (dot.y < obstacle.y + obstacle.width + 15 and dot.y > obstacle.y and dot.x < obstacle.x+obstacle.lenght):
                    dot.y -= random.randint(0, 15)
            if (dot.x < WIN_WIDTH):
                dot.x += random.randint(0, 15)
            if (dot.x > 0):
                dot.x -= random.randint(0, 15)

        draw_all(win, dots, dot_end, obstacle)


main()
