from pico2d import *
import title_state
import game_framework
import game_world

from player import Mario
from ground import Ground
from background import Background
from initblock import Initblock
from ui import UI

name = "MainState"

mario = None
ui = None
gameTime = 0

def enter():
    global mario
    global ground
    global initblock
    global ui
    mario = Mario()
    ground = Ground()
    background = Background()
    initblock= Initblock()
    ui = UI()
    ui.setCurrentState("mainState")

    global gameTime
    gameTime = 400
    ui.setTime(gameTime)

    game_world.add_object(mario, 1)
    #game_world.add_object(ground, 1)
    game_world.add_object(background, 0)
    game_world.add_object(initblock, 1)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            mario.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(mario, initblock):
        game_world.remove_object(initblock)

    if collide(mario, ground):
        if (mario.stateName!="JUMP"):
            mario.velocityY = 0

    global gameTime
    gameTime -= game_framework.frame_time
    global ui
    ui.setTime(int(gameTime))

    # fill here
    #delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    ui.draw()
    update_canvas()

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
# Ground = load_image('res/ground.png')
# Background = load_image('res/Background.png')
# mario = Mario()
# ground = Ground()
# background = Background()

