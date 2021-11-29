class Character: 
    def __init__(self, x): 
        self.height = 0
        self.frame = 0
        self.x = x
        self.movement_status = "default"
        self.is_jumping = False
        self.y_offset = 0
        self.jump_stage = 0
        self.jump_stages = 10
        self.jump_height = 125
        self.bullets = []
        self.jump_current_height = 0
        self.max_health = 100
        self.health = self.max_health