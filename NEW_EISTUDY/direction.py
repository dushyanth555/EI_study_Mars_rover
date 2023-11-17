class Direction:
    directions = ['N', 'E', 'S', 'W']

    def __init__(self, current):
        self.current_index = self.directions.index(current)

    def turn_left(self):
        self.current_index = (self.current_index - 1) % len(self.directions)

    def turn_right(self):
        self.current_index = (self.current_index + 1) % len(self.directions)

    def current(self):
        return self.directions[self.current_index]
