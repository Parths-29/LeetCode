'''
Question: 678. Valid Parenthesis String (Medium)
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')', a single left parenthesis '(', or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

---
My Approach (Greedy Range Tracking):
1. Instead of backtracking or using a stack, we maintain a range of possible open left parentheses.
2. `leftMin` is the minimum possible open left parentheses.
3. `leftMax` is the maximum possible open left parentheses.
4. If we see '(', both min and max increase.
5. If we see ')', both min and max decrease.
6. If we see '*', we decrease `leftMin` (treating it as ')') and increase `leftMax` (treating it as '(').
7. If `leftMax` ever goes below 0, it means we have too many ')' even if all '*' were '('. Return False.
8. If `leftMin` goes below 0, we simply reset it to 0, because we can choose to treat some '*' as empty strings instead of ')'.
9. The string is valid if `leftMin` is exactly 0 at the end (meaning we successfully paired all mandatory '(').

Time Complexity: O(N) where N is the length of the string. We do a single pass.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                # Wildcard '*' can be ')', '(', or empty
                leftMin -= 1
                leftMax += 1
                
            # If max possible open parentheses is negative, we have too many ')'
            if leftMax < 0:
                return False
                
            # We can't have negative open parentheses; reset to 0 (treat '*' as empty instead of ')')
            if leftMin < 0:
                leftMin = 0
                
        # Valid if we perfectly paired all required open parentheses
        return leftMin == 0

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 678. Valid Parenthesis String Interactive Runner ---")
    try:
        s_input = input("Enter the string (e.g., (*)) ): ").strip()
        
        # Clean up input if you accidentally paste LeetCode quotes
        if s_input.startswith(('"', "'")) and s_input.endswith(('"', "'")):
            s_input = s_input[1:-1]
            
        # Calling the function
        result = solution.checkValidString(s_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")