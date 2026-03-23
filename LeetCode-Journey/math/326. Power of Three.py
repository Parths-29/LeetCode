'''
Question: 326. Power of Three (Easy)
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).

---
My Approach (Math / Magic Number):
1. The maximum value of a 32-bit signed integer is 2^31 - 1 (2147483647).
2. The largest power of 3 that is strictly less than this maximum is 3^19, which equals 1162261467.
3. Since 3 is a prime number, the only divisors of 3^19 are other powers of 3.
4. If n is positive and perfectly divides 1162261467 (i.e., modulo is 0), then n MUST be a power of 3.

Time Complexity: O(1) as it requires a single mathematical modulo operation.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if positive and a divisor of the max 32-bit power of 3
        if n <= 0:
            return False
        return 1162261467 % n == 0

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 326. Power of Three Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 27): ").strip()
        
        # Safely evaluate input
        n = int(n_input)
            
        # Calling the function
        result = solution.isPowerOfThree(n)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")