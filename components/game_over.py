from components.rect import Rect, IOptions as IRectOptions
from components.button import Button, IButtonOptions
import views.constants.views as views
import pygame

class GameOver: 
    def __init__(self, view_engine): 
        self.view_engine = view_engine
        self.width = 300
        self.height = 300

    def render(self, message=""): 
        x = (self.view_engine.engine.WINDOW_WIDTH // 2) - (self.width // 2)
        y = (self.view_engine.engine.WINDOW_HEIGHT // 2) - (self.height // 2)

        rect = Rect(
            display=self.view_engine.engine.display,
            x=x,
            y=y,
            options=IRectOptions(
                width=self.width, 
                height=self.height, 
                color=(0, 164, 244),
                borderColor=(0, 75, 111),
                borderWidth=6,
            ),
            border=True
        )
        rect.render()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(message, True, color=(0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.view_engine.engine.WINDOW_WIDTH // 2, self.height // 2)
        self.view_engine.engine.display.blit(text, textRect)

        button_y = y + self.height - 50
        buttonCount = 2
        points = [ ((self.width // (buttonCount + 1)) * (i + 1)) + x for i in range(buttonCount + 1) ]

        restart = Button(
            view_engine=self.view_engine,
            options=IButtonOptions(
                width=100, 
                height=40, 
                center=True,
                color=(0, 164, 244),
                borderColor=(0, 75, 111),
                borderWidth=6,
                text="Restart",
                isBorder=True
            ),
            x=points[0] - 10,
            y=button_y,
            onClick=self.handleRestart
        )
        restart.render()

        home = Button(
            view_engine=self.view_engine,
            options=IButtonOptions(
                width=100, 
                height=40, 
                center=True,
                color=(0, 164, 244),
                borderColor=(0, 75, 111),
                borderWidth=6,
                text="Home",
                isBorder=True
            ),
            x=points[1] + 10,
            y=button_y,
            onClick=self.handleHome
        )
        home.render()

    def handleHome(self): 
        self.handleRestart()
        self.view_engine.view = views.HOME_VIEW

    def handleRestart(self): 
        state_left = self.view_engine.engine.state.characterLeft
        state_right = self.view_engine.engine.state.characterRight

        state_left.disabled = False
        state_right.disabled = False

        state_left.bullets = []
        state_right.bullets = []

        state_left.movement_status = "default"
        state_right.movement_status = "default"

        state_left.health = state_left.max_health
        state_right.health = state_right.max_health
    
