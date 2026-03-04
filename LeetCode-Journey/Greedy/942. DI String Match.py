'''
Question: 942. DI String Match (Easy)
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
- s[i] == 'I' if perm[i] < perm[i + 1]
- s[i] == 'D' if perm[i] > perm[i + 1]
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

---
My Approach (Greedy + Two Pointers):
1. Create a result array `perm`.
2. Initialize two pointers: `low = 0` and `high = n` (where n is the length of the string).
3. Loop through each character in the string `s`.
4. If the character is 'I' (Increase), append the current `low` value to `perm` and increment `low` by 1.
5. If the character is 'D' (Decrease), append the current `high` value to `perm` and decrement `high` by 1.
6. After the loop, `low` and `high` will be equal. Append this final remaining number to `perm`.
7. Return the completed `perm` array.

Time Complexity: O(N) where N is the length of the string. We process each character exactly once.
Space Complexity: O(N) to store the resulting permutation array.
'''

from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1
                
        # Append the last remaining number
        perm.append(low)
        
        return perm

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 942. DI String Match Interactive Runner ---")
    try:
        # Responsive input setup for the string
        s_input = input("Enter the string s (e.g., IDID): ").strip()
        
        # Clean up input if you accidentally paste LeetCode quotes
        if s_input.startswith(('"', "'")) and s_input.endswith(('"', "'")):
            s_input = s_input[1:-1]
            
        if not s_input:
            raise ValueError("Input string cannot be empty.")
            
        # Calling the function
        result = solution.diStringMatch(s_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")