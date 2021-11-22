import pygame, sys
from pygame import locals
from os import path
from state.state import State
from view_engine import ViewEngine

class Main: 
    def __init__(self):
        self.run = True
        self.fps = 60
        self.name = "Island Wars"
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 500
        self.display = None
        self.clock = None
        self.backgroundColor = (0, 0, 0)
        self.events = []
        self.state:State = State()
        self.view_engine = ViewEngine(events=self.events, fps=self.fps, engine=self)
    
    def init(self) -> None: 
        pygame.init()
        pygame.display.set_caption(self.name)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.view_engine.init()

    def loop(self) -> None: 
        while self.run:
            self.events = pygame.event.get()

            self.view_engine.events = self.events
            self.view_engine.fps = self.fps

            for event in self.events:
                if event.type == locals.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display.fill(self.backgroundColor)

            self.view_engine.render()

            self.clock.tick(self.fps)

            pygame.display.update()
    

if __name__ == "__main__": 
    engine = Main()
    engine.init()
    engine.loop()
