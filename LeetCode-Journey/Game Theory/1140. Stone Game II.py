'''
Question: 1140. Stone Game II (Medium/Hard)
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. Alice and Bob take turns, with Alice starting first.
Initially, M = 1. On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X).
The game continues until all the stones have been taken. Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

---
My Approach (Minimax Dynamic Programming + Suffix Sums):
1. State Representation: We define our DP state by `i` (the current index in the piles) and `m` (the current value of M).
2. Suffix Sum: To quickly calculate the total stones remaining from index `i` to the end, we precompute a `suffix_sum` array.
3. End-Game Pruning: If the current player is allowed to take `2 * m` piles, and that exceeds the remaining piles on the board, they should greedily take everything left: `return suffix_sum[i]`.
4. Zero-Sum Minimax: The maximum score the current player can get is the total remaining stones MINUS the maximum score the opponent can get from the remaining piles. `res = max(res, suffix_sum[i] - dp(i + x, max(m, x)))`.
5. Pythonic Optimization: Instead of manually building and passing a 2D array, we use Python's `@cache` from the `functools` library to automatically memoize the recursive states.

Time Complexity: $O(N^3)$. There are $O(N^2)$ states (N values for `i`, and M can grow up to N). For each state, we iterate up to $2M \approx O(N)$ times. 
Space Complexity: $O(N^2)$ auxiliary space for the DP cache and the recursion stack.
'''

import ast
from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        if not piles:
            return 0
            
        # Build the suffix sum array in O(N) time
        # suffix_sum[i] will store the sum of all elements from index i to the end
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        # @cache automatically memoizes the inputs (i, m) so we don't recalculate states
        @cache
        def dp(i: int, m: int) -> int:
            # Base case: no piles left
            if i == n:
                return 0
                
            # Pruning: If you can take everything that's left, take it all!
            if i + 2 * m >= n:
                return suffix_sum[i]

            res = 0
            # Try taking every possible valid amount of piles `x`
            for x in range(1, 2 * m + 1):
                # We want to maximize: (Total stones left) - (What the opponent gets next turn)
                res = max(res, suffix_sum[i] - dp(i + x, max(m, x)))

            return res

        # Alice starts at index 0 with M = 1
        return dp(0, 1)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1140. Stone Game II Interactive Runner ---")
    try:
        piles_input = input("Enter the piles array (e.g., [2,7,9,4,4]): ").strip()
        
        # Safely evaluate input
        parsed_piles = ast.literal_eval(piles_input)
        
        if not isinstance(parsed_piles, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.stoneGameII(parsed_piles)
        print(f"\nMaximum stones Alice can get: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")