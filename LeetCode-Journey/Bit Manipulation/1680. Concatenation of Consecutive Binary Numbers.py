'''
Question: 1680. Concatenation of Consecutive Binary Numbers (Medium)
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

Example 2:
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

---
My Approach (Bit Manipulation & Modular Arithmetic):
1. We need to maintain a running total `ans`, starting at 0.
2. The modulo value is `MOD = 10**9 + 7`. We apply this at every step to keep our number from growing too large and slowing down calculations.
3. Iterate `i` from 1 up to `n`.
4. For each number `i`, we need to find out how many bits it has. Python has a built-in `i.bit_length()` function that gives us this instantly.
5. To "concatenate" `i` to our running total, we use a bitwise left shift (`<<`). We shift `ans` to the left by the number of bits in `i`, which creates exact space for `i`.
6. Then, we use the bitwise OR operator (`|`) to insert `i` into those empty spaces (or just addition `+`). 
7. Finally, take the result modulo `MOD`.

Time Complexity: $O(N)$
Space Complexity: $O(1)$
'''

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        
        for i in range(1, n + 1):
            # Shift the current answer left by the number of bits in 'i'
            # Then bitwise OR with 'i' to append it, and take modulo
            ans = ((ans << i.bit_length()) | i) % MOD
            
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1680. Concatenation of Consecutive Binary Numbers Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 3): ")
        n = int(n_input)
        
        # Calling the function
        result = solution.concatenatedBinary(n)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")