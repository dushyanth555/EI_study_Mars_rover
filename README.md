Mars Rover Simulation - README

Description:
--
This Python program simulates the movement of a Mars Rover on a grid-based terrain. The program takes user inputs for the grid size, starting position, commands, and optional obstacles. The Rover is designed to move forward, turn left, and turn right while avoiding obstacles and staying within the grid boundaries.

Files:
--
1. **rover.py:** Contains the Rover class representing the Mars Rover.
2. **grid.py:** Implements the Grid class to represent the terrain, including obstacles.
3. **command.py:** Defines command classes (MoveForwardCommand, TurnLeftCommand, TurnRightCommand) using the Command Pattern.

Usage:
--
1. Run the program:
    
    python main.py
    

2. Enter the requested information:
    - Grid Size (width height): Enter the width and height of the grid (e.g., 10 10).
    - Starting Position (x, y, direction): Enter the initial position and direction of the Rover (e.g., 0, 0, N).
    - Commands (e.g., M, M, R, M, L, M): Enter the sequence of commands for the Rover.
    - Obstacles (e.g., 2,2; 3,5): Enter obstacle positions separated by semicolons (optional).

3. View the program's output:
    - Final Position: Displaying the Rover's position after executing the command sequence.
    - Status Report: Providing information on the final position and whether obstacles were detected.

Criteria used:
---------------------
1. **Code Quality:**
   - Adherence to Python best practices and coding conventions.
   - Clear and modular code structure.

2. **Functionality:**
   - Successful implementation of Rover movement, obstacle avoidance, and grid boundary checks.

3. **User Interaction:**
   - Intuitive user input and clear output presentation.

4. **Documentation:**
   - Adequate comments in the code explaining major functionalities and design choices.

5. **Error Handling:**
   - Effective handling of input validation and possible runtime errors.

Note:
-----
This README is a basic guide. Customize it based on specific requirements or additional details. Ensure that users understand the expected input format and how to interpret the program's output.

