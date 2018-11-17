from pico2d import *
import random

# class code
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball():
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 600
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        self.down = random.randint(2, 15)

    def update(self):
        self.y -= self.down

    def draw1(self):
        self.image1.clip_draw(0, 0, 21, 21, self.x, self.y)

    def draw2(self):
        self.image2.clip_draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy = Boy()
grass = Grass()
ball = Ball()

running = True

team = [Boy() for i in range(11)]
rain = [Ball() for i in range(random.randint(0, 20))]
rain_s = [Ball() for i in range(20 - len(rain))]

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in rain:
        ball.update()
    for ball in rain_s:
        ball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in rain:
        ball.draw1()
    for ball in rain_s:
        ball.draw2()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()