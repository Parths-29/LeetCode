'''
Question: 1784. Check if Binary String Has at Most One Segment of Ones (Easy)
Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones. Otherwise, return false.

Example 1:
Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.

Example 2:
Input: s = "110"
Output: true

---
My Approach (Substring Search):
1. The string is guaranteed to have no leading zeros, so it always starts with '1' (or is empty, though constraints usually say length >= 1).
2. If there is more than one contiguous segment of '1's, there must be at least one '0' separating them.
3. This means the transition from the separating '0' back to the new segment of '1's will always create the exact substring "01".
4. We can solve this instantly by just checking if "01" is inside the string. 
5. If "01" is found, return False. If not, return True.

Time Complexity: O(N) where N is the length of the string, as Python's 'in' operator does a fast underlying C-level substring search.
Space Complexity: O(1)
'''

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If "01" exists, it means a new segment of 1s started after a 0.
        return "01" not in s

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1784. Check if Binary String Has at Most One Segment Interactive Runner ---")
    try:
        # Responsive input setup for string
        user_input = input("Enter the binary string s (e.g., 1001): ").strip()
        
        # Clean up input if you accidentally paste LeetCode quotes
        if user_input.startswith(('"', "'")) and user_input.endswith(('"', "'")):
            user_input = user_input[1:-1]
            
        if not user_input:
            raise ValueError("Input string cannot be empty.")
            
        # Calling the function
        result = solution.checkOnesSegment(user_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")