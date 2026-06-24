from pygame import *
from pygame.locals import *

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
        self.fruta = [100 , 100]
        self.fskin = Surface((10,10))
        self.fskin.fill((250,0,0))
        self.fruta_spaw = True

class Placar():