import pygame
import math
import pygame.font

screen =pygame.display.set_mode((1,1))


def button (x,y,width):
    pass

def text ():
    pass


def line (_x,_y,x,y):
    point_1=(_x,_y)
    point_2=(x,y)
    

    

class pannel :  
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect=pygame.rect.Rect(x,y,width,height)

    def re_pos(self,n_x,n_y):
        self.x=n_x
        self.y=n_y

    def  re_scale(self,n_width,n_height):
        self.width=n_width
        self.hieght=n_height

    def re_color(self,n_color): 
        self.color=n_color

    def render(self): 
        pygame.draw.rect(screen,self.color, self.rect)

class pannel_colison (pannel): 
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)
        self.rect=pygame.rect.Rect(x,y,width,height)

    def check_col (self):
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False 