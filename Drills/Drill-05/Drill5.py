from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_to_point_203_535():
    x = 0
    y = 90
    frame = 0
    while (x < 204):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.05)
        get_events()

    x = 203
    y = 90
    while (y < 536):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.05)
        get_events()
    pass
def move_to_point_132_243():
    x = 203
    y = 535
    frame = 0
    while (x > 131):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.05)
        get_events()

    x = 132
    y = 535
    while (y > 242):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.05)
        get_events()
    pass
def move_to_point_535_470():
    x = 132
    y = 242
    frame = 0
    while (x < 536):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.05)
        get_events()

    x = 535
    y = 242
    while (y < 471):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.05)
        get_events()
    pass
def move_to_point_477_203():
    x = 535
    y = 470
    frame = 0
    while (x > 476):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.05)
        get_events()

    x = 477
    y = 470
    while (y > 202):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.05)
        get_events()
    pass
def move_to_point_715_136():
    x = 477
    y = 203
    frame = 0
    while (x < 716):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.05)
        get_events()

    x = 715
    y = 203
    while (y < 137):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.05)
        get_events()
    pass
def move_to_point_316_225():
    x = 715
    y = 136
    frame = 0
    while (x > 316):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.05)
        get_events()

    x = 316
    y = 136
    frame = 0
    while (y < 225):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.05)
        get_events()
    pass
def move_to_point_510_92():
    x = 316
    y = 225
    frame = 0
    while (x < 510):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.05)
        get_events()

    x = 510
    y = 225
    frame = 0
    while (y > 92):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.05)
        get_events()
    pass
def move_to_point_692_518():
    x = 510
    y = 92
    frame = 0
    while (x < 692):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.05)
        get_events()

    x = 692
    y = 92
    frame = 0
    while (y < 518):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.05)
        get_events()
    pass
def move_to_point_682_336():
    pass
def move_to_point_712_348():
    pass

while True:
    #move_to_point_203_535()
    #move_to_point_132_243()
    #move_to_point_535_470()
    #move_to_point_477_203()
    #move_to_point_715_136()
    #move_to_point_316_225()
    #move_to_point_510_92()
    move_to_point_692_518()
    move_to_point_682_336()
    move_to_point_712_348()


close_canvas()

