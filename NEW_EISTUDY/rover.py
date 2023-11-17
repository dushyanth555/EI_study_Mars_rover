from direction import Direction

class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = Direction(direction)
        self.grid = grid

    def move(self):
        if self.grid.can_move_to(self.x, self.y, self.direction):
            self.x, self.y = self.grid.next_position(self.x, self.y, self.direction)

    def turn_left(self):
        self.direction.turn_left()

    def turn_right(self):
        self.direction.turn_right()

    def current_position(self):
        return self.x, self.y, self.direction.current()
