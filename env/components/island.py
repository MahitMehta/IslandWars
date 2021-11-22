from state.state import State

class Island: 
    def __init__(self, state, fps):
        self.state:State = state
        self.movement_range = 25
        self.increment = 15 / fps
    
    def increment_height(self, height, ascending, setAscending) -> int: 
        adjusted_height = height 

        if height < self.movement_range and ascending:
            adjusted_height += self.increment
            if (adjusted_height >= self.movement_range): 
                setAscending()
        elif height >= self.movement_range or not ascending: 
            adjusted_height -= self.increment
            if (adjusted_height <= -self.movement_range):
                setAscending()


        return adjusted_height
    
    