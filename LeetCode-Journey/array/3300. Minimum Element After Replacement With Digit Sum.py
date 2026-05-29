'''
Question: 3300. Minimum Element After Replacement With Digit Sum (Easy)
You are given an integer array nums. You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.

---
My Approach (Number Theory / O(1) Math Identity):
1. The standard approach converts integers to strings or uses a while loop with modulo 10. Both carry overhead.
2. We can compute the digit sum mathematically. For any number N, the digit sum is equal to N minus 9 times the sum of its successive floor divisions by powers of 10.
   Derivation for a 3-digit number (100a + 10b + c):
   (N // 10) + (N // 100) = (10a + b) + a = 11a + b
   N - 9 * (11a + b) = 100a + 10b + c - 99a - 9b = a + b + c.
3. Because constraints guarantee nums[i] <= 10^4, we only need to unroll the floor divisions up to 10,000.
4. Using an `if` statement is slightly faster at the interpreter level than calling Python's built-in `min()` inside a tight loop.

Time Complexity: O(N) where N is the length of the array. The digit sum calculation is strictly O(1).
Space Complexity: O(1) auxiliary space.
'''

import ast
from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        
        for n in nums:
            # Mathematical extraction of digit sum
            digit_sum = n - 9 * ((n // 10) + (n // 100) + (n // 1000) + (n // 10000))
            if digit_sum < res:
                res = digit_sum
                
        return res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3300. Min Element After Digit Sum (Math Approach) ---")
    try:
        nums_input = input("Enter the nums array (e.g., [10, 12, 13, 14]): ").strip()
        
        # Safely evaluate input
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.minElement(parsed_nums)
        print(f"\nMinimum element after replacement: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")