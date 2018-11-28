import game_framework
from pico2d import *
from ball import Ball
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm

# Tower Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Tower Event

# Tower States

class IdleState:

    @staticmethod
    def enter(tower, event):
        pass

    @staticmethod
    def exit(tower, event):
        pass

    @staticmethod
    def do(tower):
        tower.frame = (tower.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(DaoTower):
        for i in range(DaoTower.tower1):
            DaoTower.image.clip_draw(int(DaoTower.frame) * 70, 0, 70, 70, DaoTower.Save_mouseX[i], DaoTower.Save_mouseY[i])

class DaoTower:

    def __init__(self):
        # Tower is only once created, so instance image loading is fine
        self.image = load_image('Dao_tower.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.attack = 10
        self.mouseX, self.mouseY = 0, 0
        self.tower1 = 0
        self.Save_mouseX = [0 for n in range(0, 30)]
        self.Save_mouseY = [0 for n in range(0, 30)]
        self.Flag_mouse = [False for n in range(0, 30)]

    def get_bb(self):
        return self.mouseX - 30, self.mouseY - 30, self.mouseX + 30, self.mouseY + 30

    def attack_ball(self):
        ball = Ball(self.x, self.y, self.dir * 4)
        game_world.add_object(ball, 1)

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

    def handle_event(self, event):
        pass


