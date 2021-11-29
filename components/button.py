import pygame

class IOptions: 
    width: int
    height: int
    borderColor: tuple
    center: bool
    color: tuple
    text: str
    
class Button:
    def __init__(self, view_engine, options:IOptions, onClick): 
        self.view_engine = view_engine
        self.options:IOptions = options
        self.x:int | None = None
        self.y: int | None = None
        self.onClick = onClick

    def init(self): 
        self.x = int(self.view_engine.engine.WINDOW_WIDTH / 2) 
        self.y = int(self.view_engine.engine.WINDOW_HEIGHT / 2)

    def render(self): 
        try: 
            if isinstance(self.options['borderColor'], tuple): 
                self.border()
        except KeyError: 
            pass
        
        self.body()
        self.handleClick()

        # try: 
        #     if isinstance(self.options['text'], str): 
        #        self.setText()
        # except: 
        #     pass
        
    def handleClick(self): 
        borderWidth = 0
        try: 
            borderWidth = self.options['borderWidth']
        except: 
            pass
    
        x = int(self.x)
        y = int(self.y)

        width = int(self.options['width']) + borderWidth
        height = int(self.options['height']) + borderWidth

        maxWidth = int(x + self.options['width'])
        maxHeight = int(y + self.options['height'])

        try: 
            if self.options['center'] == True: 
                x -= int(width / 2)
                y -= int(height / 2)
        except: 
            pass

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


    def border(self):
        try: 
            borderWidth = self.options['borderWidth']
            x = int(self.x)
            y = int(self.y)

            width = int(self.options['width']) + borderWidth
            height = int(self.options['height']) + borderWidth

            if self.options['center'] == True: 
                x -= int(width / 2)
                y -= int(height / 2)

            pygame.draw.rect(
                self.view_engine.engine.display,
                self.options['borderColor'],
                [ x, y, width, height ]
            )
        except KeyError: 
            pass

    def body(self): 
        x = self.x
        y = self.y

        try: 
            if self.options['center'] == True: 
                x -= int(self.options['width'] / 2)
                y -= int(self.options['height'] / 2)
        except KeyError: 
            pass

        pygame.draw.rect(
            self.view_engine.engine.display,
            self.options['color'],
            [ x, y, self.options['width'], self.options['height'] ]
        )