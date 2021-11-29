from views.island_view import IslandView
from views.home_view import HomeView
import views.constants.views as views

class ViewEngine: 
    def __init__(self, events:list, fps:int, engine):
        self.events:list = events
        self.fps:int = fps
        self.view:str = views.HOME_VIEW

        self.home_view:HomeView | None = None
        self.island_view:IslandView | None = None

        self.engine = engine

    def init(self) -> None: 
        self.home_view = HomeView(view_engine=self)
        self.island_view = IslandView(view_engine=self)

    def setBackground(self, color:tuple) -> None: 
        self.engine.backgroundColor = color

    def display_vector(self, image, x, y): 
        self.engine.display.blit(image, (x, y))

    def render(self) -> None:  
        if self.view == views.HOME_VIEW:
            self.home_view.init()
            self.home_view.render()
        elif self.view == views.ISLAND_VIEW: 
            self.island_view.init()
            self.island_view.render()
