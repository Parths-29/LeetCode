'''
Question: 55. Jump Game (Medium)
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
which makes it impossible to reach the last index.

---
My Approach:
Reverse Greedy Algorithm:
1. Set the initial `goal` to the last index of the array.
2. Iterate backward through the array, starting from the second-to-last element down to the 0th element.
3. At each step, check if the current position `i` plus the maximum jump from there `nums[i]` can reach or pass the `goal`.
4. If it can, shift the `goal` to the current index `i`.
5. After the loop finishes, if the `goal` has successfully reached the 0th index, it means there is a valid path from start to finish, so return True. Otherwise, return False.

Time Complexity: O(N)
Space Complexity: O(1)
'''

import ast
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)- 2, -1,-1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 55. Jump Game Interactive Runner ---")
    try:
        # Responsive input setup 
        user_input = input("Enter the nums array (e.g., [2,3,1,1,4]): ")
        
        # Safely evaluate the string input into a Python list
        parsed_nums = ast.literal_eval(user_input) 
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list.")
            
        # Calling your function
        result = solution.canJump(parsed_nums)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Please make sure you enter a valid Python list. Details: {e}")