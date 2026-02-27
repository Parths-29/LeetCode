'''
Question: 3666. Minimum Operations to Equalize Binary String (Hard)
You are given a binary string s, and an integer k.
In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.
Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

Example 1:
Input: s = "110", k = 1
Output: 1

Example 2:
Input: s = "0101", k = 3
Output: 2

---
My Approach (Math + BFS + DSU):
1. Instead of tracking the actual string, we only track `cur`, which is the current number of '0's.
2. If we flip exactly `k` indices, let `x` be the number of '0's we choose to flip to '1'. 
   We are forced to flip `k - x` '1's into '0's.
3. The new number of zeros becomes: `cur - x + (k - x) = cur + k - 2x`.
4. We can calculate the minimum and maximum valid values for `x` based on the available '0's and '1's.
   This gives us a contiguous range of possible zero-counts we can reach, stepping by 2.
5. We use BFS to find the shortest path to 0 zeros.
6. Crucially, to prevent our BFS from re-checking visited states and getting a TLE, we use a Disjoint Set Union (DSU) array. `head[i]` acts as a fast-forward button, instantly pointing us to the next unvisited number of zeros with the same parity.

Time Complexity: O(N * α(N)) (Practically O(N))
Space Complexity: O(N)
'''

from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')
        
        # DSU to quickly jump over visited states
        # Size n + 3 ensures we never hit an Index Out Of Bounds
        head = list(range(n + 3))
        
        # Iterative DSU find with path compression to avoid recursion limits
        def find(i):
            curr = i
            while head[curr] != curr:
                head[curr] = head[head[curr]] 
                curr = head[curr]
            return curr

        # Mark our starting point as visited by pointing to the next node of same parity
        head[cnt0] = find(cnt0 + 2)
        
        q = deque([cnt0])
        steps = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                if cur == 0:
                    return steps
                
                # Math limits for how many 0s we can actually flip to 1s
                min_x = max(0, k - n + cur)
                max_x = min(cur, k)
                
                # l and r represent the lowest and highest number of zeros we can reach next
                l = cur + k - 2 * max_x
                r = cur + k - 2 * min_x
                
                # Traverse the unvisited states between l and r
                curr_node = find(l)
                while curr_node <= r:
                    q.append(curr_node)
                    # Mark visited by linking to the next node of the same parity
                    head[curr_node] = find(curr_node + 2)
                    curr_node = find(curr_node)
                    
            steps += 1
            
        return -1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 3666. Minimum Operations Interactive Runner ---")
    try:
        s_input = input("Enter the binary string s (e.g., 110): ").strip()
        k_input = input("Enter the integer k (e.g., 1): ").strip()
        
        # Clean up string if quotes were pasted
        if s_input.startswith(('"', "'")) and s_input.endswith(('"', "'")):
            s_input = s_input[1:-1]
            
        k = int(k_input)
        
        result = solution.minOperations(s_input, k)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")