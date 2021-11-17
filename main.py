from pico2d import *
import random
import title_state
import game_framework

from player import Mario
from ground import Ground
from background import Background
X,Y=512*2,160*5
running = True

def enter():
    global mario,ground,background
    mario = Mario()
    ground = Ground()
    background = Background()

def exit():
    global mario, ground, background
    del(mario)
    del(ground)
    del(background)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        mario.handle_event(event)

def update():
    mario.update()
    delay(0.05)

def draw():
    clear_canvas()
    ground.draw()
    background.draw()
    mario.draw()
    update_canvas()


# Ground = load_image('res/ground.png')
# Background = load_image('res/Background.png')
# mario = Mario()
# ground = Ground()
# background = Background()

