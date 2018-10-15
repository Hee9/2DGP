import game_framework
import main_state
from pico2d import *

name = "pause_state"
image = None
frame = 0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def handle_events():
    global frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
                frame = 0

def draw():
    global frame
    clear_canvas()
    if (frame % 250 < 100):
        image.clip_draw(250, 250, 400, 400, 400, 300)
    update_canvas()

def update():
    global frame
    frame = (frame + 1) % 250

def pause():
    pass

def resume():
    pass