from utils import tools
from constants import assets 
import pygame
from time import time

class Character: 
    def __init__(self, view_engine, characterKey): 
        self.view_engine = view_engine

        self.right_vectors = tools.load_assets([assets.RIGHT_ONE, assets.RIGHT_TWO, assets.RIGHT_THREE])
        self.left_vectors = tools.load_assets([ assets.LEFT_ONE, assets.LEFT_TWO, assets.LEFT_THREE ])
        self.default_vector = tools.load_asset(assets.DEFAULT)
        self.red_bullet_vector = tools.load_asset(assets.RED_BULLET)
        self.blue_bullet_vector = tools.load_asset(assets.BLUE_BULLET)

        self.characterKey = characterKey
        self.height = 150
        self.width = 150

        self.state = getattr(self.view_engine.engine.state, self.characterKey)
        self.movement_status = self.state.movement_status
        self.frame = int(self.state.frame)
        self.shoot_vector = tools.load_asset(assets.RIGHT_SHOOTING if self.characterKey == 'characterRight' else assets.LEFT_SHOOTING)

    def init(self): 
        self.left_vectors = [ tools.scale_asset(i, (self.height, self.width)) for i in self.left_vectors ]
        self.right_vectors = [ tools.scale_asset(i, (self.height, self.width)) for i in self.right_vectors ]
        self.default_vector = tools.scale_asset(self.default_vector, (self.height, self.width))
        self.shoot_vector = tools.scale_asset(self.shoot_vector, (self.height, self.width))
        self.red_bullet_vector = tools.scale_asset(self.red_bullet_vector, (50, 50))
        self.blue_bullet_vector = tools.scale_asset(self.blue_bullet_vector, (50, 50))

    def render(self, pos:tuple): 
        x, y = pos
        y -= self.jump_offset()
        self.y = y
                
        if self.movement_status == 'default': 
            self.render_vector(self.default_vector, x, y)
        elif self.movement_status == 'left': 
            self.render_vector(self.left_vectors[self.frame], x, y)
        elif self.movement_status == 'right': 
            self.render_vector(self.right_vectors[self.frame], x, y) 
        elif self.movement_status == "shooting": 
            self.render_vector(self.shoot_vector, x, y)

        if self.state.disabled: return

        self.render_bullets()
        self.movementListener()

    def bullet_collision(self, bullet) -> bool: 
        x, y = (bullet['x'], bullet['y'])

        if self.characterKey == 'characterLeft': 
            state = getattr(self.view_engine.engine.state, 'characterRight')
            state_y = int(self.view_engine.engine.state.island_right_height)
            base = state_y - state.jump_current_height 
            collided_y = y - 15 > base and y < base + self.height 
            collided_x = x - 15 > state.x and x - 15 < state.x + 50
        else: 
            state = getattr(self.view_engine.engine.state, 'characterLeft')
            state_y = int(self.view_engine.engine.state.island_left_height)
            base = state_y - state.jump_current_height 
            collided_y = y - 15 > base and y < base + self.height 
            collided_x = x - 90 < state.x and x - 90 > state.x - 50
        
        if collided_x and collided_y: 
            if self.characterKey == 'characterLeft':
                state = getattr(self.view_engine.engine.state, 'characterRight')
                if state.health >= 5: getattr(self.view_engine.engine.state, 'characterRight').health -= 5
            else: 
                state = getattr(self.view_engine.engine.state, 'characterLeft')
                if state.health >= 5: getattr(self.view_engine.engine.state, 'characterLeft').health -= 5

        return collided_x and collided_y

    def render_bullets(self): 
        for index, bullet in enumerate(self.state.bullets): 
            bullet_vector = self.blue_bullet_vector if self.characterKey == 'characterLeft' else self.red_bullet_vector
            x = bullet['x']
            if x < -35 or x > 985:
                continue  
            self.render_vector(bullet_vector, bullet['x'], bullet['y'])

            vel = 325 / self.view_engine.engine.fps
            vel = vel if self.characterKey == 'characterLeft' else -vel
            getattr(self.view_engine.engine.state, self.characterKey).bullets[index]['x'] += vel
        
        self.state.bullets = \
            [ i for i in self.state.bullets if i['x'] >= -35 and i['x'] <= 985 and not self.bullet_collision(i) ]

    def render_vector(self, vector, x, y): 
            self.view_engine.display_vector(vector, int(x), y + 135)   
    
    def jump_offset(self):
        if not self.state.is_jumping: return 0

        stages = self.state.jump_stages
        vel = 12 / self.view_engine.engine.fps

        if int(self.state.jump_stage) < stages: 
            self.state.jump_stage += vel
        elif int(self.state.jump_stage) == stages: 
            self.state.is_jumping = False
            self.state.jump_stage = 0

        base = self.state.y_offset
        stage = self.state.jump_stage
        max_height = self.state.jump_height
        a = int(max_height / ((stages / 2) * ((stages / 2) - stages)))
        extra = int(a * (stage) * (stage - stages))

        if int(stage) >= stages: 
            return base + (a * int(stage) * (int(stage) - stages))

        jump_offset = base + extra
        self.state.jump_current_height = jump_offset
        return jump_offset

    def movementListener(self): 
        keys = pygame.key.get_pressed()
        vel = 95 / self.view_engine.engine.fps
        
        if self.characterKey == 'characterRight':
            inc =  (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
            self.handle_frame(inc)
            if self.in_boundry(inc): 
                self.state.x += inc

            if keys[pygame.K_UP]: 
                self.state.is_jumping = True
            
            if keys[pygame.K_DOWN]: 
                self.handle_shooting()
                self.state.movement_status = "shooting"

        elif self.characterKey == 'characterLeft': 
            inc = (keys[pygame.K_d] - keys[pygame.K_a]) * vel
            self.handle_frame(inc)
            if self.in_boundry(inc): 
                self.state.x += inc
            
            if keys[pygame.K_w]: 
                self.state.is_jumping = True

            if keys[pygame.K_s]: 
                self.handle_shooting()
                self.state.movement_status = "shooting"

    def handle_shooting(self): 
        bullets = self.state.bullets
        x_padding = 125 if self.characterKey == 'characterLeft' else -10
        deltaMet = time() - bullets[len(bullets) - 1]['timestamp'] > 0.5 if len(bullets) else True
        if len(bullets) < 25 and deltaMet: 
            self.state.bullets.append({
                "x": self.state.x + x_padding,
                "y": self.y + 60,
                "timestamp": time()
            })

    def in_boundry(self, inc): 
        updated_x = self.state.x + inc
        width = self.view_engine.engine.WINDOW_WIDTH

        if self.characterKey == 'characterRight': 
            max_x = width - 25 - 135 # define constants
            min_x = width - 25 - 25 - 450 # define constants
            if updated_x > max_x or updated_x < min_x:
                return False
        elif self.characterKey == 'characterLeft': 
            max_x = 450 - 115
            min_x = 0
            if updated_x > max_x or updated_x < min_x:
                return False

        return True

    def handle_frame(self, inc): 
        if inc > 0: 
            self.change_frame(self.right_vectors)
            self.state.movement_status = "right"
        elif inc < 0: 
            self.change_frame(self.left_vectors)
            self.state.movement_status = "left"
        else: 
            self.state.frame = 0
            self.state.movement_status = "default"

    def change_frame(self, vectors): 
        inc = 10 / self.view_engine.engine.fps
        if self.state.frame < len(vectors) - 1: 
            self.state.frame += inc
        else: 
            self.state.frame = 0