from pygame import *

init()
def tela():
    display.set_mode((800,800))
    display.set_caption("Snake")
    rodando = True
    while rodando: 
        for eventos in event.get():
            if eventos.type == QUIT:
                rodando = False
        
        display.flip()
    

tela()
quit()
