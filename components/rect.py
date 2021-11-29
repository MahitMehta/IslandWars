import pygame

class IOptions: 
    def __init__(
            self, 
            width=0, 
            height=0, 
            color=(0, 0, 0), 
            borderColor=(0, 0, 0), 
            borderWidth=2, 
            textOptions={}, 
            transparant=False, 
            text=None
        ): 
        self.width: int = width
        self.height: int = height
        self.color: tuple = color
        self.borderWidth: int = borderWidth
        self.borderColor: tuple = borderColor
        self.transparant: bool = transparant
        self.text = text
        self.textOptions = textOptions

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

        if isinstance(self.options.text, str): self.render_text()

    def render_text(self): 
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.options.text, True, **self.options.textOptions)
        textRect = text.get_rect()
        textRect.center = (self.x + self.options.width // 2, self.y + self.options.height // 2)
        self.display.blit(text, textRect)

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
