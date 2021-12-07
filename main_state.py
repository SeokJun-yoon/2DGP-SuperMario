from pico2d import *
import title_state
import game_framework
import game_world
import server

from object import Object
from player import Mario
from ground import Ground
from background import Background
from initblock import Initblock
from ui import UI

with open('ground.json', 'r') as f:
    ground_data = json.load(f)

name = "MainState"

#mario = None
ui = None
gameTime = 0
groundTiles = []
testob = []
initblock = []

def enter():

    global ui
    server.mario = Mario()
    ground = Ground()
    server.background = Background()

    ui = UI()
    ui.setCurrentState("mainState")

    global gameTime
    gameTime = 400
    ui.setTime(gameTime)

    global groundTiles
    groundTiles = [Object("groundtile") for i in range(ground_data["firstCount"])]
    for i in range(ground_data["firstCount"]):
        groundTiles[i].x = int(ground_data["firstStage"][str(i)]["x"])
        groundTiles[i].y = int(ground_data["firstStage"][str(i)]["y"])
        groundTiles[i].set_bb()

    global initblock
    initblock = [Object("initblock"), Object("pipe1"),Object("pipe2"),Object("pipe3")]
    for i,test in enumerate(initblock):
        test.checkType()
        test.x = 200 + i * 100
        test.y = 300 + i * 100
        test.set_bb()

    # global testob
    # testob = [Object("qmark")]
    #
    # testob.append(Object("pipe1"))
    #
    #
    # for i in testob:
    #     i.checkType()
    #     i.x = 500
    #     i.y = 350
    #
    #
    # testob[1].x = 800
    # testob[1].y = 500
    #
    # for i in testob:
    #     i.set_bb()


    for tile in groundTiles:
        game_world.add_object(tile, 1)

    # for ob in testob:
    #     game_world.add_object(ob, 1)

    game_world.add_object(server.mario, 1)
    #game_world.add_object(ground, 1)
    game_world.add_object(server.background, 0)

    for ib in initblock:
        game_world.add_object(ib,1)

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
            server.mario.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # if collide(mario, initblock):
    #     game_world.remove_object(initblock)

    for groundTile in groundTiles:
        if collide(server.mario, groundTile):
            if server.mario.stateName != "JUMP":
                server.mario.velocityY = 0

    # for s in testob:
    #     if s.type == 1:
    #         if collide(mario, s):
    #             print("파이프 아닌것")
    #     elif s.type == 2:
    #         if collide2(mario,s.bb[0],s.bb[1],s.bb[2],s.bb[3]):
    #             print("파이프")
    #
    #         elif collide2(mario,s.bb[4],s.bb[5],s.bb[6],s.bb[7]):
    #             print("파이프 어딘가")

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

def collide2(a, left, bottom, right, top):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    if left_a > right: return False
    if right_a < left: return False
    if top_a < bottom: return False
    if bottom_a > top: return False
    return True

# Ground = load_image('res/ground.png')
# Background = load_image('res/Background.png')
# mario = Mario()
# ground = Ground()
# background = Background()

