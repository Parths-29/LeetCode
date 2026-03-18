'''
Question: 757. Set Intersection Size At Least Two (Hard)
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.
A containing set is an array nums where each interval from intervals has at least two integers in nums.
Return the minimum possible size of a containing set.

Example 1:
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: Consider the set {2, 3, 4}. 
For [1, 3], the integers 2 and 3 are in the set.
For [1, 4], the integers 2, 3, and 4 are in the set.
For [2, 5], the integers 2, 3, and 4 are in the set.
For [3, 5], the integers 3 and 4 are in the set.
An intersection size of at least two is achieved, and it's the minimum possible size.

---
My Approach (Greedy + Custom Sorting):
1. Sort the intervals primarily by their end points (ascending). This allows us to process them left-to-right safely.
2. If the end points tie, sort by their start points (descending). This forces us to satisfy the most restrictive (shortest) intervals first.
3. Keep track of the two largest points we've added to our containing set so far: `p1` and `p2` (where p1 < p2). Initialize them to -1.
4. Iterate through each interval `[start, end]`:
   - Case A: `start > p2`. Neither of our tracked points are in the interval. We MUST add 2 new points. To maximize overlap with future intervals, we pick the two largest possible values: `end - 1` and `end`.
   - Case B: `start > p1`. Only `p2` is in the interval. We MUST add 1 new point. The best choice is `end`. Our new two largest points become `p2` and `end`.
   - Case C: `start <= p1`. Both points are already in the interval. We don't need to add anything!
5. Accumulate the size changes and return the total.

Time Complexity: O(N log N) where N is the number of intervals, driven entirely by the sorting step. The greedy pass is O(N).
Space Complexity: O(1) auxiliary space (or O(N) depending on Python's Timsort) as we only use a few variables.
'''

import ast
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        ans = 0
        p1 = -1
        p2 = -1
        
        for start, end in intervals:
            if start > p2:
                # Case A: We need 2 new points
                ans += 2
                p1 = end - 1
                p2 = end
            elif start > p1:
                # Case B: We need 1 new point
                ans += 1
                p1 = p2
                p2 = end
            # Case C: start <= p1, we already have 2 points inside, do nothing
                
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 757. Set Intersection Size At Least Two Interactive Runner ---")
    try:
        intervals_input = input("Enter the intervals array (e.g., [[1,3],[1,4],[2,5],[3,5]]): ")
        
        # Safely evaluate input
        parsed_intervals = ast.literal_eval(intervals_input)
        
        if not isinstance(parsed_intervals, list) or (parsed_intervals and not isinstance(parsed_intervals[0], list)):
            raise ValueError("Input must be a 2D list of intervals.")
            
        # Calling the function
        result = solution.intersectionSizeTwo(parsed_intervals)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")