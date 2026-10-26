import pygame
import levels
pygame.init()
#pygame.time.init()
#screen=pygame.display.set_mode((500,400))
running=True
# settings varable 
flags=[]
level="home"
# functions


# classes 


while running:
    #screen.fill(bg_color)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False

    if level == "home":
        result =levels.game_levels.home()
        # print(f" result:  {result}")
        if result == "quit":
            running=False
        if result == "play" :
            level=1 

    elif level == "level_menue":
        result=level.game_levels.level_menue()
        if result == "home": 
            level="home"


    elif level == 0:
        # calls the levels file 

        result=levels.game_levels.level_0()
        if result == "fin_lever":
            level="leve"

    elif level == 1 : 
        result=levels.game_levels.level_1()

        if result == "home":
            level="home"
        elif result == "level_menu":
            level=levels

    elif level == 2 : 
        levels.game_levels.level_2()

    else:
        print(f"Error, level: {level}  could not be found")
        level="home"
        


    pygame.display.flip()

    
