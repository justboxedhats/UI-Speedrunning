import pygame
import levels
pygame.init()
#pygame.time.init()
screen=pygame.display.set_mode((500,400))
running=True
# settings varable 
flags=[]
level="home"
# functions 


# classes 


while running:
    screen.fill("teal")
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False
    if level == "home":
        levels.game_levels.home()

    if level == 0:
        # calls the levels file 
        levels.game_levels.level_0()
    if level == 2 :
        levels.game_levels.level_2()
        


    pygame.display.flip()

    

pygame.QUIT()