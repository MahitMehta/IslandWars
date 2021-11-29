from components.rect import Rect, IOptions
from state.character import Character
import pygame

class HealthBar: 
    def __init__(self, view_engine, state:Character, left=True): 
        self.view_engine = view_engine
        self.display = self.view_engine.engine.display
        self.width = 135
        self.height = 30
        self.state:Character = state
        self.left = left

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

        adjusted_x = x if self.left else (self.width - width) + x

        if percentage:
            rect = Rect(display=self.display, x=adjusted_x, y=y, options=options, border=False)
            rect.render()

        white = (255, 255, 255)
        font_size = 32
        font = pygame.font.Font('freesansbold.ttf', font_size)
        percentage_label = f'{int(percentage * 100)}%'
        text = font.render(percentage_label, True, white)
        text_width, _ = font.size(percentage_label)
        text_x = x + 10 if self.left else x + self.width - text_width - 10

        self.view_engine.engine.display.blit(text, (text_x, y + 5))