'''
Question: 1727. Largest Submatrix With Rearrangements (Medium)
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

Example 1:
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns to [[1,0,0],[1,1,1],[1,1,0]]. The largest submatrix of 1s has an area of 4.

Example 2:
Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns to align the 1s to get an area of 3.

---
My Approach (Histogram + Greedy Sorting):
1. Treat each column like a histogram. We iterate through the matrix row by row starting from index 1.
2. If a cell contains a 1, we add the height of the consecutive 1s from the row above it: `matrix[i][j] += matrix[i-1][j]`. If it's 0, the height resets to 0.
3. After updating the matrix, the numbers represent the height of solid 1s ending at that exact row.
4. Since we are allowed to rearrange columns in any order, we maximize the area for the current row by simply sorting its heights in descending order.
5. Once sorted, for each column `j`, the height is `row[j]`, and the width of the submatrix we can form with at least this height is `j + 1`. 
6. The area is `height * width`. We calculate this for every column and keep track of the absolute maximum area.

Time Complexity: $O(M \\times N \\log N)$ where M is the number of rows and N is the number of columns. Calculating the heights is $O(M \\times N)$, and sorting each of the M rows takes $O(N \\log N)$.
Space Complexity: $O(N)$ to store a copy of the row for sorting (Python's `sorted()` creates a new list), keeping our logic clean without destroying the original height accumulations completely.
'''

import ast
from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0

        # Step 1: Calculate consecutive heights column by column
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # Step 2: Sort each row and calculate the max area
        for i in range(m):
            # Sort the heights in descending order to group the tallest columns
            sorted_row = sorted(matrix[i], reverse=True)
            
            # Calculate the max area that can be formed using this row as the base
            for j in range(n):
                height = sorted_row[j]
                width = j + 1
                max_area = max(max_area, height * width)

        return max_area

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1727. Largest Submatrix With Rearrangements Interactive Runner ---")
    try:
        matrix_input = input("Enter the binary matrix (e.g., [[0,0,1],[1,1,1],[1,0,1]]): ")
        
        # Safely evaluate input into a Python list of lists
        parsed_matrix = ast.literal_eval(matrix_input)
        
        if not isinstance(parsed_matrix, list) or (parsed_matrix and not isinstance(parsed_matrix[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.largestSubmatrix(parsed_matrix)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")