from pico2d import *
import server
import game_framework

SIZE = 4
NONCOLLIDABLE = ["bush1", "bush2", "bush3", "cloud1", "cloud2", "cloud3", "hill1", "hill2"]
COLLIDABLE = ["castle","pipe1","pipe2","pipe3","flag","hardblock","qmark","groundtile","initblock"]     # 충돌체크 해야 하는 오브젝트들


class Object:
    def __init__(self, fileName):
        self.image = load_image('res/' + fileName + '.png')
        # type == 0 unable collide, type == 1 can collide
        self.type = 0
        self.x = 0
        self.y = 0
        self.width = self.image.w * SIZE
        self.height = self.image.h * SIZE
        self.bb = [0,0,0,0,0,0,0,0]
        self.fileName = fileName
        self.checkType()


    def get_bb(self):
        return self.bb[0],self.bb[1],self.bb[2],self.bb[3]

    def get_secondbb(self):
        return self.bb[4],self.bb[5],self.bb[6],self.bb[7]

    def set_bb(self):
        if self.fileName == "castle":
            self.bb[0] = self.x - self.width * 0.125
            self.bb[1] = self.y - self.height*0.5
            self.bb[2] = self.x + self.width * 0.125
            self.bb[3] = self.y
        elif self.fileName == "pipe1":
            self.bb[0] = self.x - self.width * 0.5
            self.bb[1] = self.y + self.height *0.5 * 0.0625
            self.bb[2] = self.x + self.width * 0.5
            self.bb[3] = self.y + self.height * 0.5
            self.bb[4] = self.x - self.width * 0.5 * 0.875
            self.bb[5] = self.y - self.height * 0.5
            self.bb[6] = self.x + self.width * 0.5 * 0.875
            self.bb[7] = self.bb[1]
        elif self.fileName == "pipe2":
            self.bb[0] = self.x - self.width * 0.5
            self.bb[1] = self.y + self.height *0.5* 0.375
            self.bb[2] = self.x + self.width * 0.5
            self.bb[3] = self.y + self.height * 0.5
            self.bb[4] = self.x - self.width *0.5* 0.875
            self.bb[5] = self.y - self.height * 0.5
            self.bb[6] = self.x + self.width *0.5* 0.875
            self.bb[7] = self.bb[1]
        elif self.fileName == "pipe3":
            self.bb[0] = self.x - self.width * 0.5
            self.bb[1] = self.y + self.height *0.5* 0.53125
            self.bb[2] = self.x + self.width * 0.5
            self.bb[3] = self.y + self.height * 0.5
            self.bb[4] = self.x - self.width *0.5* 0.875
            self.bb[5] = self.y - self.height * 0.5
            self.bb[6] = self.x + self.width *0.5* 0.875
            self.bb[7] = self.bb[1]
        elif self.fileName in ["flag", "hardblock", "groundtile", "qmark", "initblock"]:
            self.bb[0] = self.x - self.width * 0.5
            self.bb[1] = self.y - self.height * 0.5
            self.bb[2] = self.x + self.width * 0.5
            self.bb[3] = self.y + self.height * 0.5


    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        self.image.clip_draw(0, 0, self.image.w, self.image.h, self.x, self.y, self.width, self.height)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_secondbb())

    def update(self):
        if(server.mario.screenLock == False):
            self.x -= server.mario.velocity*game_framework.frame_time
            self.set_bb()


    def checkType(self):
        if self.fileName in COLLIDABLE:
            self.type = 1
            if self.fileName in ["pipe1","pipe2","pipe3"]:
                self.type = 2



