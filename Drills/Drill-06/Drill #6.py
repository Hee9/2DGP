from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def character_move():
    c_x = 100
    c_y = 100
    frame = 0
    m_x, m_y = KPU_WIDTH // 2, KPU_HEIGHT // 2

    while(c_x < m_x):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, c_x, c_y)
        mouse.draw(m_x + 20, m_y - 20)
        update_canvas()
        frame = (frame + 1) % 8
        c_x += 5
        delay(0.05)
        get_events()

    while(c_y < m_y):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, c_x, c_y)
        mouse.draw(m_x + 20, m_y - 20)
        update_canvas()
        frame = (frame + 1) % 8
        c_y += 5
        delay(0.05)
        get_events()

    pass

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    #character_move()
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()


close_canvas()




