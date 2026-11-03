import pygame
import math
pygame.init()
pygame.font.init()

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

    def render(self): 
        pygame.draw.rect(screen,self.color, self.rect)

class pannel_colison (pannel): 
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)

    def check_col (self):
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True 
        else:
            return False 
    def check_click (self):
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_just_pressed()[0]:
            return True
        else: 
            return False

class text :

    def __init__(self,in_text,x,y,color=(180,180,180),font="arial",size=30):
        self.in_text =in_text
        self.x=x
        self.y=y
        self.color=color
        self.font=font 
        self.size=size
        bc_font=pygame.font.SysFont("arial",size)
        text_surf=bc_font.render(in_text,True,(self.color))
        screen.blit(text_surf,(x,y))
"""
    def text(in_text,x,y):# this solution may change
    n_font=
    print(in_text)"""




class drop_down :
    drop_down= False
    item_list=["win", "lose"]


    def __init__(self,x,y,width,height,item_list,color):
        super.__init__(self)
        self.rect=pygame.revt.Rect(x,y,width,height)
        self.item_list=item_list

    def check_click (self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            drop_down= not drop_down
        if drop_down :
            for i in self.item_list :
                self.rect.y-=i*self.height()
                pygame.draw.rect(self.rect,color)
                text(f"{self.item_list[i]}",x,y)
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    return self.item_list[i]
                self.rect.y+=self.height()*i


    def check_colide (self):
        mouse_pos=pygame.mouse.get_pos()
        for i in self.item_list: 
            return 
        
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.getpressed()[0]:
            self.y=mouse_pos[1]





class switch :
    
    def __init__(self,x,y,width,height,color, long):
        super(pannel).__init__(x,y,width,height,color)

        self.rect=pygame.rect.Rect(x,y,width, height) 
        self.long=long
        self.mode=False
        

        def render_long (self): 
            self.render()
            color=(self.color[0]/2,self.color[1]/2,self.color[2]/2)
            long_rect=pygame.rect.Rect(self.x,self.y,self.width,self.height + long) 
            pygame.draw.rect(long_rect,color)

        def check_col (self):
            mouse_pos=pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True 
            else:
                return False
            
        def check_click (self):
            mouse_pos=pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_just_pressed()[0]:
                self.rect.y=pygame.mouse.getpos()[1]
            if self.rect.y > self.y-(self.height/2):
                self.mode=True
            elif self.rect.y <  self.long+ self.height:
                self.mode=False
            return self.mode

class dragable ():
    def __init__ (self,x,y,width,height):
        super(pannel).__init__(self,x,y,width,height)
        self.rect=pygame.rect.Rect(x,y,width,height)

    def check_drag (self):
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_just_pressed[0]:
            self.rect.x=mouse_pos[0]+(self.width/2)
            self.rect.y=mouse_pos[1]+(self.height/2)

class lose_squ : 
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)
        self.rect=pygame.rect.Rect(x,y,width,height)

    def check_mouse (self):
        global win,lose 
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) :
            return True


    def check_mouse_c (self):
        global win,lose 
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_just_pressed()[0]:
            win=False
            lose=True


    #def check_ob (self): # check obkejects  

        


# lever
# charecter 