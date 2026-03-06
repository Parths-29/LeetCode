'''
Question: 624. Maximum Distance in Arrays (Medium)
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:
Input: arrays = [[1],[1]]
Output: 0

---
My Approach (Greedy / Running Min-Max):
1. We only care about the first element (minimum) and last element (maximum) of each array because they are already sorted.
2. Initialize `global_min` and `global_max` using the first and last elements of the very first array `arrays[0]`.
3. Initialize `max_distance = 0`.
4. Loop through the remaining arrays starting from index 1.
5. For each array, calculate two potential maximum distances:
   - The current array's maximum minus the `global_min`.
   - The `global_max` minus the current array's minimum.
6. Update `max_distance` if either of these is larger than the current `max_distance`.
7. Finally, update the `global_min` and `global_max` using the current array's extremes to prep for the next iteration.
8. By checking the distance *before* updating the globals, we guarantee the elements are chosen from two different arrays.

Time Complexity: O(M) where M is the total number of arrays. We process each array exactly once.
Space Complexity: O(1) as we only use a few variables to track the extremes.
'''

import ast
from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate the max distance using the current array and previous extremes
            max_distance = max(
                max_distance, 
                abs(current_max - global_min), 
                abs(global_max - current_min)
            )
            
            # Update the global extremes for the next iterations
            global_min = min(global_min, current_min)
            global_max = max(global_max, current_max)
            
        return max_distance

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 624. Maximum Distance in Arrays Interactive Runner ---")
    try:
        arrays_input = input("Enter the arrays (e.g., [[1,2,3],[4,5],[1,2,3]]): ")
        
        # Safely evaluate input into a Python list of lists
        parsed_arrays = ast.literal_eval(arrays_input)
        
        if not isinstance(parsed_arrays, list) or (parsed_arrays and not isinstance(parsed_arrays[0], list)):
            raise ValueError("Input must be a 2D list (list of lists).")
            
        # Calling the function
        result = solution.maxDistance(parsed_arrays)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")