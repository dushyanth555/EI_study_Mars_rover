import tkinter as tk
from rover import Rover
from grid import Grid
from command import MoveForwardCommand, TurnLeftCommand, TurnRightCommand

class RoverGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rover Control")

        self.grid_label = tk.Label(master, text="Enter Grid Size (width height):")
        self.grid_label.pack()

        self.grid_entry = tk.Entry(master)
        self.grid_entry.pack()

        self.start_label = tk.Label(master, text="Enter Starting Position (x, y, direction):")
        self.start_label.pack()

        self.start_entry = tk.Entry(master)
        self.start_entry.pack()

        self.command_label = tk.Label(master, text="Enter Commands (e.g., M, M, R, M, L, M):")
        self.command_label.pack()

        self.command_entry = tk.Entry(master)
        self.command_entry.pack()

        self.obstacle_label = tk.Label(master, text="Enter Obstacles (e.g., 2,2; 3,5):")
        self.obstacle_label.pack()

        self.obstacle_entry = tk.Entry(master)
        self.obstacle_entry.pack()

        self.run_button = tk.Button(master, text="Run Rover", command=self.run_rover)
        self.run_button.pack()

    def parse_position(self, input_str):
        x, y, direction = input_str.split(',')
        return int(x), int(y), direction.strip()

    def parse_obstacles(self, input_str):
        obstacles = input_str.split(';')
        return [tuple(map(int, obs.split(','))) for obs in obstacles]

    def run_rover(self):
        grid_width, grid_height = map(int, self.grid_entry.get().split())
        start_x, start_y, start_direction = self.parse_position(self.start_entry.get())
        command_sequence = list(self.command_entry.get().replace(" ", "").upper())
        obstacles_input = self.obstacle_entry.get()
        obstacles = self.parse_obstacles(obstacles_input) if obstacles_input else []

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
        result_text = f"Final Position: ({x}, {y}, {direction})\nStatus Report: Rover is at ({x}, {y}) facing {direction}. {obstacle_detected}"

        result_window = tk.Toplevel(self.master)
        result_label = tk.Label(result_window, text=result_text)
        result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoverGUI(root)
    root.mainloop()
