from pygame import *
from pygame.locals import *
from cobra import *
from time import *
from random import *

init()

cobra = Cobra()
tela = display.set_mode((600,600))
display.set_caption("Snake")
rodando = True
while rodando: 
    for eventos in event.get():
        if eventos.type == QUIT:
            rodando = False
        elif eventos.type == KEYDOWN:
            if eventos.key == K_UP:
                cobra.change_to = "UP"
            if eventos.key == K_DOWN:
                cobra.change_to = "DOWN"
            if eventos.key == K_LEFT:
                cobra.change_to = "LEFT"
            if eventos.key == K_RIGHT:
                cobra.change_to = "RIGHT"

    for cobra_pos in cobra.cobra:
        tela.blit(cobra.skin, cobra_pos)  
    if cobra.direction == "UP":
        cobra.cobra_direction[1] -= 10
    if cobra.direction == "DOWN":
        cobra.cobra_direction[1] += 10
    if cobra.direction == "LEFT":
        cobra.cobra_direction[0] -= 10
    if cobra.direction == "RIGHT":
        cobra.cobra_direction[0] += 10
  
    display.update()

quit()
