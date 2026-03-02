'''
Question: 1536. Minimum Swaps to Arrange a Binary Grid (Medium)
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

Example 1:
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

---
My Approach (Greedy / Trailing Zeros):
1. Convert the 2D grid into a 1D array called `zeros`, where `zeros[i]` represents the number of trailing zeros in the i-th row.
2. Iterate through each row index `i` from 0 to n-1. 
3. For the grid to be valid, row `i` requires at least `n - 1 - i` trailing zeros.
4. Scan the `zeros` array from index `i` downwards to find the *first* row `j` that meets or exceeds this requirement. (We want the first one to minimize adjacent swaps).
5. If no such row exists, it's impossible to make the grid valid, so return -1.
6. If we find a valid row at `j`, it will take exactly `j - i` swaps to bubble it up to position `i`. Add this to our total swaps.
7. Simulate the swap by popping the element at index `j` and inserting it at index `i`.
8. Return the total swaps.

Time Complexity: $O(N^2)$ where N is the number of rows/cols. Finding a valid row and shifting takes $O(N)$, and we do this $N$ times. Since $N \le 200$, this is extremely fast.
Space Complexity: $O(N)$ to store the 1D array of trailing zero counts.
'''

import ast
from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        
        # Step 1: Count trailing zeros for each row
        for row in grid:
            count = 0
            # Read the row backwards
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
            
        total_swaps = 0
        
        # Step 2: Greedy approach to place a valid row at each index i
        for i in range(n):
            required_zeros = n - 1 - i
            found_idx = -1
            
            # Find the closest row that has enough trailing zeros
            for j in range(i, n):
                if zeros[j] >= required_zeros:
                    found_idx = j
                    break
                    
            # If we couldn't find any valid row, it's impossible
            if found_idx == -1:
                return -1
                
            # Step 3: Add the number of adjacent swaps needed
            total_swaps += (found_idx - i)
            
            # Step 4: Simulate bubbling the row up to index i
            # Pop the row from its current position and insert it at i
            val = zeros.pop(found_idx)
            zeros.insert(i, val)
            
        return total_swaps

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1536. Min Swaps for Binary Grid Interactive Runner ---")
    try:
        grid_input = input("Enter the binary grid (e.g., [[0,0,1],[1,1,0],[1,0,0]]): ")
        
        # Safely evaluate input into a Python list of lists
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.minSwaps(parsed_grid)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")