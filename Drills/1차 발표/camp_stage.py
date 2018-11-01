from pico2d import *

import game_framework
import game_world

from Tower import Tower
from Enemy import Enemy

name = "CAMP Stage"
image = None
tower = None
enemy = None

def enter():
    global image, tower, enemy
    image = load_image('camp.png')
    tower = Tower()
    enemy = Enemy()
    game_world.add_object(tower, 0)
    game_world.add_object(enemy, 1)

def exit():
    global image
    del(image)
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    global image
    clear_canvas()
    image.draw(520,520)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

def pause():
    pass

def resume():
    pass