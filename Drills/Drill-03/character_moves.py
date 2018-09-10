from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 400):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.005)

while(True):

    x = 390
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.005)

    y = 90
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, y)
        y = y + 2
        delay(0.005)

    x = 780
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 570)
        x = x - 2
        delay(0.005)

    y = 570
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        y = y - 2
        delay(0.005)

    x = 10
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.005)

    for i in range(0,360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + (4 * (math.cos(math.pi * (i/180))))
        y = y + (4 * (math.sin(math.pi * (i/180))))
        delay(0.005)
    

close_canvas()

