from pico2d import *

class Mario:
    def __init__(self): # 생성자
        self.x = 50
        self.y = 200
        self.frame=0
        self.index=0
        self.speed=0
        self.dir=[1,0]          # -1 left, +1 right

        self.state="Idle"
        self.Idle_image = load_image('res/MarioIdle.png')
        self.Run_image = load_image('res/MarioRun.png')

    def Run(self):
        pass

    def Jump(self):
        pass

    def change_state(self):
        pass

    def draw(self):
        # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        if self.state == "Idle":
            self.Idle_image.clip_draw(self.frame * 210, self.index * 290, 210, 290,self.x,self.y,100,140)
        elif self.state == "Run":
            self.Run_image.clip_draw(self.frame*223,self.index*275,223,275,self.x,self.y,100,140)

    def handle_event(self, e):
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_RIGHT:
                    self.speed=1
                    self.dir[0]= 1
                    self.state = "Run"
                    self.index=0
                elif e.key == SDLK_LEFT:
                    self.speed=1
                    self.dir[0] = -1
                    self.state = "Run"
                    self.index=1
                elif e.key == SDLK_UP:
                    self.speed=1
                    self.dir[1] = 1
                    self.state="Idle"  # jump로 바꿔야함
            elif e.type == SDL_KEYUP:
                if e.key == SDLK_RIGHT:
                    self.speed=0
                    self.state = "Idle"
                elif e.key == SDLK_LEFT:
                    self.speed=0
                    self.state = "Idle"
                elif e.key == SDLK_UP:
                    self.speed=0
                    self.dir[1]=0
                    self.state = "Idle"  # jump로 바꿔야 함

    def update(self):
        self.frame= (self.frame+1) % 3   # 프레임
        # self.handle_event()
        self.x+=self.dir[0]*self.speed*20
        self.y+=self.dir[1]*self.speed*20