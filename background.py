from pico2d import *
import server

# 배경 맵 사이즈 : 1000 x 800

class Background:
    def __init__(self):
        self.image = load_image('res/sky.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = self.image.w / 2   # x 좌표
        self.y = self.image.h / 2   # y 좌표

    def draw(self):
        # # # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
        # # self.image.draw(self.x,self.y,self.image.w,self.image.h)
        # self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)  # quadrant 3
        # self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)  # quadrant 2
        # self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)  # quadrant 4
        # self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)  # quadrant 1

        # 무한 스크롤링으로 시도
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, 0)
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q2w, 0)

        # 일반 스크롤링으로 시도
        #self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height,0 ,0)

        # #draw_rectangle(self.x-self.image.w/2+10,self.y-self.image.h/2+10,self.x+self.image.w/2-10,self.y+self.image.h/2-10)

    def update(self):
        # 일반 스크롤링으로 시도
        #self.window_left = clamp(0, int(server.mario.x)-server.background.canvas_width//2, server.background.w - server.background.canvas_width)
        #self.window_bottom = clamp(0, int(server.mario.y) - server.background.canvas_height//2, server.background.h - server.background.canvas_height)

        # 무한 스크롤링으로 시도
        self.q2l = (int(server.mario.x)-self.canvas_width//2) % self.w
        self.q2b = 0
        self.q2w = clamp(0, self.w - self.q2l, self.w)
        self.q2h = self.canvas_height

        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q2l
        self.q1h = self.canvas_height


        # # quadrant 3
        # self.q3l = (int(server.mario.x)-self.canvas_width//2) % self.w
        # self.q3b = (int(server.mario.y)-self.canvas_height//2) % self.h
        # self.q3w = clamp(0,self.w - self.q3l, self.w)
        # self.q3h = clamp(0, self.h - self.q3b, self.h)
        #
        # # quadrant 2
        # self.q2l = self.q3l
        # self.q2b = 0
        # self.q2w = self.q3w
        # self.q2h = self.canvas_height - self.q3h
        #
        # # quadrand 4
        # self.q4l = 0
        # self.q4b = self.q3b
        # self.q4w = self.canvas_width - self.q3w
        # self.q4h = self.q3h
        #
        # # quadrand 1
        # self.q1l = 0
        # self.q1b = 0
        # self.q1w = self.q4w
        # self.q1h = self.q2h

        #pass

    def handle_event(self, event):
        pass