'''
Question: 3661. Maximum Walls Destroyed by Robots
You are given an array of robot positions, their respective blast distances, and the positions of walls on a 1D line. 
Each robot can fire either left or right, destroying all walls within its distance. 
Return the maximum number of walls that can be destroyed.

---
My Approach (Binary Search + 1D Dynamic Programming):
1. Create a dictionary to map each robot to its distance, allowing us to safely sort the robots array.
2. Sort both the `robots` and `walls` arrays to process them sequentially from left to right.
3. For each robot, use binary search (`bisect_left` and `bisect_right`) to count how many walls it can destroy if it fires LEFT (`left[i]`) or RIGHT (`right[i]`).
4. To prevent double-counting, strictly bound the blast radius so a robot's blast doesn't overlap past the adjacent robot's position.
5. Track `num[i]`, which represents the total number of walls sitting strictly between the previous robot and the current robot.
6. Use a DP state machine (`sub_left`, `sub_right`) to iterate through the robots. At each step, calculate the absolute maximum walls destroyed up to that point based on whether the current robot fires left or right, safely accounting for overlapping crossfire in the `num[i]` region.

Time Complexity: $O(R \log R + W \log W + R \log W)$ where R is the number of robots and W is the number of walls. Driven by sorting and the binary searches for each robot.
Space Complexity: $O(R)$ auxiliary space for the `left`, `right`, and `num` arrays, plus the dictionary mapping.
'''

import ast
import bisect
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        robots_to_distance = {}

        # Map robots to their distances before sorting
        for i in range(n):
            robots_to_distance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        # Calculate exact wall counts for each robot's left and right blasts
        for i in range(n):
            pos1 = bisect.bisect_right(walls, robots[i])

            # Calculate left destruction
            if i >= 1:
                left_bound = max(
                    robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1
                )
                left_pos = bisect.bisect_left(walls, left_bound)
            else:
                left_pos = bisect.bisect_left(
                    walls, robots[i] - robots_to_distance[robots[i]]
                )

            left[i] = pos1 - left_pos

            # Calculate right destruction
            if i < n - 1:
                right_bound = min(
                    robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1
                )
                right_pos = bisect.bisect_right(walls, right_bound)
            else:
                right_pos = bisect.bisect_right(
                    walls, robots[i] + robots_to_distance[robots[i]]
                )

            pos2 = bisect.bisect_left(walls, robots[i])
            right[i] = right_pos - pos2

            if i == 0:
                continue

            # Calculate total walls strictly between previous and current robot
            pos3 = bisect.bisect_left(walls, robots[i - 1])
            num[i] = pos1 - pos3

        # State machine DP
        sub_left, sub_right = left[0], right[0]
        
        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- Maximum Walls Destroyed Interactive Runner ---")
    try:
        robots_input = input("Enter the robots array (e.g., [1, 5]): ").strip()
        distance_input = input("Enter the distance array (e.g., [2, 3]): ").strip()
        walls_input = input("Enter the walls array (e.g., [0, 2, 4, 6]): ").strip()
        
        # Safely evaluate inputs
        parsed_robots = ast.literal_eval(robots_input)
        parsed_distance = ast.literal_eval(distance_input)
        parsed_walls = ast.literal_eval(walls_input)
        
        if not all(isinstance(lst, list) for lst in [parsed_robots, parsed_distance, parsed_walls]):
            raise ValueError("All inputs must be valid lists of integers.")
            
        # Calling the function
        result = solution.maxWalls(parsed_robots, parsed_distance, parsed_walls)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")