import game_framework
from pico2d import *
import main

name = "TitleState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('res/start.png')


def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)==(SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main)

def draw():
    clear_canvas()
    image.draw(500,400,1000,800)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass






