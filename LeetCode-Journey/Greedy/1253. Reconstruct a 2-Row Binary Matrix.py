'''
Question: 1253. Reconstruct a 2-Row Binary Matrix (Medium)
Given the following details of a matrix with n columns and 2 rows:
- The matrix is a binary matrix (elements are 0 or 1).
- The sum of elements of the 0-th (upper) row is upper.
- The sum of elements of the 1-st (lower) row is lower.
- The sum of elements in the i-th column is colsum[i].
Your task is to reconstruct the matrix with upper, lower and colsum. Return it as a 2-D integer array. If no valid solution exists, return an empty 2-D array.

Example 1:
Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

Example 2:
Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []

---
My Approach (Greedy / Two-Pass):
1. Create two arrays `row0` and `row1` initialized to 0s.
2. Pass 1 (The 2s): Iterate through `colsum`. Whenever we see a 2, we have no choice but to place a 1 in both rows. We deduct 1 from both the `upper` and `lower` remaining budgets.
3. If after Pass 1 our budgets drop below 0, we immediately return an empty array because it's impossible.
4. Pass 2 (The 1s): Iterate through `colsum` again. Whenever we see a 1, we greedily assign it to `row0` if `upper` still has budget. If not, we assign it to `row1` if `lower` has budget. If neither has budget, it's impossible.
5. Finally, verify that both `upper` and `lower` budgets have been perfectly spent down to 0. If so, return the constructed matrix.

Time Complexity: O(N) where N is the length of colsum. We traverse the array exactly twice.
Space Complexity: O(N) to construct and return the two rows.
'''

import ast
from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        row0 = [0] * n
        row1 = [0] * n
        
        # Pass 1: Handle all the 2s first because they are non-negotiable
        for i in range(n):
            if colsum[i] == 2:
                row0[i] = 1
                row1[i] = 1
                upper -= 1
                lower -= 1
                
        # If we already overspent our upper or lower budget, it's impossible
        if upper < 0 or lower < 0:
            return []
            
        # Pass 2: Greedily distribute the 1s
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    row0[i] = 1
                    upper -= 1
                elif lower > 0:
                    row1[i] = 1
                    lower -= 1
                else:
                    # We ran out of budget for both rows, impossible!
                    return []
                    
        # If we still have leftover budget that wasn't used, it's invalid
        if upper > 0 or lower > 0:
            return []
            
        return [row0, row1]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1253. Reconstruct a 2-Row Binary Matrix Interactive Runner ---")
    try:
        upper_input = input("Enter upper sum (e.g., 2): ").strip()
        lower_input = input("Enter lower sum (e.g., 1): ").strip()
        colsum_input = input("Enter colsum array (e.g., [1,1,1]): ").strip()
        
        # Safely evaluate inputs
        upper = int(upper_input)
        lower = int(lower_input)
        parsed_colsum = ast.literal_eval(colsum_input)
        
        if not isinstance(parsed_colsum, list):
            raise ValueError("colsum must be a list of integers.")
            
        # Calling the function
        result = solution.reconstructMatrix(upper, lower, parsed_colsum)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")