'''
Question: 821. Shortest Distance to a Character (Easy)
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

---
My Approach (Two-Pass Array Sweep):
1. Initialize an array with `0` where the target character `c` is found, and infinity (`float('inf')`) everywhere else.
2. First Pass (Left-to-Right): We sweep through the array. If we pass a target character, we keep counting up by 1. `res[i] = min(res[i], res[i - 1] + 1)`.
3. Second Pass (Right-to-Left): We sweep backward. If the target character is closer on the right side, it will overwrite the left-side distance. `res[i] = min(res[i], res[i + 1] + 1)`.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(1) auxiliary space (excluding the output array).
'''

from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        # Initialize with infinity for unreached states
        res = [0 if char == c else float('inf') for char in s]
        
        # Left-to-right sweep
        for i in range(1, n):
            res[i] = min(res[i], res[i - 1] + 1)
            
        # Right-to-left sweep
        for i in range(n - 2, -1, -1):
            res[i] = min(res[i], res[i + 1] + 1)
            
        return res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 821. Shortest Distance to a Character Interactive Runner ---")
    try:
        s_input = input("Enter the string s (e.g., loveleetcode): ").strip()
        c_input = input("Enter the character c (e.g., e): ").strip()
        
        if s_input.startswith(('"', "'")): s_input = s_input[1:-1]
        if c_input.startswith(('"', "'")): c_input = c_input[1:-1]
            
        result = solution.shortestToChar(s_input, c_input)
        print(f"\nOutput: {result}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")