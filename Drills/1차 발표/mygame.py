import game_framework
import pico2d
import camp_stage

pico2d.open_canvas(1040, 1040)
game_framework.run(camp_stage)
pico2d.close_canvas()