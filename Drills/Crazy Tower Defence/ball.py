from pico2d import *
import game_world
import math

class Ball:
    image = None

    def __init__(self, x , y , enemy):
        if Ball.image == None:
            Ball.image = load_image('attack.png')
        self.x, self.y = x, y
        self.velocity = 3
        self.target_enemy = enemy

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def move_to_target(self):
        self.x += self.velocity * math.cos(math.atan2(self.target_enemy.y-self.y,self.target_enemy.x-self.x))
        self.y += self.velocity * math.sin(math.atan2(self.target_enemy.y - self.y, self.target_enemy.x - self.x))
    def update(self):
        self.move_to_target()

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
