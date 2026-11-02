'''
Question: 462. Minimum Moves to Equal Array Elements II (Medium)
Given an integer array nums of size n, return the minimum number of moves required 
to make all array elements equal by incrementing/decrementing elements by 1.

---
My Approach (Median Convergence & Pair Decoupling Identity):
1. The Mean Trap: Average minimizes squared error sum((x - k)^2), whereas absolute 
   distance sum(|x - k|) is strictly minimized by the MEDIAN.
2. The Pair Distance Identity: For any extreme pair (a, b) with a <= b, placing target 
   k inside [a, b] makes (k - a) + (b - k) == b - a (constant).
3. Nested Interval Intersection: To satisfy all outer-to-inner pairs simultaneously, 
   the optimal target k must lie in the intersection of all pairs, which is the Median.
4. C-Optimized Bitwise Pairing: After sorting, the total moves equal sum(nums[N - 1 - i] - nums[i]). 
   Using Python's bitwise NOT index `~i` (which maps 0 -> -1, 1 -> -2), we can aggregate 
   the pair costs without even explicitly calculating the median!

Time Complexity: O(N log N) using Timsort (executed in C-speed).
Space Complexity: O(1) auxiliary space (in-place sort).
'''

import ast
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Bitwise ~i maps i to -1-i (e.g., i=0 -> -1, i=1 -> -2)
        # This sums (nums[-1-i] - nums[i]) for all pairs in C-speed
        return sum(nums[~i] - nums[i] for i in range(n // 2))

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 462. Minimum Moves to Equal Array Elements II ---")
    try:
        raw_input = input("Enter nums array (e.g., [1, 10, 2, 9]): ").strip()
        nums_input = ast.literal_eval(raw_input)
        
        result = solution.minMoves2(nums_input)
        print(f"\nMinimum moves required: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")