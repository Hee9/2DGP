from pico2d import *

import game_framework
import game_world

from Bazzi_tower import Bazzi_T
from Dao_tower import Dao_T
from Uni_tower import Uni_T

from Enemy import Enemy

name = "CAMP Stage"
image = None
Bazzi = None
Dao = None
Uni = None
bazzi_t = None
dao_t = None
uni_t = None
enemy = None
enemies = None

MouseCheck = False
y = 1030

def enter():
    global image, enemy, enemies
    global Bazzi, Dao, Uni
    global bazzi_t, dao_t, uni_t
    image = load_image('camp.png')
    Bazzi = load_image('bazzi.png')
    Dao = load_image('Dao.png')
    Uni = load_image('Uni.png')
    bazzi_t = Bazzi_T()
    dao_t = Dao_T()
    uni_t = Uni_T()
    enemy = Enemy()
    enemies = [Enemy() for n in range(100)]
    game_world.add_object(bazzi_t, 1)
    game_world.add_object(dao_t, 1)
    game_world.add_object(uni_t, 1)
    for enemy in enemies:
        game_world.add_object(enemy, 1)

def exit():
    global image, Bazzi, Dao, Uni
    del(image, Bazzi, Dao, Uni)
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    global image, Bazzi, Dao, Uni
    clear_canvas()
    image.draw(520, 520)
    Bazzi.draw(1124, 550)
    Dao.draw(1224, 550)
    Uni.draw(1324, 550)
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
        elif event.type == SDL_MOUSEMOTION:
            if bazzi_t.Flag_mouse[bazzi_t.tower1] == True:
                bazzi_t.mouseX, bazzi_t.mouseY = event.x, 1024 - 1 - event.y
            elif dao_t.Flag_mouse[dao_t.tower1] == True:
                dao_t.mouseX, dao_t.mouseY = event.x, 1024 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # BazziTower
            if event.x <= 1150 and event.x >= 1096:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    bazzi_t.Flag_mouse[bazzi_t.tower1] = True
                    print(bazzi_t.Save_mouseX[bazzi_t.tower1], bazzi_t.Save_mouseY[bazzi_t.tower1])
            # DaoTower
            elif event.x <= 1250 and event.x >= 1196:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    dao_t.Flag_mouse[dao_t.tower1] = True
                    print(dao_t.Save_mouseX[dao_t.tower1], dao_t.Save_mouseY[dao_t.tower1])
             # UniTower
            elif event.x <= 1350 and event.x >= 1296:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    uni_t.Flag_mouse[uni_t.tower1] = True
                    print(uni_t.Save_mouseX[uni_t.tower1], uni_t.Save_mouseY[uni_t.tower1])

        elif event.type == SDL_MOUSEBUTTONUP:
            # BazziTower
            if bazzi_t.Flag_mouse[bazzi_t.tower1]:
                bazzi_t.Save_mouseX[bazzi_t.tower1], bazzi_t.Save_mouseY[bazzi_t.tower1] = event.x, 1024 - 1 - event.y
                print(bazzi_t.Save_mouseX, bazzi_t.Save_mouseY)
                bazzi_t.tower1 += 1
            # DaoTower
            elif dao_t.Flag_mouse[dao_t.tower1]:
                dao_t.Save_mouseX[dao_t.tower1], dao_t.Save_mouseY[dao_t.tower1] = event.x, 1024 - 1 - event.y
                print(dao_t.Save_mouseX, dao_t.Save_mouseY)
                dao_t.tower1 += 1
             # UniTower
            elif uni_t.Flag_mouse[uni_t.tower1]:
                uni_t.Save_mouseX[uni_t.tower1], uni_t.Save_mouseY[uni_t.tower1] = event.x, 1024 - 1 - event.y
                print(uni_t.Save_mouseX, uni_t.Save_mouseY)
                uni_t.tower1 += 1

def pause():
    pass

def resume():
    pass