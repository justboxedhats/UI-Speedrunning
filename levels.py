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
anti_time=0
pos_tracker=0
total_levels=6
pause=False
list_vaule=""# for dropdown list
list_vaule= ""

# input loop 

for input in pygame.event.get():
    if input == "K_ESCAPE":
        pause=True
    if input == "K_up":
        pass
    if input == "K_down":
        pass
    if input == "k_left":
        pass
    if input == "K_right":
        pass 
    if input == "K_SPACE":
        pass

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
        tital_bg=UI_system.pannel(per2pix(30),per2pix(5,"s_h"),per2pix(50),per2pix(11,"s_h"),(200,100,100))
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
        ver_text=UI_system.text("ver 0.2 A",per2pix(0),per2pix(2,"s_h"),(100,100,100))

    def level_menu ():
        global st_level_time ,ed_level_time
        screen.fill(bg_color)
        menue_text=UI_system.text("level_menu",per2pix(35),per2pix(3,"s_h"),(200,130,210))
        menu_square=pygame.rect.Rect(per2pix(8),per2pix( 20,"s_h"),per2pix(4),per2pix(4,"s_h"))
        for i in range(total_levels):
            menu_square.x=(per2pix(8)+(i*30))
            pygame.draw.rect(screen,(34,134,90),menu_square)
            if menu_square.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                print(f"level_{i+1}")
                st_level_time=time.gmtime()
                ed_level_time=time.gmtime()
                return i+1
            text_1=UI_system.text(f"{i+1}",per2pix(8)+(i*30),per2pix(20,"s_h"),(0,0,0),None,24)  



    def level_win ():
        global st_level_time ,ed_level_time
        bg_color=("AliceBlue")
        main_button = UI_system.pannel_colison(per2pix(35),per2pix(25,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))
        levels_button= UI_system.pannel_colison(per2pix(35),per2pix(45,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))
        next_button= UI_system.pannel_colison(per2pix(35),per2pix(65,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))
        retry_button= UI_system.pannel_colison(per2pix(35),per2pix(85,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))

        main_button.render()
        levels_button.render()
        next_button.render() 
        retry_button.render()

        main_text= UI_system.text("Main Menu",per2pix(35),per2pix(25,"s_h"),(204,100,140))
        levels_text= UI_system.text("Levels",per2pix(35),per2pix(45,"s_h"),(204,100,140))
        next_text= UI_system.text("Next",per2pix(35),per2pix(65,"s_h"),(204,100,140))
        retry_text = UI_system.text("Retry",per2pix(35),per2pix(85,"s_h"),(204,100,140)) 
        win_text = UI_system.text("FINISH! ",per2pix(35),per2pix(3,"s_h"),(204,100,140)) 
        fin_time_text= UI_system.text(f" Time: {ed_level_time.tm_sec-st_level_time.tm_sec} ",per2pix(35),per2pix(9,"s_h"),(204,100,140))

        if retry_button.check_click():
            #resets the timer and level flags 
            win=False
            st_level_time=time.gmtime()
            ed_level_time=time.gmtime()
            return "retry"
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
        if next_button.check_click():
            win=False
            st_level_time=time.gmtime()
            ed_level_time=time.gmtime()
            return "next_level"
        else:
            return"win"


    def level_lose ():
        bg_color=("salmond")
        global st_level_time ,ed_level_time
        bg_color=("AliceBlue")
        main_button = UI_system.pannel_colison(per2pix(35),per2pix(25,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))
        levels_button= UI_system.pannel_colison(per2pix(35),per2pix(45,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))
        retry_button= UI_system.pannel_colison(per2pix(35),per2pix(85,"s_h"),per2pix(33),per2pix(10,"s_h"),(180,220,220))

        main_button.render()
        levels_button.render()
        retry_button.render()

        main_text= UI_system.text("Main Menu",per2pix(35),per2pix(25,"s_h"),(204,100,140))
        levels_text= UI_system.text("Levels",per2pix(35),per2pix(45,"s_h"),(204,100,140))
        retry_text = UI_system.text("Retry",per2pix(35),per2pix(85,"s_h"),(204,100,140)) 
        win_text = UI_system.text("No Win :(",per2pix(35),per2pix(3,"s_h"),(204,100,140)) 

        if retry_button.check_click():
            #resets the timer and level flags 
            win=False
            lose = False
            st_level_time=time.gmtime()
            ed_level_time=time.gmtime()
            return "retry"
        elif main_button.check_click():
            win=False
            lose = False
            st_level_time=time.gmtime()
            ed_level_time=time.gmtime()
            return  "home"
        elif levels_button.check_click():
            win=False
            lose = False
            st_level_time=time.gmtime()
            ed_level_time=time.gmtime()
            return "level_menu"
        else:
            return"lose"

    def game_pause():#may be unused
        bg_color=(180,180,180)

        #define buttons 
        # render buttons 
        #render
        # check buttons  
        #        
        
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
            finish_text=UI_system.text("win",per2pix(45),per2pix(40,"s_h"),(200,213,212),)
            level_text=UI_system.text("Level 1", per2pix(5),per2pix(8,"s_h"),(100,100,150),None,10)
            timer_text=UI_system.text(f" time: {time.gmtime().tm_sec-st_level_time.tm_sec}",per2pix(80),per2pix(10,"s_h"),(200,41,184),None,13)
            goal_text=UI_system.text("press the win button to win", per2pix(20),per2pix(8,"s_h"),(100,100,100),None,20)
            if finish_button.check_click():
                ed_level_time=time.gmtime()
                win=True

        elif win and lose == False:
            win=False
            lose=False
            return "win"    

            #load winning screen
        elif win == False and lose == True:
            win=False
            lose=False
            return "lose"
            # loads failior screen 
    
    def level_2 ():
        # set varables (constant)
        global st_level_time ,ed_level_time ,win ,lose ,pause ,pos_tracker
        screen.fill(bg_color)
        pos_list=[(per2pix(50),per2pix(50,"s_h")),(per2pix(20),per2pix(10,"s_h")),(per2pix(80),per2pix(80,"s_h")),(per2pix(50),per2pix(0,"s_h"))]

        if win == False and lose == False:
            # loads the playable 

            # sets buttons 
