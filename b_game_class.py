class Platform(object):
    def __init__(self, x, y, w, l, color):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.color = color
    def draw (self):
        print("MOVE")