'''
Question: 221. Maximal Square (Medium)
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

---
My Approach (1D Dynamic Programming / State Compression):
1. The classic 2D DP approach requires O(M * N) space. However, since the DP state only depends on the current cell's left, top, and top-left diagonal neighbors, we can compress this into a single 1D array of size N + 1.
2. `dp[c+1]` will represent the value from the row directly ABOVE.
3. `dp[c]` will represent the value directly to the LEFT.
4. We use a variable `prev` to store the TOP-LEFT diagonal value before `dp[c+1]` is overwritten for the next column.
5. If the current matrix cell is '1', we calculate the new square side length and update our `max_side`.
6. CRITICAL: If the current matrix cell is '0', we MUST reset `dp[c+1] = 0` because we are reusing the same 1D array for every row!
7. Return `max_side * max_side` to get the area.

Time Complexity: $O(M \times N)$ where M is rows and N is columns. We visit every cell exactly once.
Space Complexity: $O(N)$ auxiliary space because we compressed the state into a single 1D array representing the columns.
'''

import ast
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 1D array to store the state of the current row
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0 # This will hold the top-left diagonal value (dp[r][c])
        
        for r in range(rows):
            for c in range(cols):
                # Save the current value of dp[c+1] before we overwrite it.
                # It will become the top-left diagonal 'prev' for the NEXT cell.
                temp = dp[c + 1] 
                
                if matrix[r][c] == '1':
                    dp[c + 1] = min(dp[c], dp[c + 1], prev) + 1
                    max_side = max(max_side, dp[c + 1])
                else:
                    # We must explicitly reset to 0 because we are reusing the array
                    dp[c + 1] = 0 
                    
                # Pass the old top value forward to act as the diagonal for the next column
                prev = temp 
                
        return max_side * max_side

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 221. Maximal Square Interactive Runner ---")
    try:
        matrix_input = input("Enter the binary matrix (e.g., [['1','0','1'],['1','1','1'],['1','1','1']]): ")
        
        # Safely evaluate inputs
        parsed_matrix = ast.literal_eval(matrix_input)
        
        if not isinstance(parsed_matrix, list) or (parsed_matrix and not isinstance(parsed_matrix[0], list)):
            raise ValueError("Input must be a 2D list of strings.")
            
        # Calling the function
        result = solution.maximalSquare(parsed_matrix)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")