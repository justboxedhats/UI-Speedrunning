import pygame
import math
import pygame.font

screen =pygame.display.set_mode((1,1))


def button (x,y,width, height):
    button_rect=pygame.rect.Rect(x,y,width,height)
    pygame.mouse.get_pos()
    if button_rect.colide_point() :
        return True
    else: 
        return False
    pygame.rect.draw(button_rect,(200,200,200))

def text (text,x,y,font):
    pygame.font.draw()

    pass

def image (x,y,directory, width=-1,height=-1):
    if width == -1:
        print("skip w scale")
    else:
        pygame.trandsform
    if height ==-1:
        print("skip H scale")
    else:
        pygame.transform()
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

    def text(in_text):
        print(in_text)

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
    def check_click (self):
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_just_pressed():
            return True
        else: 
            return False