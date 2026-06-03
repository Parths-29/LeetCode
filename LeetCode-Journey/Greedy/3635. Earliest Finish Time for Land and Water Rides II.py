'''
Question: 3635. Earliest Finish Time for Land and Water Rides II (Medium)
You are given two categories of theme park attractions: land rides and water rides.
You must experience exactly one ride from each category, in either order.
Return the earliest possible time you can finish both rides.

---
My Approach (Greedy Decoupling / Monotonic Minimization):
1. The naive approach tries every Land ride against every Water ride, leading to an O(N * M) explosion that causes a Time Limit Exceeded (TLE) error.
2. We can optimize this by realizing a mathematical invariant: The completion time of the second ride is `max(first_finish_time, second_start_time) + second_duration`. 
3. Because this function is monotonically non-decreasing with respect to `first_finish_time`, the absolute optimal choice for the FIRST ride is ALWAYS the one that finishes the earliest, completely independent of the second ride!
4. This allows us to decouple the nested loops into two sequential O(N) passes:
   - Pass 1: Find the absolute earliest finish time of Category A.
   - Pass 2: Calculate the best completion time for Category B assuming we start at the time found in Pass 1.
5. We calculate this for both global sequences (Land -> Water AND Water -> Land) and return the minimum.

Time Complexity: O(N + M) where N and M are the number of land and water rides.
Space Complexity: O(1) auxiliary space. Python's generators and zip() evaluate without building large intermediate arrays.
'''

import ast
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        # Helper function to evaluate Category 1 -> Category 2
        def get_best_sequence(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:
            # Step 1: Find the absolute earliest finish time for the first category
            min_end_first = min(s + d for s, d in zip(start1, dur1))
            
            # Step 2: Find the optimal second ride assuming we transition at `min_end_first`
            # We start at the max of when we arrive (min_end_first) or when it opens (s)
            return min(max(min_end_first, s) + d for s, d in zip(start2, dur2))

        # Evaluate both global permutations and return the minimum
        return min(
            get_best_sequence(landStartTime, landDuration, waterStartTime, waterDuration),
            get_best_sequence(waterStartTime, waterDuration, landStartTime, landDuration)
        )

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3635. Earliest Finish Time for Land and Water Rides II ---")
    try:
        ls_input = input("Enter landStartTime array (e.g., [2,8]): ").strip()
        ld_input = input("Enter landDuration array (e.g., [4,1]): ").strip()
        ws_input = input("Enter waterStartTime array (e.g., [6]): ").strip()
        wd_input = input("Enter waterDuration array (e.g., [3]): ").strip()
        
        # Safely evaluate inputs
        parsed_ls = ast.literal_eval(ls_input)
        parsed_ld = ast.literal_eval(ld_input)
        parsed_ws = ast.literal_eval(ws_input)
        parsed_wd = ast.literal_eval(wd_input)
        
        result = solution.earliestFinishTime(parsed_ls, parsed_ld, parsed_ws, parsed_wd)
        print(f"\nEarliest finish time: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")