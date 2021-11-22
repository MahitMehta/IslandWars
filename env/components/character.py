from utils import tools
import pygame

class Character: 
    def __init__(self, view_engine, asset_paths:list, characterKey): 
        self.view_engine = view_engine
        self.left_vectors = tools.load_assets(asset_paths)
        self.characterKey = characterKey
        self.height = 150
        self.width = 150
    
    def init(self): 
        self.left_vectors = [ tools.scale_asset(i, (self.height, self.width)) for i in self.left_vectors ]

    def render(self, pos:tuple, frame): 
        x, y = pos
        self.view_engine.display_vector(self.left_vectors[frame], int(x), y + 135)   
        self.movementListener()
    
    def movementListener(self): 
        keys = pygame.key.get_pressed()
        vel = 45 / self.view_engine.engine.fps
        (getattr(self.view_engine.engine.state, self.characterKey)).x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel