'''
Question: 788. Rotated Digits (Medium)
An integer x is good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x.
Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Return the number of good integers in the range [1, n].

---
My Approach (Digit DP / Logarithmic Scaling):
1. A brute-force approach checks every number from 1 to N, taking O(N * D) time, where D is the number of digits.
2. We optimize this drastically using Digit Dynamic Programming. Instead of counting numbers, we BUILD valid numbers digit-by-digit from left to right.
3. Our DP state tracks:
   - `i`: current index of the digit we are choosing.
   - `is_bound`: a boolean tracking if our chosen digits strictly match the prefix of `N`. If true, our next digit choice is capped by N's digit at index `i`.
   - `has_diff`: a boolean tracking if we have placed at least one digit that rotates to a different value (2, 5, 6, 9).
4. If we place a 3, 4, or 7, that branch is instantly pruned.
5. Using Python's `@cache`, the states are memoized, reducing the time complexity to strictly the number of digits in N.

Time Complexity: $O(\log_{10} N)$ which is astronomically faster than O(N). For N = 10000, it takes a few operations instead of tens of thousands.
Space Complexity: $O(\log_{10} N)$ auxiliary space for the DP recursion stack.
'''

import ast
from functools import cache

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        valid_diff = {2, 5, 6, 9}
        invalid = {3, 4, 7}

        @cache
        def dp(i: int, is_bound: bool, has_diff: bool) -> int:
            # Base Case: We've built a full number. It's valid if it has at least one rotated diff.
            if i == len(s):
                return 1 if has_diff else 0

            res = 0
            # If our prefix matches N, we can't exceed N's current digit. Otherwise, go up to 9.
            limit = int(s[i]) if is_bound else 9

            for d in range(limit + 1):
                # Prune invalid branches instantly
                if d in invalid:
                    continue
                
                # Transition to the next digit state
                res += dp(
                    i + 1,
                    is_bound and (d == limit),
                    has_diff or (d in valid_diff)
                )

            return res

        # Start at index 0, strictly bound to N's prefix, having no diff digits yet
        return dp(0, True, False)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 788. Rotated Digits Interactive Runner ---")
    try:
        n_input = input("Enter the upper limit integer n (e.g., 10): ").strip()
        
        # Safely evaluate input
        parsed_n = int(n_input)
            
        result = solution.rotatedDigits(parsed_n)
        print(f"\nNumber of good integers up to {parsed_n}: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")