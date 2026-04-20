'''
Question: 2078. Two Furthest Houses With Different Colors (Easy)
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.
Return the maximum distance between two houses with different colors.

Example 1:
Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance is abs(0 - 3) = 3.

---
My Approach (Dual-Anchor Greedy Sweep):
1. A brute-force nested loop takes O(N^2) time. We can do this in O(N).
2. The Mathematical Invariant: The maximum distance MUST involve either the very first house (index 0) or the very last house (index n-1). 
3. Why? If the optimal pair was somewhere in the middle, extending that distance to either the start or the end would yield an even greater distance unless the colors match.
4. We iterate `i` from 0 to n-1. Here, `i` acts as a "shrink factor" from the absolute maximum distance.
5. In each step, we check:
   - Does the house `i` steps from the left differ from the last house?
   - OR does the house `i` steps from the right differ from the first house?
6. Because we iterate `i` starting from 0, the very first match we find is guaranteed to be the absolute maximum possible distance.

Time Complexity: $O(N)$ where N is the length of the array. In the worst case, we sweep half the array.
Space Complexity: $O(1)$ auxiliary space.
'''

import ast
from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        # i represents how much we are shrinking the max distance by
        for i in range(n):
            # Check left-anchor vs right-moving OR right-anchor vs left-moving
            # We use 'or' to allow short-circuiting for maximum speed
            if colors[i] != colors[-1] or colors[-1 - i] != colors[0]:
                return n - 1 - i

        return 0

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2078. Two Furthest Houses Interactive Runner ---")
    try:
        colors_input = input("Enter the colors array (e.g., [1,1,1,6,1,1,1]): ").strip()
        
        # Safely evaluate input
        parsed_colors = ast.literal_eval(colors_input)
        
        if not isinstance(parsed_colors, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.maxDistance(parsed_colors)
        print(f"\nMaximum Distance: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")