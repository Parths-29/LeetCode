
'''
Question: 32. Longest Valid Parentheses (Hard)
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

---
My Approach (Two-Pass Counters / Space Optimization):
1. Instead of using a Stack which takes O(N) space, we can use two integer counters: `left` and `right`.
2. First Pass (Left to Right): Traverse the string. Increment `left` for '(' and `right` for ')'. 
   - If `left == right`, we have a valid sequence. Calculate the length and update `max_len`.
   - If `right > left`, the sequence is invalid, so reset both counters to 0.
3. Second Pass (Right to Left): The first pass misses sequences where there are more left parentheses than right (e.g., "(()"). To fix this, we traverse backward.
   - Increment `left` and `right` identically.
   - If `left == right`, update `max_len`.
   - If `left > right`, the sequence is invalid from this direction, so reset both counters to 0.
   
Time Complexity: O(N) where N is the length of the string. We traverse the string exactly twice.
Space Complexity: O(1) auxiliary space as we only use three integer variables.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        
        # Pass 1: Left to Right
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
                
        # Pass 2: Right to Left
        left, right = 0, 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_len

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 32. Longest Valid Parentheses Interactive Runner ---")
    try:
        s_input = input("Enter the parentheses string (e.g., )()()) : ").strip()
        
        # Clean up input if you accidentally paste LeetCode quotes
        if s_input.startswith(('"', "'")) and s_input.endswith(('"', "'")):
            s_input = s_input[1:-1]
            
        # Calling the function
        result = solution.longestValidParentheses(s_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")