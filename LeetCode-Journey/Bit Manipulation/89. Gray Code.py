'''
Question: 89. Gray Code (Medium)
An n-bit gray code sequence is a sequence of 2^n integers where:
- Every integer is in the inclusive range [0, 2^n - 1]
- The first integer is 0
- An integer appears no more than once in the sequence
- The binary representation of every pair of adjacent integers differs by exactly one bit
- The binary representation of the first and last integers differs by exactly one bit
Given an integer n, return any valid n-bit gray code sequence.

Example 1:
Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

---
My Approach (Bitwise Magic):
1. The total number of integers in an n-bit Gray code sequence is exactly 2^n. We can represent this using the bitwise left shift: `1 << n`.
2. Iterate `i` from `0` up to `(2^n) - 1`.
3. Apply the Gray code conversion formula: `i ^ (i >> 1)`.
4. Return the fully generated array.

Time Complexity: $O(2^n)$ because we mathematically generate exactly 2^n numbers in a single pass.
Space Complexity: $O(1)$ auxiliary space, as we are only storing the required output array.
'''

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Generate the Gray code sequence using the bitwise XOR trick
        return [i ^ (i >> 1) for i in range(1 << n)]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 89. Gray Code Interactive Runner ---")
    try:
        n_input = input("Enter the number of bits n (e.g., 2): ").strip()
        
        if not n_input.isdigit():
            raise ValueError("Input must be a positive integer.")
            
        n = int(n_input)
        
        # Calling the function
        result = solution.grayCode(n)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")