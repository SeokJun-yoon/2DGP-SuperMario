import game_framework
from pico2d import *

import json
import server

with open('characters.json', 'r') as f:
    characters = json.load(f)

canvas_sizeX = 1000
canvas_sizeY = 800

# Mario Run Speed
PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 1 cm
RUN_SPEED_KMPH = 5.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Mario Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

# Mario Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP, CHANGE, CHANGE2 = range(8)

# key event_table
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}


class IdleState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "IDLE"
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS

    def exit(mario, event):
        #if event == SPACE:
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_IDLE"]["FRAMESIZE"]
        mario.y += mario.velocityY * game_framework.frame_time

        mario.y = clamp(0, mario.y, 1000 - 25)


    def draw(mario):
        #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
        #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"] * 5,
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"] * 5)
        else:
            mario.image.clip_draw(
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)


class RunState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "RUN"
        if event==RIGHT_DOWN:
            mario.isRight = True
            mario.velocity +=RUN_SPEED_PPS
        elif event==LEFT_DOWN:
            mario.isRight = False
            mario.velocity -= RUN_SPEED_PPS
        elif event ==RIGHT_UP:
            mario.isRight = False
            mario.velocity -=RUN_SPEED_PPS
        elif event==LEFT_UP:
            mario.isRight = False
            mario.velocity +=RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)
        pass

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_RUN"]["FRAMESIZE"]
        mario.x += mario.velocity * game_framework.frame_time
#
        mario.x = clamp(mario.minimumX, mario.x, 40000)

        if mario.isRight == True and mario.screenX >= server.background.canvas_width // 2 :
            mario.scrollMode = True
        else:
            mario.scrollMode = False

        if mario.scrollMode == True :
            mario.screenX = server.background.canvas_width // 2
            mario.minimumX = mario.x - server.background.canvas_width // 2
        else:
            mario.screenX += mario.velocity * game_framework.frame_time
            mario.screenX = clamp(0, mario.screenX, server.background.canvas_width // 2)


    def draw(mario):
        #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
        #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom

        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"] * 5,
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"] * 5)
        else:
            mario.image.clip_draw(
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)


# 점프 상태
class IdleJumpState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "JUMP"
        mario.velocityY = RUN_SPEED_PPS
        # if event == RIGHT_DOWN:
        #     mario.velocity += RUN_SPEED_PPS
        # elif event == LEFT_DOWN:
        #     mario.velocity -= RUN_SPEED_PPS
        # elif event == RIGHT_UP:
        #     mario.velocity -= RUN_SPEED_PPS
        # elif event == LEFT_UP:
        #     mario.velocity += RUN_SPEED_PPS
        # mario.dir = clamp(-1, mario.velocity, 1)


    def exit(mario, event):
        if event == SPACE_UP:
            mario.velocityY = -RUN_SPEED_PPS


    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_JUMP"]["FRAMESIZE"]
        #mario.x += mario.velocity * game_framework.frame_time
        mario.y += mario.velocityY * game_framework.frame_time
        mario.y = clamp(0, mario.y, 1000 - 500)
        if mario.y >= 500:
            mario.velocityY = -RUN_SPEED_PPS
            mario.add_event(CHANGE)
            print("mario.y : ", mario.y)
            print("mario.velocityY : ",mario.velocityY)


        #print(mario.dir)


    def draw(mario):
        #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2

        # 일반
        #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom

        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)
        else:
            mario.image.clip_draw(
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)

