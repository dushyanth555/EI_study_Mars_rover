class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles

    def can_move_to(self, x, y, direction):
        next_x, next_y = self.next_position(x, y, direction)
        return self.is_within_bounds(next_x, next_y) and not self.is_obstacle(next_x, next_y)

    def next_position(self, x, y, direction):
        if direction.current() == 'N':
            return x, y + 1
        elif direction.current() == 'E':
            return x + 1, y
        elif direction.current() == 'S':
            return x, y - 1
        elif direction.current() == 'W':
            return x - 1, y
