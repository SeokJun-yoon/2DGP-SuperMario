from pico2d import *
import title_state
import game_framework
import game_world

from player import Mario
from ground import Ground
from background import Background

name = "MainState"

mario = None
def enter():
    global mario
    mario = Mario()
    ground = Ground()
    background = Background()

    game_world.add_object(mario, 1)
    game_world.add_object(ground, 1)
    game_world.add_object(background,0)

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
    # fill here
    #delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


# Ground = load_image('res/ground.png')
# Background = load_image('res/Background.png')
# mario = Mario()
# ground = Ground()
# background = Background()

