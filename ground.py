from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('res/ground.png')
        #self.x = 75
        #self.y = 75
        #self.width = 150
        #self.height = 150
        self.size = 15*10


    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        for i in range(8):
            self.image.draw(self.size/2+i*self.size, self.size/2,self.size,self.size)
