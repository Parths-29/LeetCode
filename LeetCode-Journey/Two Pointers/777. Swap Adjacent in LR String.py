'''
Question: 777. Swap Adjacent in LR String (Medium)
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string result, return True if and only if there exists a sequence of moves to transform start to result.

Example 1:
Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
Output: true
Explanation: We can transform start to result following these steps:
RXXLRXRXL -> XRXLRXRXL -> XRLXRXRXL -> XRLXXRRXL -> XRLXXRRLX

---
My Approach (Two Pointers / Mathematical Invariant):
1. 'L' and 'R' can only move through 'X's. They can NEVER cross each other. Therefore, if we ignore all 'X's, the sequence of 'L's and 'R's in both strings must be absolutely identical.
2. We use two pointers, `i` for `start` and `j` for `result`, skipping over 'X's.
3. If one pointer reaches the end before the other, the sequences don't match (handled cleanly via XOR).
4. Spatial Constraints:
   - "XL" -> "LX" means 'L' can only move LEFT. So, the index of 'L' in `start` MUST be >= the index of 'L' in `result`.
   - "RX" -> "XR" means 'R' can only move RIGHT. So, the index of 'R' in `start` MUST be <= the index of 'R' in `result`.
5. If all constraints hold, the transformation is possible.

Time Complexity: $O(N)$ where N is the length of the string. Both pointers only traverse the string once.
Space Complexity: $O(1)$ auxiliary space, as we are only tracking two integer pointers.
'''

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        i = j = 0

        while i < n or j < n:
            # Skip 'X's in both strings
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1

            # If one reaches the end but the other doesn't, sequence lengths differ
            if (i == n) ^ (j == n):
                return False

            if i < n and j < n:
                # If the characters don't match, they can't cross each other
                if start[i] != result[j]:
                    return False

                # 'L' can only move to the left (target index j must be <= i)
                if start[i] == 'L' and j > i:
                    return False

                # 'R' can only move to the right (target index j must be >= i)
                if start[i] == 'R' and j < i:
                    return False

            i += 1
            j += 1

        return True

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 777. Swap Adjacent in LR String Interactive Runner ---")
    try:
        start_input = input("Enter the start string (e.g., RXXLRXRXL): ").strip()
        result_input = input("Enter the result string (e.g., XRLXXRRLX): ").strip()
        
        # Clean up input if LeetCode quotes are accidentally pasted
        if start_input.startswith(('"', "'")): start_input = start_input[1:-1]
        if result_input.startswith(('"', "'")): result_input = result_input[1:-1]
            
        # Calling the function
        is_possible = solution.canTransform(start_input, result_input)
        print(f"\nOutput: {is_possible}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")