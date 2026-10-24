import UI_system

class game_levels :

    def home ():
        in_pannal=UI_system.pannel_colison(200,214,23,90,(39,100,255))
        pannal=UI_system.pannel(20,30,50,40,(100,100,100))
        pannal.render()
        if in_pannal.check_col():
            print("click")
        in_pannal.render() 

    def level_0 () :
        pannal=UI_system.pannel(20,30,50,40,(100,100,100))
        pannal.render()

    def level_1():
        pannel=UI_system
        pannel.render()
    
    def level_2 ():
        pannal=UI_system.pannel(200,30,120,40,(200,140,210))
        pannal.render()