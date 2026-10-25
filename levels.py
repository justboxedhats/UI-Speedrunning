import UI_system
import time
import pygame

screen=pygame.display.set_mode((500,400))

win=False
lose=False
bg_color="white"
ply_levels=[]
st_level_time=time.gmtime()


def per2pix(per , whole="s_h"):
    if whole =="s_h":
        pix= int((per/100)*screen.height)
        return pix 
    elif whole == "s_w":
        pix= int((per/100)*screen.width)
        return pix
    else:
        pix= int((per/100)*whole)
        return pix 
    

class game_levels:

    def home ():
        screen.fill(bg_color)
        tital_bg=UI_system.pannel(per2pix(30),per2pix(5,"s_h"),per2pix(40),per2pix(15,"s_h"),(200,100,100))
        tital_bg.render()
        tital_text=UI_system.text("UI Speedrunning!",per2pix(30),per2pix(5,"s_h"),(200,200,200))

        if ply_levels != []:# checks if the player played levels before 
            continue_button=UI_system.pannel_colison(per2pix(30),per2pix(25,"s_h"),per2pix(40),per2pix(5),(200,123,250))
            continue_text=UI_system.text("continue",per2pix(30),per2pix(25,"s_h"),(100,100,100))
            continue_button.render()

        play_button=UI_system.pannel_colison(per2pix(30),per2pix(40,"s_h"),per2pix(40),per2pix(5),(200,123,250))
        play_button.render()
        play_text=UI_system.text("PLAY",per2pix(30),per2pix(40,"s_h"),(100,100,100))

        quit_button=UI_system.pannel_colison(per2pix(30),per2pix(55,"s_h"),per2pix(40),per2pix(5),(200,123,250))
        quit_button.render()
        quit_text=UI_system.text("QUIT",per2pix(30),per2pix(55,"s_h"),(100,100,100))
        if play_button.check_click():
            return "play"
        if quit_button.check_click():
            return "quit"

        # tital_img=Ui_system.pannel.image()
        ver_text=UI_system.text("v_0.1A",per2pix(0),per2pix(2,"s_h"),(100,100,100))

         


    def settings ():
        # music volume, mute, show timer
        settings_text=UI_system.text("v_0.1A",300,250,(100,100,100))
        settings_bg=UI_system.pannel(per2pix(35),)
        pass 

    def level_0 () :
        pannal=UI_system.pannel(20,30,50,40,(100,100,100))
        pannal.render()

    def level_1(): 
        #bg_color=("limegreen")
        screen.fill(bg_color)
        global win, lose
        if win != True and lose == False:
            goal_bg=UI_system.pannel(per2pix(20),per2pix(8,"s_h"),per2pix(30),per2pix( 10,"s_h"),(235,90,150))
            goal_bg.render()
            finish_button=UI_system.pannel_colison(per2pix(45),per2pix(40,"s_h"),per2pix(10),per2pix(10,"s_h"),(200,255,200))
            finish_button.render()
            finish_text=UI_system.text("win button",per2pix(45),per2pix(40,"s_h"),(200,213,212))
            level_text=UI_system.text("Level 1", per2pix(5),per2pix(8,"s_h"),(100,100,100))
            timer_text=UI_system.text(f" time",per2pix(80),per2pix(10,"s_h"),(200,41,184))
            goal_text=UI_system.text("pressed the win button as soon as possable", per2pix(20),per2pix(8,"s_h"),(100,100,100))
            if finish_button.check_click():
                win=True



        elif win == True and lose != False:
            win=False
            lose=False
            return True
            
            #load winning screen
        elif win == False and lose == True:
            win=False
            lose=False
            return True
            pass
            # loads failior screen 
    
    def level_2 ():
        pannal=UI_system.pannel(200,30,120,40,(200,140,210))
        pannal.render()
