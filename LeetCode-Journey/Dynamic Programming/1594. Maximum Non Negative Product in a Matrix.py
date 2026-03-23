'''
Question: 1594. Maximum Non Negative Product in a Matrix (Medium)
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down.
Find the path with the maximum non-negative product.
Return the maximum non-negative product modulo 10^9 + 7. If the maximum product is negative, return -1.

Example 1:
Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:
Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is 1 * 1 * -2 * -4 * 1 = 8.

---
My Approach (1D Dynamic Programming / State Compression):
1. To handle negative numbers multiplying to become large positives, we must track BOTH the maximum and minimum products at every step.
2. Instead of building two full M x N matrices, we compress the state into two 1D arrays of size N: `max_dp` and `min_dp`.
3. We pre-fill the first row since it can only be reached by moving strictly right.
4. As we iterate row by row:
   - We first update the 0th index (which can only be reached by moving strictly down).
   - For the rest of the row, `max_dp[j]` represents the value from ABOVE, and `max_dp[j-1]` represents the value from the LEFT.
5. If the current cell is >= 0, the new max comes from the previous max.
6. If the current cell is < 0, the new max comes from the previous MIN (negative * negative = positive).
7. Finally, check if the bottom-right value is negative. If not, modulo 10^9 + 7 and return.

Time Complexity: O(M * N) where M is rows and N is columns.
Space Complexity: O(N) because we compressed the state into two 1D arrays.
'''

import ast
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        
        # Using 1D arrays to track the current row's min and max products
        max_dp = [0] * n
        min_dp = [0] * n
        
        # Initialize the top-left cell
        max_dp[0] = min_dp[0] = grid[0][0]
        
        # Pre-fill the first row (can only arrive from the left)
        for j in range(1, n):
            max_dp[j] = min_dp[j] = max_dp[j-1] * grid[0][j]
            
        for i in range(1, m):
            # Update the first column (can only arrive from directly above)
            max_dp[0] = min_dp[0] = max_dp[0] * grid[i][0]
            
            for j in range(1, n):
                curr = grid[i][j]
                
                # Before overwriting, max_dp[j] is the value from ABOVE
                # max_dp[j-1] is the value from the LEFT (already updated for this row)
                best_prev_max = max(max_dp[j-1], max_dp[j])
                worst_prev_min = min(min_dp[j-1], min_dp[j])
                
                if curr >= 0:
                    max_dp[j] = best_prev_max * curr
                    min_dp[j] = worst_prev_min * curr
                else:
                    # A negative current number perfectly flips our min and max bounds!
                    max_dp[j] = worst_prev_min * curr
                    min_dp[j] = best_prev_max * curr
                    
        ans = max_dp[-1]
        return ans % mod if ans >= 0 else -1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1594. Maximum Non Negative Product Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[1,-2,1],[1,-2,1],[3,-4,1]]): ")
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        # Calling the function
        result = solution.maxProductPath(parsed_grid)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")