'''
Question: 231. Power of Two (Easy)
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: n = 3
Output: false

---
My Approach (Bitwise Magic):
1. A power of two in binary always has exactly ONE bit set to '1' (e.g., 2 is 10, 4 is 100, 8 is 1000).
2. If we subtract 1 from a power of two, that single '1' becomes a '0', and all the trailing '0's become '1's (e.g., 8 - 1 = 7, which is 0111 in binary).
3. If we perform a bitwise AND (&) between n and n - 1, the result will be exactly 0 if and only if n had exactly one '1' bit.
4. We also need to ensure n > 0 because negative numbers and 0 cannot be powers of two.

Time Complexity: O(1) as it is a single bitwise operation evaluated at the hardware level.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 231. Power of Two Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 16): ").strip()
        
        # Safely evaluate input
        n = int(n_input)
            
        # Calling the function
        result = solution.isPowerOfTwo(n)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")