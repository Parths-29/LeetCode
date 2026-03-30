'''
Question: 438. Find All Anagrams in a String (Medium)
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

---
My Approach (Sliding Window + Fixed-Size Frequency Array):
1. Fast Fail: If `s` is shorter than `p`, it's impossible to find any anagrams.
2. Initialize two arrays of size 26 to track character frequencies for `p` and our current sliding window in `s`.
3. Pre-calculate the frequencies for the target string `p`.
4. Iterate through `s`, expanding the window to the right by incrementing the count of the current character.
5. If the window size exceeds the length of `p`, we shrink it from the left by decrementing the count of the character that just exited the window.
6. Compare the two frequency arrays. If they match perfectly, we've found an anagram! Record the starting index.

Time Complexity: $O(N)$ where N is the length of string s. The sliding window processes each character at most twice, and comparing arrays of size 26 is an $O(1)$ operation.
Space Complexity: $O(1)$ auxiliary space, as our frequency arrays are strictly bounded to 26 elements regardless of string length.
'''

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26
        
        # Populate the frequency array for the target string
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        result = []
        
        # Slide the window across string s
        for i in range(len(s)):
            # Add the new character on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            
            # If window exceeds the target length, remove the character on the left
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            
            # If the frequency arrays match, we found an anagram
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 438. Find All Anagrams in a String Interactive Runner ---")
    try:
        s_input = input("Enter string s (e.g., cbaebabacd): ").strip()
        p_input = input("Enter target string p (e.g., abc): ").strip()
        
        # Clean up input if LeetCode quotes are accidentally pasted
        if s_input.startswith(('"', "'")): s_input = s_input[1:-1]
        if p_input.startswith(('"', "'")): p_input = p_input[1:-1]
            
        # Calling the function
        result = solution.findAnagrams(s_input, p_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")