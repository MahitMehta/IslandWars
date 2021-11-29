from components.button import Button
from views.constants import views

class HomeView: 
    def __init__(self, view_engine): 
        self.view_engine = view_engine

    def init(self): 
        self.view_engine.setBackground((174, 228, 255))

    def render(self):
        button = Button(
            view_engine=self.view_engine,
            options={ 
                "width": 100, 
                "height": 40, 
                "center": True,
                "color": (0, 164, 244),
                "borderColor": (0, 75, 111),
                "borderWidth": 6,
                "text": "Play"
            },
            onClick=self.onClick
        ) 
        button.init()
        button.render()

    def onClick(self):
        self.view_engine.view = views.ISLAND_VIEW