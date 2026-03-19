'''
Question: 3212. Count Submatrices With Equal Frequency of X and Y (Medium)
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:
1. grid[0][0]
2. an equal frequency of 'X' and 'Y'.
3. at least one 'X'.

Example 1:
Input: grid = [["X","Y","."],["Y",".","."]]
Output: 3
Explanation:
- Submatrix (0,0) to (0,1) has one 'X' and one 'Y'.
- Submatrix (0,0) to (1,0) has one 'X' and one 'Y'.
- Submatrix (0,0) to (1,2) has two 'X's and two 'Y's.

---
My Approach (1D Compressed Prefix Sums):
1. Since all valid submatrices must start at (0,0), the count of 'X's and 'Y's at any cell (i, j) is simply the sum of the current row up to j, PLUS the sum of the submatrix ending directly above it at (i-1, j).
2. We can optimize space by using two 1D arrays: `dp_x` and `dp_y` of size N. These will store the accumulated column sums as we push downwards row by row.
3. For each row, we maintain a `row_x` and `row_y` counter.
4. As we sweep left to right, we update our row counters, add them to our `dp` vertical accumulators, and instantly check if `dp_x[j] == dp_y[j]` and `dp_x[j] > 0`.
5. If the conditions are met, we increment our valid submatrix count!

Time Complexity: $O(M \\times N)$ where M is the number of rows and N is the number of columns. We process every cell exactly once.
Space Complexity: $O(N)$ because we compressed the 2D grid states into two 1D arrays of size N.
'''

import ast
from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1D arrays to track the vertical prefix sums
        dp_x = [0] * n
        dp_y = [0] * n
        
        count = 0
        
        for i in range(m):
            row_x = 0
            row_y = 0
            
            for j in range(n):
                # Update horizontal row counts
                if grid[i][j] == 'X':
                    row_x += 1
                elif grid[i][j] == 'Y':
                    row_y += 1
                    
                # Add horizontal row counts to the vertical accumulators
                dp_x[j] += row_x
                dp_y[j] += row_y
                
                # Check constraints: Equal frequency AND at least one 'X'
                if dp_x[j] > 0 and dp_x[j] == dp_y[j]:
                    count += 1
                    
        return count

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3212. Count Submatrices With Equal Frequency Interactive Runner ---")
    try:
        grid_input = input("Enter the 2D character grid (e.g., [['X','Y','.'],['Y','.','.']]): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of strings.")
            
        # Calling the function
        result = solution.numberOfSubmatrices(parsed_grid)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")