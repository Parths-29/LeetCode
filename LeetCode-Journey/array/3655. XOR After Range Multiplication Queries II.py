'''
Question: 3655. XOR After Range Multiplication Queries II (Hard)
You are given an integer array nums and a 2D array queries where queries[i] = [l, r, k, v].
For each query, multiply nums[j] by v modulo 10^9 + 7 for all j = l + c * k (where c >= 0 and j <= r).
Return the XOR sum of all elements in the array after processing all queries.

---
My Approach (Square Root Decomposition + Multiplicative Difference Array):
1. A naive simulation will result in TLE for queries with a very small step size `k`.
2. We use Square Root Decomposition, setting a threshold limit at `isqrt(n)`.
3. Heavy Queries (k >= limit): Brute force the multiplication. Because `k` is large, the inner loop runs at most `sqrt(n)` times, ensuring it stays well within the time limits.
4. Light Queries (k < limit): Group these queries by their step size `k`. We use a Multiplicative Difference Array to process them.
   - We multiply `diff[l]` by `v`.
   - To "stop" the multiplication after the range ends, we multiply the next step index `diff[nxt]` by the Modular Multiplicative Inverse of `v` using `pow(v, -1, MOD)`.
5. We then sweep through the array, propagating the `diff` multipliers forward by `k` steps and applying them to the `nums` array.
6. Finally, we calculate and return the XOR sum of the updated `nums` array.

Time Complexity: $O((N + Q) \sqrt{N})$ where N is the length of nums and Q is the number of queries. 
Space Complexity: $O(N + Q)$ auxiliary space to store the grouped queries and the difference array.
'''

import ast
import math
from typing import List
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        limit = math.isqrt(n)
        
        # Group queries with small k for later processing
        lightK = defaultdict(list)
        
        for q in queries:
            l, r, k, v = q
            if k >= limit:
                # Large k: apply brute force (runs at most sqrt(N) times per query)
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                # Small k: process later using difference array
                lightK[k].append(q)
                
        for k, query_list in lightK.items():
            # Process small queries grouped by step size k
            diff = [1] * n
            for q in query_list:
                l, r, _, v = q
                
                # Multiply starting position
                diff[l] = (diff[l] * v) % MOD
                
                # Cancel the multiplication using modular inverse
                steps = (r - l) // k
                nxt = l + (steps + 1) * k
                
                if nxt < n:
                    # pow(v, -1, MOD) computes the modular inverse natively in Python 3.8+
                    diff[nxt] = (diff[nxt] * pow(v, -1, MOD)) % MOD
                    
            # Propagate the multipliers with a step size of k
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                nums[i] = (nums[i] * diff[i]) % MOD
                
        # Calculate final XOR sum
        ans = 0
        for num in nums:
            ans ^= num
            
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3655. XOR After Range Multiplication Queries II Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [1, 2, 3]): ").strip()
        queries_input = input("Enter the queries array (e.g., [[0, 2, 1, 2]]): ").strip()
        
        # Safely evaluate inputs
        parsed_nums = ast.literal_eval(nums_input)
        parsed_queries = ast.literal_eval(queries_input)
        
        if not isinstance(parsed_nums, list) or not isinstance(parsed_queries, list):
            raise ValueError("Inputs must be valid lists.")
            
        # Calling the function
        result = solution.xorAfterQueries(parsed_nums, parsed_queries)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")