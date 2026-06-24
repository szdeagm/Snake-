from pygame import *
from pygame.locals import *
from cobra import *
from pygame import time
from random import *

init()

cobra = Cobra()
fruta = Fruta()
tela = display.set_mode((600,600))
display.set_caption("Snake")
fps = time.Clock()
rodando = True

while rodando: 
    fps.tick(10)
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
        
    if cobra.change_to == 'UP' and cobra.direction != 'DOWN':
        cobra.direction = 'UP'
    if cobra.change_to == 'DOWN' and cobra.direction != 'UP':
        cobra.direction = 'DOWN'
    if cobra.change_to == 'LEFT' and cobra.direction != 'RIGHT':
        cobra.direction = 'LEFT'
    if cobra.change_to == 'RIGHT' and cobra.direction != 'LEFT':
        cobra.direction = 'RIGHT'

    for i in range(len(cobra.cobra) - 1):
        cobra.cobra[i] = cobra.cobra[i + 1]

    if cobra.direction == "UP":
        cobra.cobra[-1][1] -= 10
    if cobra.direction == "DOWN":
        cobra.cobra[-1][1] += 10
    if cobra.direction == "LEFT":
        cobra.cobra[-1][0] -= 10
    if cobra.direction == "RIGHT":
        cobra.cobra[-1][0] += 10

    tela.fill((0,0,0))
    for cobra_pos in cobra.cobra:
        tela.blit(cobra.skin, cobra_pos)
    
    display.update()

quit()