#                UI_system.pannel_colison.re_pos
            try: # this could be better :(
                win_button=UI_system.pannel_colison(pos_list[pos_tracker][0],pos_list[pos_tracker][1],30,30,(200,255,200))

            except:
                win_button=UI_system.pannel_colison(per2pix(45),per2pix(45,"s_h"),30,30,(200,255,200))
                print("define no")

            # render buttons

            win_button.render()

            if not pause : 

                # renders text
                intruct_text=UI_system.text("click the real win button",per2pix(30),per2pix(5,"s_h"))
                level_text=UI_system.text("level 2",per2pix(1),per2pix(2,"s_h"))
                time_text=UI_system.text(f"time: {ed_level_time.tm_sec-st_level_time.tm_sec}",per2pix(98),per2pix(5,"s_h"))
                # check buttons 

                if win_button.check_click() and pos_tracker < len(pos_list) :
                    pos_tracker+=1
                    #print(f"rect: {win_button.rect.x} , {win_button.rect.y}   list :   {pos_list[pos_tracker][0]}  , {pos_list[pos_tracker][1]}")

                    
                elif  pos_tracker == len(pos_list):
                    #  win_button.check_click() and win_button.x == pos_list[-1] and win_button.y == pos_list[-1]:
                    #print(f" pos_t :  { pos_tracker}  ,  pos_li:  { len(pos_list)}")
                    
                    ed_level_time=time.gmtime()
                    win=True
            else:
                if time == 0:
                    #load start menu
                    pause_bg=pygame.rect.Rect(0,0,screen.width(),screen.height())
                    pygame.draw.rect(screen,(100,100,100,100),pause_bg)
                    # load buttons 
                    start_button=UI_system.pannel_colison()
                    main_button=UI_system.pannel_colison(per2pix(10))
                else:
                    # load pause menu 
                    pause_bg=pygame.rect.Rect(0,0,screen.width(),screen.hueght())
                    #load buttons
                    cont_button=UI_system.pannel_colison(per2pix(40),per2pix(40,"s_h"),per2pix(10),per2pix(5,"s_h"),(180,210,180))
                    retry_button=UI_system.pannel_colison(per2pix(40),per2pix(50,"s_h"),per2pix(10),per2pix(5,"s_h"),(180,210,180))
                    main_button=UI_system.pannel_colison(per2pix(40),per2pix(60,"s_h"),per2pix(10),per2pix(5,"s_h"),(180,210,180))

                    #render buttons 
                    cont_button.render()
                    retry_button.render()
                    main_button.render()

                    #load text
                    UI_system.text("Pause",per2pix(40),per2pix(10,"s_h"),(0,0,0),None,30)
                    UI_system.text("continue",per2pix(40),per2pix(40,"s_h"),(20,30,100),None,15)
                    UI_system.text("retry",per2pix(40),per2pix(50,"s_h"),(20,30,100),None,15)
                    UI_system.text("main menu",per2pix(40),per2pix(60,"s_h"),(20,30,100),None,15)

                
        elif win and lose != True :
                # win menue

                #continue to load visuals 
                pos_tracker=0
                win=False
                lose=False
                return "win"    

                # load win animation

                # return win 




    def level_3 ():
        screen.fill(bg_color)
        global st_level_time ,ed_level_time ,win ,lose ,pause ,pos_tracker,list_vaule,dropdown
        item_list=["click","the","win", "button"]
        # set varables (constant)
        if not pause : 
            if win != True and lose != True:
                # loads the playable 
                
                dropdown=UI_system.ui_drop_down(per2pix(35),per2pix(35,"s_h"),per2pix(10),per2pix(4,"s_h"),(200,200,250),item_list)
                win_button=UI_system.pannel_colison(per2pix(45),per2pix(45,"s_h"),30,30,(200,255,200))

                # sets buttons 

                #renders buttons
                
                list_result=dropdown.check_click()
                # renders text
                intruct_text=UI_system.text("use the drop down menu",per2pix(30),per2pix(5,"s_h"))
                level_text=UI_system.text("level 3",per2pix(1),per2pix(2,"s_h"))
                time_text=UI_system.text(f"time: {ed_level_time.tm_sec-st_level_time.tm_sec}",per2pix(98),per2pix(5,"s_h"))
                # check buttons 
                if list_result =="win":
                    list_vaule="win"
                if list_vaule== "win":
                    win_button.render()
                    if win_button.check_click():
                        ed_level_time=time.gmtime()
                        win=True


                
            elif win and lose != True :
                # win menue

                #continue to load visuals 

                win=False
                lose=False
                return "win"    
                # load win animation

                # return win 
        else:
            if time == 0:
                #load start menu
                win_avalable=False
                pause_text=UI_system.text("start_ pause menu",per2pix(43),per2pix(10,"s_h"))
                pass
            else:
                # load pause menu 
                pause_text=UI_system.text("pause menu",per2pix(43),per2pix(10,"s_h"))
                pass


    def level_4 ():
        screen.fill(bg_color)
        global st_level_time ,ed_level_time ,win ,lose ,pause ,pos_tracker
        # set varables (constant)
        if not pause : 
            if win != True and lose != True:
                # loads the playable 
                
                lose_squ=UI_system.lose_squ(per2pix(35),per2pix(45,"s_h"),per2pix(10),per2pix(30,"s_h"),(255,0,0))
                win_button=UI_system.pannel_colison(per2pix(45),per2pix(45,"s_h"),30,30,(200,255,200))


                # sets buttons 


                #renders buttons
                lose_squ.render()
                win_button.render()

                # renders text
                intruct_text=UI_system.text("click the win button",per2pix(30),per2pix(5,"s_h"))
                level_text=UI_system.text("level 4",per2pix(1),per2pix(2,"s_h"))
                time_text=UI_system.text(f"time: {ed_level_time.tm_sec-st_level_time.tm_sec}",per2pix(98),per2pix(5,"s_h"))
                # check buttons 
                print(f"win: {win} , loose:  {lose} ")
                if lose_squ.check_mouse():
                    print("click lose")
                    lose = True
                if win_button.check_click():
                    print("click win")
                    win= True
                
            elif win and lose != True :
                # win menue

                #continue to load visuals 
                win=False
                lose=False
                return "win" 
                # load win animation

                # return win 

                pass
            elif win != True and lose:
                #lose menu

                # render visuals 
                win=False
                lose=False
                return "lose" 
                # load lose animation

                # return to lose screen
                pass 
        else:
            if time == 0: # needs to fix timer system
                #load start menu
                pass
            else:
                # load pause menu 
                pass

    def  level_5():
        screen.fill(bg_color)
        global st_level_time ,ed_level_time ,win ,lose ,pause ,pos_tracker
        # set varables (constant)
        if not pause : 
            if win != True and lose != True:
                # loads the playable 

                # sets buttons 

                # the switch should be set before the gameloop starts 
                switch=UI_system.switch(per2pix(70),per2pix(25,"s_h"),per2pix(10),per2pix(5,"s_h"),(200,200,200),100)
                win_button=UI_system.pannel_colison(per2pix(25),per2pix(45,"s_h"),30,30,(200,255,200))
                #renders buttons
                switch.render_long()

                # renders text
                intruct_text=UI_system.text("pull the switch down",per2pix(30),per2pix(5,"s_h"))
                level_text=UI_system.text("level 5",per2pix(1),per2pix(2,"s_h"))
                time_text=UI_system.text(f"time: {ed_level_time.tm_sec-st_level_time.tm_sec}",per2pix(98),per2pix(5,"s_h"))
                # check buttons 
                if switch.check_click():
                    win_button.render()
                    if win_button.check_click():
                        win=True


            elif win and lose != True :
                # win menue

                #continue to load visuals 

                # load win animation
                win=False
                lose=False
                return "win"
                # return win 


            elif win != True and lose:
                #lose menu

                # render visuals 

                # load lose animation

                # return to lose screen

                pass 
        else:
            if time == 0:
                #load start menu
                pass
            else:
                # load pause menu 
                pass


    def level_temp ():
        screen.fill(bg_color)
        global st_level_time ,ed_level_time ,win ,lose ,pause ,pos_tracker
        # set varables (constant)
        if not pause : 
            if win != True and lose != True:
                # loads the playable 

                # sets buttons 

                #renders buttons

                # renders text
                intruct_text=UI_system.text("win",per2pix(30),per2pix(5,"s_h"))
                level_text=UI_system.text("level #",per2pix(1),per2pix(2,"s_h"))
                time_text=UI_system.text(f"time: {ed_level_time.tm_sec-st_level_time.tm_sec}",per2pix(98),per2pix(5,"s_h"))
                # check buttons 
                
                pass
            elif win and lose != True :
                # win menue

                #continue to load visuals 

                # load win animation

                # return win 

                pass
            elif win != True and lose:
                #lose menu

                # render visuals 

                # load lose animation

                # return to lose screen
                pass 
        else:
            if time == 0:
                #load start menu
                pause_text=UI_system.text("start_ pause menu",per2pix(43),per2pix(10,"s_h"))
                pass
            else:
                # load pause menu 
                pause_text=UI_system.text("pause menu",per2pix(43),per2pix(10,"s_h"))
                pass

# up dates level timer
 
if pause == True:
    pass
    # anti_time+=#pygame frame


