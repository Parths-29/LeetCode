'''
Question: 3742. Maximum Path Score in a Grid
Given an m x n grid, find the maximum path score from top-left (0,0) to bottom-right (m-1, n-1).
You can only move right or down. You are allowed to pick at most `k` non-zero elements along the path.
Return the maximum score, or -1 if no valid path exists.

---
My Approach (Space-Optimized 2D DP):
1. State Definition: We want to track the maximum score at column `j` with exactly `c` non-zero elements picked.
2. Space Compression: Instead of an O(M * N * K) 3D array, we use a 2D array `dp[j][c]` because the current row only depends on the previous row (moving down) and the previous column (moving right).
3. Initialization: We accurately process `grid[0][0]` first to ensure its value and cost are tracked.
4. Transitions: For each cell, we calculate its `cost` (1 if val > 0 else 0). We then look at the valid DP states from the cell ABOVE and the cell to the LEFT, and transition to `c + cost`.

Time Complexity: $O(M \times N \times K)$ where M is rows, N is cols, and K is the constraint.
Space Complexity: $O(N \times K)$ auxiliary space, a massive improvement over O(M * N * K).
'''

import ast
from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float("-inf")
        
        # dp[j][c] represents the max score at column j with cost c
        dp = [[INF] * (k + 1) for _ in range(n)]
        
        # 1. Safely initialize the starting cell
        start_val = grid[0][0]
        start_cost = 0 if start_val == 0 else 1
        
        if start_cost <= k:
            dp[0][start_cost] = start_val
            
        # 2. Traverse the grid
        for i in range(m):
            for j in range(n):
                # Skip the very first cell as it's already initialized
                if i == 0 and j == 0:
                    continue
                
                # We build a new state array for the current cell
                new_dp = [INF] * (k + 1)
                val = grid[i][j]
                cost = 0 if val == 0 else 1
                
                # Check transitions from the LEFT (j - 1)
                if j > 0:
                    for c in range(k + 1 - cost):
                        if dp[j - 1][c] != INF:
                            new_dp[c + cost] = max(new_dp[c + cost], dp[j - 1][c] + val)
                            
                # Check transitions from ABOVE (i - 1), which is currently sitting in dp[j]
                if i > 0:
                    for c in range(k + 1 - cost):
                        if dp[j][c] != INF:
                            new_dp[c + cost] = max(new_dp[c + cost], dp[j][c] + val)
                            
                # Overwrite the current column's DP state with the newly calculated state
                dp[j] = new_dp
                
        # The answer is the maximum score we can achieve at the bottom-right cell
        ans = max(dp[n - 1])
        return -1 if ans == INF else ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3742. Maximum Path Score in a Grid Interactive Runner ---")
    try:
        grid_input = input("Enter the 2D grid array (e.g., [[0,1,0],[0,0,2]]): ").strip()
        k_input = input("Enter the maximum non-zero elements allowed (k): ").strip()
        
        # Safely evaluate inputs
        parsed_grid = ast.literal_eval(grid_input)
        parsed_k = int(k_input)
        
        if not isinstance(parsed_grid, list) or not isinstance(parsed_grid[0], list):
            raise ValueError("Input must be a valid 2D list of integers.")
            
        result = solution.maxPathScore(parsed_grid, parsed_k)
        print(f"\nMaximum Valid Path Score: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")