'''
Question: 59. Spiral Matrix II (Medium)
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

---
My Approach (Boundary Traversal):
1. Initialize an n x n matrix filled with zeros using list comprehension.
2. Define the four boundaries: `top` (0), `bottom` (n - 1), `left` (0), and `right` (n - 1).
3. Use a counter variable `val` starting at 1. The goal is to fill up to `n * n`.
4. Traverse the matrix in a spiral pattern using a while loop (`while val <= n * n`):
   - Left to right across the `top` row, then increment `top`.
   - Top to bottom down the `right` column, then decrement `right`.
   - Right to left across the `bottom` row, then decrement `bottom`.
   - Bottom to top up the `left` column, then increment `left`.
5. At each cell we visit, we place `val` into it and then increment `val`.
6. Return the completed matrix.

Time Complexity: O(N^2) where N is the input integer, because we fill exactly N*N elements.
Space Complexity: O(N^2) to store the result matrix (or O(1) auxiliary space if you don't count the output array).
'''

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create an n x n matrix filled with zeros
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        val = 1
        
        # Loop until we've placed all numbers from 1 to n^2
        while val <= n * n:
            # 1. Traverse from left to right across the top row
            for i in range(left, right + 1):
                matrix[top][i] = val
                val += 1
            top += 1
            
            # 2. Traverse from top to bottom down the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = val
                val += 1
            right -= 1
            
            # 3. Traverse from right to left across the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = val
                val += 1
            bottom -= 1
            
            # 4. Traverse from bottom to top up the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = val
                val += 1
            left += 1
            
        return matrix

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 59. Spiral Matrix II Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 3): ")
        n = int(n_input)
        
        # Calling the function
        result = solution.generateMatrix(n)
        
        # Printing the matrix beautifully row by row
        print("\nOutput Matrix:")
        for row in result:
            print(row)
            
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")