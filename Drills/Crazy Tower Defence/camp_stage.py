from pico2d import *

import game_framework
import game_world
import pause_state
import game_over_state
import pirate_stage

from Tower_Bazzi import Bazzi
from Tower_Dao import Dao
from Tower_Uni import Uni
from Camp_Enemy_First import Camp_Enemy_First
from Camp_Enemy_Second import Camp_Enemy_Second
from Camp_Enemy_Boss import Camp_Enemy_Boss

NONE, BAZZI, DAO, UNI = range(4)
name = "CAMP Stage"
font = None

camp_image = None
background_image = None
pause_image = None
money_image = None
store_image = None
money_up_image = None
life_up_image = None
small_power_up_image = None
big_power_up_image = None

Click_Bazzi = None
Click_Dao = None
Click_Uni = None

bazzi_image = None
dao_image = None
uni_image = None

camp_enemy_first = None
camp_enemies_first = []
camp_enemy_second = None
camp_enemies_second = []
camp_enemy_boss = None
camp_enemies_boss = []

Enemy_gap = 1030
Enemy_timer = 0
select_image = NONE
change_stage_check = False

money = 30
life = 20
increase_money = 0

def enter():
    global camp_image, background_image, start_bgm, bgm, font, pause_image, money_image
    global store_image, money_up_image, life_up_image, small_power_up_image, big_power_up_image
    global Click_Bazzi, Click_Dao, Click_Uni
    global bazzi_image, dao_image, uni_image
    global increase_money
    increase_money = 0.01

    camp_image = load_image('camp.png')
    background_image = load_image('background.png')
    pause_image = load_image('pause.png')
    money_image = load_image('Money.png')
    store_image = load_image('Store.png')
    money_up_image = load_image('Money_UP.png')
    life_up_image = load_image('Life_UP.png')
    small_power_up_image = load_image('Small_Power_UP.png')
    big_power_up_image = load_image('Big_Power_UP.png')

    Click_Bazzi = load_image('Click_Bazzi.png')
    Click_Dao = load_image('Click_Dao.png')
    Click_Uni = load_image('Click_Uni.png')

    bazzi_image = load_image('Bazzi.png')
    dao_image = load_image('Dao.png')
    uni_image = load_image('uni.png')

    font = load_font('ENCR10B.TTF', 32)
    start_bgm = load_wav('GameStart.ogg')
    bgm = load_music('camp_BGM.ogg')

    start_bgm.set_volume(50)
    start_bgm.play(1)

    bgm.set_volume(30)
    bgm.play()

def exit():
    global camp_image, background_image, start_bgm, bgm, font, pause_image, money_image
    global store_image, money_up_image, life_up_image, small_power_up_image, big_power_up_image
    global Click_Bazzi, Click_Dao, Click_Uni
    global bazzi_image, dao_image, uni_image
    del(camp_image, background_image, start_bgm, bgm, font, pause_image, money_image)
    del(store_image, money_up_image, life_up_image, small_power_up_image, big_power_up_image)
    del(Click_Bazzi, Click_Dao, Click_Uni)
    del(bazzi_image, dao_image, uni_image)
    game_world.clear()

def update():
    global Enemy_timer, money, life, increase_money
    global camp_enemy_first, camp_enemy_second, camp_enemy_boss
    global camp_enemies_first, camp_enemy_second, camp_enemies_boss

    for game_object in game_world.all_objects():
        game_object.update()

    #increase_money = 0.01
    money += increase_money
    Enemy_timer += 1

    #print(Camp_Enemy_First.draw_count)

    if Enemy_timer == 50:
        camp_enemy_first = Camp_Enemy_First()
        camp_enemy_second = Camp_Enemy_Second()
        camp_enemy_boss = Camp_Enemy_Boss()
        if Camp_Enemy_First.draw_count < 15:
            camp_enemies_first.append(camp_enemy_first)
            game_world.add_object(camp_enemy_first, 1)
            Camp_Enemy_First.draw_count += 1
        elif Camp_Enemy_First.draw_count < 30:
            camp_enemies_second.append(camp_enemy_second)
            game_world.add_object(camp_enemy_second, 1)
            Camp_Enemy_First.draw_count += 1
            Enemy_timer += 1
        elif Camp_Enemy_First.draw_count < 31:
            camp_enemies_boss.append(camp_enemy_boss)
            game_world.add_object(camp_enemy_boss, 1)
            Camp_Enemy_First.draw_count += 1
            Enemy_timer += 1
        Enemy_timer = 0
    print(Camp_Enemy_First.die_count)

    if life <= 0:
        game_framework.change_state(game_over_state)

    if Camp_Enemy_First.die_count == 30:
        game_framework.change_state(pirate_stage)


