

class Block:
    def __init__(self, x, y, idle):
        self.x = x
        self.y = y
        self.idle = idle
    
    def get_rotation(self):
        pass
    
    def get_idle(self):
        return self.idle