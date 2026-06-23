from pygame import *
from pygame.locals import *

class Cobra():
    def __init__(self):
        self.cobra = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.skin = Surface((10,10))
        self.skin.fill((0, 250, 55))