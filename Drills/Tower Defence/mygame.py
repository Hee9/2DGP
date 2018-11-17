import game_framework
import pico2d
import camp_stage
import start_state

DEFENCE_WIDTH, DEFENCE_HEIGHT = 1536, 1024

pico2d.open_canvas(DEFENCE_WIDTH, DEFENCE_HEIGHT)
game_framework.run(start_state)
game_framework.run(camp_stage)
pico2d.close_canvas()