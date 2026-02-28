'''
Question: 54. Spiral Matrix (Medium)
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

---
My Approach (Boundary Traversal):
1. Define four boundaries for the matrix: `top` (0), `bottom` (rows - 1), `left` (0), and `right` (cols - 1).
2. Set up a `while` loop that continues as long as `left <= right` and `top <= bottom`.
3. Traverse from left to right along the `top` boundary, then move the `top` boundary down by 1.
4. Traverse from top to bottom along the `right` boundary, then move the `right` boundary left by 1.
5. Check if `top <= bottom`. If so, traverse from right to left along the `bottom` boundary, then move the `bottom` boundary up by 1.
6. Check if `left <= right`. If so, traverse from bottom to top along the `left` boundary, then move the `left` boundary right by 1.
7. Repeat until the boundaries cross, meaning we've spiraled into the very center.

Time Complexity: O(M * N) where M is the number of rows and N is the number of columns. We visit each element exactly once.
Space Complexity: O(1) auxiliary space (ignoring the space used for the output array).
'''

import ast
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            # 1. Traverse from left to right across the top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Traverse from top to bottom down the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # 3. Traverse from right to left across the bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                # 4. Traverse from bottom to top up the left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 54. Spiral Matrix Interactive Runner ---")
    try:
        matrix_input = input("Enter the matrix (e.g., [[1,2,3],[4,5,6],[7,8,9]]): ")
        
        # Safely evaluate the input into a Python list of lists
        matrix = ast.literal_eval(matrix_input) 
        
        if not isinstance(matrix, list) or (matrix and not isinstance(matrix[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.spiralOrder(matrix)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")