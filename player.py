import game_framework
from pico2d import *

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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP = range(6)

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
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.y += mario.velocityY * game_framework.frame_time

        mario.y = clamp(225, mario.y, 1000 - 25)


    def draw(mario):
        if mario.dir == 1:
            mario.Idle_image.clip_draw(int(mario.frame) * 210, mario.index * 290, 210, 290, mario.x, mario.y, 100, 140)
        else:
            mario.Idle_image.clip_draw(int(mario.frame) * 210, mario.index * 290, 210, 290, mario.x, mario.y, 100, 140)


class RunState:
    def enter(mario, event):
        if event==RIGHT_DOWN:
            mario.velocity +=RUN_SPEED_PPS
        elif event==LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event ==RIGHT_UP:
            mario.velocity -=RUN_SPEED_PPS
        elif event==LEFT_UP:
            mario.velocity +=RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)
        pass

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1024 - 25)

    def draw(mario):
        if mario.dir == 1:
            mario.Run_image.clip_draw(int(mario.frame)*223, mario.index*275, 223, 275, mario.x, mario.y, 100, 140)
        else:
            mario.Run_image.clip_draw(int(mario.frame)*223, mario.index*275, 223, 275, mario.x, mario.y, 100, 140)


# 점프 상태
class JumpState:
    def enter(mario, event):
        mario.velocityY = RUN_SPEED_PPS
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)
        pass

    def exit(mario, event):
        if event == SPACE_UP:
            mario.velocityY = -RUN_SPEED_PPS

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.x += mario.velocity * game_framework.frame_time
        mario.y += mario.velocityY * game_framework.frame_time
        mario.y = clamp(225, mario.y, 1000 - 25)
        if mario.y<=225:
            mario.add_event(IdleState)


    def draw(mario):
        if mario.dir == 1:
            mario.Run_image.clip_draw(int(mario.frame)*223, mario.index*275, 223, 275, mario.x, mario.y, 100, 140)
        else:
            mario.Run_image.clip_draw(int(mario.frame)*223, mario.index*275, 223, 275, mario.x, mario.y, 100, 140)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, SPACE_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE_DOWN: JumpState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, SPACE_UP: IdleState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, SPACE_DOWN: JumpState}
}

class Mario:
    def __init__(self): # 생성자
        self.x, self.y = 50, 225 # 초기 마리오 좌표
        #self.image = load_image('res/MarioIdle.png')
        self.Idle_image = load_image('no_using_res/MarioIdle.png')
        self.Run_image = load_image('no_using_res/MarioRun.png')
        self.frame = 0
        self.index = 0
        self.velocity = 0     # 속도
        self.dir = 1          # -1 left, +1 right
        self.velocityY = -10    # y 속도
        self.mass=70
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        #self.state="Idle"


    def add_event(self, event):
        self.event_que.insert(0,event)

    def Run(self):
        pass

    def Jump(self, j):
        pass

    def update(self):
        #print(self.cur_state)
        #print(self.velocity)
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)