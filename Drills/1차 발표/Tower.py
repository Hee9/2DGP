from pico2d import *

class Tower:
    def __init__(self):
        self.x, self.y = 500, 500
        self.image = load_image('Bazzi.png')
        self.frame = 0
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.draw(self.x, self.y, 52, 52)

