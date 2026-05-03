'''
Question: 796. Rotate String (Easy/Medium)
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

---
My Approach (Knuth-Morris-Pratt (KMP) + Circular Modulo Traversal):
1. The one-liner `(s+s).find(goal)` is fast in Python but theoretically worst-case O(N^2) time and requires O(N) space to allocate the new concatenated string.
2. We implement KMP to guarantee strict O(N) worst-case time complexity.
3. We first build the Longest Prefix Suffix (LPS) array for the `goal` string. This tells us exactly how far to safely backtrack when a character mismatch occurs, completely bypassing the need to rescan characters we already matched.
4. The Modulo Flex: Instead of concatenating `s + s` to search across the boundary, we just iterate `i` up to `2 * n` and use `s[i % n]`. This simulates a circular string in perfect O(1) auxiliary space!

Time Complexity: $O(N)$ strictly, where N is the length of the string.
Space Complexity: $O(N)$ to store the LPS array for the goal string.
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if not s and not goal:
            return True

        n = len(s)
        
        # 1. Build the LPS (Longest Prefix Suffix) Array for the goal
        lps = [0] * n
        length = 0
        i = 1
        
        while i < n:
            if goal[i] == goal[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Backtrack the prefix length using the LPS array
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # 2. KMP Search using Modulo wrapping (no s+s concatenation needed!)
        i = 0  # conceptual index for s + s
        j = 0  # index for goal
        
        while i < 2 * n:
            if s[i % n] == goal[j]:
                i += 1
                j += 1
                
            if j == n:
                return True  # We matched the entire goal string!
                
            # Mismatch after j matches
            elif i < 2 * n and s[i % n] != goal[j]:
                if j != 0:
                    # Do not reset i back to 0! Just shift j back using LPS
                    j = lps[j - 1]
                else:
                    i += 1
                    
        return False

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 796. Rotate String (KMP Algorithm) ---")
    try:
        s_input = input("Enter string s: ").strip()
        goal_input = input("Enter string goal: ").strip()
        
        # Clean quotes if entered
        if s_input.startswith(('"', "'")): s_input = s_input[1:-1]
        if goal_input.startswith(('"', "'")): goal_input = goal_input[1:-1]
            
        result = solution.rotateString(s_input, goal_input)
        print(f"\nCan rotate? {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")