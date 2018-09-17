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

    pass
def move_to_point_535_470():
    pass
def move_to_point_477_203():
    pass
def move_to_point_715_136():
    pass
def move_to_point_316_225():
    pass
def move_to_point_510_92():
    pass
def move_to_point_692_518():
    pass
def move_to_point_682_336():
    pass
def move_to_point_712_348():
    pass


while True:
    move_to_point_203_535()
    move_to_point_132_243()
    move_to_point_535_470()
    move_to_point_477_203()
    move_to_point_715_136()
    move_to_point_316_225()
    move_to_point_510_92()
    move_to_point_692_518()
    move_to_point_682_336()
    move_to_point_712_348()


close_canvas()

