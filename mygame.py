import game_framework
import pico2d

import start_state
import title_state
canvas_sizeX = 1000
canvas_sizeY = 800

pico2d.open_canvas(canvas_sizeX,canvas_sizeY)
game_framework.run(start_state)
pico2d.close_canvas()