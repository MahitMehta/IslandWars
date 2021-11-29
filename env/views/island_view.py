from components.island_left import IslandLeft
from components.island_right import IslandRight
from components.character import Character
from components.health_bar import HealthBar

class IslandView: 
    def __init__(self, view_engine): 
        self.view_engine = view_engine
        self.island_width = 450

    def init(self): 
        self.view_engine.setBackground((168, 226, 255))

    def render(self):
        self.islands()
        self.characters()
        self.health_bars()

    def health_bars(self): 
        width = self.view_engine.engine.WINDOW_WIDTH
        state = self.view_engine.engine.state

        character_left = getattr(state, 'characterLeft')
        character_right = getattr(state, 'characterRight')

        health_bar_left = HealthBar(self.view_engine, state=character_left)
        x, y = (30, 30)
        health_bar_left.render(x=x, y=y, color=(0, 104, 255), borderColor=(0, 81, 199))

        health_bar_right = HealthBar(self.view_engine, state=character_right)
        x, y = (width - 30 - health_bar_left.width, 30)
        health_bar_right.render(x=x, y=y, color=(255, 67, 67), borderColor=(199, 0, 0))

    def characters(self):
        characterLeft = Character(self.view_engine, characterKey="characterLeft")
        x = self.view_engine.engine.state.characterLeft.x
        y = int(self.view_engine.engine.state.island_left_height)
        characterLeft.init()
        characterLeft.render((x, y))

        characterRight = Character(self.view_engine, characterKey="characterRight")
        x = self.view_engine.engine.state.characterRight.x
        y = int(self.view_engine.engine.state.island_right_height)
        characterRight.init()
        characterRight.render((x, y))

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
        island_right = IslandRight(self.view_engine)
        island_right.island_width = self.island_width
        island_right.init()
        island_right.render((island_right_start, paddingVertical))