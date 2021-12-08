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
RUN_SPEED_KMPH = 3.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Mario Action Speed
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

# Mario Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP, JUMP_TO_IDLE, JUMP_TO_RUN = range(8)

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

        mario.y = clamp(128 + 40, mario.y, 1000 - 25)


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

        mario.velocity = clamp(-RUN_SPEED_PPS, mario.velocity, RUN_SPEED_PPS)
        mario.dir = clamp(-1, mario.velocity, 1)
        pass

    def exit(mario, event):
        mario.scrollMode = False
        mario.screenLock = True


    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_RUN"]["FRAMESIZE"]
        mario.x += mario.velocity * game_framework.frame_time
#
        mario.x = clamp(mario.minimumX, mario.x, 40000)

        if mario.isRight == True and mario.screenX >= server.background.canvas_width // 2 :
            mario.scrollMode = True
        else:
            mario.scrollMode = False

        if mario.scrollMode == True:
            mario.screenX = server.background.canvas_width//2
            mario.minPosition = mario.x - server.background.canvas_width//2
            mario.screenLock = False
        else:
            mario.screenX += mario.velocity * game_framework.frame_time
            mario.screenX = clamp(0, mario.screenX, server.background.canvas_width//2)
            mario.screenLock = True


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
class JumpState:
    def enter(mario, event):
        mario.frame = 0
        mario.stateName = "JUMP"

        if mario.isInground == True:
            mario.velocityY = RUN_SPEED_PPS
            mario.isInground = False
            mario.isGoUp = True
        else:
            pass

        if event == RIGHT_DOWN:
            mario.isMove = True
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.isMove = True
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.isMove = False
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.isMove = False
            mario.velocity += RUN_SPEED_PPS
        elif event == SPACE_UP:
            mario.velocityY = -RUN_SPEED_PPS

        mario.velocity = clamp(-RUN_SPEED_PPS, mario.velocity, RUN_SPEED_PPS)

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_JUMP"]["FRAMESIZE"]
        mario.x += mario.velocity * game_framework.frame_time
        mario.y += mario.velocityY * game_framework.frame_time
        maxHeight = 600

        if(mario.y >= maxHeight):
            mario.velocityY = -RUN_SPEED_PPS
            mario.isGoUp = False

        if mario.isInground == True:
            # 판단 idle이나 run으로 어떤걸로 가는지 판단.
            mario.velocityY = 0
            # y값은 바닥으로 떨어질지, 오브젝트 위에 떨어질지 판단해서 y값 결정
            mario.y = 128 + 40
            if mario.isMove == True:
                mario.add_event(JUMP_TO_RUN)
            else:
                mario.add_event(JUMP_TO_IDLE)


        if mario.isRight == True and mario.screenX >= server.background.canvas_width//2:
            mario.scrollMode = True
        else:
            mario.scrollMode = False

        if mario.scrollMode == True:
            mario.screenX = server.background.canvas_width//2
            mario.minPosition = mario.x - server.background.canvas_width//2
            mario.screenLock = False
        else:
            mario.screenX += mario.velocity * game_framework.frame_time
            mario.screenX = clamp(0, mario.screenX, server.background.canvas_width//2)
            mario.screenLock = True

        # 언제 idle이나 run 갈거냐 판단을 해야 하자나


    def draw(mario):
        cy = server.mario.y

        if mario.dir == 1:
            mario.image.clip_draw(
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
                characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
                server.mario.screenX, cy,
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
                server.mario.screenX, cy,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "WIDTH"] * 5,
                characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
                    "HEIGHT"] * 5)

# 점프 움직임 상태
# class RunJumpState:
#     def enter(mario, event):
#         mario.frame = 0
#         mario.stateName = "JUMP"
#         mario.velocityY = RUN_SPEED_PPS
#         if mario.scrollmode== True :
#             mario.screenLock = False
#
#     def exit(mario, event):
#         pass
#
#
#
#     def do(mario):
#         mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_JUMP"]["FRAMESIZE"]
#         mario.x += mario.velocity * game_framework.frame_time
#         mario.y += mario.velocityY * game_framework.frame_time
#         mario.y = clamp(0, mario.y, 1000 - 500)
#         mario.x = clamp(mario.minimumX, mario.x, 40000)
#         if mario.y >= 500:
#             mario.velocityY = -RUN_SPEED_PPS
#             mario.add_event(CHANGE_STATE)
#
#         #print("mario.y : ", mario.y)
#         #print("mario.velocityY : ",mario.velocityY)
#
#         if mario.isRight == True and mario.screenX >= server.background.canvas_width // 2:
#             mario.scrollMode = True
#         else:
#             mario.scrollMode = False
#
#         if mario.scrollMode == True:
#             mario.screenX = server.background.canvas_width // 2
#             mario.minimumX = mario.x - server.background.canvas_width // 2
#         else:
#             mario.screenX += mario.velocity * game_framework.frame_time
#             mario.screenX = clamp(0, mario.screenX, server.background.canvas_width // 2)
#
#
#         #print(mario.dir)
#         #print(mario.y)
#
#     def draw(mario):
#         #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
#
#         # 일반
#         #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
#         if mario.dir == 1:
#             mario.image.clip_draw(
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
#                 server.mario.screenX, server.mario.y,
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "WIDTH"] * 5,
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "HEIGHT"] * 5)
#         else:
#             mario.image.clip_draw(
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
#                 server.mario.screenX, server.mario.y,
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "WIDTH"] * 5,
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "HEIGHT"] * 5)

