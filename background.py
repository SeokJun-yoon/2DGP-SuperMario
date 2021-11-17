from pico2d import *
X,Y=512*2,160*5
class Background:
    def __init__(self):
        self.image = load_image('res/Background.png')
        self.x = 512*2
        self.y = 160*5
        #self.width = 150
        #self.height = 150
        self.size = 15*10


    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        self.image.draw(self.x / 2, 475,self.x,650)
        X / 2, 475, X, 650