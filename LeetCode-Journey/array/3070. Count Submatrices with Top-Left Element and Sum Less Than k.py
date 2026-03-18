'''
Question: 3070. Count Submatrices with Top-Left Element and Sum Less Than k (Medium)
You are given a 0-indexed integer matrix grid and an integer k.
Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

Example 1:
Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, starting from the top-left element, that have a sum less than or equal to 18.

---
My Approach (2D Prefix Sum + Early Exit):
1. A submatrix starting at the top-left (0,0) and ending at (i,j) has a sum that is exactly the 2D Prefix Sum at (i,j).
2. We can calculate this in-place by updating the grid iteratively: 
   `current_sum = original_val + sum_above + sum_left - overlap_diagonal`
3. If the calculated sum is `<= k`, we increment our valid submatrix count.
4. ELITE OPTIMIZATION: Since the problem guarantees all numbers are non-negative, the row sums monotonically increase. The moment our prefix sum exceeds `k`, we can immediately `break` out of the inner loop and jump to the next row, entirely avoiding useless calculations!

Time Complexity: O(M * N) in the absolute worst case, but significantly faster on average due to the early exit.
Space Complexity: O(1) because we mathematically modify the grid in-place without allocating any new 2D arrays.
'''

import ast
from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # Add the accumulated sum from the cell directly above
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                
                # Add the accumulated sum from the cell directly to the left
                if j > 0:
                    grid[i][j] += grid[i][j - 1]
                
                # Subtract the diagonal to remove the double-counted overlapping region
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i - 1][j - 1]
                    
                # Check our constraint
                if grid[i][j] <= k:
                    count += 1
                else:
                    # Since grid values are non-negative, extending this submatrix 
                    # further right will ONLY make it larger. Break early!
                    break
                    
        return count

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3070. Count Submatrices Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[7,6,3],[6,6,1]]): ")
        k_input = input("Enter the integer k (e.g., 18): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        parsed_k = int(k_input.strip())
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.countSubmatrices(parsed_grid, parsed_k)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")