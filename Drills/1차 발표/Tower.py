import game_framework
from pico2d import *
from ball import  Ball
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm

# Tower Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Tower Event
MOUSE_DOWN, SPACE = range(2)

key_event_table = {
    (SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN): MOUSE_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

# Tower States

class IdleState:

    @staticmethod
    def enter(tower, event):
        if event == MOUSE_DOWN:
            tower.x = event.x
            tower.y = 1040 - 1 - event.y
        if event == SPACE:
            tower.attack_ball()

    @staticmethod
    def exit(tower, event):
        pass

    @staticmethod
    def do(tower):
        tower.frame = (tower.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(tower):
        tower.image.clip_draw(int(tower.frame) * 70, 0, 70, 70, tower.x, tower.y)

class Tower:

    def __init__(self):
        # Tower is only once created, so instance image loading is fine
        self.x, self.y = 676, 576
        self.image = load_image('tower.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.attack = 10


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

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

