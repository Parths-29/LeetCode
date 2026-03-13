'''
Question: 3296. Minimum Number of Seconds to Make Mountain Height Zero (Medium)
You are given an integer mountainHeight denoting the height of a mountain.
You are also given an integer array workerTimes representing the base times of workers.
The i-th worker takes workerTimes[i] * x seconds to reduce the x-th unit of height.
Return the minimum number of seconds required to reduce the mountain height to zero.

---
My Approach (Binary Search on Answer + Quadratic Math Formula):
1. We are looking for the minimum time, so we Binary Search over the possible total seconds. 
2. `lo` starts at 1, and `hi` is set to a massive upper bound (10^16) to ensure we cover the worst-case scenario.
3. For a given time `mid`, we calculate how much total height all workers can reduce.
4. Instead of simulating the work, we use the quadratic formula to calculate exactly how many units `k` a single worker with base time `t` can reduce in `mid` seconds:
   k = floor(sqrt(2 * mid / t + 0.25) - 0.5)
5. We sum up `k` for all workers. If the total reduced height is greater than or equal to `height`, this `mid` time is valid! We shrink the upper bound (`hi = mid`) to see if we can do it even faster.
6. If the total height reduced is less than `height`, we need more time, so we increase the lower bound (`lo = mid + 1`).
7. The loop terminates when `lo == hi`, which will be our minimum required time.

Time Complexity: O(N log(MAX_TIME)) where N is the number of workers.
Space Complexity: O(1) auxiliary space.
'''

import ast
import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, height: int, times: List[int]) -> int:
        lo, hi = 1, 10**16

        while lo < hi:
            mid = (lo + hi) >> 1
            tot = 0
            for t in times:
                # O(1) math optimization to find max units reduced by this worker
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                # Early exit if we already reached the required height
                if tot >= height: 
                    break
                    
            if tot >= height:
                hi = mid
            else:
                lo = mid + 1

        return lo

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3296. Min Seconds to Make Mountain Height Zero Interactive Runner ---")
    try:
        height_input = input("Enter the mountain height (e.g., 4): ")
        times_input = input("Enter the worker times array (e.g., [2,1,1]): ")
        
        # Safely evaluate inputs
        height = int(height_input)
        parsed_times = ast.literal_eval(times_input)
        
        if not isinstance(parsed_times, list):
            raise ValueError("Times input must be a list.")
            
        # Calling the function
        result = solution.minNumberOfSeconds(height, parsed_times)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")