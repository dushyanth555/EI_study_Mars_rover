from rover import Rover
from grid import Grid
from command import MoveForwardCommand, TurnLeftCommand, TurnRightCommand

def parse_position(input_str):
    x, y, direction = input_str.split(',')
    return int(x), int(y), direction.strip()

def parse_obstacles(input_str):
    obstacles = input_str.split(';')
    return [tuple(map(int, obs.split(','))) for obs in obstacles]

def main():
    grid_width, grid_height = map(int, input("Enter Grid Size (width height): ").split())
    start_x, start_y, start_direction = parse_position(input("Enter Starting Position (x, y, direction): "))
    command_sequence = list(input("Enter Commands (e.g., M, M, R, M, L, M): ").replace(" ", "").upper())
    obstacles_input = input("Enter Obstacles (e.g., 2,2; 3,5): ")
    obstacles = parse_obstacles(obstacles_input) if obstacles_input else []

    grid = Grid(grid_width, grid_height, obstacles)
    rover = Rover(start_x, start_y, start_direction, grid)
    commands = {
        'M': MoveForwardCommand(),
        'L': TurnLeftCommand(),
        'R': TurnRightCommand()
    }

    for cmd in command_sequence:
        if not grid.can_move_to(rover.x, rover.y, rover.direction):
            break
        commands[cmd].execute(rover)

    x, y, direction = rover.current_position()
    obstacle_detected = "No Obstacles detected." if grid.can_move_to(x, y, rover.direction) else "Obstacle detected!"
    print(f"Final Position: ({x}, {y}, {direction})")
    print(f"Status Report: Rover is at ({x}, {y}) facing {direction}. {obstacle_detected}")

if __name__ == "__main__":
    main()
