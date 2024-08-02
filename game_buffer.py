import numpy as np
import pygame
import random
class game_buffer:
    maxwidth=10
    maxheight=20
    LEVEL=10 #(-ve level)

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
    drawrot=0
    onetap=True

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
        bottom_clear=0
        left_clear=3
        right_clear=0
        for i in range(4):
            for j in range(4):
                indx=self.get_index(i,j,rott)
                y=y1+i
                x=x1+j
                block_val=self.tetrominos[self.current][indx]==1
                #checking for last row/colum of tetramino with
                # visible block
                if block_val:
                    bottom_clear=max(bottom_clear,i)
                    right_clear=max(right_clear,j)
                    left_clear=min(left_clear,j)
                
                if (x>=0 and x<self.maxwidth 
                    and y>=0 and y<self.maxheight 
                    and (self.buffer[y][x]==1 and block_val)):
                    return [True,True,True] 
                
        if (y1+bottom_clear>=self.maxheight):
            return [True,True,True]
      
        return [False,x1+left_clear<0,x1+right_clear>=self.maxwidth]

    


    def clear_block(self):
        for i in range(4):
            for j in range(4):
                indx=self.get_index(i,j,self.rot)
                y=self.y+i
                x=self.x+j
                if (x>=0 and x<self.maxwidth 
                    and y>=0 and y<self.maxheight 
                    and (self.buffer[y][x]==1 and self.tetrominos[self.current][indx]==1)):
                    self.buffer[y][x]=0


    frame=0
    def move_tetromino(self,keys):
        self.frame+=1
        down=False
        self.clear_block()
        if(keys[pygame.K_s]):
            down=True
        elif (keys[pygame.K_a] 
            and not self.collition(self.x-1,self.y+1,self.rot)[1]):
            self.x-=1
        elif (keys[pygame.K_d] 
              and not self.collition(self.x+1,self.y+1,self.rot)[2]):
            self.x+=1
        elif keys[pygame.K_r] and not any(self.collition(self.x,self.y+1,(self.rot+1)%4)) and self.onetap:
            self.rot=(self.rot+1)%4
            self.onetap=False
        
        if not keys[pygame.K_r]:
            self.onetap=True
                


        if not self.collition(self.x,self.y+1,self.rot)[0]:
            if self.frame%self.LEVEL==0 or down:
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
                y=self.y+i
                x=self.x+j
                if (x>=0 and x<self.maxwidth 
                    and y>=0 and y<self.maxheight 
                    and self.tetrominos[self.current][indx]==1):

                    self.buffer[y][x]=1

    






