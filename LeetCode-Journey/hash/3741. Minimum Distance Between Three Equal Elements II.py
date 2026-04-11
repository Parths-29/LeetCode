'''
Question: 3741. Minimum Distance Between Three Equal Elements II (Hard)
You are given an integer array nums. A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k]. 
The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i).
Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

---
My Approach (Math Simplification + Constant State Hash Map):
1. The distance formula simplifies mathematically to `2 * (k - i)` where i and k are the first and third indices of the triplet.
2. We do NOT need to store every index of every number. To minimize `k - i`, we only ever care about the sliding window of the last 3 occurrences.
3. We use a Hash Map `pos` to track the `(latest_index, previous_index)` for each number. This avoids the Memory Limit Exceeded (MLE) trap of allocating massive arrays when `max(nums)` is huge.
4. As we sweep through the array:
   - We check if the current number has a valid `previous_index`. If so, we found 3 occurrences! We calculate the distance and update our minimum.
   - We shift the state machine: the current index `k` becomes the new `latest_index`, and the old `latest_index` becomes the new `previous_index`.

Time Complexity: O(N) where N is the length of nums. We do a single pass through the array.
Space Complexity: O(N) auxiliary space. The Hash Map only scales with the number of unique elements in the array, completely bypassing large value constraints.
'''

import ast
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Dictionary to store the (latest_index, previous_index)
        pos = {}
        ans = float('inf')
        
        for k, x in enumerate(nums):
            # Fetch the state, default to (-1, -1) if we haven't seen it
            latest, previous = pos.get(x, (-1, -1))
            
            # If we have a valid previous index, we've found our 3rd occurrence
            if previous != -1:
                ans = min(ans, (k - previous) * 2)
                
            # Shift the window forward
            pos[x] = (k, latest)
            
        return -1 if ans == float('inf') else ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3741. Min Distance Between Three Equal Elements II Interactive Runner ---")
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