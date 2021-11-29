from os import X_OK
from components.button import Button, IButtonOptions
from views.constants import views

class HomeView: 
    def __init__(self, view_engine): 
        self.view_engine = view_engine

    def init(self): 
        self.view_engine.setBackground((174, 228, 255))

    def render(self):
        x = int(self.view_engine.engine.WINDOW_WIDTH / 2) 
        y = int(self.view_engine.engine.WINDOW_HEIGHT / 2)

        button = Button(
            view_engine=self.view_engine,
            options=IButtonOptions(
                width=100, 
                height=40, 
                center=True,
                color=(0, 164, 244),
                borderColor=(0, 75, 111),
                borderWidth=6,
                text="Play",
                isBorder=True
            ),
            x=x,
            y=y,
            onClick=self.handleStart
        ) 
        button.render()

    def handleStart(self):
        self.view_engine.view = views.ISLAND_VIEW