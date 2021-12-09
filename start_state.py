import game_framework
from pico2d import *
import main_state

from ui import UI


name = "StartState"
image = None
logo_time = 0.0

myUI = None

def enter():
    global image
    image = load_image('res/Intro.png')
    global myUI
    myUI = UI()
    myUI.setCurrentState("StartState")

def exit():
    global image
    global logo_time
    logo_time = 0.0
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)==(SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
        pass
def draw():
    clear_canvas()
    image.draw(500,400,1000,800)
    myUI.draw()
    update_canvas()


def update():
    global logo_time
    if (logo_time > 1.5) :
        logo_time = 0.0
        game_framework.change_state(main_state)



    delay(0.01)
    logo_time += 0.01


def pause():
    pass


def resume():
    pass




