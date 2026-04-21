'''
Question: 1722. Minimize Hamming Distance After Swap Operations (Medium)
You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source.
Return the minimum Hamming distance of source and target after performing any number of swap operations on array source.

---
My Approach (Disjoint Set Union / Graph Components):
1. If we can swap index A with B, and B with C, we can effectively place any element from {A, B, C} into any position within {A, B, C}. These form a "Connected Component".
2. We use a Disjoint Set Union (DSU) / Union-Find data structure to group all connected indices based on `allowedSwaps`.
3. We use path compression in our `find` function to ensure operations run in near O(1) time.
4. Pythonic Optimization: We map each component's root to a `Counter` dictionary. We do a single pass through `source`, instantly tallying the frequencies of elements available within each connected component.
5. Finally, we iterate through `target`. For each index, we look at its component root. If the target value exists in our component's pool, we use it (decrement). If it doesn't, it's a mismatch, and we increment the Hamming distance.

Time Complexity: $O(N \log N)$ or near $O(N)$ with path compression, where N is the length of the arrays.
Space Complexity: $O(N)$ auxiliary space for the DSU parent array and the component Counters.
'''

import ast
from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        # Find with Path Compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union
        def unite(a, b):
            parent[find(a)] = find(b)

        # Build connected components
        for a, b in allowedSwaps:
            unite(a, b)

        # Elite Pythonic Optimization: Direct Counter initialization
        # Bypasses intermediate list allocations completely
        groups = defaultdict(Counter)
        for i in range(n):
            groups[find(i)][source[i]] += 1

        hamming_dist = 0
        
        # Verify target elements against the available pool in their respective components
        for i in range(n):
            root = find(i)
            if groups[root][target[i]] > 0:
                groups[root][target[i]] -= 1  # matched, consume this source value
            else:
                hamming_dist += 1             # no match found in this component

        return hamming_dist

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print(">>> [SYSTEM] INITIATING SWAP PROTOCOL...")
    print("--- 1722. Minimize Hamming Distance Interactive Runner ---")
    try:
        source_input = input("Enter source array (e.g., [1,2,3,4]): ").strip()
        target_input = input("Enter target array (e.g., [2,1,4,5]): ").strip()
        swaps_input = input("Enter allowedSwaps (e.g., [[0,1],[2,3]]): ").strip()
        
        # Safely evaluate inputs
        parsed_source = ast.literal_eval(source_input)
        parsed_target = ast.literal_eval(target_input)
        parsed_swaps = ast.literal_eval(swaps_input)
        
        if not all(isinstance(lst, list) for lst in [parsed_source, parsed_target, parsed_swaps]):
            raise ValueError("All inputs must be valid lists.")
            
        result = solution.minimumHammingDistance(parsed_source, parsed_target, parsed_swaps)
        print(f"\n>>> [RESULT] Minimum Hamming Distance: {result}")
        
    except ValueError as ve:
        print(f">>> [ERROR] Parsing input failed. Details: {ve}")
    except Exception as e:
        print(f">>> [FATAL ERROR] An unexpected exception occurred: {e}")