# 점프 움직임 상태
class RunJumpState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "JUMP"
        mario.velocityY = RUN_SPEED_PPS

    def exit(mario, event):
        # if event == SPACE_UP:
        #     mario.add_event(FallingState)
        # if mario.y == 500:
        #     mario.add_event(FallingState)
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_JUMP"]["FRAMESIZE"]
        mario.x += mario.velocity * game_framework.frame_time
        mario.y += mario.velocityY * game_framework.frame_time
        mario.y = clamp(0, mario.y, 1000 - 500)
        #if mario.y<=225:
        #    mario.add_event(IdleState)
        mario.x = clamp(mario.minimumX, mario.x, 40000)
        if mario.y >= 500:
            mario.velocityY = -RUN_SPEED_PPS
            mario.add_event(CHANGE)
            print("mario.y : ", mario.y)
            print("mario.velocityY : ",mario.velocityY)

        if mario.isRight == True and mario.screenX >= server.background.canvas_width // 2:
            mario.scrollMode = True
        else:
            mario.scrollMode = False

        if mario.scrollMode == True:
            mario.screenX = server.background.canvas_width // 2
            mario.minimumX = mario.x - server.background.canvas_width // 2
        else:
            mario.screenX += mario.velocity * game_framework.frame_time
            mario.screenX = clamp(0, mario.screenX, server.background.canvas_width // 2)
        #print(mario.dir)
        print(mario.y)

    def draw(mario):
        #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2

        # 일반
        #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)
        else:
            mario.image.clip_draw(
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)

class FallingState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "JUMP"
        mario.velocityY = -RUN_SPEED_PPS


        # if event == RIGHT_DOWN:
        #     mario.velocity += RUN_SPEED_PPS
        # elif event == LEFT_DOWN:
        #     mario.velocity -= RUN_SPEED_PPS
        # elif event == RIGHT_UP:
        #     mario.velocity -= RUN_SPEED_PPS
        # elif event == LEFT_UP:
        #     mario.velocity += RUN_SPEED_PPS
        # mario.dir = clamp(-1, mario.velocity, 1)


    def exit(mario, event):
        if event == SPACE_UP:
            mario.velocityY = -RUN_SPEED_PPS

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_JUMP"]["FRAMESIZE"]
        mario.x += mario.velocity * game_framework.frame_time
        mario.y += mario.velocityY * game_framework.frame_time
        mario.y = clamp(0, mario.y, 1000 - 500)
        mario.x = clamp(mario.minimumX, mario.x, 40000)

        if mario.isRight == True and mario.screenX >= server.background.canvas_width // 2:
            mario.scrollMode = True
        else:
            mario.scrollMode = False

        if mario.scrollMode == True:
            mario.screenX = server.background.canvas_width // 2
            mario.minimumX = mario.x - server.background.canvas_width // 2
        else:
            mario.screenX += mario.velocity * game_framework.frame_time
            mario.screenX = clamp(0, mario.screenX, server.background.canvas_width // 2)

        if mario.y <= 100:
            mario.add_event(CHANGE)
        print("mario.velocityY : ", mario.velocityY)
        print("mario.y : ",mario.y)

    def draw(mario):
        #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2

        # 일반
        #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom

        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)
        else:
            mario.image.clip_draw(
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)

class LandingState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "JUMP"
        mario.velocityY = 0


    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_IDLE"]["FRAMESIZE"]

        if mario.velocity != 0:
            mario.add_event(CHANGE2)
        else:
            mario.add_event(CHANGE)

    def draw(mario):
        #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
        #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"] * 5,
                characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"] * 5)
        else:
            mario.image.clip_draw(
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, server.mario.y,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)

next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: IdleJumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE_DOWN: RunJumpState},
    IdleJumpState: {RIGHT_UP: FallingState, LEFT_UP: FallingState, SPACE_UP: FallingState, RIGHT_DOWN: RunJumpState, LEFT_DOWN: RunJumpState, SPACE_DOWN: IdleJumpState, CHANGE:FallingState },
    RunJumpState: {RIGHT_UP: IdleJumpState, LEFT_UP: IdleJumpState, SPACE_UP: FallingState, RIGHT_DOWN: IdleJumpState, LEFT_DOWN: IdleJumpState, SPACE_DOWN: RunJumpState,CHANGE:FallingState},
    FallingState: {RIGHT_UP: FallingState, LEFT_UP: FallingState, SPACE_UP: FallingState, RIGHT_DOWN: FallingState, LEFT_DOWN: FallingState, SPACE_DOWN: FallingState, CHANGE:LandingState},
    LandingState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: LandingState,CHANGE:IdleState, CHANGE2:RunState}
}

class Mario:
    def __init__(self): # 생성자
        self.x, self.y = 100, 150 # 초기 마리오 좌표
        #self.image = load_image('res/MarioIdle.png')
        self.image = load_image('res/characters.gif')
        self.characterName = "SMALLMARIO"
        self.stateName = "IDLE"
        self.frame = 0
        self.index = 0
        self.velocity = 0     # 속도
        self.dir = 1          # -1 left, +1 right
        self.velocityY = -300    # y 속도
        self.mass=70
        self.screenX = self.x
        self.minimumX = 0
        self.scrollmode = False
        self.isRight = False

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        #self.state="Idle"


    def add_event(self, event):
        self.event_que.insert(0,event)


    def update(self):
        self.cur_state.do(self)
        print(self.cur_state)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        # 일반 스크롤링의 경우
        # self.x = clamp(0, self.x, server.background.w-1)
        # self.y = clamp(0, self.y, server.background.h-1)

    def get_bb(self):
        return self.x-36, self.y-38, self.x+36,self.y+38

    def draw(self):
        self.cur_state.draw(self)
        #self.font.draw(self.x-60, self.y+50,
                       #'Time: %3.2f)'%get_time(),(255,255,0))
        #draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)