# class FallingState:
#     def enter(mario, event):
#         mario.frame = 0
#         mario.stateName = "JUMP"
#         mario.velocityY = -RUN_SPEED_PPS
#
#
#         # if event == RIGHT_DOWN:
#         #     mario.velocity += RUN_SPEED_PPS
#         # elif event == LEFT_DOWN:
#         #     mario.velocity -= RUN_SPEED_PPS
#         # elif event == RIGHT_UP:
#         #     mario.velocity -= RUN_SPEED_PPS
#         # elif event == LEFT_UP:
#         #     mario.velocity += RUN_SPEED_PPS
#         # mario.dir = clamp(-1, mario.velocity, 1)
#
#
#     def exit(mario, event):
#         pass
#
#     def do(mario):
#         mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_JUMP"]["FRAMESIZE"]
#         mario.x += mario.velocity * game_framework.frame_time
#         mario.y += mario.velocityY * game_framework.frame_time
#         mario.y = clamp(0, mario.y, 1000 - 500)
#         mario.x = clamp(mario.minimumX, mario.x, 40000)
#
#         if mario.isRight == True and mario.screenX >= server.background.canvas_width // 2:
#             mario.scrollMode = True
#         else:
#             mario.scrollMode = False
#
#         if mario.scrollMode == True:
#             mario.screenX = server.background.canvas_width // 2
#             mario.minimumX = mario.x - server.background.canvas_width // 2
#         else:
#             mario.screenX += mario.velocity * game_framework.frame_time
#             mario.screenX = clamp(0, mario.screenX, server.background.canvas_width // 2)
#
#         print("mario.y : ", mario.y)
#         if mario.y <= 175:
#             print("문제지점 발생!")
#             mario.add_event(CHANGE_STATE)
#         #print("mario.velocityY : ", mario.velocityY)
#
#
#     def draw(mario):
#         #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
#
#         # 일반
#         #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
#
#         if mario.dir == 1:
#             mario.image.clip_draw(
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
#                 server.mario.screenX, server.mario.y,
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "WIDTH"] * 5,
#                 characters[mario.characterName]["RIGHT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "HEIGHT"] * 5)
#         else:
#             mario.image.clip_draw(
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
#                 server.mario.screenX, server.mario.y,
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "WIDTH"] * 5,
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "HEIGHT"] * 5)

# class LandingState:
#     def enter(mario, event):
#         mario.frame = 0
#         mario.stateName = "IDLE"
#         mario.velocityY = 0
#
#
#     def exit(mario, event):
#         pass
#
#     def do(mario):
#         mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[mario.characterName]["RIGHT_IDLE"]["FRAMESIZE"]
#
#         if mario.velocity != 0:
#             mario.add_event(CHANGE_STATE2)
#         else:
#             mario.add_event(CHANGE_STATE)
#
#     def draw(mario):
#         #cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
#         #cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
#         if mario.dir == 1:
#             mario.image.clip_draw(
#                 characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
#                 characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
#                 characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
#                 characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
#                 server.mario.screenX, server.mario.y,
#                 characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"] * 5,
#                 characters[mario.characterName]["RIGHT_"+mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"] * 5)
#         else:
#             mario.image.clip_draw(
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["LEFT"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["BOTTOM"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["WIDTH"],
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))]["HEIGHT"],
#                 server.mario.screenX, server.mario.y,
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "WIDTH"] * 5,
#                 characters[mario.characterName]["LEFT_" + mario.stateName]["FRAMES"][str(int(mario.frame))][
#                     "HEIGHT"] * 5)

next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE_DOWN: JumpState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, SPACE_UP: JumpState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, SPACE_DOWN: JumpState,
                JUMP_TO_IDLE:IdleState, JUMP_TO_RUN : RunState}
}

class Mario:
    def __init__(self): # 생성자
        self.x, self.y = 100, 200 # 초기 마리오 좌표
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

        self.isInground = False
        self.scrollmode = False
        self.isRight = False
        self.screenLock = True

        self.isMove = False
        self.isInGround = False
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        #self.state="Idle"


    def add_event(self, event):
        self.event_que.insert(0,event)


    def update(self):
        self.cur_state.do(self)
        print("현재 스테이트 :", self.cur_state)
        # print("screenLock : ", self.screenLock)
        # print("scrollmode : ", self.scrollmode)
        # print("velocity : ", self.velocity)
        # print("\n")
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        # 일반 스크롤링의 경우
        # self.x = clamp(0, self.x, server.background.w-1)
        # self.y = clamp(0, self.y, server.background.h-1)

    def get_bb(self):
        return self.screenX-36, self.y-38, self.screenX+36,self.y+38

    def draw(self):
        self.cur_state.draw(self)
        #self.font.draw(self.x-60, self.y+50,
                       #'Time: %3.2f)'%get_time(),(255,255,0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)