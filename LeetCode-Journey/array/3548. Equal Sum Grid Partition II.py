'''
Question: 3548. Equal Sum Grid Partition II (Hard)
You are given an m x n matrix grid of positive integers. Determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
- Each of the two resulting sections is non-empty.
- The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
- If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.

Example 1:
Input: grid = [[1,2],[3,4]]
Output: true
Explanation: A vertical cut after the first column gives sums 4 and 6. By discounting 2 from the right section, both are 4. 

---
My Approach (Prefix Sum + Hash Set + Graph Theory Insight):
1. Instead of writing massive logic blocks for cutting horizontally/vertically and removing from top/bottom/left/right, we write one clean `check()` function.
2. The `check()` function only makes horizontal cuts and only looks for an element to drop from the TOP section (`diff > 0`).
3. As we sweep row by row, we track the `top_sum` and add the row's elements to a HashSet called `seen`.
4. If `diff == 0`, we have a perfect split.
5. If `diff > 0`, we need to drop a number.
   - If the top section is >= 2 rows and > 1 column, it is 2-connected. We can drop ANY element we've seen.
   - If the top section is exactly 1 row, we can only drop the endpoints `grid[0][0]` or `grid[0][-1]`.
   - If the top section is exactly 1 column, we can only drop the endpoints `grid[0][0]` or `grid[i][0]`.
6. To check if we should drop from the bottom section, we just run `check(grid[::-1])`.
7. To check vertical cuts, we transpose the grid and run `check(transposed)` and `check(transposed[::-1])`.

Time Complexity: O(M * N) where M is rows and N is columns. We sweep the grid a constant 4 times.
Space Complexity: O(M * N) to store the transposed grids and the HashSet of seen elements.
'''

import ast
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        def check(g):
            m, n = len(g), len(g[0])
            total = sum(sum(row) for row in g)
            top_sum = 0
            seen = set()
            
            for i in range(m - 1):
                top_sum += sum(g[i])
                bot_sum = total - top_sum
                
                # Track elements we have available to drop in the top section
                for val in g[i]:
                    seen.add(val)
                    
                diff = top_sum - bot_sum
                
                # Perfect match without dropping anything
                if diff == 0:
                    return True
                    
                # We need to drop a number equal to `diff` from the top section
                if diff > 0:
                    if i > 0 and n > 1:
                        # Top section is at least 2x2. It's 2-connected!
                        # Removing ANY cell leaves it connected.
                        if diff in seen:
                            return True
                    elif i == 0:
                        # Top section is exactly 1 row. Only ends can be removed safely.
                        if diff == g[0][0] or diff == g[0][-1]:
                            return True
                    elif n == 1:
                        # Top section is exactly 1 column. Only ends can be removed safely.
                        if diff == g[0][0] or diff == g[i][0]:
                            return True
                            
            return False

        # Transpose the grid to handle vertical cuts using the exact same logic
        transposed = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
        
        # Check removing from Top, Bottom, Left, and Right
        return (check(grid) or 
                check(grid[::-1]) or 
                check(transposed) or 
                check(transposed[::-1]))

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3548. Equal Sum Grid Partition II Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[1,2],[3,4]]): ")
        
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