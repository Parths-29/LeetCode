'''
Question: 1509. Minimum Difference Between Largest and Smallest Value in Three Moves (Medium)
You are given an integer array nums.
In one move, you can choose one element of nums and change it to any value.
Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

Example 1:
Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

Example 2:
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change 10 to 1, 14 to 1, and 5 to 1. nums becomes [1,1,0,1,1].
The difference is 1 - 0 = 1.

---
My Approach (Greedy + Sorting):
1. If the array length is 4 or less, we can change all elements to match, so the minimum difference is always 0.
2. Otherwise, we sort the array to easily access the largest and smallest elements.
3. Changing a number to minimize the range is mathematically identical to just deleting it from the extremes.
4. Since we have 3 moves, there are exactly 4 scenarios:
   - Delete 3 smallest elements (compare nums[-1] and nums[3])
   - Delete 2 smallest, 1 largest (compare nums[-2] and nums[2])
   - Delete 1 smallest, 2 largest (compare nums[-3] and nums[1])
   - Delete 3 largest elements (compare nums[-4] and nums[0])
5. We calculate the difference for all 4 scenarios and return the absolute minimum.

Time Complexity: O(N log N) where N is the number of elements in the array, due to sorting. (Note: An absolute wizard could optimize this to O(N) by just finding the 4 largest and 4 smallest elements using a heap, but sorting is generally the cleanest and most accepted interview answer).
Space Complexity: O(1) assuming the sort is done in-place, or O(N) depending on Python's underlying Timsort implementation.
'''

import ast
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If we have 4 or fewer elements, we can make them all identical
        if len(nums) <= 4:
            return 0
            
        nums.sort()
        
        # Calculate the 4 possible windows after removing 3 elements from the extremes
        ans = min(
            nums[-1] - nums[3],   # Kill 3 smallest
            nums[-2] - nums[2],   # Kill 2 smallest, 1 largest
            nums[-3] - nums[1],   # Kill 1 smallest, 2 largest
            nums[-4] - nums[0]    # Kill 3 largest
        )
        
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1509. Min Difference in 3 Moves Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [1,5,0,10,14]): ").strip()
        
        # Safely evaluate input
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.minDifference(parsed_nums)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")