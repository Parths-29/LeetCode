'''
Question: 1888. Minimum Number of Flips to Make the Binary String Alternating (Medium)
You are given a binary string s. You are allowed to perform two types of operations:
Type-1: Remove the character at the start of the string s and append it to the end.
Type-2: Pick any character in s and flip its value (0 to 1 or 1 to 0).
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

Example 1:
Input: s = "111000"
Output: 2
Explanation: Use Type-1 operation 2 times to obtain "100011". Then flip the 1st and 4th characters to get "101010".

---
My Approach (Sliding Window + String Concatenation):
1. A valid alternating string can only start with '1' (e.g., "1010...") or '0' (e.g., "0101...").
2. Simulating the Type-1 rotation is too slow. Instead, concatenate `s` to itself (`s = s + s`). A window of length `n` sliding across this double string perfectly simulates every possible rotation.
3. Build the two target alternating strings (`target1` and `target2`) up to the length of `2n`.
4. Initialize a sliding window. As we iterate through the double string, count how many characters mismatch `target1` and `target2`.
5. If the window size exceeds `n`, subtract the mismatch count of the character that just fell out of the left side of the window.
6. Once the window size reaches exactly `n`, record the minimum flips required.

Time Complexity: O(N) where N is the length of the string. We do a single pass over a string of length 2N.
Space Complexity: O(N) to store the concatenated string and target patterns.
'''

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Double the string to simulate rotations
        s = s + s
        
        # Build the two alternating target patterns of length 2n
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "1" if i % 2 == 0 else "0"
            target2 += "0" if i % 2 == 0 else "1"
            
        res = float('inf')
        diff1, diff2 = 0, 0
        
        # Slide a window of size n across the double string
        for i in range(len(s)):
            if s[i] != target1[i]: diff1 += 1
            if s[i] != target2[i]: diff2 += 1
            
            # If the window size exceeds n, remove the left-most character's contribution
            if i >= n:
                if s[i - n] != target1[i - n]: diff1 -= 1
                if s[i - n] != target2[i - n]: diff2 -= 1
                
            # Once the window is exactly size n, record the minimum flips
            if i >= n - 1:
                res = min(res, diff1, diff2)
                
        return res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1888. Minimum Flips to Make Alternating Interactive Runner ---")
    try:
        # Responsive input setup for string
        user_input = input("Enter the binary string s (e.g., 111000): ").strip()
        
        # Clean up input if you accidentally paste LeetCode quotes
        if user_input.startswith(('"', "'")) and user_input.endswith(('"', "'")):
            user_input = user_input[1:-1]
            
        if not user_input:
            raise ValueError("Input string cannot be empty.")
            
        # Calling the function
        result = solution.minFlips(user_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")