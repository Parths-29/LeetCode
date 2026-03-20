'''
Question: 64. Minimum Path Sum (Medium)
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

---
My Approach (Dynamic Programming / In-Place Modification):
1. Instead of creating a separate DP table, we modify the original grid to store the minimum path sum to reach each cell.
2. The top-left cell remains the same.
3. We pre-calculate the first row (can only be reached from the left) by accumulating the sums horizontally.
4. We pre-calculate the first column (can only be reached from above) by accumulating the sums vertically.
5. For all remaining cells, the minimum path sum to reach `grid[i][j]` is its current value PLUS the minimum of the cell directly above it or directly to its left.
6. The bottom-right cell will contain the final minimum path sum.

Time Complexity: O(M * N) where M is rows and N is columns. We visit every cell exactly once.
Space Complexity: O(1) auxiliary space, because we mathematically overwrite the provided grid in-place.
'''

import ast
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Accumulate the first row (can only come from the left)
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            
        # Accumulate the first column (can only come from above)
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        # Calculate the minimum path sum for the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        # The bottom-right cell holds the answer
        return grid[-1][-1]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 64. Minimum Path Sum Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[1,3,1],[1,5,1],[4,2,1]]): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        # Calling the function
        result = solution.minPathSum(parsed_grid)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")