'''
Question: 375. Guess Number Higher or Lower II (Medium)
We are playing the Guessing Game. The game will work as follows:
1. I pick a number between 1 and n.
2. You guess a number.
3. If you guess the right number, you win the game.
4. If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
5. Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

Example 1:
Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- Guess 7.
- If this is wrong, your cost is $7.
- If I tell you my number is higher, guess 9. (Total cost: $7 + $9 = $16).
- If I tell you my number is lower, guess 3. (Total cost: $7 + $3 = $10).
- The worst-case cost is $16.

---
My Approach (Minimax / Bottom-Up Dynamic Programming):
1. This is a classic Minimax problem. We want to find a guess `x` in the range `[i, j]` that minimizes our worst-case cost.
2. The worst-case cost of guessing `x` is `x + max(cost of left range [i, x-1], cost of right range [x+1, j])`.
3. To avoid the overhead of recursion and tuple-hashing in a dictionary, we use a 2D DP table.
4. `dp[i][j]` represents the minimum cost to guarantee a win in the range from `i` to `j`.
5. We build the table bottom-up, starting with intervals of length 2, then length 3, all the way up to length `n`.
6. Elite Pruning: We only iterate our guess `x` from `i` to `j - 1`. Guessing `j` is strictly sub-optimal because guessing `j - 1` guarantees a lower immediate cost and leaves a right-side remaining cost of 0.

Time Complexity: $O(N^3)$ where N is the number of elements. We check all sub-intervals of length 2 to N, and for each, we iterate through the possible guesses.
Space Complexity: $O(N^2)$ to store the 2D DP table.
'''

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] will store the minimum cost to guarantee a win for range [i, j].
        # We pad the matrix to n + 2 to safely handle index + 1 calls without out-of-bounds errors.
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # length represents the size of the interval we are currently evaluating
        for length in range(2, n + 1):
            # i is the start of the interval
            for i in range(1, n - length + 2):
                # j is the end of the interval
                j = i + length - 1
                
                min_cost = float('inf')
                
                # Try every guess x in the interval [i, j-1]
                for x in range(i, j):
                    # Minimax core logic: cost of guess + worst-case feedback
                    cost = x + max(dp[i][x - 1], dp[x + 1][j])
                    if cost < min_cost:
                        min_cost = cost
                        
                dp[i][j] = min_cost
                
        return dp[1][n]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 375. Guess Number Higher or Lower II Interactive Runner ---")
    try:
        n_input = input("Enter the upper bound n (e.g., 10): ").strip()
        
        # Safely evaluate input
        n = int(n_input)
            
        # Calling the function
        result = solution.getMoneyAmount(n)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")