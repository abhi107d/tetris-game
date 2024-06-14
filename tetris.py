import time
import pygame
from sys import exit
from game_buffer import game_buffer # type: ignore
W=650
H=760
framerate=30
marginx=150
marginy=30
pix_sz=35

pygame.init()
screen=pygame.display.set_mode((W,H))
clock=pygame.time.Clock()
pygame.display.set_caption("Tetris")

game_buff=game_buffer()
game_buff.set_new_tetromino() #test


def draw_columns():
    for j in range(marginx,(W-marginx+1),pix_sz):
        pygame.draw.line(screen,'white',start_pos=(j,marginy),end_pos=(j,H-marginy))
    for i in range(marginy,(H-marginy+1),pix_sz):
        pygame.draw.line(screen,'white',start_pos=(marginx,i),end_pos=(W-marginx,i))
        
        
        
    
def draw():

    for i in range(20):
        for j in range(10):
            if game_buff.buffer[i][j]!=0:
                x=marginx+j*pix_sz
                y=marginy+i*pix_sz
                rect=pygame.Rect(x,y,pix_sz,pix_sz)
                pygame.draw.rect(screen,"blue",rect=rect)    
def game():
    while(True):
        clock.tick(framerate)
        pygame.display.update()
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                exit()
            

        keys = pygame.key.get_pressed()
        game_buff.move_tetromino(keys)

        draw()
        draw_columns()


        
            
game()


      
    