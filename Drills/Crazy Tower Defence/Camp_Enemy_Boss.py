from pico2d import *

import game_framework
import game_world
import random
import camp_stage

from Camp_Enemy_First import Camp_Enemy_First

# Enemy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
RUN_SPEED_KMPH = 20.0 # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Enemy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Enemy States

class RunState:

    @staticmethod
    def enter(enemy, event):
        pass
        #enemy.dir = clamp(-2, enemy.velocity, 2)

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        #enemy.x += enemy.velocity * game_framework.frame_time
        #enemy.x = clamp(52, enemy.x, 1040 - 52)
        #enemy.y = clamp(52, enemy.y, 1040 - 52)
        if enemy.dir == 0:
            enemy.y -= 0.5
            if enemy.y == 572 and enemy.x == 780:
                enemy.dir = 1
            if enemy.y == 260 and enemy.x == 988:
                enemy.dir = 2
        if enemy.dir == 1:
            enemy.x += 0.5
            if enemy.x == 988:
                enemy.dir = 0
        if enemy.dir == 2:
            enemy.x -= 0.5
            if enemy.x == 572:
                enemy.dir = 3
            if enemy.x == 264:
                enemy.dir = 0
        if enemy.dir == 3:
            enemy.y += 0.5
            if enemy.y == 780:
                enemy.dir = 2
        if enemy.y == 0:
            camp_stage.camp_enemies_boss.remove(enemy)
            game_world.remove_object(enemy)
            camp_stage.life -= 1
            Camp_Enemy_First.die_count += 1

        enemy.life_check()

    @staticmethod
    def draw(enemy):
        if enemy.dir == 0:
            enemy.image.clip_draw(int(enemy.frame) * 110, 330, 100, 100, enemy.x, enemy.y)
        if enemy.dir == 1:
            enemy.image.clip_draw(int(enemy.frame) * 110, 110, 100, 100, enemy.x, enemy.y)
        if enemy.dir == 2:
            enemy.image.clip_draw(int(enemy.frame) * 110, 0, 100, 100, enemy.x, enemy.y)
        if enemy.dir == 3:
            enemy.image.clip_draw(int(enemy.frame) * 110, 215, 100, 100, enemy.x, enemy.y)

class Camp_Enemy_Boss:
    def __init__(self):
        #self.x, self.y = 780, random.randint(988, random.randint(1500, random.randint(5000, 8000)))
        self.x, self.y = 780, camp_stage.Enemy_gap
        # Enemy is only once created, so instance image loading is fine
        self.image = load_image('camp_enemy_boss.png')
        self.dir = 0
        self.velocity = 0
        self.frame = random.randint(0, 10)
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.hp = 2

        camp_stage.Enemy_gap += random.randint(40, 100)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def life_check(self):
        if self.hp <= 0:
            camp_stage.camp_enemies_boss.remove(self)
            game_world.remove_object(self)
            camp_stage.money += 7

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)
            Camp_Enemy_First.die_count += 1

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.cur_state.draw(self)
        #draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass
