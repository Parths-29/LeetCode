'''
Question: 1855. Maximum Distance Between a Pair of Values (Medium)
You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if i <= j and nums1[i] <= nums2[j].
The distance of the pair is j - i.
Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

Example 1:
Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

---
My Approach (Monotonic Sliding Window / Two Pointers):
1. Because both arrays are strictly non-increasing, we can use a two-pointer sliding window.
2. We want to maximize the distance `j - i`. Therefore, we track an implicitly growing window.
3. Pointer `j` moves forward unconditionally on every single iteration to explore larger distances.
4. If `A[i] > B[j]`, the current value in A is too large for B, meaning this distance is invalid. To fix this without shrinking our max-distance window, we shift the entire window to the right by incrementing `i` as well.
5. Elite Python Optimization: `i += A[i] > B[j]` uses boolean-to-integer conversion. If True, it adds 1. If False, it adds 0. This avoids `if` statements and branch prediction overhead.
6. The window size `j - i` only ever grows or stays the same. The final calculation `j - i - 1` perfectly captures the maximum distance.

Time Complexity: O(N + M) where N is the length of A and M is the length of B. Both pointers only traverse forward.
Space Complexity: O(1) auxiliary space.
'''

import ast
from typing import List

class Solution:
    def maxDistance(self, A: List[int], B: List[int]) -> int:
        i, j = 0, 1

        # The implicit window size is (j - i). It never shrinks.
        while i < len(A) and j < len(B):
            # If A[i] > B[j], the pair is invalid, so we must shift 'i' forward
            i += A[i] > B[j]
            # 'j' always moves forward, attempting to expand the window
            j += 1

        # Calculate the final maximum window size
        return j - i - 1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1855. Max Distance Between Pair of Values Interactive Runner ---")
    try:
        a_input = input("Enter array A (e.g., [55,30,5,4,2]): ").strip()
        b_input = input("Enter array B (e.g., [100,20,10,10,5]): ").strip()
        
        # Safely evaluate inputs
        parsed_A = ast.literal_eval(a_input)
        parsed_B = ast.literal_eval(b_input)
        
        if not isinstance(parsed_A, list) or not isinstance(parsed_B, list):
            raise ValueError("Inputs must be valid lists of integers.")
            
        result = solution.maxDistance(parsed_A, parsed_B)
        print(f"\nMaximum Distance: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")