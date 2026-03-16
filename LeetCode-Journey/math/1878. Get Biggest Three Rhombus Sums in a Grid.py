'''
Question: 1878. Get Biggest Three Rhombus Sums in a Grid (Medium)
You are given an m x n integer matrix grid.
A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid. 
The rhombus must have the shape of a square rotated 45 degrees with each of the vertices centered on a grid cell.
Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

---
My Approach (Iterative Expansion / Matrix Traversal):
1. The grid is small (max 50x50), meaning we can check every possible rhombus without hitting a Time Limit Exceeded (TLE) error.
2. Initialize a `Set` to keep track of all distinct rhombus sums.
3. Iterate through every cell `(i, j)` in the grid. We will treat every cell as the TOP vertex of a potential rhombus.
4. For each top vertex, calculate the maximum possible side length `L` it can expand to without hitting the walls or floor of the grid.
5. If `L == 0`, the rhombus is just the single cell itself.
6. If `L > 0`, we calculate the perimeter sum by walking down-right, down-left, up-left, and up-right exactly `L` steps each, taking care not to double-count the corners.
7. Add the sum to the `Set`.
8. Finally, convert the `Set` to a list, sort it in descending order, and return the top 3 elements.

Time Complexity: O(M * N * min(M, N)^2) where M and N are the grid dimensions. With max dimensions of 50, this is roughly 1.5 million operations, which is incredibly fast.
Space Complexity: O(D) where D is the number of distinct sums stored in our set.
'''

import ast
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        distinct_sums = set()
        
        for i in range(m):
            for j in range(n):
                # Calculate the maximum possible "radius" or step size L from this top vertex
                max_L = min(j, n - 1 - j, (m - 1 - i) // 2)
                
                for L in range(max_L + 1):
                    if L == 0:
                        distinct_sums.add(grid[i][j])
                    else:
                        current_sum = 0
                        # Walk Top to Right
                        for k in range(L):
                            current_sum += grid[i + k][j + k]
                        # Walk Right to Bottom
                        for k in range(L):
                            current_sum += grid[i + L + k][j + L - k]
                        # Walk Bottom to Left
                        for k in range(L):
                            current_sum += grid[i + 2 * L - k][j - k]
                        # Walk Left to Top
                        for k in range(L):
                            current_sum += grid[i + L - k][j - L + k]
                            
                        distinct_sums.add(current_sum)
                        
        # Sort in descending order and grab up to the first 3 elements
        return sorted(list(distinct_sums), reverse=True)[:3]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1878. Biggest Three Rhombus Sums Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]): ")
        
        # Safely evaluate input into a Python list of lists
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.getBiggestThree(parsed_grid)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")