import UI_system
import time


win=False
lose=False
st_level_time=time.clock_gettime()

def per2pix(per , whole):
    pix= ((per/100)*whole)
    return pix 
    

class game_levels:

    def home ():
        if ply_levels != []:
            continue_button
            continue_text
        play_button
        play_text
        quit_button
        quit_text
        tital_bg=UI_system.pannel
        tital_img
        ver_text

        in_pannal=UI_system.pannel_colison(200,214,23,90,(39,100,255))
        pannal=UI_system.pannel(20,30,50,40,(100,100,100))
        pannal.render()
        if in_pannal.check_col() == True:
            print("click")

        in_pannal.render() 

    def settings ():
        # music volume, mute, show timer
        settings_text
        settings_bg=UI_system.pannel(per2pix(35),)
        pass 

    def level_0 () :
        pannal=UI_system.pannel(20,30,50,40,(100,100,100))
        pannal.render()

    def level_1(): 
        if win != True and lose != False:
            if finish_button.check_click():
                win=True

        elif win == True and lose == False:
            return True
            
            #load winning screen
        elif win == False and lose == True:
            return True
            pass
            # loads failior screen 
        level_text
        goal_text
        goal_bg=UI_system.pannel()
        timer_text
        finish_button
        finish_text
        pannel=UI_system
        pannel.render() 
    
    def level_2 ():
        pannal=UI_system.pannel(200,30,120,40,(200,140,210))
        pannal.render()
