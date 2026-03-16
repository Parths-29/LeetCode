'''
Question: 7. Reverse Integer (Medium)
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

---
My Approach (Mathematical & 32-bit Safe):
1. The string slicing approach violates the strict 32-bit environment constraint. We must use math.
2. We extract digits from the end of `x` using modulo 10 (`x % 10`) and strip them using integer division by 10 (`x // 10`).
3. To avoid Python's unique negative modulo behavior, we work with the absolute value of `x` and store the sign.
4. Before we multiply our `res` by 10 and add the next digit, we strictly check if doing so will overflow the 32-bit limit (2147483647).
5. Apply the original sign to the result and return.

Time Complexity: O(log(x)) because there are roughly log10(x) digits in the integer.
Space Complexity: O(1) as we only use a few variables for tracking.
'''

class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit max boundary
        INT_MAX_DIV_10 = (2**31 - 1) // 10
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow BEFORE it happens to simulate 32-bit strictness
            if res > INT_MAX_DIV_10 or (res == INT_MAX_DIV_10 and pop > 7):
                return 0
                
            res = res * 10 + pop
            
        return res * sign

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 7. Reverse Integer Interactive Runner ---")
    try:
        x_input = input("Enter the integer x (e.g., -123): ").strip()
        
        # Safely evaluate input
        x = int(x_input)
            
        # Calling the function
        result = solution.reverse(x)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")