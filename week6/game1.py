import pygame
import MyVector as mv  # 지난 번에 구현했던 vector 클래스

# 컬러 설정할때 편하라고 정의해 놓은 딕셔너리
rgb = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'BLUE': (0, 0, 255),
    'GREEN': (0, 255, 0),
    'RED': (255, 0, 0),
    'YELLOW': (255, 255, 0)
}


# Implementor
class Actor:
    # constructor
    def __init__(self, x, y):
        self.pos = mv.MyVector(x, y)
        self.name = ""
        self.skill = ""

    # position setter
    def setPos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    # move position
    def move(self, delta):
        self.pos = self.pos + delta

    # name setter
    def setName(self, name):
        self.name = name

    # ADDED: name getter
    def getName(self):
        return self.name

    # skill setter
    def setSkill(self, skill):
        pass

    # ADDED: skill getter
    def getSkill(self):
        pass


# Concrete Implementor 1
class Hero(Actor):
    # override skill setter
    def setSkill(self, skill):
        self.skill = skill

    # ADDED: skill getter
    def getSkill(self):
        return self.skill


# Concrete Implementor 2
class Enemy(Actor):
    # override skill setter
    def setSkill(self, skill):
        self.skill = skill

    # ADDED: skill getter
    def getSkill(self):
        return self.skill


# ADDED: NPC Concrete Implementor
class NPC(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.quest = ""

    def setQuest(self, quest):
        self.quest = quest

    # redirect to setQuest
    def setSkill(self, skill):
        self.setQuest(skill)

    # redirect skill to quest
    def getSkill(self):
        return self.quest


# Abstraction
class GameFramework:
    # constructor
    def __init__(self):
        self.pygame = pygame
        self.screen = 0

        self.nY = 0  # 화면 차원
        self.nX = 0

        self.hero = 0  # 지금은 주인공이 1명있다고 가정

        print("init")

    def setDisplay(self, nX, nY):  # 게임화면의 크기를 결정
        self.nY = nY
        self.nX = nX
        self.screen = self.pygame.display.set_mode([self.nX, self.nY])
        self.pygame.display.set_caption("Prince")  # 게임창의 이름

    # Bridge Pattern에서 Implementor를 속성으로 가질 수 있도록 하는 부분
    # Abstraction과 Implementor가 연결되는 부분
    def setHero(self, hero: Actor):
        self.hero = hero

    # ready event handler
    def ready(self):
        self.pygame.init()  # pygame 초기화

    def drawPolygon(self, color, points, thickness):
        self.pygame.draw.polygon(self.screen, color, points, thickness)

    def drawEdges(self):
        p1 = mv.MyVector(0, 0)
        p2 = mv.MyVector(0, 10)
        p3 = mv.MyVector(10, 0)

        self.drawPolygon(rgb["WHITE"], [p1.vec(), p2.vec(), p3.vec()], 1)

    def printText(self, msg, color, pos):
        font = self.pygame.font.SysFont("consolas", 20)
        textSurface = font.render(msg, True, color, None)  # self.pygame.Color(color)
        textRect = textSurface.get_rect()
        textRect.topleft = pos
        self.screen.blit(textSurface, textRect)

    # 게임 실행
    def launch(self):
        pass


class WhiteGame(GameFramework):
    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done:
            clock.tick(30)  # set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:  # 키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT:  # 어떤키가 눌렸는가?
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False

            if keyFlag == True:
                self.hero.move(delta)  # 주인공의 위치가 업데이트가 됨

                print("pressed", self.hero.pos.getState())  # in console
                self.screen.fill(rgb["WHITE"])  # 특성을 살린 부분

                # ADDED: fix raw property to getter
                self.printText(self.hero.getName(), rgb["RED"], self.hero.pos.vec())
                self.printText(self.hero.getSkill(), rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()


class BlackGame(GameFramework):
    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done:
            clock.tick(30)  # set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False

            if keyFlag == True:
                self.hero.move(delta)

                print("pressed", self.hero.pos.getState())  # in console
                self.screen.fill(rgb["BLACK"])  # 특성화된 부분

                # ADDED: fix raw property to getter
                self.printText(self.hero.getName(), rgb["RED"], self.hero.pos.vec())
                self.printText(self.hero.getSkill(), rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()


# ADDED: Yellow Refined Abstraction class
class YellowGame(GameFramework):
    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done:
            clock.tick(30)  # set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False

            if keyFlag == True:
                self.hero.move(delta)

                print("pressed", self.hero.pos.getState())  # in console
                self.screen.fill(rgb["YELLOW"])  # 특성화된 부분

                # ADDED: fix raw property to getter
                self.printText(self.hero.getName(), rgb["RED"], self.hero.pos.vec())
                self.printText(self.hero.getSkill(), rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()


# ADDED: Util Class for Generate Actor
class ActorInitializer:
    def __init__(self, loc=(0, 0), name="", skill=""):
        self.loc = loc
        self.name = name
        self.skill = skill

    def initHero(self):
        actor = Hero(self.loc[0], self.loc[1])
        actor.setName(self.name)
        actor.setSkill(self.skill)
        return actor

    def initEnemy(self):
        actor = Enemy(self.loc[0], self.loc[1])
        actor.setName(self.name)
        actor.setSkill(self.skill)
        return actor

    def initNPC(self):
        actor = NPC(self.loc[0], self.loc[1])
        actor.setName(self.name)
        actor.setQuest(self.skill)
        return actor


# ADDED: Singleton base class
class SingletonInstance:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__instance


# ADDED: Facade Pattern class for launch game
class GameLauncher(SingletonInstance):  # w/ Singleton Pattern
    def __init__(self):
        self.actor = ActorInitializer((0, 0), "JUNHYUK CHOI", "202004520").initHero()
        self.game = YellowGame()

    def launch(self):
        # init YellowGame
        game = YellowGame()
        game.ready()
        game.setDisplay(1280, 720)
        game.setHero(self.actor)
        game.launch()


# launch game with Singleton Facade class
GameLauncher.instance().launch()
