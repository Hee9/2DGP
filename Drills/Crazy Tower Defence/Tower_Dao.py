import game_world
import game_framework

from pico2d import *
import camp_stage
from ball import Ball

PIXEL_PER_METER = (10,0 / 0.3)      # 10 pixel 30cm

# Tower Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class IdleState:

    @staticmethod
    def enter(tower, event):
        pass

    @staticmethod
    def exit(tower, event):
        pass

    @staticmethod
    def do(tower):
        tower.frame = (tower.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        tower.timer +=1

        if tower.timer == 100:
            tower.check_enemy_in_range()
            tower.timer = 0

    @staticmethod
    def draw(tower):
        #tower.image.clip_draw(int(tower.frame) * 70, 0, 70, 70, tower.x, tower.y)
        tower.image.draw(tower.x, tower.y)
        print(tower.x)

class Dao:
    def __init__(self, x=0, y=0):
        # Tower is only once created, so instance image loading is fine
        self.image = load_image('Dao.png')
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.attack = 0.1
        self.x, self.y = x, y
        self.tower_collide_check = False
        self.timer = 0
        self.attack_damage = 0.05

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def get_range_bb(self):
        return self.x - 150, self.y - 150, self.x + 150, self.y + 150

    def attack_ball(self, enemy, damage):
        ball = Ball(self.x, self.y, enemy, damage)
        game_world.add_object(ball, 1)

    def collide(self, a):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_range_bb()

        if left_a > right_b:
            return False
        if right_a < left_b:
            return False
        if top_a < bottom_b:
            return False
        if bottom_a > top_b:
            return False

        return True

    def check_enemy_in_range(self):
        for enemy in camp_stage.enemies:
            if self.collide(enemy):
                self.attack_ball(enemy, self.attack_damage)
                break

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_range_bb())

    def handle_event(self, event):
        pass
