


class Block:
    def __init__(self, x, y, animations):
        self.x = x
        self.y = y
        self.animations = animations
        self.current_index = 0
        self.sprite = self.animations[self.current_index]
        self.generate_splitted()
        self.generate_coords()

    def rotate(self):
        if self.current_index == len(self.animations) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        self.sprite = self.animations[self.current_index]
        self.generate_splitted()
        self.generate_coords()
    
    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.generate_coords()

    def generate_coords(self):
        self.coords = []
        t_x = self.x
        t_y = self.y
        base_x = t_x
        for line in self.splitted:
            new_coords = []
            for char in line:
                if char != ' ':
                    coord = (t_x, t_y)
                    new_coords.append(coord)
                t_x += 1
            self.coords.append(new_coords)
            t_y += 1
            t_x = base_x
        # return coords

    def is_coord_of_block(self, x, y):
        for coord in self.coords:
            for _coord in coord:
                if _coord[0] == x and _coord[1] == y:
                    return True
        return False

    def get_x_length(self):
        exes = []
        for line in self.coords:
            for coord in line:
                exes.append(coord[0])
        exes.sort()
        exes = set(exes)
        return len(exes)

    def generate_splitted(self):
        self.splitted = self.sprite.split('\n')

    def get_coords(self):
        return self.coords
