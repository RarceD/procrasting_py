import pygame

class Platform(object):
    def __init__(self, x, y,w, l ):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        # self.color = color
    def draw(self, win):
        pygame.draw.rect(win, (255,0,0),(350,150,110,30))
