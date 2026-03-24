'''
Question: 910. Smallest Range II (Medium)
You are given an integer array nums and an integer k.
For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.
The score of nums is the difference between the maximum and minimum elements in nums.
Return the minimum score of nums after changing the values at each index.

Example 1:
Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

Example 2:
Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

Example 3:
Input: nums = [1,3,6], k = 3
Output: 3
Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.

---
My Approach (Sorting + Greedy Partitioning):
1. Sort the array so we can cleanly separate smaller elements from larger elements.
2. Initialize the answer with the trivial case where all elements are moved in the same direction (score = nums[-1] - nums[0]).
3. Place a sliding "divider" between index 0 and N-1.
4. Assume all elements from 0 to `divider` are incremented by k (pushing smalls UP).
5. Assume all elements from `divider+1` to the end are decremented by k (pushing larges DOWN).
6. After the split, the new maximum must be either the largest incremented value `nums[divider] + k` or the largest decremented value `nums[-1] - k`.
7. The new minimum must be either the smallest incremented value `nums[0] + k` or the smallest decremented value `nums[divider+1] - k`.
8. Calculate the score for this partition and keep track of the minimum possible score.

Time Complexity: $O(N \\log N)$ driven entirely by the sorting step. The sliding window partition takes $O(N)$ time.
Space Complexity: $O(1)$ auxiliary space, assuming an in-place sort.
'''

import ast
from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Number of Elements
        N  = len(nums)
      
        # Sort so that we can have a clean partition
        nums.sort()

        # Trivial Case, all incremented OR all decremented
        score = nums[-1] - nums[0]

        # To store minimum score
        ans = score

        # Check all N-1 Non-Trivial partitions/walls. 
        # Both sets will be non-empty   
        for divider in range(0, N - 1):

            # Compute maximum and minimum after partitioning
            # Kudos! We only have two candidates for each
            maximumAfterDivision = max(nums[divider] + k, nums[-1] - k)
            minimumAfterDivision = min(nums[divider + 1] - k, nums[0] + k)

            # Score after dividing here
            score = maximumAfterDivision - minimumAfterDivision

            # ans will be minimum score
            ans = min(ans, score)
        
        # return answer
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 910. Smallest Range II Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [1,3,6]): ").strip()
        k_input = input("Enter the integer k (e.g., 3): ").strip()
        
        # Safely evaluate inputs
        parsed_nums = ast.literal_eval(nums_input)
        parsed_k = int(k_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.smallestRangeII(parsed_nums, parsed_k)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")