from pico2d import *

# 배경 맵 사이즈 : 1000 x 800

class Background:
    def __init__(self):
        self.image = load_image('res/sky.png')
        self.x = self.image.w / 2   # x 좌표
        self.y = self.image.h / 2   # y 좌표

    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        self.image.draw(self.x,self.y,self.image.w,self.image.h)

    def update(self):
        pass