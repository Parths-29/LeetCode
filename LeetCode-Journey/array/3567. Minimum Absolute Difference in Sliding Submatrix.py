'''
Question: 3567. Minimum Absolute Difference in Sliding Submatrix (Medium)
You are given an m x n integer matrix grid and an integer k. 
For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.
Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j).
Note: If all elements in the submatrix have the same value, the answer will be 0.

Example 1:
Input: grid = [[1,8],[3,-2]], k = 2
Output: [[2]]
Explanation: 
- The only 2x2 submatrix contains [1, 8, 3, -2].
- The distinct values are [-2, 1, 3, 8].
- The minimum absolute difference is |1 - 3| = 2.

---
My Approach (Brute Force + Set + Sorting):
1. The constraints for this problem are unusually small (m, n <= 30), meaning we don't need a complex 2D data structure.
2. We initialize our result matrix `ans` with the dimensions `(m - k + 1) x (n - k + 1)`.
3. We loop over every possible top-left corner `(i, j)` of a `k x k` submatrix.
4. For each submatrix, we extract all its elements and throw them straight into a Python `set`. This automatically removes duplicates, satisfying the "distinct values" requirement.
5. If the set has 1 or fewer elements, it means all values in the submatrix were identical, so we instantly record the difference as 0.
6. Otherwise, we convert the set into a list and sort it. The minimum absolute difference is guaranteed to be between two adjacent elements.
7. We iterate through the sorted list, find the minimum difference between adjacent elements, and store it in `ans[i][j]`.

Time Complexity: O((m - k + 1) * (n - k + 1) * k^2 log(k)). Given the maximum grid size of 30x30, this evaluates to at most ~8 million operations, which Python handles effortlessly.
Space Complexity: O(k^2) auxiliary space to store the distinct elements of the current submatrix.
'''

import ast
from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # Initialize the result grid with 0s
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Extract the submatrix into a set to keep only distinct values
                distinct_vals = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        distinct_vals.add(grid[x][y])
                        
                # If all elements are the same, the diff is 0 (already set by default)
                if len(distinct_vals) > 1:
                    # Sort the distinct values
                    sorted_vals = sorted(list(distinct_vals))
                    min_diff = float('inf')
                    
                    # Find the minimum difference between adjacent elements
                    for t in range(1, len(sorted_vals)):
                        min_diff = min(min_diff, sorted_vals[t] - sorted_vals[t - 1])
                        
                    ans[i][j] = min_diff
                    
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3567. Min Abs Diff in Sliding Submatrix Interactive Runner ---")
    try:
        grid_input = input("Enter the grid (e.g., [[1,8],[3,-2]]): ")
        k_input = input("Enter the integer k (e.g., 2): ")
        
        parsed_grid = ast.literal_eval(grid_input)
        parsed_k = int(k_input.strip())
        
        if not isinstance(parsed_grid, list) or (parsed_grid and not isinstance(parsed_grid[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        result = solution.minAbsDiff(parsed_grid, parsed_k)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")