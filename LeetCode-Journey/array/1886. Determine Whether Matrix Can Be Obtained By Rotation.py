'''
Question: 1886. Determine Whether Matrix Can Be Obtained By Rotation (Easy)
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

---
My Approach (In-Place Transpose + Reverse):
1. The most optimal way to rotate a matrix 90 degrees clockwise without using extra space is a two-step mathematical process.
2. Step 1: Transpose the matrix by swapping mat[i][j] with mat[j][i].
3. Step 2: Reverse every individual row in the matrix.
4. We check if the current matrix equals the target. If it does, we return True.
5. If not, we rotate it. Since 4 rotations (360 degrees) bring a matrix back to its original state, we only need to loop a maximum of 4 times.

Time Complexity: O(N^2) where N is the dimension of the matrix. We do a constant number of O(N^2) operations.
Space Complexity: O(1) auxiliary space because the matrix manipulation is done entirely in-place.
'''

import ast
from typing import List

class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # Step 2: Reverse rows
        for i in range(n):
            mat[i].reverse()

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check all 4 possible orientations (0, 90, 180, 270 degrees)
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
            
        return False

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1886. Matrix Rotation Interactive Runner ---")
    try:
        mat_input = input("Enter the source matrix (e.g., [[0,1],[1,1]]): ")
        target_input = input("Enter the target matrix (e.g., [[1,0],[0,1]]): ")
        
        # Safely evaluate inputs
        parsed_mat = ast.literal_eval(mat_input)
        parsed_target = ast.literal_eval(target_input)
        
        if not isinstance(parsed_mat, list) or not isinstance(parsed_target, list):
            raise ValueError("Inputs must be 2D lists of integers.")
            
        # Calling the function
        result = solution.findRotation(parsed_mat, parsed_target)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")