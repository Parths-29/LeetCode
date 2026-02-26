'''
Question: 680. Valid Palindrome II (Easy)
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

---
My Approach (Two Pointers):
1. Initialize two pointers: `p1` at the start (0) and `p2` at the end (len(s) - 1).
2. Move the pointers inward. If the characters at `p1` and `p2` match, move them closer (`p1 += 1`, `p2 -= 1`).
3. If a mismatch is found (`s[p1] != s[p2]`), it means we must use our single allowed deletion. We can either:
   - Skip the character at `p1` (create `string1`).
   - Skip the character at `p2` (create `string2`).
4. Check if either `string1` or `string2` is a valid palindrome by comparing it to its reversed self (`[::-1]`).
5. If the loop finishes without any mismatches, the original string was already a palindrome, so return True.

Time Complexity: $O(N)$ - We traverse the string with two pointers, and the string slicing/reversing takes $O(N)$ but only happens at most once.
Space Complexity: $O(N)$ - Creating `string1` and `string2` requires allocating new memory for the sliced strings.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
            p1=0
            p2=len(s)-1
            while p1<=p2:
                if s[p1]!=s[p2]:
                    string1=s[:p1]+s[p1+1:]
                    string2=s[:p2]+s[p2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                p1+=1
                p2-=1
            return True

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 680. Valid Palindrome II Interactive Runner ---")
    try:
        # Responsive input setup for strings
        user_input = input('Enter the string (e.g., abca): ').strip()
        
        # Clean up input in case you accidentally paste quotes from LeetCode
        if user_input.startswith(('"', "'")) and user_input.endswith(('"', "'")):
            user_input = user_input[1:-1]
            
        # Calling your function
        result = solution.validPalindrome(user_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")