def draw():
    global background_image, font, pause_image, money_image
    global store_image, money_up_image, life_up_image, small_power_up_image, big_power_up_image
    global Click_Bazzi, Click_Dao, Click_Uni
    global money, life
    global bazzi_image, dao_image, uni_image

    clear_canvas()
    camp_image.draw(520, 520)
    background_image.draw(1288, 520)
    pause_image.draw(1500, 980)
    money_image.draw(1124, 940)
    store_image.draw(1200, 570)
    store_image.draw(1360, 570)
    money_up_image.draw(1150, 500)
    life_up_image.draw(1400, 500)
    small_power_up_image.draw(1150, 350)
    big_power_up_image.draw(1150, 200)

    Click_Bazzi.draw(1400, 370)
    Click_Dao.draw(1400, 320)
    Click_Uni.draw(1400, 270)

    Click_Bazzi.draw(1400, 200)
    Click_Dao.draw(1400, 150)
    Click_Uni.draw(1400, 100)

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
    font.draw(1070, 420, '200 Won', (0, 0, 255))
    font.draw(1330, 450, 'LIFE UP', (0, 0, 255))
    font.draw(1330, 420, '300 Won', (0, 0, 255))
    font.draw(1055, 300, 'SMALL_POWER_UP', (0, 0, 255))
    font.draw(1055, 270, '100 Won', (0, 0, 255))
    font.draw(1055, 150, 'BIG_POWER_UP', (0, 0, 255))
    font.draw(1055, 120, '200 Won', (0, 0, 255))

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
            # pause_state
            if event.x <= 1533 and event.x >= 1467 and 1024 - 1 - event.y <= 1110 and 1024 - 1 - event.y >= 947:
                game_framework.push_state(pause_state)
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
                if money >= 200:
                    increase_money += 0.01
                    money -= 200
            # Life_UP
            elif event.x <= 1422 and event.x >= 1378 and 1024 - 1 - event.y <= 525 and 1024 - 1 - event.y >= 475:
                if money >= 100:
                    life += 1
                    money -= 100
            # Samll_Power_UP
            # Bazzi_Power_UP
            elif event.x <= 1420 and event.x >= 1378 and 1024 - 1 - event.y <= 388 and 1024 - 1 - event.y >= 351:
                Bazzi.attack_damage += 0.01
                money -= 100
            # Dao_Power_UP
            elif event.x <= 1420 and event.x >= 1378 and 1024 - 1 - event.y <= 336 and 1024 - 1 - event.y >= 301:
                Dao.attack_damage += 0.01
                money -= 100
            # Uni_Power_UP
            elif event.x <= 1420 and event.x >= 1378 and 1024 - 1 - event.y <= 286 and 1024 - 1 - event.y >= 251:
                Uni.attack_damage += 0.01
                money -= 100
            # Big_Power_UP
            # Bazzi_Power_UP
            elif event.x <= 1420 and event.x >= 1378 and 1024 - 1 - event.y <= 218 and 1024 - 1 - event.y >= 180:
                Bazzi.attack_damage += 0.03
                money -= 200
            # Dao_Power_UP
            elif event.x <= 1420 and event.x >= 1378 and 1024 - 1 - event.y <= 168 and 1024 - 1 - event.y >= 130:
                Dao.attack_damage += 0.03
                money -= 200
            # Uni_Power_UP
            elif event.x <= 1420 and event.x >= 1378 and 1024 - 1 - event.y <= 118 and 1024 - 1 - event.y >= 80:
                Uni.attack_damage += 0.03
                money -= 200

        elif event.type == SDL_MOUSEBUTTONUP:
            # BazziTower
            if select_image == BAZZI:
                if event.x < 1040:
                    if money >= 20:
                        bazzi = Bazzi(event.x, 1024 - 1 - event.y)
                        game_world.add_object(bazzi, 1)
                        select_image = NONE
                        money -= 20
            # BazziTower
            elif select_image == Dao:
                if event.x < 1040:
                    if money >= 35:
                        dao = Dao(event.x, 1024 - 1 - event.y)
                        game_world.add_object(dao, 1)
                        select_image = NONE
                        money -= 35
            # BazziTower
            elif select_image == Uni:
                if event.x < 1040:
                    if money >= 50:
                        uni = Uni(event.x, 1024 - 1 - event.y)
                        game_world.add_object(uni, 1)
                        select_image = NONE
                        money -= 50

def pause():
    pass

def resume():
    pass