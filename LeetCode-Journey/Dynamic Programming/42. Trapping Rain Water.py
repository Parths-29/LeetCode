'''
Question: 42. Trapping Rain Water (Hard)
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

---
My Approach (Two Pointers / Spatial Optimization):
1. The water trapped above any block is `min(max_left, max_right) - height[i]`.
2. Instead of precomputing `max_left` and `max_right` arrays (which takes O(N) space), we use two pointers starting at the ends of the array.
3. We maintain `left_max` and `right_max` variables.
4. If `left_max < right_max`, we know the water level at the `left` pointer is bounded by `left_max`. We increment `left`, update `left_max`, and add `left_max - height[left]` to our total.
5. If `right_max <= left_max`, we do the inverse for the `right` pointer.
6. This effectively sweeps the array from the outside in, calculating water levels on the fly with zero extra memory allocations.

Time Complexity: $O(N)$ where N is the length of the elevation map. We visit every element exactly once.
Space Complexity: $O(1)$ auxiliary space, an elite optimization over the standard O(N) DP approach.
'''

import ast
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        # Sweep from the outside in
        while left < right:
            if left_max < right_max:
                left += 1
                # Update the max boundary seen so far on the left
                left_max = max(left_max, height[left])
                # Add trapped water (if height[left] is the new max, this adds 0)
                water += left_max - height[left]
            else:
                right -= 1
                # Update the max boundary seen so far on the right
                right_max = max(right_max, height[right])
                # Add trapped water
                water += right_max - height[right]

        return water

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 42. Trapping Rain Water Interactive Runner ---")
    try:
        height_input = input("Enter the elevation map (e.g., [0,1,0,2,1,0,1,3,2,1,2,1]): ").strip()
        
        # Safely evaluate input
        parsed_height = ast.literal_eval(height_input)
        
        if not isinstance(parsed_height, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.trap(parsed_height)
        print(f"\nTotal Water Trapped: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")