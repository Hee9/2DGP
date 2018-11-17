from pico2d import *

import game_framework
import game_world

from Bazzi_tower import BazziTower
from Dao_tower import DaoTower
from Uni_tower import UniTower

from Enemy import Enemy

name = "CAMP Stage"
image = None
ClickBazziImage = None
Dao = None
Uni = None
bazzitower = None
daotower = None
unitower = None
enemy = None
enemies = None

MouseCheck = False
y = 1030

def enter():
    global image, enemy, enemies
    global ClickBazziImage, ClickDaoImage, ClickUniImage
    global bazzitower, daotower, unitower
    image = load_image('camp.png')
    ClickBazziImage = load_image('bazzi.png')
    ClickDaoImage = load_image('Dao.png')
    ClickUniImage = load_image('Uni.png')
    bazzitower = BazziTower()
    daotower = DaoTower()
    unitower = UniTower()
    enemy = Enemy()
    enemies = [Enemy() for n in range(100)]
    game_world.add_object(bazzitower, 1)
    game_world.add_object(daotower, 1)
    game_world.add_object(unitower, 1)
    for enemy in enemies:
        game_world.add_object(enemy, 1)

def exit():
    global image, ClickBazziImage, ClickDaoImage, ClickUniImage
    del(image, ClickBazziImage, ClickDaoImage, ClickUniImage)
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    global image, ClickBazziImage, ClickDaoImage, ClickUniImage
    clear_canvas()
    image.draw(520, 520)
    ClickBazziImage.draw(1124, 550)
    ClickDaoImage.draw(1224, 550)
    ClickUniImage.draw(1324, 550)
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
            if bazzitower.Flag_mouse[bazzitower.tower1]:
                bazzitower.mouseX, bazzitower.mouseY = event.x, 1024 - 1 - event.y
            elif daotower.Flag_mouse[daotower.tower1]:
                daotower.mouseX, daotower.mouseY = event.x, 1024 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # BazziTower
            if event.x <= 1150 and event.x >= 1096:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    bazzitower.Flag_mouse[bazzitower.tower1] = True
                    print(bazzitower.Save_mouseX[bazzitower.tower1], bazzitower.Save_mouseY[bazzitower.tower1])
            # DaoTower
            elif event.x <= 1250 and event.x >= 1196:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    daotower.Flag_mouse[daotower.tower1] = True
                    print(daotower.Save_mouseX[daotower.tower1], daotower.Save_mouseY[daotower.tower1])
             # UniTower
            elif event.x <= 1350 and event.x >= 1296:
                if 1024 - 1 - event.y <= 576 and 1024 - 1 - event.y >= 524:
                    unitower.Flag_mouse[unitower.tower1] = True
                    print(unitower.Save_mouseX[unitower.tower1], unitower.Save_mouseY[unitower.tower1])

        elif event.type == SDL_MOUSEBUTTONUP:
            # BazziTower
            if bazzitower.Flag_mouse[bazzitower.tower1]:
                bazzitower.Save_mouseX[bazzitower.tower1], bazzitower.Save_mouseY[bazzitower.tower1] = event.x, 1024 - 1 - event.y
                print(bazzitower.Save_mouseX, bazzitower.Save_mouseY)
                bazzitower.tower1 += 1
            # DaoTower
            elif daotower.Flag_mouse[daotower.tower1]:
                daotower.Save_mouseX[daotower.tower1], daotower.Save_mouseY[daotower.tower1] = event.x, 1024 - 1 - event.y
                print(daotower.Save_mouseX, daotower.Save_mouseY)
                daotower.tower1 += 1
             # UniTower
            elif unitower.Flag_mouse[unitower.tower1]:
                unitower.Save_mouseX[unitower.tower1], unitower.Save_mouseY[unitower.tower1] = event.x, 1024 - 1 - event.y
                print(unitower.Save_mouseX, unitower.Save_mouseY)
                unitower.tower1 += 1

def pause():
    pass

def resume():
    pass