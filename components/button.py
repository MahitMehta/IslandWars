import pygame
from components.rect import Rect, IOptions as IRectOptions

class IButtonOptions: 
    def __init__(self, width=0, height=0, borderColor=None, isBorder=False, borderWidth=2, center=False, color=(0, 0, 0), text=""): 
        self.width: int = width
        self.height: int = height
        self.borderColor: tuple = borderColor
        self.borderWidth: int = borderWidth
        self.center: bool = center
        self.color: tuple = color
        self.text: str = text 
        self.isBorder: bool = isBorder
    
class Button:
    def __init__(self, view_engine, options:IButtonOptions, onClick, x=0, y=0): 
        self.view_engine = view_engine
        self.options:IButtonOptions = options
        self.x:int = x
        self.y: int = y
        self.onClick = onClick

    def render(self): 
        x, y = (self.x, self.y)
        if self.options.center: x -= (self.options.width // 2); y -= (self.options.height // 2)

        if self.options.isBorder: 
            rect = Rect(
                display=self.view_engine.engine.display,
                x=x, 
                y=y, 
                options=IRectOptions(
                    width=self.options.width, 
                    height=self.options.height, 
                    color=self.options.color,
                    borderColor=self.options.borderColor,
                    borderWidth=self.options.borderWidth,
                    text=self.options.text,
                    textOptions={ "color": (0, 0, 0) }
                ), 
                border=True)
            rect.render()

        self.handleClick()
        
    def handleClick(self): 
        borderWidth = self.options.borderWidth if self.options.borderWidth else 0
    
        x = int(self.x)
        y = int(self.y)

        width = int(self.options.width) + borderWidth
        height = int(self.options.height) + borderWidth

        if self.options.center: 
            x -= int(width / 2)
            y -= int(height / 2)

        maxWidth = int(x + self.options.width)
        maxHeight = int(y + self.options.height)

        for ev in self.view_engine.events:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = ev.pos
                if x <= mouse[0] <= maxWidth and y <= mouse[1] <= maxHeight:
                    self.onClick()
        

    def setText(self): 
        x = self.x
        y = self.y

        smallfont = pygame.font.SysFont('Corbel',15)
        text = smallfont.render(self.options['text'] , True , (0, 0, 0))

        self.view_engine.engine.display.blit(text , x, y)