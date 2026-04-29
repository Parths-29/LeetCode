'''
Question: 3225. Maximum Score From Grid Operations (Hard)
You are given a 2D matrix grid of size n x n. Initially, all cells are white. You may perform the following operation any number of times:
- Choose any cell (i, j) and color it black.
- If you color a cell black, all cells above it in the same column must also be colored black.
Your score is the sum of the values of all white cells that share at least one edge with a black cell.
Return the maximum score you can achieve.

---
My Approach (3D Dynamic Programming + Suffix/Prefix State Optimization):
1. State Definition: We iterate column by column. The score depends on the number of black cells (height) in the current column `curr_h` and the previous column `prev_h`.
2. Prefix Sums: We precompute `col_sum` to instantly calculate the score of white cells covered by adjacent taller black columns.
3. Overlapping Subproblems: To avoid double counting and missing scores, we must consider the height of column `i-2`. A naive approach takes $O(N^4)$.
4. $O(N^3)$ Optimization: We maintain `prev_max` and `prev_suffix_max` matrices. Instead of iterating through all possible heights of column `i-2` for every state, we pre-calculate the maximum possible scores at the end of each column `i`. This drops the transition lookup to $O(1)$.
5. Transition Logic:
   - If `curr_h <= prev_h`: The previous column extends further down, scoring the white cells in the current column.
   - If `curr_h > prev_h`: The current column extends further down, scoring the white cells in the previous column.

Time Complexity: $O(N^3)$ where N is the grid size.
Space Complexity: $O(N^3)$ to store the DP table, plus $O(N^2)$ for prefix arrays.
'''

import ast
from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

        # dp[i][curr_h][prev_h]
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        
        # O(1) Lookup tables to replace the O(N) loop for column i-2
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]
        
        # col_sum[c][r] stores the sum of the first r elements in column c
        col_sum = [[0] * (n + 1) for _ in range(n)]

        # Precompute vertical prefix sums
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        for i in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    
                    if curr_h <= prev_h:
                        # Previous column is taller; scores white cells in the current column
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score,
                        )
                    else:
                        # Current column is taller; scores white cells in the previous column
                        extra_score = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][curr_h],
                            prev_max[prev_h][curr_h] + extra_score,
                        )

            # Update our O(1) lookup matrices for the next column's transitions
            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[i][curr_h][0]
                for prev_h in range(1, n + 1):
                    # Penalty for overlapping coverage avoiding double-counting
                    penalty = (col_sum[i][prev_h] - col_sum[i][curr_h] if prev_h > curr_h else 0)
                    
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        dp[i][curr_h][prev_h] - penalty,
                    )

                prev_suffix_max[curr_h][n] = dp[i][curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        dp[i][curr_h][prev_h],
                    )

        # The maximum score could end with any height configuration in the final column
        ans = 0
        for k in range(n + 1):
            ans = max(ans, dp[n - 1][n][k], dp[n - 1][0][k])

        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3225. Maximum Score From Grid Operations Interactive Runner ---")
    try:
        grid_input = input("Enter the 2D grid array (e.g., [[0,0,0],[0,0,0],[0,0,0]]): ").strip()
        
        # Safely evaluate input
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or not isinstance(parsed_grid[0], list):
            raise ValueError("Input must be a valid 2D list of integers.")
            
        result = solution.maximumScore(parsed_grid)
        print(f"\nMaximum Possible Score: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")