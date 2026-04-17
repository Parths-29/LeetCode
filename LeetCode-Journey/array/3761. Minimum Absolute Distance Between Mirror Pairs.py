'''
Question: Minimum Mirror Pair Distance
Given an integer array nums, find the minimum distance between two indices i and j (where i != j) 
such that nums[j] is the exact reversed integer of nums[i].
Return the minimum distance. If no such pair exists, return -1.

---
My Approach (Single-Pass Hash Map / "Two Sum" Paradigm):
1. A brute-force nested loop to check every pair takes $O(N^2)$ time and will hit TLE on large arrays.
2. We optimize this to $O(N)$ using a Hash Map (`mpp`).
3. As we iterate through the array, we check if the current number exists in our map. If it does, we found a match to a previously stored "reversed target" and calculate the distance `i - mpp[nums[i]]`.
4. We then reverse the CURRENT number and store it in the map with its index `i`. This acts as a target for future numbers.
5. If the reversed number is already in the map, overwriting it with the current index `i` is strictly optimal because we are looking for the *minimum* distance, so we always want the most recent index.
6. We use Python's native string slicing `[::-1]` to handle integer reversal safely and efficiently.

Time Complexity: $O(N)$ where N is the length of the array. We visit each element exactly once.
Space Complexity: $O(N)$ auxiliary space to store the target numbers in the hash map.
'''

import ast
from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mpp = {}
        ans = float('inf')

        for i, num in enumerate(nums):
            # If the current number is a match for a previously expected reversed number
            if num in mpp:
                ans = min(ans, i - mpp[num])

            # Pythonic integer reversal: Handle negative numbers safely if they exist, 
            # though standard array problems usually use absolute values.
            # Convert to string, reverse the string, convert back to int.
            rev_num = int(str(abs(num))[::-1]) 
            if num < 0:
                rev_num *= -1

            # Store the expectation for future numbers. 
            # Overwriting is optimal to keep the most recent (closest) index.
            mpp[rev_num] = i

        return -1 if ans == float('inf') else ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- Minimum Mirror Pair Distance Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [12, 34, 21, 43, 12]): ").strip()
        
        # Safely evaluate input
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a valid list of integers.")
            
        # Calling the function
        result = solution.minMirrorPairDistance(parsed_nums)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")