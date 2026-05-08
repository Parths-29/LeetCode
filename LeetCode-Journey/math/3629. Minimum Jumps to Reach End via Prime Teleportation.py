'''
Question: 3629. Minimum Jumps to Reach End via Prime Teleportation
You are given an integer array `nums`. You are initially positioned at index 0.
You can jump to:
- i - 1 (if i > 0)
- i + 1 (if i < n - 1)
- Any index j where nums[j] is a prime factor of nums[i].
Return the minimum number of jumps to reach the last index.

---
My Approach (Global Sieve + Reverse BFS + Edge Clearing):
1. Global Prime Factor Sieve: We precompute prime factors for all numbers up to 10^6. This is done globally so it only runs once across all test cases.
2. We map out teleportation targets: `edges` stores the indices of all prime numbers present in the array.
3. Reverse Level-Order BFS: We start at the last index and search layer by layer towards index 0.
4. Edge Clearing Optimization: The moment we use a prime number `p` to teleport, we append its indices to the queue and instantly CLEAR the list `edges[p]`. This guarantees we never evaluate the same teleportation paths twice, keeping the time complexity strictly linear!

Time Complexity: O(N) where N is the length of nums.
Space Complexity: O(N) auxiliary space for the BFS queue and seen array. (Sieve space is O(MX)).
'''

import ast
from typing import List
from collections import defaultdict

# --- Global Sieve for O(1) Prime Factor Lookups ---
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:  # i is a prime
        for j in range(i, MX, i):
            factors[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        edges = defaultdict(list)
        
        # Populate teleportation targets
        # Only map actual primes (where its only prime factor is itself)
        for i, a in enumerate(nums):
            if factors[a] == [a]:  
                edges[a].append(i)
                
        res = 0
        seen = [False] * n
        seen[-1] = True
        
        # Level-order BFS starting from the end
        q = [n - 1]
        
        while q:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                    
                # 1. Step backward
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                    
                # 2. Step forward
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                    
                # 3. Prime Teleportation
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    # O(1) Amortization: Nuke the edges so we never traverse them again!
                    edges[p].clear()
                    
            q = q2
            res += 1
            
        return -1 # Fallback if unreachable

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3629. Min Jumps via Prime Teleportation Interactive Runner ---")
    try:
        nums_input = input("Enter the nums array (e.g., [4, 2, 10, 5, 25]): ").strip()
        
        # Safely evaluate input
        parsed_nums = ast.literal_eval(nums_input)
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.minJumps(parsed_nums)
        print(f"\nMinimum jumps to reach the end: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")