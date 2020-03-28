import pygame

cat_picture = pygame.image.load('cat.png')

class Platform(object):
    def __init__(self, x, y, w, l):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.vel = 8
        # self.color = color

    def draw(self, win):
        ajust = 3
        pygame.draw.rect(win, (255, 78, 8),
                         (self.x, self.y, self.w, self.l))
        pygame.draw.rect(win, (255, 182, 8), (self.x + ajust,
                                              self.y + ajust, self.w-ajust*2, self.l-ajust*2))


class Cat(object):

    def __init__(self, x, y, w, l):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.vel = 10

    def draw(self, win):
        win.blit(cat_picture, (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.l), 2)
