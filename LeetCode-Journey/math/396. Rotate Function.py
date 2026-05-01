'''
Question: 396. Rotate Function (Medium)
You are given an integer array nums of length n.
Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

---
My Approach (Mathematical Derivation / O(1) DP Transition):
1. A naive brute force simulates every rotation and calculates the sum, resulting in O(N^2) time which hits TLE.
2. We can optimize this to O(N) by finding the mathematical relationship between F(k) and F(k-1).
3. Derivation:
   F(k)   = 0*A[n-k] + 1*A[0] + 2*A[1] + ... + (n-1)*A[n-k-1]
   F(k-1) = 0*A[n-k+1] + 1*A[n-k] + ... + (n-1)*A[n-k]
   F(k) - F(k-1) = A[0] + A[1] + ... + A[n-1] - n * A[n-k]
   F(k) = F(k-1) + SUM(A) - n * A[n-k]
4. We precalculate the total sum of the array and F(0).
5. We then loop N-1 times, updating F(k) in strictly O(1) time using our derived formula, and keeping track of the maximum value seen.
6. Pythonic Optimization: We use `sum()` and a generator expression with `enumerate()` to calculate the initial values at C-level speeds.

Time Complexity: O(N) where N is the length of the array.
Space Complexity: O(1) auxiliary space.
'''

import ast
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        a_sum = sum(nums)
        
        # Calculate base case F(0) using Pythonic enumeration
        F = sum(i * val for i, val in enumerate(nums))
        res = F

        # O(1) transition for F(1) through F(n-1)
        for i in range(1, n):
            # F(k) = F(k-1) + sum - n * nums[last_element_rotated_to_front]
            F += a_sum - n * nums[-i]
            res = max(res, F)

        return res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 396. Rotate Function Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [4, 3, 2, 6]): ").strip()
        
        # Safely evaluate input
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.maxRotateFunction(parsed_nums)
        print(f"\nMaximum Rotation Value: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")