'''
Question: 324. Wiggle Sort II (Medium)
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

Example 1:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

Example 2:
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]

---
My Approach (Sorting & Interleaving):
1. Sort the input array `nums`.
2. Find the middle point of the array to conceptually split it into a "smaller" half and a "larger" half.
3. To ensure that duplicate numbers (specifically the median) don't end up adjacent to each other, we must place elements from the *end* of both halves.
4. Place the elements from the back of the "larger" half into the odd indices (1, 3, 5...). These are our peaks.
5. Place the elements from the back of the "smaller" half into the even indices (0, 2, 4...). These are our valleys.
6. Using Python's slice assignment `nums[::2]` and `nums[1::2]`, we can do this interleaving instantly.

Time Complexity: O(N log N) due to the sorting step.
Space Complexity: O(N) because Python's sorting and slicing creates copies under the hood.
'''

import ast
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the array
        nums.sort()
        
        # Find the middle index
        mid = (len(nums) - 1) // 2
        
        # Interleave the reversed halves into the even and odd indices
        # nums[::2] captures even indices: 0, 2, 4...
        # nums[1::2] captures odd indices: 1, 3, 5...
        nums[::2] = nums[mid::-1]
        nums[1::2] = nums[:mid:-1]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 324. Wiggle Sort II Interactive Runner ---")
    try:
        user_input = input("Enter the nums array (e.g., [1,5,1,1,6,4]): ")
        parsed_nums = ast.literal_eval(user_input) 
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list.")
            
        # Calling the function (it modifies the list in-place and returns None)
        solution.wiggleSort(parsed_nums)
        
        # Print the modified list
        print(f"\nOutput: {parsed_nums}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")