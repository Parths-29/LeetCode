'''
Question: 2906. Construct Product Matrix (Medium)
Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if:
- Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j].
- This product is then taken modulo 12345.
Return the product matrix of grid.

Example 1:
Input: grid = [[1,2],[3,4]]
Output: [[24,12],[8,6]]
Explanation: 
p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6

---
My Approach (Prefix and Suffix Products / O(1) Aux Space):
1. We cannot use division because of zeros and because modulo arithmetic doesn't support basic division (and 12345 is not prime, so no guaranteed modular inverse).
2. Instead, we use a two-pass approach to calculate the product of everything BEFORE a cell and everything AFTER a cell.
3. Initialize the result matrix `p` with 0s.
4. Forward Pass: Track a `prefix` product. Traverse top-to-bottom, left-to-right. Assign the current `prefix` to `p[i][j]`, then multiply `prefix` by `grid[i][j]` (modulo 12345).
5. Backward Pass: Track a `suffix` product. Traverse bottom-to-top, right-to-left. Multiply the existing `p[i][j]` by the `suffix` (modulo 12345), then multiply `suffix` by `grid[i][j]` (modulo 12345).
6. By the end of both passes, `p[i][j]` holds the exact product of all elements except itself!

Time Complexity: $O(n \times m)$ where n is rows and m is columns. We traverse the matrix exactly twice.
Space Complexity: $O(1)$ auxiliary space, as the output matrix `p` does not count towards extra space complexity in standard interview constraints.
'''

import ast
from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mod = 12345
        
        # Initialize the result matrix
        p = [[0] * n for _ in range(m)]
        
        # Forward pass: Calculate prefix products
        prefix = 1
        for i in range(m):
            for j in range(n):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % mod
                
        # Backward pass: Calculate suffix products and combine
        suffix = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % mod
                suffix = (suffix * grid[i][j]) % mod
                
        return p

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 2906. Construct Product Matrix Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[1,2],[3,4]]): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        # Calling the function
        result = solution.constructProductMatrix(parsed_grid)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")