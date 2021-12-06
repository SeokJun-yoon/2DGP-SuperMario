from pico2d import *

TEXTSIZE = 30
import json
with open('text_data.json', 'r') as f:
    text = json.load(f)

class Text:
    def __init__(self, x,y, string): # 생성자
        self.x, self.y = x, y # 초기 마리오 좌표
        self.image = load_image('res/text.png')
        self.text = string

    def update(self):
        pass

    def draw(self):
        for i,t in enumerate(self.text):
            self.image.clip_draw(text[str(t)]["LEFT"],text[str(t)]["BOTTOM"],text[str(t)]["WIDTH"],text[str(t)]["HEIGHT"],self.x + i * TEXTSIZE,self.y,TEXTSIZE,TEXTSIZE)


    def setString(self, string):
        self.text = string