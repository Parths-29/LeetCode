'''
Question: 1345. Jump Game IV (Hard)
Given an array of integers arr, you are initially positioned at the first index of the array.
In one step you can jump from index i to index:
- i + 1 where: i + 1 < arr.length.
- i - 1 where: i - 1 >= 0.
- j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

---
My Approach (Bidirectional BFS + Elite Memory Optimization):
1. Standard BFS grows exponentially and wastes memory/time checking massive middle layers.
2. We implement a Bidirectional BFS, searching from BOTH the start (index 0) and the end (index n-1) simultaneously.
3. Every step, we ALWAYS choose to expand the smaller of the two search frontiers. This completely neutralizes the exponential explosion of standard BFS.
4. Pythonic Data Structure Flex: We keep one frontier as a `list` (for extremely fast iteration and appending) and the other as a `set` (for O(1) instantaneous intersection lookup).
5. Fast Map Clearing: Instead of using `pop(..., None)`, we use the native Python `del` statement to instantly free memory and guarantee we never process the same teleportation group twice.

Time Complexity: $O(N)$ where N is the length of the array. We visit each index at most once.
Space Complexity: $O(N)$ auxiliary space for the map, search frontiers, and visited array.
'''

import ast
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # Step 1: Map values to their indices using native dict for slight speed boost
        mp = {}
        for i, num in enumerate(arr):
            if num not in mp:
                mp[num] = []
            mp[num].append(i)

        # Step 2: Initialize Bidirectional BFS
        # head is a list for fast iteration/appending
        # tail is a set for O(1) intersection lookups
        head = [0]
        tail = {n - 1}
        
        visited = [False] * n
        visited[0] = True
        visited[n - 1] = True
        
        step = 0
        
        # Step 3: Expand layer by layer
        while head:
            # ALWAYS expand the smaller frontier to save massive amounts of time
            if len(head) > len(tail):
                head, tail = list(tail), set(head)
            
            next_head = []
            
            for node in head:
                # 1. Check directional neighbors (left and right)
                for nxt in (node - 1, node + 1):
                    if 0 <= nxt < n:
                        if nxt in tail:           # We met in the middle!
                            return step + 1
                        if not visited[nxt]:
                            visited[nxt] = True
                            next_head.append(nxt)
                
                # 2. Check teleportation neighbors
                val = arr[node]
                if val in mp:
                    for nxt in mp[val]:
                        if nxt in tail:           # We met in the middle!
                            return step + 1
                        if not visited[nxt]:
                            visited[nxt] = True
                            next_head.append(nxt)
                    
                    # O(1) memory clear to prevent redundant processing
                    del mp[val] 
                    
            # Move to the next layer
            head = next_head
            step += 1
            
        return -1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1345. Jump Game IV (Bidirectional BFS) ---")
    try:
        arr_input = input("Enter the arr (e.g., [100,-23,-23,404,100,23,23,23,3,404]): ").strip()
        
        # Safely evaluate input
        parsed_arr = ast.literal_eval(arr_input)
        
        if not isinstance(parsed_arr, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.minJumps(parsed_arr)
        print(f"\nMinimum steps to reach the end: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")