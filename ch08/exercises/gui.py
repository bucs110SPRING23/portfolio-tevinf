class BackgroundSprite(): 
    def __init__(self): 
        self.identity = ("cloud", "shrub")
        self.x_pos = 300 
        self.y_pos = -10 
        self.isanimated = True 
class Goomba(): 
    def __init__(self): 
        self.quantity = 2 
        self.motion = True 
        self.independence = True 
        self.unison = False 
class MysteryBlock(): 
    def __init__(self, mysteryitem): 
        self.collide_player = False 
        self.ispressed = True 
        self.contents = mysteryitem 



