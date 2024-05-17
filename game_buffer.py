import numpy as np
import pygame
import random
class game_buffer:

    #assets
    tetrominos={
        1:  [ 0, 0, 1, 0,
              0, 0, 1, 0,
              0, 0, 1, 0,
              0, 0, 1, 0,
            ],
        2:  [ 0, 0, 0, 0,
              0, 0, 1, 0,
              0, 1, 1, 0,
              0, 1, 0, 0,
            ],
        3:  [ 0, 0, 0, 0,
              0, 1, 0, 0,
              0, 1, 1, 0,
              0, 0, 1, 0,
            ],
        4:  [ 0, 0, 0, 0,
              0, 1, 1, 0,
              0, 1, 1, 0,
              0, 0, 0, 0,
            ],
        5:  [ 0, 0, 0, 0,
              0, 1, 1, 0,
              0, 0, 1, 0,
              0, 0, 1, 0,
            ],
        6:  [ 0, 0, 0, 0,
              0, 1, 1, 0,
              0, 1, 0, 0,
              0, 1, 0, 0,
            ],
        7:  [ 0, 0, 0, 0,
              0, 1, 0, 0,
              0, 1, 1, 0,
              0, 1, 0, 0,
            ],
            
    }

    buffer=np.zeros((20, 10), dtype=int)
    rot=0

    def set_new_tetromino(self):
        self.current=random.randint(1,7)
        self.x=3
        self.y=-3
    def get_index(self,i,j):
        if self.rot==0:
            indx=i*4+j
        elif self.rot==1:
            indx=i+12-4*j
        elif self.rot==2:
            indx=15-j-4*i
        else:
            indx=3+j*4-i
        return indx
    
    def clear_block_border(self,clear): #may be unsessary

        for i in range(4):
            if clear=="t":
                x=self.y
                y=self.x+i
                c=i
                r=0
            elif clear=="l":
                y=self.x
                x=self.y+i-1
                r=i
                c=0
            else:
                x=self.y+i-1
                y=self.x+3
                r=i
                c=3
            if (y>=0 and y<10 and x>=0 and x<20 and
                self.tetrominos[self.current][self.get_index(r,c)]==1):
                self.buffer[x][y]=0


    def collition(self):
        #TODO collition detection later
        return self.y+4<20


    def move_tetromino(self,keys):
        colide=self.collition()
        if not self.collition():
            self.set_new_tetromino()
 
        if colide:
            self.clear_block_border("t")    
            self.y+=1
            
            if keys[pygame.K_a]:
                self.clear_block_border("r")
                self.x-=1
            elif keys[pygame.K_d]:
                self.clear_block_border("l")
                self.x+=1
            elif keys[pygame.K_r]:
                self.rot=(self.rot+1)%4
                
    
    def draw_tetromino(self):

        for i in range(4):
            for j in range(4):
                indx=self.get_index(i,j)
                x=self.y+i
                y=self.x+j
                if y>=0 and y<10 and x>=0 and x<20:
                    self.buffer[x][y]=self.tetrominos[self.current][indx]

    






