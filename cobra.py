from pygame import *
from pygame.locals import *
from pygame import font
import random 

class Cobra():
    def __init__(self):
        self.cobra = [[200, 200], [210, 200], [220, 200], [230, 200], [240, 200]]
        self.skin = Surface((10,10))
        self.skin.fill((0, 250, 55))
        self.direction = "Right"
        self.change_to = self.direction
        self.cobra_direction = [240, 200]

class Fruta():
    def __init__(self):
        x = random.randint(4,54)*10
        y = random.randint(4,54)*10
        self.fruta = [x, y] 
        self.fskin = Surface((10,10))
        self.fskin.fill((250,0,0))
        self.fruta_spaw = True

    def reposicionar(self):
        x = random.randint(4,54)*10
        y = random.randint(4,54)*10
        self.fruta = [x, y] 