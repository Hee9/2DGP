from pico2d import *
import game_world
import math

class Ball:
    image = None

    def __init__(self, x , y , enemy, damage):
        if Ball.image == None:
            Ball.image = load_image('attack.png')
        self.x, self.y = x, y
        self.velocity = 3
        self.target_enemy = enemy
        self.damage = damage

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def move_to_target(self):
        self.x += self.velocity * math.cos(math.atan2(self.target_enemy.y-self.y,self.target_enemy.x-self.x))
        self.y += self.velocity * math.sin(math.atan2(self.target_enemy.y - self.y, self.target_enemy.x - self.x))

        if self.collide(self.target_enemy):
            game_world.remove_object(self)
            self.target_enemy.hp -= self.damage

    def collide(self, a):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a > right_b:
            return False
        if right_a < left_b:
            return False
        if top_a < bottom_b:
            return False
        if bottom_a > top_b:
            return False

        return True

    def update(self):
        self.move_to_target()


