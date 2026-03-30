'''
Question: 242. Valid Anagram (Easy)
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

---
My Approach (Fixed-Size Array Frequency Counter):
1. Fast Fail: If the strings are not the same length, they cannot be anagrams.
2. Since the constraints specify only lowercase English letters, we don't need a heavy Hash Map. We can use a simple array of size 26.
3. We iterate through both strings simultaneously.
4. For string `s`, we increment the count at the character's mapped index (`ord(char) - ord('a')`).
5. For string `t`, we decrement the count at that same mapped index.
6. After a single pass, if they are perfect anagrams, every single index in our array will have perfectly zeroed back out.
7. We do one final check of the array. If any number is not 0, return False.

Time Complexity: $O(N)$ where N is the length of the strings. We do a single pass through the characters and a constant 26-step pass through the array.
Space Complexity: $O(1)$ auxiliary space because the array size is strictly locked at 26, regardless of how massive the input strings get.
'''

import ast

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Fast fail
        if len(s) != len(t):
            return False
            
        # Initialize an array of 26 zeros for the English alphabet
        counts = [0] * 26
        
        # Single pass to increment for 's' and decrement for 't'
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        # Verify all counts zeroed out
        for count in counts:
            if count != 0:
                return False
                
        return True

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 242. Valid Anagram Interactive Runner ---")
    try:
        s_input = input("Enter string s (e.g., anagram): ").strip()
        t_input = input("Enter string t (e.g., nagaram): ").strip()
        
        # Clean up input if LeetCode quotes are accidentally pasted
        if s_input.startswith(('"', "'")): s_input = s_input[1:-1]
        if t_input.startswith(('"', "'")): t_input = t_input[1:-1]
            
        # Calling the function
        result = solution.isAnagram(s_input, t_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")