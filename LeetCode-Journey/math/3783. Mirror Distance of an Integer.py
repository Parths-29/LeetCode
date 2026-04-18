'''
Question: 3783. Mirror Distance of an Integer (Easy)
Given an integer n, the mirror distance is defined as the absolute difference between n and the integer formed by reversing its digits.
Return the mirror distance of n.

Example 1:
Input: n = 125
Output: 396
Explanation: The reverse of 125 is 521. The absolute difference is |125 - 521| = 396.

---
My Approach (Pythonic String Slicing):
1. The mathematical approach (using modulo and division) is memory-efficient but suffers from Python's interpreter loop overhead.
2. In Python, string slicing `[::-1]` is executed in highly optimized C-code.
3. We cast the integer to a string, reverse it instantly using `[::-1]`, cast it back to an integer, and subtract it from the original number.
4. We wrap the result in `abs()` to guarantee a positive distance.

Time Complexity: $O(D)$ where D is the number of digits in n. Executed at C-level speeds.
Space Complexity: $O(D)$ auxiliary space to store the string representation.
'''

import ast

class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Pythonic one-liner: convert, reverse in C-backend, convert back, get absolute difference
        return abs(n - int(str(n)[::-1]))

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3783. Mirror Distance of an Integer Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 125): ").strip()
        
        # Safely evaluate input
        parsed_n = int(n_input)
            
        result = solution.mirrorDistance(parsed_n)
        print(f"\nMirror Distance: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")