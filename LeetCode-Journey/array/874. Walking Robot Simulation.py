'''
Question: 874. Walking Robot Simulation (Medium)
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
- -2: Turn left 90 degrees.
- -1: Turn right 90 degrees.
- 1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (x, y). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. x^2 + y^2).

Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 3^2 + 4^2 = 25 units away.

---
My Approach (Simulation + Hash Set + Modulo Direction Map):
1. Convert the `obstacles` list of lists into a set of tuples. This is critical because checking if a coordinate exists in a Set is $O(1)$, whereas checking a List is $O(K)$.
2. Create a direction array `dir` representing North, East, South, and West in order.
3. Track the current direction using an index `d`. 
   - Turn Right (-1): `d = (d + 1) % 4`
   - Turn Left (-2): `d = (d + 3) % 4`
4. For movement commands, loop step-by-step. Calculate the next coordinate `(nx, ny)`.
5. Check if `(nx, ny)` is in our obstacle set. If it is, `break` the inner loop early and stop moving for this command.
6. If the path is clear, update the coordinates and calculate the new max distance squared.

Time Complexity: $O(N + K)$ where N is the total number of steps taken (commands * max 9) and K is the number of obstacles.
Space Complexity: $O(K)$ to store the obstacles in a hash set.
'''

import ast
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Pythonic optimization: map inner lists to tuples and cast directly to a set
        st = set(map(tuple, obstacles))

        # directions: North (0,1), East (1,0), South (0,-1), West (-1,0)
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        d = 0  # Start facing North
        x, y = 0, 0
        ans = 0

        for cmd in commands:
            if cmd == -1:
                # Turn right
                d = (d + 1) % 4
            elif cmd == -2:
                # Turn left
                d = (d + 3) % 4
            else:
                # Move forward step by step
                for _ in range(cmd):
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]

                    # Hit an obstacle, stop moving
                    if (nx, ny) in st:
                        break

                    x, y = nx, ny
                    # Update max distance squared
                    ans = max(ans, x*x + y*y)

        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 874. Walking Robot Simulation Interactive Runner ---")
    try:
        commands_input = input("Enter the commands array (e.g., [4,-1,4,-2,4]): ").strip()
        obstacles_input = input("Enter the obstacles array (e.g., [[2,4]]): ").strip()
        
        # Safely evaluate inputs
        parsed_commands = ast.literal_eval(commands_input)
        parsed_obstacles = ast.literal_eval(obstacles_input)
        
        if not isinstance(parsed_commands, list) or not isinstance(parsed_obstacles, list):
            raise ValueError("Both inputs must be valid lists.")
            
        # Calling the function
        result = solution.robotSim(parsed_commands, parsed_obstacles)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")