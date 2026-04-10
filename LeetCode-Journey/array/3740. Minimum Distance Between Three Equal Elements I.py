'''
Question: 3740. Minimum Distance Between Three Equal Elements I (Easy)
You are given an integer array nums. A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k]. 
The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i).
Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

Example 1:
Input: nums = [1,2,1,1,3]
Output: 6
Explanation: The minimum distance is achieved by the good tuple (0, 2, 3) because nums[0] == nums[2] == nums[3] == 1. 
Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

---
My Approach (Math Simplification + Hash Map Grouping):
1. The distance formula `abs(i - j) + abs(j - k) + abs(k - i)` simplifies mathematically. Since i < j < k, it evaluates to `(j - i) + (k - j) + (k - i)`. The `j`s cancel out, leaving exactly `2 * (k - i)`.
2. This means the middle element `j` has zero impact on the distance. We only care about minimizing the distance between the 1st and 3rd occurrence.
3. We use a Hash Map (defaultdict) to group the indices of every number.
4. To find the absolute minimum distance, we only need to check three consecutive occurrences in our grouped lists (`idx_list[h + 2] - idx_list[h]`).
5. Multiply the minimum found span by 2 to get the final answer.

Time Complexity: $O(N)$ where N is the length of nums. We do one linear pass to build the map, and another linear pass to check the grouped indices.
Space Complexity: $O(N)$ to store the indices in the hash map.
'''

import ast
import collections
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Group indices by their respective numbers
        indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
            
        ans = float('inf')
        
        # Check the distance for any number that appears at least 3 times
        for idx_list in indices.values():
            # We only need to check consecutive triplets to minimize the spread
            for h in range(len(idx_list) - 2):
                ans = min(ans, idx_list[h + 2] - idx_list[h])
                
        return -1 if ans == float('inf') else ans * 2

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3740. Min Distance Between Three Equal Elements I Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [1,2,1,1,3]): ").strip()
        
        # Safely evaluate inputs
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.minimumDistance(parsed_nums)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")