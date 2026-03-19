'''
Question: 63. Unique Paths II (Medium)
You are given an m x n integer array grid. There is a robot initially located at the top-left corner.
The robot tries to move to the bottom-right corner. The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

---
My Approach (1D Dynamic Programming / State Compression):
1. Instead of an M x N matrix, we initialize a 1D array `dp` of size N (the number of columns) with 0s.
2. If the starting cell itself is an obstacle, there are 0 paths. Otherwise, we seed the starting point: `dp[0] = 1`.
3. We iterate through the grid row by row.
4. For each cell, if it contains an obstacle (`1`), we mathematically block it by setting `dp[j] = 0`.
5. If it's not an obstacle, the number of ways to reach it is the sum of the ways to reach the cell above it (which is already stored in `dp[j]`) plus the cell to its left (`dp[j-1]`).
6. By the time we finish processing the final row, the last element in our 1D array will hold the total number of unique paths to the bottom-right corner!

Time Complexity: O(M * N) where M is rows and N is columns, as we process every cell exactly once.
Space Complexity: O(N) because we compressed the state into a single 1D array representing the current row.
'''

import ast
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Edge case: If the starting point is blocked, we can't go anywhere
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
            
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    # Obstacle found, absolutely no paths can go through here
                    dp[j] = 0
                elif j > 0:
                    # Current cell paths = paths from above (current dp[j]) + paths from left (dp[j-1])
                    dp[j] += dp[j - 1]
                    
        return dp[-1]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 63. Unique Paths II Interactive Runner ---")
    try:
        grid_input = input("Enter the obstacle grid (e.g., [[0,0,0],[0,1,0],[0,0,0]]): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        # Calling the function
        result = solution.uniquePathsWithObstacles(parsed_grid)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")