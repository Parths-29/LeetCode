'''
Question: 3546. Equal Sum Grid Partition I
Given an m x n integer matrix grid, return true if you can partition the grid into two parts with equal sums by making either a single horizontal cut between two rows or a single vertical cut between two columns.

---
My Approach (1D State Compression / Prefix Sum):
1. A 2D prefix sum matrix takes O(M * N) space. Since we only make full row or full column cuts, we can compress the grid into two 1D arrays: `row_sums` and `col_sums`.
2. First, we calculate the sum of every individual row and every individual column.
3. We calculate the total sum of the grid. If the total sum is odd, it cannot be divided into two equal integer halves, so we return False immediately.
4. Our target sum for a valid cut is exactly `total_sum // 2`.
5. We sweep through our `row_sums` array. If our running prefix sum hits the target, a horizontal cut is valid.
6. We sweep through our `col_sums` array. If our running prefix sum hits the target, a vertical cut is valid.

Time Complexity: O(M * N) to iterate through the grid once to build our 1D sum arrays.
Space Complexity: O(M + N) auxiliary space to store the row and column sums, massively reducing the memory footprint compared to a full 2D prefix matrix.
'''

import ast
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Compress the 2D grid into 1D row and column sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        total_sum = sum(row_sums)
        
        # Fast fail: An odd total sum can never be split evenly
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # Check for a valid horizontal (row) cut
        current_sum = 0
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True
                
        # Check for a valid vertical (column) cut
        current_sum = 0
        for j in range(n - 1):
            current_sum += col_sums[j]
            if current_sum == target:
                return True
                
        return False

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3546. Equal Sum Grid Partition I Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[1,2,3],[3,2,1]]): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        # Calling the function
        result = solution.canPartitionGrid(parsed_grid)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")