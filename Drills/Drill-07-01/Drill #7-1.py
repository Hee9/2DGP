from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

points = [(random.randint(0,1280),random.randint(0,1024)) for i in range(20)]

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
n = 1

def draw_point(p):
    global frame,n
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if points[n-1][0] > points[n][0]:
        character.clip_draw(frame*100,0,100,100,p[0],p[1])
    else:
        character.clip_draw(frame * 100, 100, 100, 100, p[0], p[1])

    frame = (frame+1) % 8
    update_canvas()

open_canvas(KPU_WIDTH,KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

while True:

    delay(0.05)

close_canvas()