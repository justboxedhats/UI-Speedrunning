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

    elif level == "level_menu":
        result=levels.game_levels.level_menu()
        if result == "home": 
            level="home"
        if result == "level_1":
            level=1


    elif level == 0:
        # calls the levels file 

        result=levels.game_levels.level_0()
        if result == "fin_lever":
            level="leve"

    elif level == 1 :
        print(f"result: {result}")

        if result == "home":
            level="home"
        elif result == "level_menu":
            level="level_menu" 
        elif result == "next_level":
            level = 2
            result=None
        elif result == "lose":
            result=levels.game_levels.level_lose()
        elif result == "win":
            result=levels.game_levels.level_win()
        else :
            result=levels.game_levels.level_1()

         
    elif level == 2 : 

        if result == "home":
            level="home"
        elif result == "level_menu":
            level="level_menu" 
        elif result == "next_level":
            level = 3
            result=None
        elif result == "lose":
            result=levels.game_levels.level_lose()
        elif result == "win":
            result=levels.game_levels.level_win()
        else :
            result=levels.game_levels.level_2()


    elif level == 3 : 

        if result == "home":
            level="home"
        elif result == "level_menu":
            level="level_menu" 
        elif result == "next_level":
            level = 4
            result=None
        elif result == "lose":
            result=levels.game_levels.level_lose()
        elif result == "win":
            result=levels.game_levels.level_win()
        else :
            result=levels.game_levels.level_3()

    elif level == 4 : 

        if result == "home":
            level="home"
        elif result == "level_menu":
            level="level_menu" 
        elif result == "next_level":
            level = 5
            result=None
        elif result == "lose":
            result=levels.game_levels.level_lose()
        elif result == "win":
            result=levels.game_levels.level_win()
        else :
            result=levels.game_levels.level_4()
            
    elif level == 5 : 

        if result == "home":
            level="home"
        elif result == "level_menu":
            level="level_menu" 
        elif result == "next_level":
            level = 6
            result=None
        elif result == "lose":
            result=levels.game_levels.level_lose()
        elif result == "win":
            result=levels.game_levels.level_win()
        else :
            result=levels.game_levels.level_5()


    else:
        print(f"Error, level: {level}  could not be found")
        level="home"
        
        
    #print(f"level: {level} , resuult: {result}")
    pygame.display.flip()
        



    

    
