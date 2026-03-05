'''
Question: 1758. Minimum Changes To Make Alternating Binary String (Easy)
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

---
My Approach (Bitwise Parity Check):
1. There are only two valid alternating patterns: one starting with '0' and one starting with '1'.
2. Initialize an array `op` of size 2 to track the number of changes required for each of the two patterns.
3. Iterate through the string in steps of 2 (checking pairs of even/odd indices).
4. Use `ord(s[i]) & 1` to quickly determine if the character at the even index is '0' or '1'. Accumulate the mismatches.
5. Do the inverse check `1 - (ord(s[i+1]) & 1)` for the adjacent odd index (if it exists).
6. Return the minimum of the two mismatch counters.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(1) as we only use an array of size 2.
'''

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        op = [0] * 2
        
        for i in range(0, n, 2):
            # Check the even index
            op[ord(s[i]) & 1] += 1
            
            # Check the odd index if we haven't reached the end of the string
            if i + 1 < n:
                op[1 - (ord(s[i+1]) & 1)] += 1
                
        return min(op[0], op[1])

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1758. Minimum Changes To Make Alternating Binary String ---")
    try:
        # Responsive input setup for string
        user_input = input("Enter the binary string s (e.g., 0100): ").strip()
        
        # Clean up input if the user accidentally pastes LeetCode quotes
        if user_input.startswith(('"', "'")) and user_input.endswith(('"', "'")):
            user_input = user_input[1:-1]
            
        if not user_input:
            raise ValueError("Input string cannot be empty.")
            
        # Calling the function
        result = solution.minOperations(user_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")