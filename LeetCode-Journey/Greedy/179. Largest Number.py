'''
Question: 179. Largest Number (Medium)
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

---
My Approach (Custom Sorting):
1. Convert all integers in the array to strings because we need to concatenate and compare them character by character.
2. We need a custom sorting rule. For any two numbers as strings `a` and `b`, we check which combination forms a larger concatenated string: `a + b` or `b + a`.
3. If `a + b > b + a`, then `a` must come before `b` to maximize the final number.
4. Python's `functools.cmp_to_key` allows us to translate this exact logic into a sorting key.
5. After sorting, join all the strings together.
6. Handle the edge case where the array is just multiple zeros (e.g., `[0, 0]`). If the first character of our concatenated result is "0", it means the absolute largest number we could form was a 0, so the whole answer is just "0".

Time Complexity: O(N log N) for the sorting step, where N is the length of nums.
Space Complexity: O(N) to store the string representations of the numbers.
'''

import ast
from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert numbers to strings
        nums_str = [str(n) for n in nums]
        
        # Step 2 & 3: Custom comparator
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1 # n1 should come first
            elif n1 + n2 < n2 + n1:
                return 1  # n2 should come first
            else:
                return 0  # they are equal
                
        # Step 4: Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Step 5: Join the sorted strings
        res = "".join(nums_str)
        
        # Step 6: Edge case for arrays like [0, 0]
        return "0" if res[0] == "0" else res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 179. Largest Number Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [3,30,34,5,9]): ")
        
        # Safely evaluate input into a Python list
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list.")
            
        # Calling the function
        result = solution.largestNumber(parsed_nums)
        print(f"\nOutput: '{result}'")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")