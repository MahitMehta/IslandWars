from state.state import State
from utils import tools
from constants import assets 
from components.island import Island

class IslandLeft(Island): 
    def __init__(self, view_engine): 
        self.view_engine = view_engine
        self.vector = tools.load_asset(assets.ISLAND_LEFT)
        self.island_width:int = 450
        self.state:State = self.view_engine.engine.state
        self.height = self.state.island_left_height
        self.ascending = self.state.island_left_ascending
        self.fps = self.view_engine.engine.fps

        super().__init__(self.state, self.fps)

    def init(self): 
        self.vector = tools.scale_asset(self.vector, (self.island_width, self.island_width))

    def render(self, pos:tuple): 
        (x, y) = pos
        y += int(self.height)
        self.state.island_left_height = self.increment_height(self.height, self.ascending, self.setAscending)
        self.view_engine.display_vector(self.vector, x, y)
    
    def setAscending(self): 
        self.state.island_left_ascending = not self.state.island_left_ascending