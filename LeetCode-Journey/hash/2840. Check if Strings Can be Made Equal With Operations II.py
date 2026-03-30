'''
Question: 2840. Check if Strings Can be Made Equal With Operations II (Medium)
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
You can apply the following operation on any of the two strings any number of times:
- Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:
Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

---
My Approach (Parity Isolation + Frequency Counting):
1. The condition `(j - i) % 2 == 0` means that indices with the same parity (both even or both odd) can freely swap with each other.
2. An even index can NEVER swap with an odd index. The string is effectively split into two independent sub-arrays.
3. Because we can swap freely within the even indices, we just need to verify if the collection of characters at the even indices of `s1` is exactly the same as in `s2`.
4. We do the exact same verification for the odd indices.
5. In Python, `s[::2]` extracts all even-indexed characters, and `s[1::2]` extracts all odd-indexed characters.
6. Using `collections.Counter`, we can compare the frequencies in perfectly optimized $O(N)$ time.

Time Complexity: $O(N)$ where N is the length of the string. Slicing and counting both take linear time.
Space Complexity: $O(N)$ to store the sliced strings and the frequency maps.
'''

import ast
from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Check if the even-indexed characters have the same frequencies
        if Counter(s1[::2]) != Counter(s2[::2]):
            return False
            
        # Check if the odd-indexed characters have the same frequencies
        if Counter(s1[1::2]) != Counter(s2[1::2]):
            return False
            
        return True

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 2840. Check if Strings Can be Made Equal II Interactive Runner ---")
    try:
        s1_input = input("Enter string s1 (e.g., abcdba): ").strip()
        s2_input = input("Enter string s2 (e.g., cabdab): ").strip()
        
        # Clean up input if LeetCode quotes are accidentally pasted
        if s1_input.startswith(('"', "'")): s1_input = s1_input[1:-1]
        if s2_input.startswith(('"', "'")): s2_input = s2_input[1:-1]
            
        # Calling the function
        result = solution.checkStrings(s1_input, s2_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")