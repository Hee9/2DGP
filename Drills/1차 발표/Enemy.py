from pico2d import *

import game_framework
import game_world

# Enemy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
RUN_SPEED_KMPH = 10.0 # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Enemy Action Speed
TIME_PER_ACTION = 0
ACTION_PER_TIME = 0
FRAMES_PER_ACTION = 0

# Enemy States

class RunState:

    @staticmethod
    def enter(enemy, event):
        pass

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        enemy.frame = (enemy.frame + 1) % 3
        enemy.x += enemy.velocity * game_framework.frame_time
        enemy.x = clamp(25, enemy.x, 1600 - 25)

    @staticmethod
    def draw(enemy):
        if enemy.dir == 1:
            enemy.image.clip_draw(int(enemy.frame) * 100, 100, 100, 100, enemy.x, enemy.y)
        else:
            enemy.image.clip_draw(int(enemy.frame) * 100, 0, 100, 100, enemy.x, enemy.y)

class Enemy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Enemy is only once created, so instance image loading is fine
        self.image = load_image('enemy.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass

