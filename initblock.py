from pico2d import *
import game_framework

image = None


class Initblock:
    def __init__(self):
        self.image = load_image('res/initblock.png')
        self.x = 300
        self.y = 350
        self.width = 16*5
        self.height = 15*5
        self.size = 15 * 10

    def get_bb(self):
        return self.x - 40, self.y - 37, self.x + 40, self.y + 37

    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        self.image.draw(self.x, self.y, self.width, self.height)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass