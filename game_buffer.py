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
    def get_index(self,i,j,rot):
        if rot==0:
            indx=i*4+j
        elif rot==1:
            indx=i+12-4*j
        elif rot==2:
            indx=15-j-4*i
        else:
            indx=3+j*4-i
        return indx


    def collition(self,x1,y1,rott):
        s=4
        for i in range(4):
            for j in range(4):
                indx=self.get_index(i,j,rott)
                x=y1+i
                y=x1+j
                test=self.tetrominos[self.current][indx]==1
                if test and i==3:
                    s=5
                if (y>=0 and y<10 and x>=0 and x<20 and 
                    (self.buffer[x][y]==1 and test)):
                    return True 

        
        if self.y+s>20:
            return True
        
        return False
    


    def clear_block(self):
        for i in range(4):
            for j in range(4):
                indx=self.get_index(i,j,self.rot)
                x=self.y+i
                y=self.x+j
                if (y>=0 and y<10 and x>=0 and x<20 and 
                    (self.buffer[x][y]==1 and self.tetrominos[self.current][indx]==1)):
                    self.buffer[x][y]=0



    def move_tetromino(self,keys):
        self.clear_block()
        
        if keys[pygame.K_a] and not self.collition(self.x-1,self.y+1,self.rot):
            self.x-=1
            self.y+=1
        elif keys[pygame.K_d] and not self.collition(self.x+1,self.y+1,self.rot):
            self.y+=1
            self.x+=1
        elif keys[pygame.K_r] and not self.collition(self.x,self.y,(self.rot+1)%4):
            self.y+=1
            self.rot=(self.rot+1)%4
        elif not self.collition(self.x,self.y+1,self.rot):
            self.y+=1
        else:

            self.draw_tetromino()
            self.set_new_tetromino()
            return 
            
        self.draw_tetromino()


    
    def draw_tetromino(self):

        for i in range(4):
            for j in range(4):
                indx=self.get_index(i,j,self.rot)
                x=self.y+i
                y=self.x+j
                if (y>=0 and y<10 and x>=0 and x<20 and self.tetrominos[self.current][indx]==1):

                    self.buffer[x][y]=1

    






