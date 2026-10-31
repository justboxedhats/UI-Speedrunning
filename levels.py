import UI_system
import time
import pygame

screen=pygame.display.set_mode((500,400))

win=False
lose=False
bg_color="white"
ply_levels=[]
st_level_time=time.gmtime()
ed_level_time=0


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

    def level_menu ():
        screen.fill(bg_color)
        menue_text=UI_system.text("level_menu",per2pix(30),per2pix(3,"s_h"),(200,130,210))
        lev_1=UI_system.pannel_colison(per2pix(8),per2pix( 20,"s_h"),per2pix(4),per2pix(4,"s_h"),(34,134,90))
        lev_1.render()
        text_1=UI_system.text("1",per2pix(8),per2pix(20,"s_h"),(23,34,23))
        if lev_1.check_click():
            return"level_1"
        
    def settings ():
        # music volume, mute, show timer
        settings_text=UI_system.text("v_0.1A",300,250,(100,100,100))
        settings_bg=UI_system.pannel(per2pix(35),) 


    def level_0 () :
        pannal=UI_system.pannel(20,30,50,40,(100,100,100))
        pannal.render()

    def level_1(): 
        global st_level_time ,ed_level_time
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
            timer_text=UI_system.text(f" time: {time.gmtime().tm_sec-st_level_time.tm_sec}",per2pix(80),per2pix(10,"s_h"),(200,41,184))
            goal_text=UI_system.text("press the win button to win", per2pix(20),per2pix(8,"s_h"),(100,100,100))
            if finish_button.check_click():
                ed_level_time=time.gmtime()
                win=True



        elif win and lose == False:
            main_button = UI_system.pannel_colison(per2pix(35),per2pix(25,"s_h"),per2pix(30),per2pix(10,"s_h"),(180,220,220))
            levels_button= UI_system.pannel_colison(per2pix(35),per2pix(45,"s_h"),per2pix(30),per2pix(10,"s_h"),(180,220,220))
            next_button= UI_system.pannel_colison(per2pix(35),per2pix(65,"s_h"),per2pix(30),per2pix(10,"s_h"),(180,220,220))
            retry_button= UI_system.pannel_colison(per2pix(35),per2pix(85,"s_h"),per2pix(30),per2pix(10,"s_h"),(180,220,220))

            main_button.render()
            levels_button.render()
            #next_button.render()
            retry_button.render()

            main_text= UI_system.text("back to main menu",per2pix(35),per2pix(25,"s_h"),(204,100,140))
            levels_text= UI_system.text("levels",per2pix(35),per2pix(45,"s_h"),(204,100,140))
            #next_text= UI_system.text("next",per2pix(35),per2pix(65,"s_h"),(204,100,140))
            retry_text = UI_system.text("retry",per2pix(35),per2pix(85,"s_h"),(204,100,140)) 
            win_text = UI_system.text("FINISH! ",per2pix(35),per2pix(3,"s_h"),(204,100,140)) 
            fin_time_text= UI_system.text(f" time: {ed_level_time.tm_sec-st_level_time.tm_sec} ",per2pix(35),per2pix(7,"s_h"),(204,100,140))

            if retry_button.check_click():
                #resets the timer and level flags 
                win=False
                st_level_time=time.gmtime()
                ed_level_time=time.gmtime()
            if main_button.check_click():
                win=False
                st_level_time=time.gmtime()
                ed_level_time=time.gmtime()
                return  "home"
            if levels_button.check_click():
                win=False
                st_level_time=time.gmtime()
                ed_level_time=time.gmtime()
                return "level_menu"
            #if next_button.check_click():

            
            
            #load winning screen
        elif win == False and lose == True:
            win=False
            lose=False
            return "lose"
            # loads failior screen 
    
    def level_2 ():
        screen.fill(bg_color)
        pos_list=[(per2pix(50),per2pix(50,"s_h")),(per2pix(20),per2pix(10,"s_h"))]
        pos_tracker=0

        if win == False and lose ==False:

            win_button=UI_system.pannel_colison()

           
            intruct_text=UI_system.text 
            level_text=UI_system.text
            time_text=UI_system.text

            if win_button.check_click() and win_button.x != pos_list[-1] and win_button.y != pos_list[-1]:
                print
        elif win and lose == False :
            print("won")

             

        pannal=UI_system.pannel(200,30,120,40,(200,140,210))
        pannal.render()

    def level_3 ():
        screen.fill(bg_color)
        

        if win != True and lose != True:
            # loads the playable 
            
            pass
        elif win and lose != True :
            pass 
        elif win != True and lose:
            pass 

