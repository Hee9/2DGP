from pico2d import *

import game_framework
import game_world

from Tower_Bazzi import Bazzi
from Enemy import Enemy

NONE, BAZZI, DAO, UNI = range(4)
name = "CAMP Stage"
image = None
bazzi_image = None
enemy = None
enemies = []
Enemy_gap = 1030
Enemy_timer = 0

def enter():
    global image, bgm
    global bazzi_image
    image = load_image('camp.png')
    bazzi_image = load_image('bazzi.png')
    bgm = load_music('GameStart.ogg')
    bgm.set_volume(50)
    bgm.play()


def exit():
    global image, bgm
    global bazzi_image
    del(image, bgm, bazzi_image)
    game_world.clear()

def update():
    global Enemy_timer
    global enemies

    for game_object in game_world.all_objects():
        game_object.update()

    Enemy_timer +=1

    if Enemy_timer == 50:
        enemy = Enemy()
        enemies.append(enemy)
        game_world.add_object(enemy, 1)
        Enemy_timer = 0

def draw():
    global image, bazzi_image
    clear_canvas()
    image.draw(520, 520)
    bazzi_image.draw(1124, 550)

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True

select = NONE
def handle_events():
    global select, bazzi_image

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            bazzi_image.draw(event.x,1024-1-event.y)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # BazziTower
            if event.x <= 1150 and event.x >= 1096:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    select = BAZZI

        elif event.type == SDL_MOUSEBUTTONUP:
            # BazziTower
            if select == BAZZI:
                bazzi = Bazzi(event.x,1024 - 1 - event.y)
                game_world.add_object(bazzi,1)
                select = NONE

def pause():
    pass

def resume():
    pass