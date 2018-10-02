from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

points = [(random.randint(0,1280),random.randint(0,1024)) for i in range(5)]

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
n = 1

def draw_point(p):
    global frame,n
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if points[n-1][0] > points[n][0]:
        character.clip_draw(frame*100,0,100,100,p[0],p[1])
    #else:
        character.clip_draw(frame * 100, 100, 100, 100, p[0], p[1])

    frame = (frame+1) % 8
    update_canvas()

def draw_line(p1,p2):

    for i in range(0,100,2):
        t = i /100
        x = (1-t)*p1[0] + t*p2[0]
        y = (1-t)*p1[1] + t*p2[1]
        draw_point((x,y))
        delay(0.05)

    draw_point(p2)

open_canvas(KPU_WIDTH,KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

while True:

    draw_line(points[n-1],points[n])

    n = (n+1)%5

    delay(0.05)

    handle_events()

close_canvas()