'''
Question: 1582. Special Positions in a Binary Matrix (Easy)
Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

---
My Approach (Precomputing Row and Column Sums):
1. Create two arrays: `row_sums` and `col_sums` to store the sum of elements for each row and each column.
2. Iterate through the matrix once to populate these sum arrays. Because the matrix is binary, a sum of 1 means there is exactly one '1' in that row or column.
3. Iterate through the matrix a second time.
4. If the current element `mat[i][j]` is 1, check if `row_sums[i] == 1` and `col_sums[j] == 1`.
5. If both conditions are met, it's a special position! Increment our counter.
6. Return the total count.

Time Complexity: $O(M \times N)$ where M is the number of rows and N is the number of columns. We traverse the matrix twice.
Space Complexity: $O(M + N)$ to store the precomputed sums for the rows and columns.
'''

import ast
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Precompute the sum of each row
        row_sums = [sum(row) for row in mat]
        
        # Precompute the sum of each column
        col_sums = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        special_count = 0
        
        # Check for special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
                    
        return special_count

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1582. Special Positions in a Binary Matrix Interactive Runner ---")
    try:
        mat_input = input("Enter the binary matrix (e.g., [[1,0,0],[0,1,0],[0,0,1]]): ")
        
        # Safely evaluate input into a Python list of lists
        parsed_mat = ast.literal_eval(mat_input)
        
        if not isinstance(parsed_mat, list) or (parsed_mat and not isinstance(parsed_mat[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.numSpecial(parsed_mat)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")