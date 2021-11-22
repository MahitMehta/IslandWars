from state.character import Character

class State:
    def __init__(self): 
        self.island_left_height:int = 0
        self.island_right_height:int = 0
        self.island_left_ascending = False
        self.island_right_ascending = False
        self.characterLeft:Character = Character(x=150)
        self.characterRight:Character = Character(x=650)