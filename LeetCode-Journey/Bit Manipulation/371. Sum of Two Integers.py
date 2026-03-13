'''
Question: 371. Sum of Two Integers (Medium)
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

---
My Approach (Bitwise Manipulation):
1. We use XOR (`^`) to simulate addition without carrying over bits.
2. We use AND (`&`) followed by a left shift (`<< 1`) to find the exact positions of the carry bits.
3. We repeat this process, updating `a` with the carry-less sum and `b` with the shifted carry, until `b` becomes 0 (no more carries).
4. Python-specific handling: Python integers don't overflow at 32 bits; they grow infinitely. We use a 32-bit mask (`0xFFFFFFFF`) to force the numbers to stay within 32 bits during calculation.
5. If the final result is greater than the maximum positive 32-bit integer (`0x7FFFFFFF`), it means the result is supposed to be negative. We convert it back to a Python negative integer using `~(a ^ mask)`.

Time Complexity: O(1) because the loop will run at most 32 times (since we cap it at 32 bits).
Space Complexity: O(1) as we only use a few variables.
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask in hexadecimal
        mask = 0xFFFFFFFF
        # Max positive 32-bit integer in hexadecimal
        max_int = 0x7FFFFFFF
        
        while b != 0:
            # Calculate the carry and shift it left
            carry = (a & b) & mask
            
            # Calculate the sum without carry
            a = (a ^ b) & mask
            
            # b becomes the new carry to be added in the next iteration
            b = (carry << 1) & mask
            
        # If 'a' is a negative 32-bit integer, we must restore it to a Python negative integer
        return a if a <= max_int else ~(a ^ mask)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 371. Sum of Two Integers Interactive Runner ---")
    try:
        a_input = input("Enter integer a (e.g., 1): ")
        b_input = input("Enter integer b (e.g., 2): ")
        
        # Safely parse inputs
        a = int(a_input.strip())
        b = int(b_input.strip())
            
        # Calling the function
        result = solution.getSum(a, b)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")