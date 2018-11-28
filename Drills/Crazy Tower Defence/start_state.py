from pico2d import *

import game_framework
import camp_stage

name = "Start State"
image = None
logo_time = 0.0
mouseX, mouseY = 0, 0

def enter():
    global image, bgm
    image = load_image('StartState.png')
    bgm = load_music('StartState.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image, bgm
    del(image, bgm)

def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
        game_framework.change_state(camp_stage)

        delay(0.01)
        logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(768, 512)
    update_canvas()

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if event.x >= 560 and event.x <= 980 and 1024 - 1 - event.y >= 210 and 1024 - 1 - event.y <= 280:
                    game_framework.change_state(camp_stage)

def pause():
    pass

def resume():
    pass