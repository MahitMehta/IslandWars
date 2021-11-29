from components.rect import Rect, IOptions
from state.character import Character

class HealthBar: 
    def __init__(self, view_engine, state:Character): 
        self.view_engine = view_engine
        self.display = self.view_engine.engine.display
        self.width = 135
        self.height = 30
        self.state:Character = state

    def render(self, x, y, color=(0, 0, 0), borderColor=(0, 0, 0)): 
        options:IOptions = IOptions(
            width=self.width, 
            height=self.height, 
            color=color,
            transparant=True,
            borderColor=borderColor,
            borderWidth=8
        )
        border = Rect(display=self.display, x=x, y=y, options=options, border=True)
        border.render()

        percentage = self.state.health / self.state.max_health
        width = int(self.width * percentage)

        options:IOptions = IOptions(
            width=width, 
            height=self.height, 
            color=color,
        )
        rect = Rect(display=self.display, x=x, y=y, options=options, border=False)
        rect.render()

