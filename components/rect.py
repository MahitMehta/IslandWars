from typing import IO
import pygame

class IOptions: 
    def __init__(self, width=0, height=0, color=(0, 0, 0), borderColor=(0, 0, 0), borderWidth=2, transparant=False): 
        self.width: int = width
        self.height: int = height
        self.color: tuple = color
        self.borderWidth: int = borderWidth
        self.borderColor: tuple = borderColor
        self.transparant: bool = transparant

class Rect: 
    def __init__(self, display, x, y, options:IOptions, border=False): 
        self.x = x
        self.y = y
        self.options:IOptions = options
        self.display = display
        self.border:bool = border

    def render(self): 
        if self.border: self.render_border()

        if not self.options.transparant: 
            pygame.draw.rect(
                self.display,
                self.options.color,
                [ self.x, self.y, self.options.width, self.options.height ]
            )

    def render_border(self):
        borderWidth = self.options.borderWidth
        coord_adjustment = borderWidth / 2 if not borderWidth == 0 else 0
        x = int(self.x - coord_adjustment)
        y = int(self.y - coord_adjustment) 

        width = int(self.options.width) + borderWidth
        height = int(self.options.height) + borderWidth

        pygame.draw.rect(
            self.display,
            self.options.borderColor,
            [ x, y, width, height ]
        )
