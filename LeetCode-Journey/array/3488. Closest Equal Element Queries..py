'''
Question: 3488. Closest Equal Element Queries (Medium)
Given an integer array nums and an array of queries, where each query represents an index in nums.
For each query, find the minimum distance to another index j such that nums[query] == nums[j].
The array is considered circular, meaning the distance between index 0 and index n-1 is 1.
If no other equal element exists, return -1.

---
My Approach (Hash Map Indexing + Binary Search + Circular Math):
1. Precompute a Hash Map where the keys are the numbers in the array, and the values are lists of indices where that number occurs.
2. Because we iterate from 0 to n-1, these index lists are naturally sorted.
3. For each query `q`, we fetch the list of indices `v` for `nums[q]`.
4. Fast Fail: If `len(v) == 1`, the element is unique, so return -1.
5. We use `bisect_left` to find exactly where our query index `q` is positioned inside the list `v` in O(log K) time.
6. The closest identical elements MUST be our immediate left and right neighbors in the list `v`.
7. We use modulo arithmetic `(pos - 1) % len(v)` to safely wrap around the index list.
8. We use `min(d, n - d)` to calculate the true circular distance in the main array.

Time Complexity: $O(N + Q \log K)$ where N is the size of nums, Q is the number of queries, and K is the maximum occurrences of a single element.
Space Complexity: $O(N)$ auxiliary space to store the hash map of indices.
'''

import ast
from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        mp = defaultdict(list)

        # Precompute the sorted indices for each value
        for i in range(n):
            mp[nums[i]].append(i)

        ans = []

        for q in queries:
            v = mp[nums[q]]

            # If the number only appears once, there is no equal element
            if len(v) == 1:
                ans.append(-1)
                continue

            # Binary search to find our query's position in the grouped list
            pos = bisect_left(v, q)

            # Find the actual indices of the left and right identical neighbors
            left_neighbor_idx = v[(pos - 1) % len(v)]
            right_neighbor_idx = v[(pos + 1) % len(v)]

            # Calculate absolute linear distances
            d1 = abs(q - left_neighbor_idx)
            d2 = abs(q - right_neighbor_idx)

            # Find the absolute minimum circular distance
            res = min(d1, n - d1, d2, n - d2)
            
            ans.append(res)

        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3488. Closest Equal Element Queries Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [1,2,1,3,1]): ").strip()
        queries_input = input("Enter the queries array (e.g., [0, 2, 4]): ").strip()
        
        # Safely evaluate inputs
        parsed_nums = ast.literal_eval(nums_input)
        parsed_queries = ast.literal_eval(queries_input)
        
        if not isinstance(parsed_nums, list) or not isinstance(parsed_queries, list):
            raise ValueError("Inputs must be valid lists of integers.")
            
        result = solution.solveQueries(parsed_nums, parsed_queries)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")