

class Slope:

    TREE = '#'

    def __init__(self, map_as_list):
        self.map = map_as_list
        self.x_pos = 0
        self.y_pos = 0
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.x_travel = 0
        self.y_travel = 0

    @classmethod
    def read_map(cls, input_file):
        with open(input_file, 'r') as f:
            return Slope(f.read().splitlines())

    def aim(self, x_step, y_step):
        self.x_travel = x_step
        self.y_travel = y_step
        self.x_pos = 0
        self.y_pos = 0

    def traverse(self):
        trees_encountered = 0

        while self.step():
            if self.is_tree_nearby():
                trees_encountered += 1

        return trees_encountered

    def is_tree_nearby(self):
        return self.map[self.y_pos][self.x_pos] is Slope.TREE

    def step(self):
        self.x_pos = (self.x_pos + self.x_travel) % self.map_width
        self.y_pos = (self.y_pos + self.y_travel)
        return self.y_pos < self.map_height
