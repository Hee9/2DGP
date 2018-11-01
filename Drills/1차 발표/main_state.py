import random
import json
import os

from pico2d import *

import game_framework
import camp_stage

name = "MainState"

background = None
font = None

def enter():
    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def update():
    pass

def draw():
    clear_canvas()
    update_canvas()
