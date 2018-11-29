from pico2d import *

import game_framework
import game_world

from Tower_Bazzi import Bazzi
from Tower_Dao import Dao
from Tower_Uni import Uni
from Enemy import Enemy

NONE, BAZZI, DAO, UNI = range(4)
name = "CAMP Stage"
font = None

background_image = None
money_image = None
store_image = None
money_up_image = None
life_up_image = None

bazzi_image = None
dao_image = None
uni_image = None

enemy = None
enemies = []
Enemy_gap = 1030
Enemy_timer = 0
select_image = NONE

money = 200
life = 20
increase_money = 0

def enter():
    global background_image, bgm, font
    global money_image, store_image, money_up_image, life_up_image
    global bazzi_image, dao_image, uni_image

    background_image = load_image('camp.png')
    money_image = load_image('Money.png')
    store_image = load_image('Store.png')
    money_up_image = load_image('Money_UP.png')
    life_up_image = load_image('Life_UP.png')

    bazzi_image = load_image('Bazzi.png')
    dao_image = load_image('Dao.png')
    uni_image = load_image('uni.png')

    font = load_font('ENCR10B.TTF', 32)
    bgm = load_music('GameStart.ogg')
    bgm.set_volume(50)
    bgm.play()

def exit():
    global background_image, bgm, font
    global money_image, store_image, money_up_image, life_up_image
    global bazzi_image, dao_image, uni_image
    del(background_image, bgm, font)
    del(money_image, store_image, money_up_image, life_up_image)
    del(bazzi_image, dao_image, uni_image)
    game_world.clear()

def update():
    global Enemy_timer, money, life, increase_money
    global enemies

    for game_object in game_world.all_objects():
        game_object.update()

    increase_money = 0.01
    money += increase_money
    Enemy_timer += 1

    if Enemy_timer == 50:
        enemy = Enemy()
        enemies.append(enemy)
        game_world.add_object(enemy, 1)
        Enemy_timer = 0


def draw():
    global background_image, font
    global money_image, store_image, money_up_image, life_up_image
    global money, life
    global bazzi_image, dao_image, uni_image
    clear_canvas()
    background_image.draw(520, 520)
    money_image.draw(1124, 940)
    store_image.draw(1200, 570)
    store_image.draw(1360, 570)
    money_up_image.draw(1150, 500)
    life_up_image.draw(1400, 500)

    bazzi_image.draw(1124, 880)
    dao_image.draw(1124, 780)
    uni_image.draw(1124, 680)

    font.draw(1200, 940, '%1i' % money, (255, 255, 0))
    font.draw(1124, 1000, '%i LIFE' % life, (255, 0, 0))

    font.draw(1200, 880, '20 Won', (255, 255, 0))
    font.draw(1200, 780, '35 Won', (255, 255, 0))
    font.draw(1200, 680, '50 Won', (255, 255, 0))
    font.draw(1230, 570, 'STORE', (255, 0, 0))
    font.draw(1070, 450, 'MONEY UP', (0, 0, 255))
    font.draw(1330, 450, 'LIFE UP', (0, 0, 255))

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

def handle_events():
    global select_image, bazzi_image, dao_image, uni_image
    global money, increase_money, life

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            bazzi_image.draw(event.x, 1024-1-event.y)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # BazziTower
            if event.x <= 1150 and event.x >= 1096 and 1024 - 1 - event.y <= 906 and 1024 - 1 - event.y >= 854:
                select_image = BAZZI
            # DaoTower
            elif event.x <= 1150 and event.x >= 1096 and 1024 - 1 - event.y <= 806 and 1024 - 1 - event.y >= 754:
                select_image = Dao
            # UniTower
            elif event.x <= 1150 and event.x >= 1096 and 1024 - 1 - event.y <= 706 and 1024 - 1 - event.y >= 654:
                select_image = Uni
            # Money_UP
            elif event.x <= 1176 and event.x >= 1124 and 1024 - 1 - event.y <= 525 and 1024 - 1 - event.y >= 475:
                print("COLLIDE")
                increase_money = 1
            # Life_UP
            elif event.x <= 1422 and event.x >= 1378 and 1024 - 1 - event.y <= 525 and 1024 - 1 - event.y >= 475:
                life += 1

        elif event.type == SDL_MOUSEBUTTONUP:
            # BazziTower
            if select_image == BAZZI:
                bazzi = Bazzi(event.x, 1024 - 1 - event.y)
                game_world.add_object(bazzi, 1)
                select_image = NONE
            # BazziTower
            elif select_image == Dao:
                dao = Dao(event.x, 1024 - 1 - event.y)
                game_world.add_object(dao, 1)
                select_image = NONE
            # BazziTower
            elif select_image == Uni:
                uni = Uni(event.x, 1024 - 1 - event.y)
                game_world.add_object(uni, 1)
                select_image = NONE

def pause():
    pass

def resume():
    pass