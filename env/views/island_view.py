from components.island_left import IslandLeft
from components.character import Character
from constants import assets 

class IslandView: 
    def __init__(self, view_engine): 
        self.view_engine = view_engine
        self.island_width = 450

    def init(self): 
        self.view_engine.setBackground((168, 226, 255))

    def render(self):
       

        self.islands()
        self.characters()

    def characters(self):
        asset_paths = [assets.RIGHT_ONE, assets.RIGHT_TWO, assets.RIGHT_THREE, assets.LEFT_ONE, assets.LEFT_TWO, assets.LEFT_THREE]
        
        characterLeft = Character(self.view_engine, asset_paths, characterKey="characterLeft")
        x = self.view_engine.engine.state.characterLeft.x
        y = int(self.view_engine.engine.state.island_left_height)
        frame = self.view_engine.engine.state.characterLeft.frame
        characterLeft.init()
        characterLeft.render((x, y), frame)

        characterRight = Character(self.view_engine, asset_paths, characterKey="characterRight")
        x = self.view_engine.engine.state.characterRight.x
        y = int(self.view_engine.engine.state.island_left_height)
        frame = self.view_engine.engine.state.characterRight.frame
        characterRight.init()
        characterRight.render((x, y), frame)

    def islands(self): 
        width = self.view_engine.engine.WINDOW_WIDTH
        paddingHorizonatal = 25
        paddingVertical = 50
 
        island_left_start = paddingHorizonatal
        island_left = IslandLeft(self.view_engine)
        island_left.island_width = self.island_width
        island_left.init()
        island_left.render((island_left_start, paddingVertical))

        island_right_start = width - paddingHorizonatal - self.island_width
        island_left = IslandLeft(self.view_engine)
        island_left.island_width = self.island_width
        island_left.init()
        island_left.render((island_right_start, paddingVertical))