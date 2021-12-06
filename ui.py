from text import *

t = None

with open('characters.json', 'r') as f:
    characters = json.load(f)


class UI:
    def __init__(self):
        self.characterImage = load_image('res/characters.gif')

        self.score = 0
        self.coin = 0
        self.firstWorld = 1
        self.secondWorld = 1
        self.time = 0
        self.life = 0

        self.scoreText = [Text(100,750,"score"),Text(100,700,str('{0:06d}'.format(self.score)))]
        self.coinsText = Text(350,700,"O*"+str('{0:02d}'.format(self.coin)))
        self.worldText = [Text(570,750,"world"),Text(595,700,str(self.firstWorld)+"-"+str(self.secondWorld))]
        self.timeText = [Text(800,750,"time"),Text(820,700,'{0:03d}'.format(self.time))]
        self.midWorldText = Text(370,450,"world"+str(self.firstWorld)+"-"+str(self.secondWorld))
        self.lifeText = Text(530,350,'{0:02d}'.format(self.life))
        self.xText = Text(480,350,"*")

        self.currentState = None


    def update(self):
        pass

    def draw(self):
        for i in self.scoreText:
            i.draw()
        self.coinsText.draw()
        for i in self.worldText:
            i.draw()
        for i, l in enumerate(self.timeText):
            if i == 0:
                l.draw()
            else:
                if self.time != 0:
                    l.draw()

        if(self.currentState == "StartState"):
            self.midWorldText.draw()
            self.lifeText.draw()
            self.xText.draw()
            self.characterImage.clip_draw(
                characters["SMALLMARIO"]["RIGHT_IDLE"]["FRAMES"]["0"]["LEFT"],
                characters["SMALLMARIO"]["RIGHT_IDLE"]["FRAMES"]["0"]["BOTTOM"],
                characters["SMALLMARIO"]["RIGHT_IDLE"]["FRAMES"]["0"]["WIDTH"],
                characters["SMALLMARIO"]["RIGHT_IDLE"]["FRAMES"]["0"]["HEIGHT"],
                410, 370,
                characters["SMALLMARIO"]["RIGHT_IDLE"]["FRAMES"]["0"]["WIDTH"] * 4,
                characters["SMALLMARIO"]["RIGHT_IDLE"]["FRAMES"]["0"]["HEIGHT"] * 4)

    def setSocre(self,score):
        self.score = score
        self.scoreText = [Text(100,750,"score"),Text(100,700,str('{0:06d}'.format(self.score)))]


    def setTime(self,time):
        self.time = time
        self.timeText = [Text(800,750,"time"),Text(820,700,'{0:03d}'.format(self.time))]


    def setLife(self,life):
        self.life = life
        self.lifeText = Text(530,350,'{0:02d}'.format(self.life))


    def setCoin(self,coin):
        self.coin = coin
        self.coinsText = Text(350,700,"O*"+str('{0:02d}'.format(self.coin)))


    def setWorld(self, first, second):
        self.firstWorld = first
        self.secondWorld = second
        self.worldText = [Text(570,750,"world"),Text(595,700,str(self.firstWorld)+"-"+str(self.secondWorld))]
        self.midWorldText = Text(370,450,"world"+str(self.firstWorld)+"-"+str(self.secondWorld))



    def setCurrentState(self,state):
        self.currentState = state