from pygame import *
from pygame.locals import *
from cobra import *

init()

cobra = Cobra()
tela = display.set_mode((600,600))
display.set_caption("Snake")
rodando = True
while rodando: 
    for eventos in event.get():
        if eventos.type == QUIT:
            rodando = False

    for cobra_pos in cobra.cobra:
        tela.blit(cobra.skin, cobra_pos)    
    display.flip()

quit()
