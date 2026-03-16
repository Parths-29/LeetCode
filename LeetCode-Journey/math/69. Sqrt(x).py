'''
Question: 69. Sqrt(x) (Easy)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

---
My Approach (Math / Sum of Odd Numbers):
1. There is a mathematical property where the sum of the first `n` odd numbers equals `n^2`.
2. We can find the integer square root of `x` by continuously subtracting consecutive odd numbers (1, 3, 5...) from `x`.
3. We keep a counter `n` for how many odd numbers we've subtracted.
4. If `x` drops exactly to 0, it was a perfect square, and `n` is the exact root.
5. If `x` drops below 0, it wasn't a perfect square. The loop breaks, and the rounded-down root is simply `n - 1`.

Time Complexity: $O(\\sqrt{x})$ because the loop runs roughly the square root of x times.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        odd = 1
        n = 0

        # iterate till x becomes 0 or negative
        while (x > 0):
            x -= odd
            odd += 2 # next odd number on each iteration, odd = 1, 3, 5,...
            n += 1

        # if x is a perfect square then subtracting n odd numbers would result in 0
        if (x == 0):
            return n

        # if x is not a perfect square then round down
        return n - 1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 69. Sqrt(x) Interactive Runner ---")
    try:
        x_input = input("Enter the integer x (e.g., 8): ").strip()
        
        # Safely evaluate input
        x = int(x_input)
        
        if x < 0:
            raise ValueError("Input must be a non-negative integer.")
            
        # Calling the function
        result = solution.mySqrt(x)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")