import game_framework
from pico2d import *

import json
import server

with open('characters.json', 'r') as f:
    characters = json.load(f)

# Monster Run Speed
PIXEL_PER_METER = (10.0 / 0.01) # 10 pixel 1 cm
RUN_SPEED_KMPH = 2.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Monster Action Speed
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

SIZE = 1

class Monster1:
    def __init__(self): # 생성자
        self.image = load_image('res/characters.gif')
        self.x = 0
        self.y = 0
        self.characterName = "MONSTER1"
        self.frame = 0

        self.velocity = RUN_SPEED_PPS     # 속도
        self.dir = -1
        self.width = 45
        self.height = 45
        self.bb = [0, 0, 0, 0]

    def update(self):
        if (server.mario.screenLock == False):
            self.x -= server.mario.velocity * game_framework.frame_time

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % characters[self.characterName]["MOVE"]["FRAMESIZE"]
        self.x += (self.velocity * game_framework.frame_time)*self.dir
        self.set_bb()

        #self.x = clamp(0, self.x, 500)
    def get_bb(self):
        return self.bb[0], self.bb[1], self.bb[2], self.bb[3]

    def set_bb(self):
        self.bb[0] = self.x - self.width * 0.5
        self.bb[1] = self.y - self.height * 0.5
        self.bb[2] = self.x + self.width * 0.5
        self.bb[3] = self.y + self.height * 0.5


    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        #self.image.clip_draw(0, 0, self.image.w, self.image.h, self.x, self.y, self.width, self.height)
        self.image.clip_draw(
            characters[self.characterName]["MOVE"]["FRAMES"][str(int(self.frame))]["LEFT"],
            characters[self.characterName]["MOVE"]["FRAMES"][str(int(self.frame))]["BOTTOM"],
            characters[self.characterName]["MOVE"]["FRAMES"][str(int(self.frame))]["WIDTH"],
            characters[self.characterName]["MOVE"]["FRAMES"][str(int(self.frame))]["HEIGHT"],
            self.x, self.y,
            characters[self.characterName]["MOVE"]["FRAMES"][str(int(self.frame))]["WIDTH"] * 3,
            characters[self.characterName]["MOVE"]["FRAMES"][str(int(self.frame))]["HEIGHT"] * 3)
        draw_rectangle(*self.get_bb())
