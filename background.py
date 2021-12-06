from pico2d import *
X,Y=512*2,160*5
BACKGROUND_WIDTH = 3376 / 240 * 800
BACKGROUND_HEIGHT = 240 / 240 * 800

class Background:
    def __init__(self):
        self.image = load_image('res/backgroundmap.png')
        self.x = BACKGROUND_WIDTH / 2
        self.y = BACKGROUND_HEIGHT / 2


    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        #self.image.draw(self.x / 2, 475,self.x,650)
        self.image.draw(self.x,self.y,BACKGROUND_WIDTH,BACKGROUND_HEIGHT)

    def update(self):
        pass